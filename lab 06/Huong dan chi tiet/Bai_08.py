#Cách 1
input_string=input("Nhập chuỗi ký tự:")
while len(input_string)>0 and input_string[0] == " ":
    input_string=input_string[1:]
while len(input_string)>0 and input_string[-1] == " ":
    input_string= input_string[:-1]

input_string = input_string.lower()
normalized_string=""
for i in range(len(input_string)):
    if input_string[i] !=" " or (input_string[i] == " " and\
                               input_string[i-1]!=" "):
        normalized_string += input_string[i]
print("Chuỗi ký tự sau khi được chuẩn hóa là:",normalized_string)

#Cách 2
input_string=input("Nhập vào một chuỗi ký tự:")
input_string=input_string.strip()
input_string=input_string.lower()
input_string=" ".join(input_string.split())
print("Normalized string:",input_string)