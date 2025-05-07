def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def gcd_list(nums, n):
    if n == 1:
        return nums[0]
    return gcd(nums[n-1], gcd_list(nums, n-1))
nums = [12, 18, 24]
print("GCD là:", gcd_list(nums, len(nums)))
