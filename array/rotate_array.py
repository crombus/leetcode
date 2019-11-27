
def rotate_array(nums, k):
    nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]











if __name__ == '__main__':
    nums = [1, 2, 3, 4, 0, 5, 6, 7, 0]
    k = 3
    rotate_array(nums, k)
    print(nums)