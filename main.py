from os import walk
from json import dump, dumps

filenames = next(walk("audios/"), (None, None, []))[2]

data = []
for i in filenames:
    resposta = i.split("-")[0]
    data.append({
                "name": resposta,
                "url": "audios/" + i
            })


open("audios.js", "w").write("var audios = " + dumps(data))