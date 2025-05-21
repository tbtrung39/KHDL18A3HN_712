from pkg import doicoso1

n = doicoso1.nhap_so()
print("Số vừa nhập:", n)
print("Nhị phân:", doicoso1.to_binary(n))
print("Bát phân:", doicoso1.to_octal(n))
print("Thập lục phân:", doicoso1.to_hex(n))