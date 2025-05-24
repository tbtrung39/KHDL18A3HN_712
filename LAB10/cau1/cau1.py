from my_Triange import is_TamGiac, ChuViTamGiac, S_TamGiac
a,b,c=map(float,input("Nhập ba cạnh a,b,c:").split())
print(f"Hợp lệ? {is_TamGiac(a,b,c)}")
print(f"Chu vi: {ChuViTamGiac(a,b,c)}")
print(f"Diện tích: {S_TamGiac(a,b,c):.2f}")
