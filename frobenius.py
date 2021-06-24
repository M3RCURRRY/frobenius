from random import SystemRandom
import time
random = SystemRandom().randrange

def perfect_square(number):
    if number < 0:
        return False
    if number < 2:
        return True
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False
    
def ab_select(number):
    a, b = random(1, number), random(1, number)
    desc = pow(a,2) - 4 * b
    while perfect_square(delta) or math.gcd(2 * desc * a * b, number) != 1:
        a, b = random(1, number), random(1, number)
        delta = a ** 2 - 4 * b
    return a, b, delta
    
def euclide_ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = euclide_ext_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    
def jacobi(n, d):
    j = 1
    while n:
        while not n & 1:
            n >>= 1
            if d & 7 in {3, 5}:
                j = -j
        n, d = d, n
        if n & 3 == 3 == d & 3:
            j = -j
        n %= d
    return j if d == 1 else 0

def calc_seq(w1,m,n):
    a, b = 2, w1
    bits = int(math.log(m,2)) - 2
    if bits < 0:
        bits = 0
    mask = 1 << bits
    while mask <= m:
        mask <<= 1
    mask >>= 1
    while mask > 0:
        if (mask & m) != 0:
            a, b = (a*b-w1)%n, (b*b-2)%n
        else:
            a, b = (a*a-2)%n, (a*b-w1)%n
        mask >>= 1
    return a, b

def is_number_prime(number, atmp):
    if not (perfect_square(number)):
        it = 0
        while it != atmp:
            if not frobenius_prime(number):
                print('Iteration ', it + 1, ' Not prime: ', number)
                it += 1
                continue
            else:
                print('Iteration ', it + 1, ' Absolutely prime: ', number)
                return number
        print('Number isn\'t prime!\n')
    else:
        print('Number is perfect square!\n')

    
def find_prime_number(bits, atmp):
    number = random((1 << bits - 1) + 1, 1 << bits, 2)
    print('Bottom border of possible prime: ', (1 << bits - 1) + 1)
    print('Upper border of possible prime: ', 1 << bits, '\n\n')
    while True:
        if perfect_square(number):
            number += 2
        it = 0
        while it != atmp:
                if not frobenius_prime(number):
                    print('Iteration ', it + 1, ' Not prime: ', number)
                    it += 1
                    continue
                else:
                    print('Iteration ', it + 1, ' Absolutely prime: ', number)
                    return number
        number += 2


def frobenius_prime(number):
    assert number & 1 and number >= 3
    a, b, d = ab_select(number)
    w1 = (a ** 2 * euclide_ext_gcd(b, number)[1] - 2) % number
    m = (number - jacobi(d, number)) >> 1
    wm, wm1 = calc_seq(w1, m, number)
    if w1 * wm != 2 * wm1 % number:
        return False
    b = pow(b, (number - 1) >> 1, number)
    return b * wm % number == 2


time_list = list()
bits = 10
reps = 50

powers = list()

while bits < 200:
    powers.append(bits)
    curr = list()
    for i in range(reps):
        start=time.time()
        find_prime_number(bits, 10)
        end=time.time()
        curr.append(end-start)
    time_list.append(curr)
    bits += 2

norm_time = list()
for i in time_list:
    temp = 0.0
    for j in i:
        temp += j
    norm_time.append(temp/reps)
    
print(norm_time)
print('\n',powers)
#time_list

import matplotlib.pyplot as plt
plt.plot(norm_time, powers)  
plt.xlabel('X - time')
plt.ylabel('Y - Bits')
plt.title('Time per bits')
plt.show()
t_n = 10
n_list = list()
log_list = list()
while t_n < 200:
    n_list.append(t_n)
    log_list.append(float(log(t_n)))
    t_n += 2

plt.plot(n_list, log_list)
plt.xlabel('X - N')
plt.ylabel('Y - LOG(N)')
plt.title('N PER LOG')
plt.show()

is_number_prime(9,20)
find_prime_number(4,40)
is_number_prime(11,10)