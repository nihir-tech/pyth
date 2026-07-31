class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn
        self.marks = []
        self.total = 0
    def getMarks(self):
        print("Enter marks in 3 subjects:")
        for i in range(3):
            mark = float(input(f"Subject {i+1}: "))
            self.marks.append(mark)
        self.total = sum(self.marks)
    def display(self):
        percentage = self.total / 3
        print("\n----- SCORE CARD -----")
        print("Name       :", self.name)
        print("USN        :", self.usn)
        print("Marks      :", self.marks)
        print("Total      :", self.total)
        print("Percentage :", percentage, "%")
name = input("Enter Student Name: ")
usn = input("Enter USN: ")
s = Student(name, usn)
s.getMarks()
s.display()
