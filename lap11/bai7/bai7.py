with open(r'cau7\m_nums.txt', 'r') as f:
    m_nums = f.read().split()
    m_nums = list(map(int, m_nums))
with open(r'cau7\n_nums.txt', 'r') as f:
    n_nums = f.read().split()
    n_nums = list(map(int, n_nums))
so_chung = set(m_nums) & set(n_nums)
so_chung = sorted(list(so_chung))

with open(r'cau7\so_chung.txt', 'w') as f:
    f.write(' '.join(map(str, so_chung)))

with open(r'cau7\so_chung.txt', 'r') as f:
    print("Noi dung cua file so_chung.txt:")
    print(f.read())