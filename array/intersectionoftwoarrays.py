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

def intersect_opt(nums1, nums2):
    large=nums1
    small=nums2
    if len(large)<len(small):
        nums1,nums2=large,small
    d={}
    for n in nums1:
        if n in d:
            d[n]+=1
        else:
            d[n]=1
    s=[]
    for n in nums2:
        if n in d and d[n]>0:
            s+=[n]
            d[n]-=1
    return s


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 0, 5, 6, 7, 0]
    nums2 = [4,8,4,8,1,1,1,1,1,1]
    print(intersect(nums1, nums2))
    print(intersect_opt(nums1,nums2))
    