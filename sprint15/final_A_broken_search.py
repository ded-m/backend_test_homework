#  ID посылки 92472381

def broken_search(nums, target) -> int:
    left = 0
    right = len(nums)-1
    # бинарный поиск
    while (right - left) >= 0:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid + 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

    arr = [5, 1]
    assert broken_search(arr, 1) == 1

    arr = [3, 5, 6, 7, 9, 1, 2]
    assert broken_search(arr, 4) == -1


test()
