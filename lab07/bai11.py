n = int(input("Nhập số sinh viên: "))

ct = set(map(int, input("Sinh viên thi C++ (cách nhau bởi dấu cách): ").split()))
java = set(map(int, input("Sinh viên thi Java: ").split()))
python = set(map(int, input("Sinh viên thi Python: ").split()))

one_lang = (ct ^ java ^ python) - (ct & java) - (ct & python) - (java & python)


two_lang = ((ct & java) | (java & python) | (ct & python)) - (ct & java & python)

three_lang = ct & java & python

print("Sinh viên chỉ thi 1 ngôn ngữ:", sorted(one_lang))
print("Sinh viên thi 2 ngôn ngữ:", sorted(two_lang))
print("Sinh viên thi cả 3 ngôn ngữ:", sorted(three_lang))
