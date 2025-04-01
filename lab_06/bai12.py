balance = 0

n = int(input("Nhập số giao dịch: "))
for _ in range(n):
    transaction = input("Nhập giao dịch (D hoặc W theo sau là số tiền): ").split()
    action = transaction[0]
    amount = int(transaction[1])

    if action == 'D':  
        balance += amount
    elif action == 'W':  
        balance -= amount

print("Số tiền thực trong tài khoản là:", balance)