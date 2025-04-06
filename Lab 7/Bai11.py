#Bai11
c_pp = {1, 2, 3}
java = {2, 3, 4}
python = {3, 4, 5}
sv_thi_1nn = (c_pp ^ java ^ python) - (c_pp & java) - (c_pp & python) - (java & python)
sv_thi_2nn = ((c_pp & java) | (c_pp & python) | (java & python)) - (c_pp & java & python)
sv_thi_3nn = c_pp & java & python
print("Sinh viên thi 1 ngôn ngữ:", sv_thi_1nn)
print("Sinh viên thi 2 ngôn ngữ:", sv_thi_2nn)
print("Sinh viên thi 3 ngôn ngữ:", sv_thi_3nn)