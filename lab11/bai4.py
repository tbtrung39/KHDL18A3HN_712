def la_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def uoc_nt_khac_nhau(n):
    return sorted({i for i in range(1, n+1) if n % i == 0 and la_nguyen_to(i)})

def ghi_uoc_nt(input_file='f_in.dat', output_file='f_out.dat'):
    with open(input_file, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    with open(output_file, 'w') as f:
        for num in numbers:
            f.write(' '.join(map(str, uoc_nt_khac_nhau(num))) + '\n')
