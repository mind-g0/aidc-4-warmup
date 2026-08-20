import json, urllib.request, urllib.error

BOARD = "https://aidc.nadir.sh/model"
TEAM = "6"
BY = "Nassir Abusaroor"
IMAGE = "ghcr.io/mind-g0/aidc-4-warmup:latest"


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


# 1. Get the model result from our own server
status, result = request("http://localhost:8000/generate")

print("server said", status)
print(json.dumps(result, indent=2))


# 2. Put the result on the board
status, reply = request(
    BOARD,
    {
        "team": TEAM,
        "by": BY,
        "model": result["model"],
        "image": IMAGE,
        "tokens_per_sec": result["tokens_per_sec"],
        "sample": result["sample"],
    },
)

print("the board said", status)
print(json.dumps(reply, indent=2))