rating_list = [7, 5, 3, 3, 2]
rating = input("Введите рейтинг ")
rating = int(rating)
pos = -1
for i in rating_list:
    if i < rating:
        pos = rating_list.index(i)
        break
if pos == -1:
    rating_list.insert(len(rating_list), rating)
else:
    rating_list.insert(pos, rating)
print(rating_list)