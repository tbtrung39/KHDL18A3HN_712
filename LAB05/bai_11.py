# cach 1
from collections import Counter
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
word_count = Counter(words)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"Tu '{word}' xuat hien {count} lan")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"Tu '{word}' xuat hien {count} lan")
