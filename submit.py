import json, urllib.request, urllib.error

BOARD = "https://aidc.nadir.sh/register"
TEAM = 6
BY = "Nassir Abusaroor"
MODEL = "HuggingFaceTB/SmolLM2-135M-Instruct"
IMAGE = "ghcr.io/mind-g0/aidc-4-warmup:latest"
tokens_per_sec = "4.3"
SAMPLE = ""


def request(url, body=None):
    data = json.dumps(body).encode() if body else None
    headers = {"User-Agent": "aidc-student/1.0"}
    if body:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())


# 2. put them on the board
status, reply = request(
    BOARD,
    {
        "team": TEAM,
        "by": BY,
        "model": MODEL,
        "image": IMAGE,
        "tokens_per_sec": tokens_per_sec,
        "sample": SAMPLE,
    },
)
print("the board said", status)
print(json.dumps(reply, indent=2))
