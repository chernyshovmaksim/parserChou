import json

f = open('files/links.json', 'w')
def saveLinks(arr):
    f.write(json.dumps(arr))
    f.close()
    print('Готово.')