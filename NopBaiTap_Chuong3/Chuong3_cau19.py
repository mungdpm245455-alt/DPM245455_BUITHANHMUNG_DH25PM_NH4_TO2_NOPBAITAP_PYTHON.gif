#Câu 19: Tính giá trị biểu thức S
'''

'''
def S_direct(x, n):
    from math import factorial
    s = 0.0
    for k in range(n+1):
        exp = 2*k + 1
        s += x**exp / factorial(exp)
    return s


x = 2.0
n = 5
print(S_direct(x, n))
