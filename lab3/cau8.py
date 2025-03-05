n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("n phải là số nguyên dương. Nhập lại.")
else:
    #a
    S1 = 0
    for i in range(1, n + 1):
        S1 += i
    print(f"S1 = {S1}")
    #b
    S2 = 0
    for i in range(1, 2 * n + 2, 2):
        S2 += i
    print(f"S2 = {S2}")
    #c
    S3 = 0
    for i in range(2, 2 * n + 1, 2):
        S3 += i
    print(f"S3 = {S3}")
