import random
numbers=[random.randint(0,200) for i in range(50)]
ket_qua=[num for num in numbers if num%5 == 0 and num %7==0]
print("Danh sách số ngẫu nhiên:",numbers)
print("Số chia hết cho 5 và 7:",ket_qua)