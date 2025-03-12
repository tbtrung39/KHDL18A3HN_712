#Bai8
ky_tu = input("Nhập một ký tự: ")  
if ky_tu==" " or (ky_tu[0] and ky_tu[1:]):  
    print("Nhập không đúng, hãy nhập một ký tự!")  
else:  
    print("Giá trị ASCII của", ky_tu, "là:", ord(ky_tu))