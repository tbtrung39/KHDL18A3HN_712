str1=input("Nhập chuỗi ký tự thứ nhất")
str2=input('Nhập chuỗi ký tự thứ hai')
max_length=0
longest_substring=""
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        substring=str1[i:j]
        if substring in str2 and len(substring)>max_length:
            max_length=len(substring)
            longest_substring=substring
if longest_substring:
    print("Chuỗi con chung dài nhất là:",longest_substring)
else:
    print("Không có chuỗi con chung")
    