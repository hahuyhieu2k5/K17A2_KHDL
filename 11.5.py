import math
def phan_tu(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % 1 == 0:
            return False
    return True
def main():
    e=[]
    n=int(input("Nhập số phần tử trong list:"))
    for i in range(n):
        h=int(input("Nhập tiếp phần tử:".format(i+1)))
        e.append(h)
    u=[x for x in e if phan_tu(x)]
    print("Các số nguyên tố trong list là:",u)
    m=[x for x in e if x>0]
    z=[x for x in e if x<0]
    if m:
        S=sum(m)/len(m)
        print("Trung bình cộng của các phần tử dương là:",S)
    else:
        print("Không có phần tử dương trong list")
    if z:
        P=sum(z)/len(z)
        print("Trung bình cộng của các phần tử âm là:",P)
    else:
        print("Không có phần tử âm trong list")
    c=max(e)
    d=min(e)
    print("Giá trị lớn nhất trong list là:",c)
    print("Giá trị nhỏ nhất trong list là:",d)
    e.sort()
    print("List sau khi được sắp xếp tăng dần là:",e)
main()