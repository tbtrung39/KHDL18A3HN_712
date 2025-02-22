# câu 7: Viết chương trình tính vận tốc khi rơi tự do ...
import math
h = float(input("Nhập độ cao của vật: "))
g = 9.8
v = math.sqrt(2*g*h)
print(f"Vận tốc của vật khi rơi là {v: .2f}")
