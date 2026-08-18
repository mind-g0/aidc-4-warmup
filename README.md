# aidc-4-warmup

Team 4 warmup project for the AIDC bootcamp.

## History & contributions

| Date (approx) | Commit | Author | What was done |
|---------------|--------|--------|---------------|
| Initial | 97b69a1 | mind-g0 | Initial commit (empty repo) |
| PR #1 | 94225d7 | Nassir Abusaroor | Added `mind-g0` to TEAM.md |
| PR #2 | 539d3df | Abdulaziz Almalki | Added `iiAbdulaziz` to TEAM.md |
| PR #3 | 21dacc0 | Nassir Abusaroor | Added `server.py`, `register.py`, `routes/mind-g0.py` |
| PR #4 | c36b887 | Abdulaziz Almalki | Added `routes/iiAbdulaziz.py` endpoint |
| PR #5 | 4b61bac | Nassir Abusaroor | Added `.gitignore`, fixed Python syntax |
| PR #6 | b4480b6 | Nassir Abusaroor | Registered `iiAbdulaziz` on the AIDC board via `register.py` |

### By contributor

| Contributor | Commits | Work |
|-------------|---------|------|
| **Nassir Abusaroor (mind-g0)** | 5 | Project setup: `server.py`, `register.py`, `routes/mind-g0.py`, `.gitignore`; added both members to TEAM.md; ran board registration for Abdulaziz |
| **Abdulaziz Almalki (iiAbdulaziz)** | 2 | Added `routes/iiAbdulaziz.py` endpoint; added himself to TEAM.md |

## Project structure

```
server.py          # HTTP server on port 8000 
register.py        # Register a teammate on the AIDC board
routes/
  mind-g0.py       # Nassir's endpoint  → /mind-g0
  iiAbdulaziz.py   # Abdulaziz's endpoint → /iiAbdulaziz
TEAM.md            # Team goals
```

## Docker

```bash
# run the server in a container (port 8000 mapped)
docker run --rm -it -p 8000:8000 -e PYTHONUNBUFFERED=1 \
  -v "$PWD:/app" -w /app python:3.11-slim python server.py
```

```bash
# exec into the running container
docker exec -it $(docker ps -q --filter ancestor=python:3.11-slim) bash

# inside the container — install debugging tools
apt-get update && apt-get install -y procps iproute2

# inspect processes and listening ports
ps aux
ss -tlnp
```

## Endpoints

| Route | Description |
|-------|-------------|
| `GET /` | List all registered endpoints |
| `GET /mind-g0` | Nassir's team info |
| `GET /iiAbdulaziz` | Abdulaziz's team info |

## Current team

| GitHub handle | Name | Goal |
|---------------|------|------|
| mind-g0 | Nassir Abusaroor | Be better at infrastructure management |
| iiAbdulaziz | Abdulaziz Almalki | Be better in AI |

## Contributing

This project uses a PR-based workflow. Create a branch, add or update your
route, and open a pull request for review.