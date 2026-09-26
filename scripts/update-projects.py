"""Regenerate the dynamic sections of the profile README.

- fetches public repos, skips forks and the profile repo itself,
  keeps the 4 most recently updated ones (name, url, description, language)
- fetches the account creation date and renders a compact profile age
- stdlib only
"""
import json
import os
import re
import urllib.request
from datetime import date, datetime

USER = "foltzbr"
API = "https://api.github.com"


def api(path):
    req = urllib.request.Request(
        API + path,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "fg-profile-bot"},
    )
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def esc(s):
    return s.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def age_fmt(created, today):
    months = (today.year - created.year) * 12 + (today.month - created.month)
    if today.day < created.day:
        months -= 1
    if months < 0:
        months = 0
    y, m = divmod(months, 12)
    if y <= 0:
        return "%dm" % m
    if m <= 0:
        return "%dy" % y
    return "%dy %dm" % (y, m)


def replace_between(text, start, end, body):
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        raise SystemExit("markers missing: " + start)
    return pat.sub(start + "\n" + body + "\n" + end, text)


def main():
    user = api("/users/" + USER)
    created = datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()
    age = age_fmt(created, date.today())
    repos = api("/users/%s/repos?per_page=100&type=public&sort=pushed&direction=desc" % USER)
    picks = [r for r in repos if not r.get("fork") and r.get("name") != USER][:4]
    rows = ["| project | what | lang |", "|---|---|---|"]
    for r in picks:
        desc = (r.get("description") or "").strip() or "classified"
        lang = r.get("language") or "???"
        rows.append("| [%s](%s) | %s | %s |" % (r["name"], r["html_url"], esc(desc), esc(lang)))
    badges = [
        '<img src="https://komarev.com/ghpvc/?username=%s&color=00ff00&style=flat" alt="views" />' % USER,
        '<img src="https://img.shields.io/badge/profile_age-%s-00ff00" alt="profile age" />' % age.replace(" ", "_"),
        '<img src="https://img.shields.io/badge/build-passing_somehow-00ff00" alt="build" />',
    ]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p = os.path.join(root, "README.md")
    with open(p, encoding="utf-8") as f:
        s = f.read()
    s = replace_between(s, "<!-- PROJECTS:START -->", "<!-- PROJECTS:END -->", "\n".join(rows))
    s = replace_between(s, "<!-- PROFILE-BADGES:START -->", "<!-- PROFILE-BADGES:END -->", "\n".join(badges))
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)
    print("repos: " + ", ".join(r["name"] for r in picks))
    print("created_at: " + user["created_at"])
    print("age: " + age)


if __name__ == "__main__":
    main()
