with open('Inp.txt','r') as file_in:
    data=file_in.read()
numbers=list(map(int,data.strip().split()))
numbers.sort()
with open('out.dat','w') as file_out:
    file_out.write(" ".join(map(str,numbers)))