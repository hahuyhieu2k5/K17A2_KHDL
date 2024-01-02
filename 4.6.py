a=int(input("Nhập tháng trong năm 2023 là :"))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
   print("Tháng đó có 31 ngày ")
elif  a==4 or a==6 or a==11 :
   print("Tháng đó có 30 ngày ")
elif a==2:
   print("Tháng đó có 29")
else :
   print("Không tồn tại ")

#1.3
a=int(input("Nhập giá trị của a :"))
b=int(input("Nhập giá trị cua b :"))
while a!= b:
   if a>b :
      a=a-b
   else :
      b=b-a
print("Ước chung lớn nhất của 2 số a và b là :",a)      


  

    