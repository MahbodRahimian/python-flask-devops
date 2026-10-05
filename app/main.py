from flask import Flask, jsonify, Response
import time
import threading
import html
import requests

app = Flask(__name__)

start_time = time.time()
request_count = 0
slack_count = 0
_lock = threading.Lock()


SLACK_WEBHOOK_URL = "https://webhook.site/9d53dc82-3e7f-437e-ba29-4deff7257c35"  



def send_to_slack(message: str):
    
    try:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message}, timeout=2)
    except Exception:
        pass


@app.before_request
def count_request():
    global request_count, slack_count
    with _lock:
        request_count += 1

        
        slack_count += 1
        send_to_slack(f"New request received. Total Slack count = {slack_count}")


def get_uptime_seconds():
    return int(time.time() - start_time)


@app.route("/metrics")
def metrics():
    return jsonify({
        "uptime_seconds": get_uptime_seconds(),
        "requests": request_count,
        "slack_count": slack_count,
    })


@app.route("/")
def home():
    uptime = get_uptime_seconds()
    requests_local = request_count
    slack_local = slack_count

    html_page = f"""
    <!doctype html>
    <html>
      <head><meta charset="utf-8"><title>App status</title></head>
      <body>
        <h1>My App status</h1>
        <p><strong>Uptime (s):</strong> {uptime}</p>
        <p><strong>Requests:</strong> {requests_local}</p>
        <p><strong>Slack Count:</strong> {slack_local}</p>
        <p>Last updated: {html.escape(time.ctime())}</p>
      </body>
    </html>
    """
    return Response(html_page, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)