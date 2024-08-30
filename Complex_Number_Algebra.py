class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)

print("Addition:", num1 + num2)
print("Multiplication:", num1 * num2)
