d={i:'' .join([str(i//(2**j)%2)for j in range(7,-1,-1)if i//(2**j)])for i in range(1,101)}
print(d)
