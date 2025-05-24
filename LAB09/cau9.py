def dao_nguoc(n,ket_qua=0):
    return ket_qua if n==0 else dao_nguoc(n//10,ket_qua*10+n%10)
n=int(input("Nhập n: "))
print("Kết quả:",dao_nguoc(n)if n>=0 else"Chỉ hỗ trợ số nguyên dương")
