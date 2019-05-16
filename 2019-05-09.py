# 递归函数---阶乘 如：5的阶乘：5*4*3*2*1

def f(n):
    if n==1:
        return 1
    return n*f(n-1)
print(f(2))

print(f(5))

print(f(1))


# 上面的函数会在n=1000的时候存储溢出，故用下面的函数来解决这个问题
def y(n):
    a = 1
    for i in range(1,n+1):
        a*=i
    return a
print(y(1000))
        