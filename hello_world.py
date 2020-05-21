a=input()
b=""
for i in range(len(a)):
    b+=bin(int(a[i]))[2:].zfill(3)

print(int(b))