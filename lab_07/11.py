C = {"t1", "t2", "t3", "t4"}
J = {"k1", "k2", "t2", "t3"}
P = {"h1", "h2", "k1", "t2"}
cj = C & J
cp = C & P
jp = J & P
all3 = C & J & P
at_least_2 = (cj | cp | jp)
print("Sinh viên biết 2 ngôn ngữ:", at_least_2)
print("Sinh viên biết cả 3 ngôn ngữ:", all3)
