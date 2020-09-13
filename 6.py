# good = tuple()
goods = []
pr_next = True
ind = 0
price_lst = []
name_lst = []
metric_lst = []
cnt_lst = []
while True:
    ind = ind + 1
    name = input("Введите название товара ")
    price = input("Введите цену товара ")
    cnt = input("Введите количество товара ")
    metric = input("Введите eдиницы измерения товара ")
    pr_next = input("Введите 1, если хотите продолжить добавление товаров, иначе введите 0 ")
    price = int(price)
    cnt = int(cnt)
    dict = {'название': name, 'цена': price, 'количество': cnt, 'ед.': metric}
    good = (ind, dict)
    # print(good)
    goods.append(good)
    # print(goods)
    if not bool(int(pr_next)):
        break
# print(goods)
for i in goods:
    for j in i[1].items():
        if j[0] == "название":
            name_lst.append(j[1])
        elif j[0] == "цена":
            price_lst.append(j[1])
        elif j[0] == "количество":
            cnt_lst.append(j[1])
        elif j[0] == "ед.":
            metric_lst.append(j[1])
result_dict = {'название': list(set(name_lst)), 'цена': list(set(price_lst)), 'количество': list(set(cnt_lst)), 'ед': list(set(metric_lst))}
print(result_dict)
