n=int(input("Nhập số lượng sinh viên: "))
cpp=set(map(int,input("Nhập sinh viên thi C++: ").split()))
java=set(map(int,input("Nhập sinh viên thi Java: ").split()))
python=set(map(int,input("Nhập sinh viên thi Python: ").split()))
if len(cpp|java|python)!=n:
 print(f"Số lượng sinh viên tham gia thi không hợp lệ!")
else:
 print("\nSố sinh viên thi một ngôn ngữ:",len(cpp-java-python)+len(java-cpp-python)+len(python-cpp-java))
 print("Số sinh viên thi hai ngôn ngữ:",len(cpp&java-python)+len(cpp&python-java)+len(java&python-cpp))
 print("Số sinh viên thi cả 3 ngôn ngữ:",len(cpp&java&python))