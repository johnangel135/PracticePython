def run(a_list):
    b = []
    for i in a_list:
        if i not in b:
            b.append(i)
    return b


