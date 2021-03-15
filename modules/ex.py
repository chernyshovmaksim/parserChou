import json
import os

if not os.path.isdir("files"):
     os.mkdir("files")

with open('files/links.json', 'w', encoding='utf-8') as f:
    pass


def saveLinks(arr):
    f = open('files/links.json', 'w')
    f.write(json.dumps(arr))
    f.close()
    print('Готово.')