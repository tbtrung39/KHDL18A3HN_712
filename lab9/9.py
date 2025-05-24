def reverse_number(n, reversed_num=0):
    # Nếu n bằng 0, trả về số đã đảo ngược
    if n == 0:
        return reversed_num
    else:
        # Lấy chữ số cuối cùng và thêm vào reversed_num
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        # Gọi đệ quy với n đã loại bỏ chữ số cuối cùng
        return reverse_number(n // 10, reversed_num)

# Nhập số nguyên từ bàn phím
number = int(input("Nhập một số nguyên: "))

# Đảo ngược số
reversed_number = reverse_number(number)

print(f"Số đảo ngược của {number} là: {reversed_number}")