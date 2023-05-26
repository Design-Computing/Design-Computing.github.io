# -*- coding: UTF-8 -*-
import json

import requests

# writerNames = ["kmatthews25", ...]

r = requests.get("https://medium.com/code17?format=json")
data = json.loads(r.text.encode("utf-8")[16:])
users = data["payload"]["references"]["User"]
posts = data["payload"]["references"]["Post"]

usernames = {}
for k in list(users.keys()):
    us = users[k]
    usernames[us["userId"]] = {
        "username": us["username"].encode("utf8"),
        "name": us["name"].encode("utf8"),
    }
    template = "{username}, {name}, {userId}"
    print(template.format(**us).encode("utf8"))

for k in list(posts.keys()):
    p = posts[k]

    tidyD = {}
    tidyD["title"] = p["title"].strip()
    tidyD["username"] = usernames[p["creatorId"]]["username"]
    tidyD["name"] = usernames[p["creatorId"]]["name"].decode("utf-8")
    tidyD["creatorId"] = p["creatorId"]
    tidyD["firstPublishedAt"] = p["firstPublishedAt"]
    # print tidyD
    template = (
        "{title}, "
        "author: {username} - {name} ({creatorId}), "
        "pub Date {firstPublishedAt}"
    )
    details = template.format(**tidyD)
    print(details.encode("utf-8"))
