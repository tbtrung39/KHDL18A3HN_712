def permutation(n):
    # Hàm đệ quy để tìm hoán vị
    def permute(nums, path, results):
        if not nums:  # Nếu không còn số nào trong nums
            results.append(path)  # Thêm hoán vị vào kết quả
            return
        for i in range(len(nums)):
            # Gọi đệ quy với phần tử hiện tại được thêm vào path
            permute(nums[:i] + nums[i+1:], path + [nums[i]], results)

    # Tạo danh sách các số từ 1 đến n
    nums = list(range(1, n + 1))
    results = []
    permute(nums, [], results)  # Gọi hàm đệ quy
    return results

# Nhập số tự nhiên n từ bàn phím
n = int(input("Nhập số tự nhiên n: "))
result = permutation(n)

# In ra kết quả
print(f"Tất cả các hoán vị của dãy số từ 1 đến {n} là:")
for p in result:
    print(p)
