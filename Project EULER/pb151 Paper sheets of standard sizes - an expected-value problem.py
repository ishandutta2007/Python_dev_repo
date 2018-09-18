#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Paper sheets of standard sizes: an expected-value problem       -   Problem 151

A printing shop runs 16 batches (jobs) every week and each batch requires
a sheet of special colour-proofing paper of size A5.

Every Monday morning, the foreman opens a new envelope,
containing a large sheet of the special paper with size A1.

He proceeds to cut it in half, thus getting two sheets of size A2.
Then he cuts one of them in half to get two sheets of size A3 and so on
until he obtains the A5-size sheet needed for the first batch of the week.

All the unused sheets are placed back in the envelope.

At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random.
If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half' procedure until
he has what he needs and any remaining sheets are always placed back in the envelope.

Excluding the first and last batch of the week, find the expected number of times (during each week)
that the foreman finds a single sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .


'''
import time, gmpy2

# For four jobs, starting with an A3 paper, the expected number of times to find exactly
# one sheet in the envelope (excluding first and last) is 0.5, but that doesn't help you much, does it?
# Based on the clarifications in the comments, a_n is the number of ways to choose the sequence of sheets
# drawn from the envelope, assuming that the sheets are distinguishable (even if the same size).
# For example, a_2=3 counts the following 3 possibilities:

#1   {A3}→{ A4, A5 }→{ A4 }→{ A5 }→ {}            ---> outcome probability  = 1/2 because
                                                                            # we have chosen A5
#2   {A3}→{ A4, A5 }→{ A5, A5′ }→{ A5 }→ {}      ---> probability he will pick a single sheet = 1/4 because
                                                                            # we have chosen A4  and we obtained {A5, A5' } for which the tree splits into 2 posibilities :
                                                                            # this case chooses the first A5 batch
#3   {A3}→{ A4, A5 }→{ A5, A5′ }→{ A5′ }→ {}        ---> probability he will pick a single sheet = 1/4  (the same argument as above)
                                                                                # but here at the 3-rd turn we pick the A5'  batch
# _________________________________________________________       +
# 1/2 + 1/4 +1/4 == 1         All the outcomes summed must have  probability = 1

# However, these outcomes need not have equal probabilities. In this case outcome 1 has probability 1/2,
# while outcomes 2 and 3 each have probability 1/4.
# So we can't compute the expectation by counting outcomes and dividing by a_n .

# == SOLUTION :
# => Therefore, to calculate the the expected number of times (probability) that he finds a single sheet of paper we must consider
# only 2-nd and 3-rd turns. As we can see ONLY the 1-st case has a SINGLE sheet of paper => Expected nr of times = 1/2
# WHY ? : Because :  1/2 + 0 + 0  =1/2



# starts with : 1A2 , 1A3, 1A4 , 1 A5
# @ 2017-03-24 - I hoped to be able to solve this problem at this moment. but i do not understand enough
# the decisional tree algorithms. Must study those first beginning with the binary tree

print()
## CONVENTION : A1 = 1, A2 = 2, A3, = 4, A4 = 8, A5 =16

# def cut_sheet(sheet):
#     ''' :CONVENTION:   sheet sizes are :  A1 = 1,   A2 = 2,     A3, = 4,     A4 = 8,     A5 =16
#     '''
#     S = []
#     while sheet != 16 :
#         sheet = sheet << 1
#         S.append(sheet)
#     return S
#
# print('\ncut_sheet function : \t ', cut_sheet(2) )
#
# F = [  2**i for i in range(1,5) ]
# print(F)
#
# Week = dict()
# Week[2] = F[:]
# print('the start of the Week :\t',Week,'\n')
#
# i , cnt = 0, 2
#
# while len(F) >2 :
#     if F[i] == 16 :
#         cnt += 1
#         F.pop( i)
#         Week[cnt] = F[:]
#         print(str(cnt)+'.    ',F)
#     else :
#         if F[i] != 16 :
#             cnt+=1
#             H = cut_sheet(F[i])
#             F.pop( i)
#             F.extend(H)
#             print(str(cnt)+'.    ',F)
#             Week[cnt] = F[:]
#         else : i+=1
#         if i == len(F)-1 :
#             i = 0
#
# print('\n',Week)

# We start with a batch of size A1 and 0 bathes of sizes A2, A3, A4, A5
A = [ 1, 0, 0, 0, 0 ]

def pick_batch(A, no):
    A[no] -= 1
    for i in range(no, len(A)):
        A[i]+=1
    return A


# def evolution(A):
#     pick_prob = [ i/sum(A) for i  in A ]



print([ i/sum(A) for i  in A ])





print('\n--------------------------TESTS------------------------------')








print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
