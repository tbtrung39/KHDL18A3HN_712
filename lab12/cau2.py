def kiem_tra_chuoi(s):
    if not s.isalpha():
        raise Exception("Lỗi ký tự !!!")
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            raise Exception("Lỗi nhập liệu !!!")

    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            raise Exception("Lỗi nhập lặp lại !!!")

    words = s.split()
    if len(words) >= 5 and all(w == words[0] for w in words[:5]):
        raise Exception("Lỗi nhập trùng lặp!!!")

while True:
    try:
        s = input("Nhập chuỗi: ")
        kiem_tra_chuoi(s)
        print("Chuỗi hợp lệ.")
    except Exception as e:
        print(e)