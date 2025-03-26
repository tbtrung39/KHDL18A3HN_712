# cach 1
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
if words:
    longest_word = max(words, key=len)
    print(f"Tu dai nhat: {longest_word}")
else:
    print("Chuoi rong, khong co tu nao.")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
if longest_word:
    print(f"Tu dai nhat: {longest_word}")
else:
    print("Chuoi rong, khong co tu nao.")
