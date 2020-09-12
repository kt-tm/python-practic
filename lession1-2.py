time = input("Введите время ")
time = int(time)
h = time // 3600
time = time % 3600
m = time // 60
s = time % 60
if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)
print(f"{h}:{m}:{s}")
