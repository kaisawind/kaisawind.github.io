#!/usr/bin/env bash
# 重新生成 index.html：gh repo list × kaisawind, iotxfoundry, aixfoundry（含私有仓库）。
# 用法: ./generate.sh  然后提交 index.html。
set -euo pipefail

OWNERS=(kaisawind iotxfoundry aixfoundry)
FIELDS='name,description,primaryLanguage,isPrivate,updatedAt,homepageUrl,url'
ROW='sort_by(.updatedAt) | reverse | .[] |
  "<tr><td><a href=\"\(.url)\">\(.name | @html)</a>\(.isPrivate | if . then " 🔒" else "" end)</td><td>\(.primaryLanguage.name // "" | @html)</td><td>\(.description // "" | @html)</td><td>\(.updatedAt[:10])</td><td>\(if .homepageUrl != "" then "<a href=\"\(.homepageUrl)\">home</a>" else "" end)</td></tr>"'

{
  cat <<'HEAD'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>kaisawind · repositories</title>
<style>
:root{color-scheme:dark}
body{margin:0 auto;max-width:960px;padding:2rem 1rem;font:14px/1.6 -apple-system,"Segoe UI",Roboto,sans-serif;background:#0d1117;color:#c9d1d9}
h1{font-size:1.4rem}h1 small{color:#8b949e;font-weight:normal}
h2{font-size:1.1rem;margin-top:2rem;border-bottom:1px solid #30363d;padding-bottom:.3rem}
table{width:100%;border-collapse:collapse}
td,th{padding:.35rem .6rem;border-bottom:1px solid #21262d;text-align:left;vertical-align:top}
th{color:#8b949e;font-size:.85rem}
a{color:#58a6ff;text-decoration:none}a:hover{text-decoration:underline}
td:nth-child(2){color:#8b949e;white-space:nowrap}
td:nth-child(4){white-space:nowrap}
td:last-child{white-space:nowrap}
footer{margin-top:3rem;color:#8b949e;font-size:.85rem}
</style>
</head>
<body>
<h1>kaisawind · repositories <small>AI 时代，博客已死，代码即内容。</small></h1>
HEAD

  for owner in "${OWNERS[@]}"; do
    echo "<h2>$owner</h2>"
    echo '<table><tr><th>Repository</th><th>Language</th><th>Description</th><th>Updated</th><th></th></tr>'
    gh repo list "$owner" --limit 200 --json "$FIELDS" --jq "$ROW"
    echo '</table>'
  done

  echo "<footer>Generated $(date +%F) by generate.sh — gh repo list × ${OWNERS[*]}.</footer>"
  echo '</body></html>'
} > index.html

echo "index.html written: $(grep -c '<tr><td>' index.html) repos"
