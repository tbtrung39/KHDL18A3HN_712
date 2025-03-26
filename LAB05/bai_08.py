# cach 1
input_str = input("Nhap chuoi ky tu: ")
word_list = input_str.split()
word_count = len(word_list)
print(f"So luong tu trong chuoi: {word_count}")
# cach 2 
input_str = input("Nhap chuoi ky tu: ")
word_count = 0
in_word = False  
for char in input_str:
    if char != " " and not in_word:  
        word_count += 1
        in_word = True
    elif char == " ":  
        in_word = False
print(f"So luong tu trong chuoi: {word_count}")
