import json
av = 0.0
firm = {}
with open("text_7.txt", "r", encoding="utf-8") as f:
    for i in f:
        firm.update({i.split(" ")[0]: float(i.split(" ")[2]) - float(i.split(" ")[3])})
        av = av + float(i.split(" ")[2]) - float(i.split(" ")[3])  if float(i.split(" ")[2]) - float(i.split(" ")[3]) > 0.0 else av
list = [firm, {'average_profit': av}]
with open("7.json", "w") as write_f:
    json.dump(list, write_f, indent=4)