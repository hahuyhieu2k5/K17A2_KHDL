# A = tổng các số lẻ nhỏ hơn hoặc bằng n

# B = tổng các số chẵn nhỏ hơn hay bằng n

# C = tích các số từ 1 đến n

# D = tích các số chia hết cho 3

# E = tổng các cố nguyên tố nhỏ hơn hay bằng n

# F = tổng chuỗi đan dấu

import math

n = int(input("nhập số N: "))

def A(n):

    j = []

    a = 0

    for i in range(1,n):

        j.append(i)

    for v in j:

        a = a + v

    return print("A = ",a)

def B(n):

    j = []

    a = 0

    for i in range(1,n):

        if i%2==0:

            j.append(i)

    for v in j:

        a = a + v

    return print("B = ",a)

def C(n):

    j = []

    a = 1

    for i in range(1,n):

        j.append(i)

    for v in j:

        a = a*v

    return print("C = ",a)

def D(n):

    j = []

    a = 1

    for i in range(1,n):

        if i%3==0:

            j.append(i)

    for v in j:

        a = a + v

    return print("D = ",a)

def E(n):

    j = []

    a = 0

    for i in range(2,n+1):

        if i>0:

            for k in range(2,int(math.sqrt(i))+1):

                if i%k ==0:

                    break

            else:

                j.append(i)

    for v in j:

        a = a + v

    print("E = ",a)    

def F(n):

    j = []

    a = 1

    for i in range(1,n):

        j.append(i**-1)

    for v in j:

        if i%2==0:

            a = a + v

        else:

            a = a - v 

    return print("F = ",a - 1)

A(n)

B(n)

C(n)

D(n)

E(n)

F(n)