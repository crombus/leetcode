def intersect(nums1, nums2):
     """
     :type nums1: List[int]
     :type nums2: List[int]
     :rtype: List[int]
     """
     """x = set(nums1)
     y = set(nums2)
     return x.intersection(y)"""
     y = list()
     x = dict()
     for i in nums1:
         if x.__contains__(i):
             x[i]+=1
         else:
             x.update({i: 1})
        
     for i in nums2:
        if x.__contains__(i):
            if x[i]>1:
                x[i] -= 1
            else:
                x.pop(i)
                y.append(i)
     return y



if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 0, 5, 6, 7, 0]
    nums2 = [4,8,4,8,1,1,1,1,1,1]
    print(intersect(nums1, nums2))
    