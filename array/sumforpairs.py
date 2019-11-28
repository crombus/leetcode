def twoSum(nums, target):

        table = dict()

        for i in enumerate(nums):
            if target - i[1] in table:
                return [i[0] , table[target - i[1]]]
            else :
                table[i[1]] = i[0]

def twoSum_brut_force(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    k=list()
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                k.append(i)
                k.append(j)
                break
        
    return k

if __name__ == '__main__':
    nums = [8, 9, 2, 6, 3, 5]
    k = 5
    print("Efficent way --->" ,twoSum(nums, k))
    print("Brut Force way --->" ,twoSum_brut_force(nums, k))