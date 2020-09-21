import os.path
from googletrans import Translator
translator = Translator()
def fnc_create_trans(file_name):
    if os.path.isfile(file_name) == False:
        return "Файл не существует"
    with open(file_name, "r", encoding="utf-8") as file_open:
            file_new = open("translate.txt", "w", encoding="utf-8")
            for i in file_open:
                file_new.write(f"{translator.translate(i.split(' - ')[0], src='en', dest='ru').text} - {i.split(' - ')[1]}")
            file_new.close()
print(fnc_create_trans("text_4.txt"))