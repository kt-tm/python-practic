import re
with open("text_6.txt", "r", encoding="utf-8") as f:
    dict = {i.split(": ")[0]: sum(list(map(int, re.findall("\d+", i.split(": ")[1])))) for i in f}
    print(f"{dict}")