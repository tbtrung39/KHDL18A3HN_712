n=int(input("nhập số"))
S1 = 0
for i in range(1, n + 1):
    S1 += i
print(f"a) S1 = 1 + 2 + 3 + ... + {n} = {S1}")

# b. 
S2 = 0
for i in range(n + 1):
    S2 += 2*i + 1
print(f"b) S2 = 1 + 3 + 5 + ... + {2*n+1} = {S2}")

# c. 
S3 = 0
for i in range(1, n + 1):
    S3 += 2*i
print(f"c) S3 = 2 + 4 + 6 + ... + {2*n} = {S3}")