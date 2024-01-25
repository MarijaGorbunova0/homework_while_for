import random
#1 for

#r = 0
#for i in range(15): #range(0,15,1)
#    arv = float(input("Sisesta srv{0}.arv".format(i + 1)))
#    if arv == int(arv):
#        r += 1
#print("t채isarvude arv on"+ str(r))

#2 while true 

#r = 0
#i = 0
#while True:
#    i+=1
#    arv = float(input("Sisesta srv{0}.arv".format(i)))
#    if arv == int(arv):
#        r += 1  
#        if i == 15: break
#print("t채isarvude arv on"+ str(r))

# 1 wile tingimusega

#r = 0
#i = 0
#while i<15:
#    i+=1
#    arv = float(input("Sisesta srv{0}.arv".format(i)))
#    if arv == int(arv):
#        r += 1  
#print("t채isarvude arv on"+ str(r))

#2

# A = int(input("kirjuta number"))
# if A <= 0:
#     print("see number on vale")
# else:
#     summa = 0
#     i = 1
#     while i <= A:
#         summa += i
#         i += 1
#     print("summa on", summa)

#3

#otvet = 1
#r = 0
#for i in range(8):
#    user = int(input("kirjutage arv{0}.arv".format(i+1)))
#    if user > 0:
#        otvet *=user
#        r += 1
#print("vastus on", otvet)

#4

# for number in range(10, 21):
#     kvadrat = number ** 2
#     print(kvadrat)

#5

# N = int(input("Kirjutage numbrite arv N"))
# summa = 0
# count = 0
# while count < N:
#     number = float(input("Kirjuta arv"))
#     if number < 0:
#         summa += number
#     count += 1
# print(summa)

#6

# N = int(input("Kirjutage numbrite arv N"))
# positivset = 0
# negativset = 0
# nul = 0
# mitu = 0
# while mitu < N:
#     number = float(input("kirjutage arv"))
#     if number > 0:
#         positivset += 1
#     elif number < 0:
#         negativset += 1
#     else:
#         nul += 1
#     mitu += 1
# print("positivsed - ", positivset)
# print("negativsed - ", negativset)
# print("nullid - ", nul)
#7
# A = int(input("kirjuta A "))
# B = int(input("kirjuta B "))
# K = int(input("kirjuta K "))
#
# for number in range(A, B + 1):
#     if number % K == 0:
#         print(number)
#     else:
#         print("kirjuta uuesti")
#9
# euro = float(input("Sisesta algne hoiuse summa eurodes"))
# aeg = int(input("Sisesta aastate arv"))
# protsent = 3
#
# # Arvuta l천ppsumma hoiuse korral
# otvet = euro * (1 + protsent / 100) ** aeg
#print(otvet)
#10
# for _ in range(10):
#     arv1 = float(input("esimene arv"))
#     arv2 = float(input("teine arv "))
#12
# auto = int(input("kirjutage mitu autot oli"))
# aeg = float(input("kirjutage kui palju tootas esimene"))
# brigada = 0
# for vrema in range(0, auto):
#     brigada += aeg + 0.10
# print(brigada)
#13
# kogus = 0
# summa = 0
# for number in range(100, 1001):
#     if number % 7 == 0:
#         kogus += 1
#         summa += number
# print("koik arvud mis sobivad", kogus)
# print("arvude summa", summa)
#14
# N = random.randint(1, 10)
# print(N)
# summa = 1
# for arv in range(1, N + 1):
#     summa *= arv
# print(summa)


