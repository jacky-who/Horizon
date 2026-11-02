# -*- coding: utf-8 -*-
"""
把 Horizon 生成的 Markdown 日报转换成响应式 HTML，并推送到内容聚合平台。

用法（在仓库根目录执行）：
    HUB_TOKEN=xxx python scripts/publish_hub.py

可选环境变量：
    HUB_ENDPOINT   推送地址，默认 https://hub.askwhoai.com/api/publish
    HUB_SOURCE     来源标识，默认 horizon-ai-news
    HUB_LANG       推送语言，默认 zh
    HUB_DRY_RUN    设为 1 时只生成 HTML 不推送（用于本地调试）

只依赖 Python 标准库，无需额外安装包。
"""
import html as H
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------- 配置

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "docs" / "_posts"
OUT_DIR = ROOT / "data" / "hub-html"

ENDPOINT = os.environ.get("HUB_ENDPOINT", "https://hub.askwhoai.com/api/publish")
SOURCE = os.environ.get("HUB_SOURCE", "horizon-ai-news")
LANG = os.environ.get("HUB_LANG", "zh")
TAGS = ["全球AI", "AI资讯", "Horizon"]
TIMEOUT = 60


# ---------------------------------------------------------------- Markdown 解析

def inline(s: str) -> str:
    """Markdown 行内语法 -> HTML"""
    if not s:
        return ""
    s = s.replace("&\\#", "&#")
    s = H.unescape(s)
    s = s.replace("\\`", "`").replace("\\*", "*").replace("\\_", "_").replace("\\-", "-")
    s = re.sub(r"`([^`]+)`", r'<code class="hz-code">\1</code>', s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        s,
    )
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def strip_md(s: str) -> str:
    return re.sub(r"<[^>]+>", "", inline(s)).strip()


def parse(md: str):
    """解析日报，返回 (meta, toc_groups, sections)"""
    lines = md.split("\n")

    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break

    meta = {"lead": "", "anchor": ""}
    toc_groups, sections = [], []
    cur_toc = cur_sec = cur_item = None
    mode = "head"

    i = 0
    while i < len(lines):
        s = lines[i].strip()

        if mode == "head" and s.startswith(">"):
            meta["lead"] = inline(s.lstrip("> ").strip())
            i += 1
            continue

        if s.startswith("**") and s.endswith("**") and len(s) < 30 and ":" not in s:
            cur_toc = {"name": strip_md(s), "items": []}
            toc_groups.append(cur_toc)
            mode = "toc"
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+\[([^\]]+)\]\(#([^)]+)\)\s*⭐?️?\s*([\d.]+)/10\s*$", s)
        if m and mode == "toc":
            if cur_toc is None:
                cur_toc = {"name": "要闻", "items": []}
                toc_groups.append(cur_toc)
            cur_toc["items"].append({
                "n": int(m.group(1)), "title": m.group(2).strip(),
                "anchor": m.group(3), "score": m.group(4),
            })
            i += 1
            continue

        if s.startswith("## "):
            cur_sec = {"name": strip_md(s[3:]), "items": []}
            sections.append(cur_sec)
            mode = "body"
            cur_item = None
            i += 1
            continue

        m = re.match(r'^<a id="([^"]+)"></a>\s*$', s)
        if m:
            meta["anchor"] = m.group(1)
            i += 1
            continue

        m = re.match(r"^###\s+\[([^\]]+)\]\(([^)]+)\)\s*⭐?️?\s*([\d.]+)/10\s*$", s)
        if m:
            if cur_sec is None:
                cur_sec = {"name": "要闻", "items": []}
                sections.append(cur_sec)
            cur_item = {
                "n": len(cur_sec["items"]) + 1,
                "anchor": meta["anchor"],
                "title": m.group(1).strip(),
                "url": m.group(2).strip(),
                "score": m.group(3),
                "source_line": "", "body": [], "enrich": [], "refs": "", "tags": [],
            }
            cur_sec["items"].append(cur_item)
            meta["anchor"] = ""
            i += 1
            continue

        if cur_item is None:
            i += 1
            continue

        if s.startswith("**标签**"):
            tags_part = s.split(":", 1)[1] if ":" in s else ""
            cur_item["tags"] = [t.strip() for t in re.findall(r"`([^`]+)`", tags_part)]
            i += 1
            continue

        if s.startswith("<details>"):
            buf = [lines[i]]
            j = i + 1
            while j < len(lines) and "</details>" not in lines[j]:
                buf.append(lines[j])
                j += 1
            if j < len(lines):
                buf.append(lines[j])
            d = "\n".join(buf).replace("<details>", '<details class="hz-refs">', 1)
            cur_item["refs"] = d
            i = j + 1
            continue

        m = re.match(r"^\*\*「([^」]+)」\*\*\s*(.*)$", s)
        if m:
            cur_item["enrich"].append({"label": m.group(1).strip(), "text": inline(m.group(2).strip())})
            i += 1
            continue

        if s and not s.startswith("#") and s != "---" and "·" in s and len(s) < 200 and not cur_item["body"]:
            cur_item["source_line"] = inline(s)
            i += 1
            continue

        if s and s != "---":
            cur_item["body"].append(inline(s))
        i += 1

    return meta, toc_groups, sections


# ---------------------------------------------------------------- HTML 渲染

CSS = """
.hz-wrap{--b:#4f46e5;--b2:#7c3aed;--ink:#1a1d29;--ink2:#454b63;--ink3:#7b8299;--line:#e6e9f2;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  color:var(--ink);line-height:1.8;background:#f7f8fc;padding:0;margin:0;font-size:16px;-webkit-text-size-adjust:100%}
.hz-wrap *{box-sizing:border-box}
.hz-wrap a{color:var(--b);text-decoration:none}
.hz-wrap a:hover{text-decoration:underline}
.hz-hero{background:linear-gradient(135deg,#4f46e5 0%,#7c3aed 55%,#a855f7 100%);color:#fff;
  padding:40px 24px 34px;border-radius:16px 16px 0 0}
.hz-kicker{font-size:12px;letter-spacing:2.5px;opacity:.85;margin-bottom:10px;text-transform:uppercase}
.hz-hero h1{font-size:28px;line-height:1.35;margin:0 0 10px;font-weight:700;color:#fff}
.hz-lead{font-size:15px;opacity:.93;margin:0}
.hz-stats{display:flex;gap:22px;flex-wrap:wrap;margin-top:18px}
.hz-stat{background:rgba(255,255,255,.16);border-radius:10px;padding:8px 14px;min-width:88px}
.hz-stat b{display:block;font-size:20px;line-height:1.2}
.hz-stat span{font-size:11.5px;opacity:.85}
.hz-inner{padding:24px}
.hz-toc{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:22px}
.hz-toc h2{font-size:15px;margin:0 0 12px;color:var(--ink);letter-spacing:.5px}
.hz-toc-group{margin-bottom:14px}
.hz-toc-group:last-child{margin-bottom:0}
.hz-toc-name{font-size:13px;font-weight:700;color:var(--b);margin-bottom:8px;
  padding-bottom:6px;border-bottom:1px dashed var(--line)}
.hz-toc ol{margin:0;padding-left:0;list-style:none;counter-reset:tz}
.hz-toc li{counter-increment:tz;display:flex;gap:9px;align-items:baseline;padding:5px 0;font-size:14.5px}
.hz-toc li::before{content:counter(tz);flex:none;width:20px;height:20px;border-radius:6px;
  background:#eef2ff;color:var(--b);font-size:11.5px;font-weight:700;display:inline-flex;
  align-items:center;justify-content:center}
.hz-toc li a{flex:1;color:var(--ink2)}
.hz-sc{background:#fee2e2;color:#b91c1c;font-size:11.5px;font-weight:700;padding:1px 7px;border-radius:20px;flex:none}
.hz-sc.hi{background:#dcfce7;color:#15803d}
.hz-sec{margin-bottom:28px}
.hz-sec-t{display:flex;align-items:center;gap:10px;font-size:19px;font-weight:700;margin:0 0 14px}
.hz-sec-t::before{content:"";width:4px;height:19px;border-radius:3px;background:linear-gradient(180deg,var(--b),var(--b2))}
.hz-item{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin-bottom:14px}
.hz-item-h{display:flex;gap:11px;align-items:flex-start;margin-bottom:10px}
.hz-num{flex:none;width:26px;height:26px;border-radius:8px;background:linear-gradient(135deg,var(--b),var(--b2));
  color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
.hz-item-h h3{flex:1;font-size:17px;line-height:1.5;margin:0;font-weight:650}
.hz-score{flex:none;background:#fef3c7;color:#b45309;font-size:12.5px;font-weight:700;
  padding:3px 9px;border-radius:20px;margin-top:2px;white-space:nowrap}
.hz-src{font-size:12.5px;color:var(--ink3);margin-bottom:12px;padding-left:37px;word-break:break-word}
.hz-body p{margin:0 0 11px;font-size:15.2px;color:var(--ink2)}
.hz-body p:last-child{margin-bottom:0}
.hz-en{margin-top:14px;border-left:3px solid #e0e7ff;background:#f8faff;border-radius:0 10px 10px 0;padding:12px 16px}
.hz-en+.hz-en{margin-top:9px}
.hz-en-l{display:block;font-size:12.5px;font-weight:700;color:var(--b);margin-bottom:4px}
.hz-en p{margin:0;font-size:14.5px;color:var(--ink2)}
.hz-code{font-family:ui-monospace,Consolas,monospace;font-size:12.5px;background:#f1f2f8;
  padding:1px 5px;border-radius:4px;color:#5b21b6}
.hz-refs{margin-top:13px;background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:10px 14px}
.hz-refs summary{cursor:pointer;font-size:13.5px;font-weight:600;color:var(--ink2)}
.hz-refs ul{margin:8px 0 2px;padding-left:20px}
.hz-refs li{font-size:13.5px;margin-bottom:4px;word-break:break-all}
.hz-tags{margin-top:13px;display:flex;flex-wrap:wrap;gap:6px}
.hz-tag{background:#f1f2f8;color:#5b6478;font-size:12px;padding:3px 9px;border-radius:20px}
.hz-foot{text-align:center;font-size:12.5px;color:var(--ink3);padding:18px 24px 26px;
  border-top:1px solid var(--line);margin-top:8px}
.hz-foot a{color:var(--b)}
@media (max-width:600px){
  .hz-hero{padding:30px 18px 26px;border-radius:12px 12px 0 0}
  .hz-hero h1{font-size:22px}
  .hz-inner{padding:16px}
  .hz-item{padding:16px 15px;border-radius:12px}
  .hz-item-h h3{font-size:16px}
  .hz-src{padding-left:0;margin-top:8px}
  .hz-body p{font-size:15px}
  .hz-wrap{font-size:15.5px}
  .hz-stats{gap:8px}
  .hz-stat{flex:1;min-width:0;padding:7px 9px}
  .hz-stat b{font-size:15px;white-space:nowrap;letter-spacing:-.2px}
  .hz-stat span{font-size:10.5px}
}
"""


def render(meta, toc_groups, sections, date_str) -> str:
    total = sum(len(g["items"]) for g in toc_groups) or sum(len(s["items"]) for s in sections)
    p = ['<div class="hz-wrap">', f"<style>{CSS}</style>"]

    p.append('<div class="hz-hero">')
    p.append('<div class="hz-kicker">HORIZON · 全球 AI 资讯</div>')
    p.append(f"<h1>{date_str} AI 每日速递</h1>")
    if meta["lead"]:
        p.append(f'<p class="hz-lead">{meta["lead"]}</p>')
    p.append('<div class="hz-stats">')
    p.append(f'<div class="hz-stat"><b>{total}</b><span>精选条目</span></div>')
    p.append(f'<div class="hz-stat"><b>{len(sections)}</b><span>内容分区</span></div>')
    p.append(f'<div class="hz-stat"><b>{date_str}</b><span>发布周期</span></div>')
    p.append("</div></div>")

    p.append('<div class="hz-inner">')

    if toc_groups:
        p.append('<nav class="hz-toc"><h2>📋 本期目录</h2>')
        for g in toc_groups:
            if not g["items"]:
                continue
            p.append('<div class="hz-toc-group">')
            p.append(f'<div class="hz-toc-name">{H.escape(g["name"])}</div>')
            p.append("<ol>")
            for it in g["items"]:
                hi = " hi" if float(it["score"]) >= 8.0 else ""
                p.append(f'<li><a href="#{it["anchor"]}">{H.escape(it["title"])}</a>'
                         f'<span class="hz-sc{hi}">{it["score"]}</span></li>')
            p.append("</ol></div>")
        p.append("</nav>")

    for sec in sections:
        if not sec["items"]:
            continue
        p.append('<section class="hz-sec">')
        p.append(f'<h2 class="hz-sec-t">{H.escape(sec["name"])}</h2>')
        for it in sec["items"]:
            p.append('<article class="hz-item">')
            if it["anchor"]:
                p.append(f'<span id="{it["anchor"]}"></span>')
            p.append('<div class="hz-item-h">')
            p.append(f'<span class="hz-num">{it["n"]}</span>')
            p.append(f'<h3><a href="{H.escape(it["url"])}" target="_blank" rel="noopener">{H.escape(it["title"])}</a></h3>')
            p.append(f'<span class="hz-score">⭐ {it["score"]}</span>')
            p.append("</div>")
            if it["source_line"]:
                p.append(f'<div class="hz-src">{it["source_line"]}</div>')
            if it["body"]:
                p.append('<div class="hz-body">')
                p.extend(f"<p>{b}</p>" for b in it["body"])
                p.append("</div>")
            for e in it["enrich"]:
                p.append('<div class="hz-en">')
                p.append(f'<span class="hz-en-l">{H.escape(e["label"])}</span>')
                p.append(f'<p>{e["text"]}</p>')
                p.append("</div>")
            if it["refs"]:
                p.append(it["refs"])
            if it["tags"]:
                p.append('<div class="hz-tags">')
                p.extend(f'<span class="hz-tag">{H.escape(t)}</span>' for t in it["tags"])
                p.append("</div>")
            p.append("</article>")
        p.append("</section>")

    p.append("</div>")
    p.append('<div class="hz-foot">由 Horizon AI 资讯雷达自动生成 · '
             f'{date_str}<br><a href="https://jacky-who.github.io/Horizon/" target="_blank" rel="noopener">'
             "查看完整站点与往期回顾</a></div>")
    p.append("</div>")
    return "\n".join(p)


def wrap_full(fragment: str, title: str) -> str:
    """包装成完整 HTML 文档（必须带 charset，否则浏览器会按错误编码解析导致中文乱码）"""
    return (
        "<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n"
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f"<title>{H.escape(title)}</title>\n"
        "</head>\n<body style=\"margin:0;background:#f7f8fc\">\n"
        f"{fragment}\n</body>\n</html>\n"
    )


# ---------------------------------------------------------------- 主流程

def latest_post() -> tuple[str, Path]:
    """取日期最新的一期日报，返回 (日期, 文件路径)"""
    if not POSTS_DIR.exists():
        sys.exit(f"[hub] 找不到目录：{POSTS_DIR}")
    files = sorted(POSTS_DIR.glob(f"*-summary-{LANG}.md"))
    if not files:
        sys.exit(f"[hub] {POSTS_DIR} 下没有 *-summary-{LANG}.md")
    f = files[-1]
    m = re.match(r"(\d{4}-\d{2}-\d{2})-summary-", f.name)
    if not m:
        sys.exit(f"[hub] 无法从文件名解析日期：{f.name}")
    return m.group(1), f


def main():
    date_str, md_path = latest_post()
    print(f"[hub] 读取日报：{md_path.name}")

    meta, toc, secs = parse(md_path.read_text(encoding="utf-8"))
    frag = render(meta, toc, secs, date_str)
    title = f"{date_str} AI 每日速递 · Horizon"
    full = wrap_full(frag, title)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{SOURCE}-{date_str}.html"
    out_path.write_text(full, encoding="utf-8")
    print(f"[hub] HTML 已生成：{out_path}（{len(full.encode('utf-8'))} 字节）")
    print(f"[hub] 分区：{[(s['name'], len(s['items'])) for s in secs]}")

    if os.environ.get("HUB_DRY_RUN") == "1":
        print("[hub] DRY_RUN=1，跳过推送")
        return 0

    token = os.environ.get("HUB_TOKEN", "").strip()
    if not token:
        print("[hub] 缺少环境变量 HUB_TOKEN，跳过推送")
        return 1

    payload = {
        "id": f"{SOURCE}-{date_str}",
        "source": SOURCE,
        "title": title,
        "tags": TAGS,
        "published_at": f"{date_str}T08:00:00+08:00",
        "content": full,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Horizon-Hub-Publisher/1.0",
        },
    )

    print(f"[hub] 推送 → {ENDPOINT}  id={payload['id']}")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            resp = r.read().decode("utf-8", "replace")
            print(f"[hub] ← HTTP {r.status}")
            print(resp[:800])
    except urllib.error.HTTPError as e:
        print(f"[hub] ← HTTP {e.code} 推送失败")
        print(e.read().decode("utf-8", "replace")[:800])
        return 1
    except Exception as e:
        print(f"[hub] ← 请求异常：{type(e).__name__}: {e}")
        return 1

    try:
        obj = json.loads(resp)
    except Exception:
        return 0
    if obj.get("ok"):
        print(f"[hub] ✅ 推送成功（{obj.get('action')}） {obj.get('url', '')}")
        return 0
    print("[hub] ❌ 平台返回失败")
    return 1


if __name__ == "__main__":
    sys.exit(main())
