def add(dig, numbers, diary): #добавить ученика
    diary[numbers] = {dig: []}
    print("OK")
    return diary


def all(diary): #вывести текущее состояние дневника
    for y, z in diary.items():
        for y1, z1 in z.items():
            if z1 == []:
                print(f"{y}. {y1}")
            else:
                print(f"{y}. {y1}", end=" ")
                for i in range(len(z1)):
                    if i == len(z1) - 1:
                        print(f"{z1[i]}", end=" ")
                    else:
                        print(f"{z1[i]},", end=" ")
                print('')


def marks(marks, numbers, diary): #добавить оценки ученику
    for i in diary[numbers].values():
        i.append(marks)
    print("OK")
    return diary


def change(numbers, name, diary): #изменить ученика
    for i in diary[numbers].values():
        diary[numbers] = {name: i}
    print("OK")
    return diary


def delete_name(numbers, diary): #удалить ученика
    del diary[numbers]
    print("OK")
    return diary


def average_mark(diary): #вывести средний бал ученика
    for y, z in diary.items():
        for y1, z1 in z.items():
            if z1 == []:
                print(f"{y}. {y1}")
            else:
                print(f"{y}. {y1}", end=" ")
                q = 0
                for i in z1:
                    q += i
                print(f"{q / len(z1)}")


diary = {}
numbers = 1
while True:
    x = input().split()
    if x[0] == "exit":
        break
    elif x[0] == "add":
        diary = add(x[1] + " " + x[2], numbers, diary)
        numbers += 1
    elif x[0] == "all":
        all(diary)
    elif x[0] == "mark":
        diary = marks(int(x[1]), int(x[2]), diary)
    elif x[0] == "edit":
        dict = change(int(x[1]), x[2] + " " + x[3], diary)
    elif x[0] == "delete":
        dict = delete_name(int(x[1]), diary)
    elif x[0] == "average":
        average_mark(diary)
print(diary)