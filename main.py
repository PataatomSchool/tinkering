my_list = []
for x in range(int(input("> "))):
    num = int(input(f"{x + 1} num: "))
    my_list.append(num)
max_num = my_list[0]
for num in my_list:
    if num > max_num:
        max_num = num
print(max_num)
print(max(my_list))