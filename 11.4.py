def process_list():
    my_list=[]
    while True:
        try:
            a=float(input("Nhập một số:"))
            my_list.append(a)
        except ValueError:
            break
    total=sum(my_list)
    x=float(input("Nhập một số x:"))
    count_x=my_list.count(x)
    is_greater=x>max(my_list)
    greater_numbers=[a for a in my_list if a > x ]
    print("List:",my_list)
    print("Tổng list:",total)
    print("Kết quả tìm x trong list:",count_x)
    if is_greater:
        print("x lớn hơn tất cả các số trong list!!!")
    else:
        print("x không lớn hơn tất cả các số trong list!!!")
        print("Các số lớn hơn x trong list:",greater_numbers)      
process_list()