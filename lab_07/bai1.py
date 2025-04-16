number = set()
print("nhập số nguyên: (nhấn enter để tiếp tục, nhập 'ECS' Để dừng):")
while True:
    value = input()
    if value.upper() == 'ECS':
        break
    try:
        number.add(int(value))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
print("Tập hợp số nguyên: ", number)