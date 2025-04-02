#Bai12
import random
dao_dich_lst = []
for i in range(6):
    if random.randint(0, 1) == 0:
        action = "D"
    else:
        amount = random.randint(1, 6) * 100
        dao_dich_lst.append(f"{action},{amount}")
print("Giao dịch ngẫu nhiên:")
for j in dao_dich_lst:
    print(j)
so_du = 0
for dao_dich in dao_dich_lst:
    action, amount = dao_dich.split(',')
    amount = int(amount)
    if action == 'D':
        so_du += amount
    else:
        so_du -= amount
print("Số dư tài khoản:", so_du)