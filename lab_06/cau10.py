import random
list=[so for so in range(201) if so%5==0 and so%7==0]
index=random.randint(0, len(list)-1)
so_ngau_nhien=list[index]
print(f"so ngau nhien duoc chon la: {so_ngau_nhien}")