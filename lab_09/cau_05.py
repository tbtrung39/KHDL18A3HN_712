def permutation(n):
    if n == 1:
        return [[1]]
    else:
        prev_perms = permutation(n - 1)
        result = []
        for perm in prev_perms:
            for i in range(n):
                result.append(perm[:i] + [n] + perm[i:])
        return result
    
n = int(input("Nhập số tự nhiên n: "))
print(permutation(n))
