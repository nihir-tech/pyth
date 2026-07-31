class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
def add(c1, c2):
    return Complex(c1.real + c2.real, c1.imag + c2.imag)
n = int(input("Enter number of complex numbers (N >= 2): "))
if n < 2:
    print("N must be at least 2")
else:
    total = Complex(0, 0)
    for i in range(n):
        print("Complex Number", i + 1)
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        c = Complex(real, imag)
        total = add(total, c)
    print("\nSum of Complex Numbers =",
          total.real, "+", total.imag, "i")
