def merge(arr, lf, mid, rg):
    result = [0] * (rg - lf)
    left = arr[lf:mid]
    right = arr[mid:rg]
    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


def merge_sort(arr, lf, rg):
    middle = (rg + lf) // 2
    if rg - lf > 1:  # базовый случай рекурсии

        # запускаем сортировку рекурсивно на левой половине
        merge_sort(arr, lf, middle)

        # запускаем сортировку рекурсивно на правой половине
        merge_sort(arr, middle, rg)

        # объединяем левую и правую части
        arr[lf:rg] = merge(arr, lf, middle, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
