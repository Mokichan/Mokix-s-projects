def add(dig, numbers, diary):
    diary[numbers] = {dig: []}
    print("OK")
    return diary

def all(diary):
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

def marks(marks, numbers, diary):
    for v in diary[numbers].values():
        v.append(marks)
    print("OK")
    return diary

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
print(diary)