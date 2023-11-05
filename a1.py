import time
count=0

def recur_fib(n):
    global count
    count+=1
    if n<=1:    return n
    else:   return (recur_fib(n-1)+recur_fib(n-2))

def iter_fib(n):
    fib1,fib2,fib3=0,1,1
    if(n==0):
        return 0
    if(n<=2):
        return 1
    for i in range(n-2):
        fib1,fib2=fib2,fib3
        fib3=fib1+fib2
    return fib3

start=time.time()
print(recur_fib(12))
end=time.time()
print(end-start)

start=time.time()
print(iter_fib(40))
end=time.time()
print(end-start)
