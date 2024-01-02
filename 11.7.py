def elementwise_greater_than(L,thresh):
    result=[]
    for num in L:
        result.append(num>thresh)
    return result
L=[1,2,3,4]
thresh=2
P=elementwise_greater_than(L,thresh)
print(P)