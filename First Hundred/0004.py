def findKthmax(a, b, i, j, m, n, k):
    if m > n:
        return findKthmax(b, a, j, i, n, m, k)
    
    if m == 0: return b[j+k-1]
    if k == 1: return min(a[i], b[j])
    x = min(k//2, m)
    y = k - x
    if a[i+x-1] < b[j+y-1]:
        return findKthmax(a, b, i+x, j, m-x, n, k-x)
    else:
        if a[i+x-1] > b[j+y-1]:
            return findKthmax(a, b, i, j+y, m, n-y, k-y)
        else:
            return a[i+x-1]

def findMedianSortedArrays(nums1, nums2):
    m = nums1.__len__()
    n = nums2.__len__()
    tot = m + n
    if tot%2 != 0:
        return findKthmax(nums1, nums2, 0, 0, m, n, tot//2+1)
    else:
        return (findKthmax(nums1, nums2, 0, 0, m, n, tot//2)+findKthmax(nums1, nums2, 0, 0, m, n, tot//2+1))/2

print(findMedianSortedArrays([1,2],[3,4]))
