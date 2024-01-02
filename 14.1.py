def ba_canh(a,b,c):
    if a<=0 or b<0 or c<=0:
        return False
    if a+b<=c or a+c<=b or b+c<=a:
        return False
    return True 
try:
    a=int(input("Nhập cạnh thứ nhất của tam giác:"))
    b=int(input("Nhập cạnh thứ hai của tam giác:"))
    c=int(input("Nhập cạnh thứ ba của tam giác:"))
    if a<=0 or b<0 or c<=0:
        raise ValueError("Độ dài các cạnh của tam giác phải là số dương và khác 0")
    if a+b<=c or a+c<=b or b+c<=a:
        raise ValueError("KHÔNG TỒN TẠI!!!")
    print("HỢP LỆ")  
except ValueError as e:
    print("ĐÃ XẢY RA LỖI!!!",e)