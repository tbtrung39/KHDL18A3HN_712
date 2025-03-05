n = int(input("Nhập số nguyên dương n là: "))
if n<=0 :
    print("Bạn nhập sai yêu cầu.Vui lòng nhập lại nha")
else:
    #a) S4 = 12 + 22 + 32 + … + n2. 
    S4 = 0
    for i in range(1, n+1):
        S4 += i**2
    print("Tổng S4 là:",S4)
    #b)  S5 = 1^3 + 3^3 + 5^3 + … + (2n+1)^3
    S5 = 0
    for i in range(1, 2*(n+1), 2):
        S5 += i**3
    print("Tổng S5 là: ",S5)
    #c) S6 = 2^4 + 4^4 + 6^4 + … + (2n)^4.
    S6 = 0
    for i in range(2, 2*(n+1), 2):
        S6 += i**4
    print("Tổng của S6 là:",S6)