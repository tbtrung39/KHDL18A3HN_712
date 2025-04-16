Numbers=[]
 while True:
     number=input("nhập số hoặc khoảng trống để kết thúc: ")
     if number==' ': break
     if number.isdigit():Numbers.append(int(number))
 print("Numbers: ",Numbers)
 print("A: ",set(Numbers))