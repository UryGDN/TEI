import os
os.system("cls")

import math


r = []
re = 0
for i in range(1, 5):
    r = int(input("Resistencia {0}: ".format(i)))
    re += r

for i in range(1, 5):
    r = int(input("Resistencia {0}: ".format(i)))
    re += r



r_ma = 0
r_me = 10000000

for i in range(4):
    if r_ma <= r[i]:
        r_ma = r[i]
    if r_me >= r[i]:
        r_me = r[i]

print("Resistencia total {0}, Maior Resistencia {1}, Menor Resistencia {2}".format(re, r_ma, r_me))