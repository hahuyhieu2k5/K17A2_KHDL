import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

deta = b**2 - 4*a*c

if deta > 0:
    x1 = (-b + math.sqrt(deta)) / (2*a)
    x2 = (-b - math.sqrt(deta)) / (2*a)
    print("Nghiệm x1 =", x1, "x2 =", x2)
elif deta == 0:
    x = -b / (2*a)
    print("Nghiệm kép x = ",x)
else:
    print("Phương trình vô nghiệm.")
