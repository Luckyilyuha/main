import random

base =" +-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

size = int(input("размер пароля?"))

save = ""

for i in range(size):
    k = random.randint(0, len(base) - 1)
    save += base[k]

print(save)