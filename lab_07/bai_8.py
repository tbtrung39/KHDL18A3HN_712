A = [1, 2.5, "hello", 3, "world", 4.0, "Python", 5, 6.7]
count_ints = 0
count_floats = 0
count_strs = 0

for item in A:
    if isinstance(item, int):
        count_ints += 1
    elif isinstance(item, float):
        count_floats += 1
    elif isinstance(item, str):
        count_strs += 1
    
print("So luong so nguyen:", count_ints)
print("So luong so thuc:", count_floats)
print("So luong chuoi kys tu:", count_strs)
