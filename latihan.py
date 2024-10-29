from random import random

n = int(input("Masukkan jumlah bilangan acak: "))

count = 0

while count < n:
    a = random()
    if a < 0.5:
        print(a)
        count += 1