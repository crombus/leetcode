def moving_zeros(nums):
    """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    i = 0
    j = 1
    for n in range(len(nums)-1):
        if nums[j] == 0:
            j+=1
            if nums[i] != 0:
                i+=1
        elif nums[i]==0:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i+=1
            j+=1
        else:
            i+=1
            j+=1



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 0, 5, 6, 7, 0]
    k = 3
    moving_zeros(nums)
    print(nums)