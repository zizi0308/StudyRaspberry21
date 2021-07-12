
m = 0
n = 1

def func():
    global m, n
    m = m + 1
    n += 1

func()
print(m, n)

def counter(max):
    t = 0

    def output():   # counter 함수에 속한 함수로 밖에서 따로 호출불가
        print('t = {0}'.format(t))

    while t < max:
        output()
        t += 1

counter(10)
# output

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
print(factorial(9))
print(factorial(8))
print(factorial(7))

#lamda
a = lambda x, y : x * y
print(a(2, 8))


#Closure 함수 자체를 return해줌

def calc(a):
    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))


# deco
def incre(x):
    return x + 2

