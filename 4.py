word = input("Введите строку ")
word = word.split()
num = 0
for ind, i in enumerate(word):
    str = i[0:10]
    print(f"{ind} {str}")
