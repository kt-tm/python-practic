def int_func(word):
    return chr(ord(word[0]) - 32) + word[1:]
s = input("Введите строку, состоящую из латинский букв нижнего регистра ")
pr_exec = True
new_s = ''
for i in s.split():
    for j in range(len(i)):
        if ord(s[j]) < 97 or ord(s[j]) > 122:
            pr_exec = False
            break
    if pr_exec == False:
        new_s = "Строка не соответствует требованию"
        break
    new_s = new_s + ' ' + int_func(i)
print(new_s)





