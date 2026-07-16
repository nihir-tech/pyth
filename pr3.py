n = int(input("Enter no. for limit: "))

a, b = 0, 1

if n <= 0:
    print("Enter Positive Value!!!")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
