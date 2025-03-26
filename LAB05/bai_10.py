# cach 1 
from collections import Counter
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
word_count = Counter(words)
for word, count in word_count.items():
    print(f"Tu '{word}' xuat hien {count} lan")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"Tu '{word}' xuat hien {count} lan")
