import json, time, html

try:
    m = json.load(open('metrics.json'))
except Exception:
    m = {'uptime_seconds': 0, 'requests': 0, 'slack_count': 0}

html_page = f"""<!doctype html>
<html>
<head><meta charset="utf-8"><title>App status</title></head>
<body>
<h1>App status (CI)</h1>
<p><strong>Uptime (s):</strong> {m.get('uptime_seconds',0)}</p>
<p><strong>Requests:</strong> {m.get('requests',0)}</p>
<p><strong>Slack Count:</strong> {m.get('slack_count',0)}</p>
<p>Collected at: {html.escape(time.ctime())}</p>
</body>
</html>
"""

with open('app_status.html','w') as f:
    f.write(html_page)
