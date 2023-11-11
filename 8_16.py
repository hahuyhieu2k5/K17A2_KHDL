
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ket_qua = ucln(a, b)
print(f"UCLN của {a} và {b} là: {ket_qua}")