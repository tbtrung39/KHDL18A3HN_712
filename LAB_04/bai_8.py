while True:
    n = input("nhập kí tự muốn nhập:")
    if n.lower() == "exit":
        print("không hợp lệ vui lòng nhập lại")
        break
    if len(n) != 1:
        print("không hợp lệ vui lòng nhập lại")
    else:
        print(f"giá trị ASCII của{n}:{ord(n)}")