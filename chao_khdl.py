#Chương trình thứ 2
# Tính toán số học
x= float(input("Nhập giá trị x:"))
y= float(input("Nhập giá trị y:"))
tong = x+y
hieu=x-y
tich=x*y
thuong=x/y
print('Tổng của hai số    ', x, '+', y, '=',tong)
print('Hiệu của hai số    ', x, '-', y, '=',hieu)
print('Tích của hai số    ', x, '*', y, '=',tich)
print('Thương của hai số  ', x, '/', y, '=',thuong)

import math
can_bac_hai_x=math.sqrt(x)
print('Căn bậc hai của x', x, '=', can_bac_hai_x)