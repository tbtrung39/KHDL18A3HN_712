while True:
    n = input("Nhập một số nguyên dương: ")
    i = n
    hop_le = True
    while i:
        if not ("0" <= i[0] <= "9"):
            hop_le = False
            break
        i = i[1:]
    if hop_le and n:
        n = int(n)
        break

chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""

while n > 0:
    ket_qua = (chu_so[n % 10] + " " + ket_qua) if ket_qua else chu_so[n % 10]
    n //= 10

print("Dạng chữ:", ket_qua)
