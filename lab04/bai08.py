while True:
    ki_tu=input("Nhập một kí tự: ")
    if len(ki_tu)==1:
        print(f"Giá trị ASCII của kí tự '{ki_tu}' là {ord(ki_tu)}")
        break
    else:
        print("Chỉ nhập đúng một kí tự")