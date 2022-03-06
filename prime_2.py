print("入力された数までの素数を列挙します")
while True:
    num = (input("いくつまで"))
    if num.isdigit() == False:
        print("正の整数を入力してください")
    else:
        num = int(num)
        break

print(num, "までの素数は、")
for i in range(2, num):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i, end=" ")
print("\nです。")
