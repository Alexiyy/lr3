def input_valid():


def x2(x):


def x3_1(x):


def collatz(x):
    while x != 1:
        if x % 2 == 0:
            return x2(x)
        else:
            return x3_1(x)
    print('Список имеет вид: ', sp)
sp = []
input_valid()