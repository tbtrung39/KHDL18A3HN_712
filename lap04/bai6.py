num_to_words = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
while True:
    try:
        number = int(input("Nhập một số nguyên dương: "))
        if number < 0:
            print("Vui lòng nhập số không âm!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
number_str = str(number)
words = [num_to_words[int(digit)] for digit in number_str]
print("Kết quả:", " ".join(words))