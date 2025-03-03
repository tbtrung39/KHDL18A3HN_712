n = int(input("Nhập số nguyên dương n là: "))
if n<=0 :
    print("Bạn nhập sai yêu cầu.Vui lòng nhập lại nha")
else:
    S = 0
    #a) S1 = 1 + 2 + 3 + … + n=n(n+1)/2
    S1 = (n*(n+1))/2
    print("Tổng của phương trình là:",S1)
    #b)S2 = 1 + 3 + 5 + … + (2n+1)= (n+1)^2
    S2 = (n+1)**2
    print("Tổng của S2 là:",S2)
    #c) S3 = 2 + 4 + 6 + … + 2n = n(n+1)
    S3 = n*(n+1)
    print("Tổng của S3 là:",S3)