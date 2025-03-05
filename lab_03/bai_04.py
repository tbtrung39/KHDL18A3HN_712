n = int(input('Nhập vào số n: '))
print(f'\nCác số nguyên tố nhỏ hơn {n} là: ')
for i in range(2, n + 1):
    nguyen_to = 0
    for j in range(1, i + 1):
        if i % j == 0:
            nguyen_to += 1
    if nguyen_to == 2:
        print(i)