def find_chickens_and_dogs(chickens, dogs, total_chickens, total_dogs):
    # Kiểm tra điều kiện dừng
    if chickens + dogs == total_chickens and 2 * chickens + 4 * dogs == total_dogs:
        return (chickens, dogs)
    
    # Nếu số chó vượt quá tổng số con, trả về None
    if dogs > total_chickens:
        return None
    
    # Gọi đệ quy với số chó tăng lên
    return find_chickens_and_dogs(chickens, dogs + 1, total_chickens, total_dogs)

# Khởi tạo số lượng gà và chó
total_chickens = 36
total_dogs = 100

# Bắt đầu tìm kiếm với 0 gà và 0 chó
result = None
for chickens in range(total_chickens + 1):
    result = find_chickens_and_dogs(chickens, 0, total_chickens, total_dogs)
    if result is not None:
        break

if result:
    chickens, dogs = result
    print(f"Số gà: {chickens}, Số chó: {dogs}")
else:
    print("Không tìm thấy giải pháp.")
