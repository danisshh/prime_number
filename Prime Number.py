no = int(input("Enter a number: "))
flag = True
for i in range(2, (no//2)+1):
    if no % i == 0:
        flag = False
        break
if flag:
    print("Prime")
else:
    print("Not Prime")
