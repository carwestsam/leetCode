
def max_pos_not_larger_than_K(array, K):
    ln = len(array)
    left = 0
    right = ln
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] <= K:
            left = mid
        elif array[mid] > K:
            right = mid
        # print(left, right, mid)

    return left

def max_pos_smaller_then_K(array, K):
    ln = len(array)
    l = 0
    r = ln
    while l + 1 < r:
        mid = (l + r) // 2
        if array[mid] < K:
            l = mid
        else:
            r = mid

    return l

def min_pos_large_or_equal_K(array, K):
    ln = len(array)
    left = 0
    right = ln
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] >= K:
            right = mid
        else:
            left = mid

    return right
