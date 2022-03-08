print("入力された数より小さい素数を列挙します")
while True:
    num = (input("いくつまで？"))
    if num.isdigit() == False or int(num) == 0:
        print("自然数を入力してください")
    elif int(num) == 1:
        print("1は素数ではありません")
    else:
        num = int(num)
        break
print(num, "より小さい素数は、")
for i in range(2, num):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i, end=" ")
print("\nです。")
