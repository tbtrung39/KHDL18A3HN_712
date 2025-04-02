import random

numbers = [random.randint(0,200) for i in range(50)]
ket_qua = [num for num in numbers if num%5 == 0 and num%7==0]
print("Danh sach so ngau nhien:", numbers)
print("So chia het cho 5 va 7:", ket_qua)