import random

a = []
i = random.randint(50, 200)
while i > 0:
    a.append(random.randint(0, 999))
    i -= 1
order = sorted(set(a))
print(order)
num = int(input("input number: "))


def normal():
    check = False
    for element in order:
        if num == element:
            check = True
            break
    if check:
        print("%d is in the list" % num)
    else:
        print("%d is NOT in the list" % num)


def binary():
    start_index = 1
    end_index = len(order) - 1
    while True:
        middle_index = round((end_index - start_index) / 2)

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            print("False")
            break

        middle_element = order[middle_index]
        if middle_element == num:
            print("True")
            break
        elif middle_element < num:
            end_index = middle_index
        else:
            start_index = middle_index