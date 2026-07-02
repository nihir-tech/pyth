# Practical 1

name = input("Enter Student Name: ")
usn = input("Enter Student ID: ")

m1 = float(input("Enter First Subject Marks: "))
m2 = float(input("Enter Second Subject Marks: "))
m3 = float(input("Enter Third Subject Marks: "))

total = m1 + m2 + m3
per = total / 3

print("Student Name is:", name)
print("Student ID is:", usn)
print("First Subject Marks:", m1)
print("Second Subject Marks:", m2)
print("Third Subject Marks:", m3)
print("Total Marks:", total)
print("Percentage:", per)
