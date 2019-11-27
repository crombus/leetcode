def plusone(digits):
    """
        :type digits: List[int]
        :rtype: List[int]
        """
    rem = 1
    for i in range(len(digits)-1,-1,-1):
        if rem != 0:
            if(digits[i]==9 and i==0):
                digits[i] = 0
                digits.insert(0, 1)
            elif(digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                rem = 0      
                break
    return digits


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 0, 5, 6, 7, 0]
    k = 3
    print("Actual number --> " ,nums)
    print(plusone(nums))