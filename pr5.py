n = int(input("Enter the number of elements: "))
numbers = []
print("Enter the numbers:")
for i in range(n):
    num = float(input())
    numbers.append(num)
mean = sum(numbers) / n
variance = sum((x - mean) ** 2 for x in numbers) / n
std_deviation = variance ** 0.5
print("\nResults:")
print("Mean :", mean)
print("Variance :", variance)
print("Standard Deviation :", std_deviation)
