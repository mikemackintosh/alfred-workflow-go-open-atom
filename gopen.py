# -*- coding: utf-8 -*-
import os
import sys
import json
import glob

_GOPATH = os.getenv('GOPATH') + '/src/'

def list_repos(query):
    items = []
    i = 0
    try:
        repos = filter(lambda f: os.path.isdir(f), glob.glob(_GOPATH + '*/*/*'))
        for repo in repos:
            if len(query.strip()) and not query.lower() in str(repo).lower():
                continue

            display_name = repo.replace(_GOPATH, '')
            items.append({
                'title': display_name,
                'subtitle': 'Open {}'.format(display_name),
                'arg': repo
            })
            i += 1
    except:
        pass

    if len(items) == 0:
        items.append({
            'title': "No repos found",
            'subtitle': 'Could not find any repos',
            'arg': "No repos found"
        })
    return {"items": items}

print(json.dumps(list_repos(sys.argv[1])))
