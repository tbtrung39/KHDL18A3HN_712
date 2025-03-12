x = float(input("Nhập giá trị x (radian): "))
sai_so = 1e-4
cos_x = 1  
so_hang = 1  
bac = 1     
while so_hang > sai_so or so_hang < -sai_so:
    tu_so = -x * x  
    mau_so = (2 * bac - 1) * (2 * bac)  
    so_hang *= tu_so / mau_so  
    cos_x += so_hang  
    bac += 1  
print("Giá trị gần đúng của cos(", x, ") là:", cos_x)