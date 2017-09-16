compareTimes = 0


def get_ct():
    global compareTimes
    return compareTimes


def set_ct(v):
    global compareTimes
    compareTimes = v


def compare(a, b):
    global compareTimes
    compareTimes += 1
    if a >= b:
        return True
    else:
        return False


def raw(nums):
    first = 0
    second = 0
    print('raw', nums)

    if compare(second, first):
        first, second = second, first

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first >= num and num > second:
            second = num

    print(first, second)
    return first, second


def down(nums, i, n):
    l = i * 2 + 1
    r = i * 2 + 2

    if l >= n:
        return
    larger = nums[l]
    ti = l

    if r < n and compare(nums[r], nums[l]):
        larger = nums[r]
        ti = r

    if compare(larger, nums[i]):
        t = nums[i]
        nums[i] = nums[ti]
        nums[ti] = t
        down(nums, ti, n)


def sol1(nums):
    n = len(nums)
    # print(nums)
    for i in range(n // 2 - 1, -1, -1):
        down(nums, i, n)
    # print(nums)

    first = nums[0]
    second = max(nums[1], nums[2])
    return first, second


def divide(nums, l, r):
    f, s = 0,0
    if r - l == 1:
        if compare(nums[l], nums[r]):
            f,s= nums[l], nums[r]
        else:
            f,s= nums[r], nums[l]
    elif r == l:
        f,s= nums[l], 0
    else:

        mid = (l + r) // 2
        lf, ls = divide(nums, l, mid)
        rf, rs = divide(nums, mid + 1, r)

        if compare(lf, rf):
            if compare(ls, rf):
                f,s= lf, ls
            else:
                f,s= lf, rf
        else:
            if compare(rs, lf):
                f,s= rf, rs
            else:
                f,s= rf, lf

    return f,s

def sol2(nums):
    n = len(nums)
    first, second = divide(nums, 0, n - 1)
    print(first, second)

    return first, second
