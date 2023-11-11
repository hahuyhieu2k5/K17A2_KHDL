print("Tiền điện dân dụng ")
a=int(input("Mời nhập vào số điện :"))
if ((a>0)and(a<=50)) :
    tien_dien_bac1=a*1.678
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac1)
elif ((a>50)and(a<=100)):
    tien_dien_bac2=a*1.734 
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac2)  
elif ((a>100)and(a<=200)):
    tien_dien_bac3=a*2.014
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac3)
elif ((a>200)and(a<=300)):
    tien_dien_bac4=a*2.536
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac4)
elif ((a>300)and(a<400)):
    tien_dien_bac5=a*2.834
    print("Số tiền điện phải trả của gia đình là",tien_dien_bac5)
elif ((a>400)):
    tien_dien_bac6=a*2.927
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac6)
