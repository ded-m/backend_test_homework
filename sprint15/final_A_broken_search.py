#  ID посылки 93543792

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
