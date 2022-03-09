
def swap(arr_list, pos_i, pos_j):
    temp = arr_list[pos_i]
    arr_list[pos_i] = arr_list[pos_j]
    arr_list[pos_j] = temp


def qsort_recursion(nums, left, right):
    if left >= right:
        return
    swap(nums, left, int((left + right) / 2))
    last = left
    for i in range(left + 1, right + 1):
        if nums[i] < nums[left]:
            last = last + 1
            swap(nums, last, i)
    swap(nums, left, last)
    qsort_recursion(nums, left, last - 1)
    qsort_recursion(nums, last + 1, right)


def qsort(nums):
    qsort_recursion(nums, 0, len(nums) - 1)


test_data = [1, 2, 5, 4, 3, 6, 9, 7, 0, 8]
qsort(test_data)
print(test_data)

