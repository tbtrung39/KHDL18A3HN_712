so=list(map(int,input("nhập các số cách nhau bởi dấu cách: ").split()))
for i in so:
    assert i%2==0, "tất cả các số không phải là số chẵn"
print("tất cả các số đều là số chẵn")