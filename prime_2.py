print("入力された数までの素数を列挙します")
num = (input("いくつまで"))
if num.isdigit() == False:
    print("数字を入力してください")
else:
    num = int(num)

print(num, "までの素数は、")
for i in range(2, num):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i, end=" ")
print("\nです。")
