num = int(input("Nhập một số nguyên có ba chữ số: "))
if num < 100 or num > 999:
    print("Số nhập vào không phải là số nguyên có ba chữ số.")
else:
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    ones_list = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens_list = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    if tens == 0 and ones == 0:
        print(f"Số {num} đọc là {ones_list[hundreds]} trăm.")
    elif tens == 0:
        print(f"Số {num} đọc là {ones_list[hundreds]} trăm lẻ {ones_list[ones]}.")
    elif ones == 0:
        print(f"Số {num} đọc là {ones_list[hundreds]} trăm {tens_list[tens]}.")
    else:
        print(f"Số {num} đọc là {ones_list[hundreds]} trăm {tens_list[tens]} {ones_list[ones]}.")