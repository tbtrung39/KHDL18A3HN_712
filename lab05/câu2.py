#cách 1
s=input('nhâp chuỗi: ')
d=0
for k in s:
    if not (k.isalpha() or k.isdigit()):
        d+=1
print("số kí tự không phải chữ cái và không phải số là:", d)
#cach 2
s=input('nhập chuỗi: ')
d=0
for k in s:
    ma=ord(k)
    if not (48<=ma<=57 or 65<=ma<=90 or 97<=ma<=122):
        d+=1
print("số kí tự không phải chữ cái và không phải la số:", d)