def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=list()
        d={}
        j=0
        for j in range(len(nums2)-1):
            if nums2[j]> nums2[j+1]:
                d[nums2[j]]=-1
            else:
                d[nums2[j]]=nums2[j+1]
        d[nums2[len(nums2)-1]]=-1
            
        for j in nums1:
            l.append(d[j])
            
        return l
