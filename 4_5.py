a=int(input("Nhập vào số nguyên a :"))
b=int(input("Nhập vào số nguyên b :"))
x,y=a,b
while x != y :
    if x > y : x = x-y
    else : y = y - x
print ("Bội chung nhỏ nhất của 2 số",a,"va",b,"la :",a*b//x)
