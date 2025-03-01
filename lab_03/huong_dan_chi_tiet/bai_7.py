#Code lab3.7.a.py 
h=int(input("Nhập chiều cao tam giác: ")) 
#Vòng lặp bên ngoài xác định số dòng, trong bài này là h 
for i in range(0,h): 
    #Vòng lặp bên trong giữ số cột có 
    #các giá trị thay đổi đối với vòng lặp ngoài 
    for j in range(0,i+1): 
        #in các trạng thái 
        print("* ",end='') 
 
    #Kết thúc sau mỗi dòng  
    print("\r")     #'\r' xuống dòng và đưa con trỏ về đầu dòng 

#Code lab3.7.b.py 
h=int(input("Nhập giá trị chiều cao tam giác: ")) 
# Xác định số khoảng trắng 
k = 2*h -2 
# Vòng lặp bên ngoài xác định số dòng  
for dong in range(1, h+1):  
    # Vòng lặp trong để xác định số khoảng trắng  
    # thay đổi các giá trị tùy yêu cầu 
    for cot in range(1, k+1):  
        #in số dấu cách 
        print(end=" ")  
    #vòng lặp bên trong để xử lý số lượng giá trị cột  
    #thay đổi theo vòng lặp bên ngoài 
    for cot in range(1, dong+1):        
        # in  
        print("*", end=" ")  
    #Giảm k sau mỗi lầm kết thúc dòng 
    k=k-2   
    # ending line after each row  
    print("\r")  

#Code lab3.7.c.py 
h=int(input('Nhập chiều cao tam giác số :')) 
# Khởi tạo số bắt đầu 
num = 1 
#vòng lặp ngoài để xử lý số hàng 
for dong in range(1, h+1):   
    # gán lại số  
    num = 1   
    # Vòng lặp tron để xử lý các cột giá trị thay đổi theo  
    # vòng lặp ngoài 
    for cot in range(1, dong+1):        
        # in số 
        print(num, end=" ")    
            # số tăng dần ở mỗi cột 
        num = num + 1 
        # dòng kết thúc sau mỗi hàng 
    print("\r")

#Code lab3.7.d.py
h=int(input("Nhập giá trị chiều cao tam giác cân: ")) 
# Xác định số khoảng trắng 
k = 2*h -2 
# Vòng lặp bên ngoài xác định số dòng  
for dong in range(1, h+1):  
    # Vòng lặp trong để xác định số khoảng trắng  
    # thay đổi các giá trị tùy yêu cầu 
    for cot in range(1, k+1):  
        #in số dấu cách 
        print(end=" ")  
    #vòng lặp bên trong để xử lý số lượng giá trị cột  
    #thay đổi theo vòng lặp bên ngoài 
    for cot in range(1, dong+1):        
        # in  
        print("*", end=" ")  
    #Giảm k đi 1 sau mỗi lầm kết thúc dòng 
    k=k-1   
    # ending line after each row 
    print("\r") 

#Code lab3.7.e.py
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print("\r")

#Code lab3.7.f.py
# giá trị khởi tạo tương ứng với giá trị 'A' ASCII 
num = 65 
h=int(input('Nhập chiều cao tam giác ký tự: ') ) 
# Vòng lặp ngoài xử lý số hàng 
for i in range(0, h):  
    # vòng lặp trong xử lý các cột 
    # giá trị thay đổi theo vòng lặp ngoài 
        for j in range(0, i+1):  
            # ép kiểu tường minh từ số sang charater  
            ch = chr(num)  
            # in giá trị ch  
            print(ch, end=" ")  
        # Tăng giá trị số  
        num = num + 1 
        # dòng kết thúc sau mỗi hàng 
        print("\r")  