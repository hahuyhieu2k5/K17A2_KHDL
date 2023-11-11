import math
a=float(input("Nhập vào độ dài cạnh a:"))
b=float(input("Nhập vào độ dài cạnh b"))
c=float(input("Nhập vào độ dài cạnh c"))
p=(a+b+c/2)
print("Diện tích tam giác là:",math.sqrt(p*(p-a)*(p-b)*(p-c)))
