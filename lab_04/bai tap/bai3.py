x = float(input("Nhập x: "))  
x = x % (2 * 3.141592653589793)  

term = 1  
cos_x = term  
n = 2 
epsilon = 1e-4  

while abs(term) > epsilon:  
    term *= -x**2 / (n * (n - 1))  
    cos_x += term  
    n += 2  

print("Giá trị gần đúng của cos(x):", cos_x)
