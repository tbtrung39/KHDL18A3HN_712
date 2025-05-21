import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def uoc_nguyen_to(n):
    uoc_nt = set()
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            uoc_nt.add(i)
    return sorted(uoc_nt)

def xu_ly_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue
            so = int(line)
            uoc = uoc_nguyen_to(so)
            ket_qua = ' '.join(map(str, uoc))
            f_out.write(ket_qua + '\n')

# Chạy chương trình
xu_ly_file('f_in.dat', 'f_out.dat')
