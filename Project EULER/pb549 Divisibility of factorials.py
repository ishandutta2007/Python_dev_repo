#!/usr/bin/python
# Solved by Bogdan Trif @ Completed on Wed, 15 Nov 2017, 23:59
#The  Euler Project  https://projecteuler.net
'''
                    Divisibility of factorials      -       Problem 549

The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100) = 2012.

Find S(10**8).


'''
import time
# import gmpy2
# from pyprimes import factorise
from math import factorial

import sys


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):       # FOURTH      o(^_^)o
        sieve = [True] * self.bound
        for i in range(3, int(self.bound**0.5)+1, 2):
            if sieve[i]:
                sieve[ i*i :: 2*i ] = [False] * ( (self.bound-i*i-1) // (2*i) +1 )
        self.primes = [2] + [i for i in range(3, self.bound , 2) if sieve[i] ]
        print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! ' )

class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self, bound):
        self.prime_table = PrimeTable(bound)

    def get_factors(self, n):
        d = n
        f = {}
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                f[p] = e
        if d > 1:
            f[d] = 1
            #raise Exception('prime factor should be small', d)
        return f


    def get_divisors(self, n) :
        f = self.get_factors(n)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])


    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result




def count_factors(base, lim) :
    ''' :Description: # Here we generate the number of factors of  a certain base for a certain factorial !
    Example : For the base  = 2 we have that :
        [0, 1, 3, 4, 7, 8, 10, 11, 15, 16, 18, 19, 22, 23, 25, 26, 31]
        : which means that :
        2! - has a factor one 2 in it, coming from 2
        4! - has a factor three 2 in it, coming from 2 and 4 (2)
        6! - has a factor four 2 in it, coming from 2, 4 (2), 6
        8! - has a factor seven 2 in it, coming from 2, 4(2), 6(1), 8(3) => 1+2+1+3 = 7
        10! - has a factor eight 2 in it, coming from 2(1), 4(2), 6(1), 8(3), 10(1) => 1+2+1+3 + 1 = 8
        ... and so on ...

    :param base:
    :param lim:
    :return: list with number of a prime            '''
    from math import log

    n = base
    i = 0
    L=[0]
    while base**i < lim :
        c, m = 0, n
        while m % base == 0 :
            m //= base
            c+=1
        i +=  c
        L.append(i)
    #         print('n =', n ,   '    i =', i ,  base**i )
        n+=base

    #     print(L)

    #     for a in range(1,len(L)):
    #         if log(base*a, base) %1 ==0 :
    #             L[a] = L[a-1]+1

    #     print(L)
    #     print([base**i for i in L])
    #     return [base**i for i in L]
    return L

count_factors(2, 10**8)


D = { i :count_factors(i, 10**8) for i in [2, 3, 5, 7] }

def assign_corresponfing_factorial( base , how_many, D ):
    ''' :DEscription: finds out what factorial is needed for a certain prime (base).
    For example : we have the number of factors [2,2,2] --> three factors.
    Question: What is the minimum factorial which needs three 2's . Answer : 4
     example2 : [2,2] --> two factors. Question2 : Minimum factorial ?
     Answer2 :  two is not on the list because 2 has one 2 and 4 has three 2 =>
     We need 4 because 2 has only one factor and it is not enough !

    :param how_many: the number of factors
    :param base:    the prime, or base, int
    :param D: already built dictionary with the factor_count for the primes [2,3,5,7]
        Only those are needed because starting from 11 , we need 11**11 < 10**8 (our limit)
        such that the indexes are not linear.
    :return: int, minimum factorial                     '''
    L = D[base]
    for i in range(1,len(L)) :
        # print(i,'  ', L[i] )
        if how_many <= L[i] :
            return i*base

assign_corresponfing_factorial(2, 11, D)


print('\n--------------------------TESTS------------------------------')


# http://www.cut-the-knot.org/blue/LegendresTheorem.shtml
# @2017-11-13 - Problema e pe de-andoselea zisa. Practic trebuie gasit :
# alege numarul n=25 . Intrebare : care este cel mai mic factorial m! care divide 25
# Logica : 25 = [5, 5] => avem nevoie de 2 de 5. 5! are unul. urmatorul 5 il obtinem de
# la 10 ! => s(25) = 10 . Et voila !!!



# primes = prime_sieve(100)
# print(primes[:100])

def old_fashioned_pure_brute_force(up):
    S=0
    for n in range(2, up+1 ):
        if gmpy2.is_prime(n):
            S += n
            # print(n,'          m!= ' ,  n, '!')

        else :
            f = get_factors(n)
            i = max(f)
            while factorial(i)% n != 0 :

                i+=1

            S +=i
            # print(n,'          m! = ' , i ,'!         '  , f)

    print('\nResult = ', S)

# old_fashioned_pure_brute_force( 10**5)



t1  = time.time()





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def solution_1(lim):        ## SUUUUUUUUPER SLOW, Works well to 10**6

    primes = set(prime_sieve(lim))
    # sieve = [0] * lim
    #
    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # for p in primes :
    #     i=1
    #     while p**i < lim :
    #         if i==1 :
    #             # print( p**i  , ((lim-1)//(p**i)) )
    #             sieve[p**i :: p**i ] = [p*i] * ( (lim-1)//(p**i))
    #         if i > 1 :
    #             r = (lim-1) %  p**i
    #             k =  lim-1-r-p**(i+1)
    #             # print( p**i  ,' k=', k ,'   cnt=', k //(p**i) ,' r=' ,  r ,'    start = ' , p**(i+1) )
    #             sieve[p**(i+1) :: p**i ] = [p*i] * ( k //(p**i)+1 )
            # i+=1
    # print(sieve)
    S = 0
    F  = Factorization(lim)
    for i in range(2, lim+1):
        if i % 10**5 == 0 :
            sys.stdout.write('\r' + str(i//10**5) +'              '+  str(round((time.time() - t1),2)) +'  sec'   )   # Font Segoe UI Semibold

        if i in primes :
            S += i

        else :
            G = F.get_factors(i)        # G is a dictionary with factorization elements
            # print(str(i)+'.     ', G  )
            H = []
            for p, how_many in G.items() :
                if p < 11 :
                    # print('prime =  ', p, '    how_many = ', how_many )
                    min_factorial = assign_corresponfing_factorial( p, how_many, D )
                    # print('prime =  ', p, '    how_many = ', how_many , '      min_factorial = ', min_factorial )
                    H.append(min_factorial)
                else:
                    min_factorial = p*how_many
                    H.append(min_factorial)

            S += max(H)
            # print(str(i)+'.           Min_Fact = ', max(H) ,'           ' ,G  ,'             H=  ', H  )

    print('\nAnswer : ', S )
    return S

# solution_1(10**5)


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4), 's\n\n')

print(' =======  My SECOND SOLUTION,  20 min ===============\n' )
t1  = time.time()


D = { i :count_factors(i, 10**8) for i in [2, 3, 5, 7] }

def solution_with_sieve_factorization(n):   # Sieve Factorization and Totient Sieve at once
    ''':Description: Sieve Factorization as Dictionary Count            '''

    from collections import defaultdict
    F = defaultdict(int)

    S = 0

    for p in range(2, n+1):
        if p % 10**6 == 0 :
            sys.stdout.write('\r' + str(p//10**6) +'              '+  str(round((time.time() - t1),2)) +'  sec'   )   # Font Segoe UI Semibold

        if p not in F :
            S += p
            for i in range(p+p, n+1, p ) :
                j, k = i, 0
                while j % p == 0 :
                    j //= p
                    k+=1
                if p < 11 :
                    min_factorial = assign_corresponfing_factorial( p, k, D )
                else :
                    min_factorial = p*k

                if i not in F :
                    F[i] = min_factorial
                else :
                    F[i] = max(F[i] , min_factorial )


    # print(F)
    # print( [ v for v in F.values() ])
    S += sum([ v for v in F.values() ] )

    print('\nAnswer : ', S )
    return S

# solution_with_sieve_factorization(10**6)        #   Answer :  476001479068717           Completed in : 1267.3165 s

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4), 's\n\n')


print(' =======  My THIRD SOLUTION,   ===============\n' )
t1  = time.time()

def start_position(base, lim) :
    from math import log, factorial

    n = base
    i = 0
    S=[0]
    while base**i < lim :
        c, m = 0, n
        while m% base == 0 :
            m //= base
            c+=1
        i +=  c

        S.append(i)
#         print('n =', n ,   '    i =', i ,  base**i )
        n+=base

    for a in range(1,len(S)):
        if log(base*a, base) %1 ==0 :
            S[a] = S[a-1]+1

#     print(S)

    return [base**i for i in S]



def solution_pb549(lim):

    sieve = [0] * (lim+1)
    primes = [2, 3  , 5] #, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for p in primes :
        # print( p  , ((lim-1)//(p)) )
        # sieve[p :: p ] = [p] * ( (lim-1)//(p))
        # print(sieve)

        S = start_position( p, lim*p*p )
        print(S)
        i=1
        while p**i <= lim :
            print('------')
            if S[i] < lim :
                start = S[i]
                if p**i < 13 :
                    if factorial(p**i) > lim :
                        end = lim
                    else :
                        end = factorial(p**i)
                else : end = lim
                # if S[i+1] > lim : end = ( lim - lim%start) + start
                # else : end = S[i+1]
#                 for j in range(start, lim, p**i):
#                     if  sieve[j] < p*i :
#                         sieve[j] = p * i
#                         print('p = ', p,'    i = ' , i ,'    j= ',j,  '     p*i= ', p*i ,'   ', sieve[a] )
                print('start = ', start, '      end =', end)
            else : break

            # r = (lim-1) %  p**i
            # k =  lim-1-r-start
            # print( p**i  ,' k=', k ,'   cnt=', k //(p**i) ,' r=' ,  r ,'    start = ' , start, '   ' )
            # sieve[start :: p**i ] = [p*i] * ( k //(p**i)+1 )


            # r = (lim-1) %  p**i
            k =  ( end - start )//(p**i)
            print( p*i  , '     step =', p**i , '        start = ' , start, '      end = ', end ,'        k=', k    )
            sieve[start : end : p**i ] = [p*i] *  k
            print(sieve)
            i+=1

    print(sieve)
    print(sum(sieve)-2)

# solution_pb549(50)


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n------------------  SOLUTION 0,  DFS MUST LEARN IT !!!!< O(n)  ADVANCED !!, 3 sec, INCREDIBLE --------------')
t1  = time.time()

# ===== Sun, 28 Feb 2016, 20:47,  Min_25
# We can solve the problem in sub-linear time with Lucy_Hedgehog techniques.
#
# [Edited]
#
# Let m = ∏ { 1≤i≤k} (p_i^(e_i))
# and
# s(m)=max ( 1≤i≤k) {s(p_i^e^i)}, where p_1<⋯<p_k.
#
# Essentially my algorithm use a DFS, but we can skip the most of the computation time using the equation
#
# ∑ {max(p_k,s(m))< p ≤ n/m }  s (mp) = ∑ { max(p_k,s(m))<p≤n/m } p,
#
#
# which is easy to compute with Problem 10 Forum.
#
# -----
#
# Here are some additional results with PyPy 2.6:
#
# S(10^8)=476001479068717: 0.345 sec.
# S(10^9)=41985755551695435: 0.757 sec.
# S(10^10)=3755757144356656232: 2.757 sec.
# S(10^11)=339760245447471537380: 13.852 sec.
# S(10^12)=31019315737369514081083: 67.465 sec.
# S(10^13)=2853681972966816815227920: 401.336 sec.

from math import sqrt
from itertools import count

def prime_sieve(N):
  is_prime = [1] * (N + 1)
  is_prime[0] = 0
  v = isqrt(N)
  for p in range(2, v + 1):
    if not is_prime[p]:
      continue
    for k in range(p * p, N + 1, p):
      is_prime[k] = 0
  return [p for p in range(2, N + 1) if is_prime[p]]

def isqrt(n):
  x = int(sqrt(n * (1 + 1e-14)))
  while True:
    y = (x + n // x) >> 1
    if y >= x:
      return x
    x = y

def icbrt(n):
  if n <= 0:
    return 0
  x = int(n ** (1. / 3.) * (1 + 1e-12))
  while True:
    y = (2 * x + n // (x * x)) // 3
    if y >= x:
      return x
    x = y

def tabulate_all_prime_sum(N):
  def T(n):
    return n * (n + 1) // 2 - 1

  if N <= 1:
    return [0, 0], [0, 0]

  v = isqrt(N)

  smalls = [T(i) for i in range(v + 1)]
  larges = [0 if i == 0 else T(N // i) for i in range(v + 1)]

  for p in range(2, v + 1):
    if smalls[p - 1] == smalls[p]:
      continue
    p_sum = smalls[p - 1]
    q = p * p
    end = min(v, N // q)
    for i in range(1, end + 1):
      d = i * p
      if d <= v:
        larges[i] -= (larges[d] - p_sum) * p
      else:
        larges[i] -= (smalls[N // d] - p_sum) * p
    for i in range(v, q - 1, -1):
      smalls[i] -= (smalls[i // p] - p_sum) * p
  return smalls, larges

def prob549(N):
  def rec(n, beg, s, primes):
    ret = s
    for pi in range(beg, len(primes)):
      p = primes[pi]
      if p > n:
        break
      if p > s and p * p > n:
        ret += larges[N // n] if n > sqrtN else smalls[n]
        ret -= smalls[p - 1 if p <= sqrtN else sqrtN]
        break
      q = 1
      for e in count(1):
        q *= p
        if q > n:
          break
        ret += rec(n // q, pi + 1, max(s, ss[pi][e]), primes)
    return ret

  sqrtN = isqrt(N)
  smalls, larges = tabulate_all_prime_sum(N)
  primes = prime_sieve(sqrtN)
  primes += [sqrtN + 1] # dummy

  ans = 0
  ss = []
  for p in primes:
    q = p
    c, t, e = 0, 0, 1
    seq = [0]
    while q <= N:
      while c < e:
        t += p
        s = t
        while s % p == 0:
          s //= p
          c += 1
      seq += [t]
      q *= p
      e += 1
    ss += [seq]
  ans += rec(N, 0, 0, primes)
  print(ans)

prob549(10 ** 8)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ====Sun, 28 Feb 2016, 12:19, Nore, France
# Hm, strangely, is still says that no one solved the problem, but that I am 9th to solve it...
#
# Anyway, here is my solution:
# It was a simple sieve, where you look for each prime factor of a number n=∏{ i=1, k} p_i^(α_i)
# the least m such that  m! |p_^α_i .
#
# In the code, the v_p function returns the p-valuation of a number, and val(k, p)
# returns the least m such that m! | p^k .
#
# This took 13s using pypy.
#
# EDIT: Got it down to 6.5s avoiding useless recalculations of the val function;
# see updated code below. It runs in 1m52s with normal Python though,
# I haven't been able to get under 1 minute.


def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def sieve_ff(n):
    l = [0] * (n + 1)
    for p in range(2, n + 1):
        if l[p] == 0:
            u = p
            k = 1
            s = 0
            while u <= n:
                while k > 0:
                    s += p
                    k -= v_p(s, p)
                j = u
                while j <= n:
                    if s > l[j]:
                        l[j] = s
                    j += u
                k += 1
                u *= p
    return l

# l = sieve_ff(10 ** 8)
# print(sum(l[1:]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   3 min --------------------------')
t1  = time.time()

# === Mon, 13 Mar 2017, 22:12, saramfish
# This was a lot of fun! Right now this runs in just over 2 minutes, but I'm working on improving it.

import math

def is_prime(n):
    if n<0:
        return is_prime(-n)
    if n==0 or n==1:
        return False
    else:
        for d in range(2,int(math.sqrt(n))+1):
            if n%d==0:
                return False
        return True

def do(N=10**8):
    total = 0
    small_primes = [i for i in range(int(math.sqrt(N))+1) if is_prime(i)]#small primes, here <10^4
    #Now we need to store s(p^k) for the small primes.
    s_sto = []#So s_sto[i][k] gives s( (p_i)^k ).
    for p in small_primes:
        s_sto.append([0,p])
        k = 2
        while p**k < N:
            last = s_sto[-1][-1]
            #If last has p^i power, then it appears i times.
            mult = 0
            while last%(p**mult) == 0:
                mult += 1
            mult -= 1
            if s_sto[-1][-mult] == last:
                s_sto[-1].append(last+p)
            else:
                s_sto[-1].append(last)
            k += 1
    #So every n < 10**8 is a product of small primes and AT MOST one big prime.
    s_array = [0 for i in range(N+1)]
    for pi in range(len(small_primes)):
        k = 1
        pk = small_primes[pi]
        while pk <= N:
            i = pk
            while i<=N:
                s_array[i] = max(s_array[i], s_sto[pi][k])
                i += pk
            k += 1
            pk *= small_primes[pi]
    #Now, everything = 0 is a big prime.s
    for si in range(int(math.sqrt(N)),len(s_array)):
        if s_array[si]==0:
            sik = si
            while sik <= N:
                s_array[sik] = max(s_array[sik],si)
                sik += si
    return sum(s_array)


# do()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Tue, 1 Mar 2016, 11:37, MrDrake, Australia
# 20s sieve method - the function to find the smallest k such that pn|k! for a prime p was annoying.

def f(x, y):
    a = 0
    while y > 1:
        a += x
        b = a
        while y > 1 and b % x == 0:
            b //= x
            y //= x
    return a

N = 10**8
answer = 0

sieve = list(range(N+1))
s = [0 for i in range(N+1)]

for i in range(2, N+1):
    if sieve[i] > 1:
        k = i
        while k <= N:
            s[k] = f(i, k)
            for j in range(k, N+1, k):
                sieve[j] //= i
                s[j] = max(s[j], s[k])
            k *= i

    answer += s[i]

print(answer)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Mon, 7 Mar 2016, 07:05, ktheis, USA
# Pure python (with some imports...) in 12 sec.
#
# 3 sec to generate primes, 6 seconds to tally i with s(i) < sqrt(N), and another 3 sec to tally the rest.
#
# Instead of iterating over 2..10^8, I iterated over the function values s(i).
# For every possible s(i), I determined how many i's exist. Values of s(i) are either prime numbers ' \
# or low multipliers (<17) of prime numbers, so the outer loop is much shorter
# (and you don't have to do any factorization, it turns out).
#
# For s(i) = p with p prime, possible i's are p * any divisor of (p-1)!, and i has to be smaller than 10^8.
# If you save all i's with s(i) < p and i < 10^8 / p, this calculation is straightforward and fast.
#
# For s(i) = n * p with p prime and n small, the procedure is a bit trickier, but also fast.
#
# For p = s(i) > sqrt(10^8) and p prime, things become really easy because possible i's are simply integer multiples of p,
# making sure again that i stays below 10^8.


from collections import defaultdict
from bisect import bisect

nonprimes = defaultdict(list)
SRMax = 10000
Max = SRMax * SRMax

import itertools
izip = itertools.zip_longest
chain = itertools.chain.from_iterable
compress = itertools.compress

def rwh_primes2_python3(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n
    see http://stackoverflow.com/a/3035188 and
    http://stackoverflow.com/a/33356284
    """
    zero = bytearray([False])
    size = n//3 + (n % 6 == 2)
    sieve = bytearray([True]) * size
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        start = (k*k+4*k-2*k*(i&1))//3
        sieve[(k*k)//3::2*k]=zero*((size - (k*k)//3 - 1) // (2 * k) + 1)
        sieve[  start ::2*k]=zero*((size -   start  - 1) // (2 * k) + 1)
    ans = [2,3]
    poss = chain(izip(*[range(i, n, 6) for i in (1,5)]))
    ans.extend(compress(poss, sieve))
    return ans

def prepphase():
    for ilow, p in enumerate(mmp):
        if p > SRMax:
            break
        mult = 1
        number = p*p
        oldexp = 1
        while number < Max:
            mult += 1
            m = mult * p
            exp = 0
            while m % p == 0 and number <= Max:
                m //= p
                number *= p
                exp += 1
            if exp:
                nonprimes[mult * p].append((p, exp, oldexp))
            oldexp += exp
    return ilow

def newprime(i, done):
    newdone = []
    C = bisect(done, Max // i)
    C2 = bisect(done, Max //(i * i))
    for number in done[:C2]:
        newdone.append(number * i)
    del done[C:]
    done.extend(newdone)
    done.sort()
    return done, C

def oldprime(i, toomuch, factor, done):
    C= 0
    newdone = []
    maxprod = Max // factor
    maxprod2 = Max // i
    ni = bisect(done,maxprod2)
    for number in done[:ni]:
        newnumber = number * factor
        if number > maxprod or ((newnumber >= toomuch) and (newnumber % toomuch == 0)): #newnumber >= toomuch and
            continue
        C += 1
        if newnumber <= maxprod2:
            newdone.append(newnumber)
    del done[ni:]
    done.extend(newdone)
    done.sort()
    return done, C

def firstphase(ilow):
    done = [1]
    S = C = 0
    lowprimes = set(mmp[:ilow])
    for i in range(2, SRMax+1):
        if i in lowprimes:
            done, aC = newprime(i, done)
            S += aC * i
            C += aC
        elif i in nonprimes:
            for p, exp, oldexp in nonprimes[i]:
                done, aC = oldprime(i, p**(oldexp+exp+1), p**(oldexp+1), done)
                S += aC * i
                C += aC
    return S, C

def secondphase(S,C,ilow):
    for np in nonprimes:
        if np <= SRMax:
            continue
        for p, _, _ in nonprimes[np]:
            aC = Max//(p*p)
            S += aC * np
            C += aC
    for i in mmp[ilow:]:
        if i > Max:
            break
        aC = Max//i
        S += aC * i
        C += aC
    return S, C

mmp = None

def euler549():
    global mmp
    mmp = rwh_primes2_python3(Max)
    ilow = prepphase()
    S, C = firstphase(ilow)
    S, C = secondphase(S,C, ilow)
    print(S, C)

euler549()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
