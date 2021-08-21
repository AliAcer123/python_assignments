 # Assignment(Fibonacci Numbers)
def fibo(n):
    a = 0
    b = 1
    if n==1:
       print("0")
    elif n==2:
       print("0", "1")
    else:
       print("fibonacci series using ıterative approach")
       print(a,b, end=" ")
       for i in range(n):
           total = a + b
           print(total,end =" ")
           a == b
           b == total
