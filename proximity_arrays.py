def calc_prefix_similarity(arr1, arr2):
    """Вычисления длины наибольшего общего префикса между двумя массивами."""
    min_length = min(len(arr1), len(arr2))
    for i in range(min_length):
        if arr1[i] != arr2[i]:
            return i
    return min_length


def total_proximity(arrays: list[list[int]]) -> int:
    """Вычисление суммарной близости между всеми парами массивов."""
    total = 0
    n = len(arrays)
    for i in range(n):
        for j in range(i + 1, n):
            total += calc_prefix_similarity(arrays[i], arrays[j])
    return total


def main():
    n = int(input())  # Считываем количество массивов

    arrays = []
    for _ in range(n):
        input()  # Считываем размер массива и далее не используем
        arrays.append(list(map(int, input().split())))

    result = total_proximity(arrays)
    print(result)  # Выводим результат


def test_total_proximity():
    # Первый тестовый набор
    arrays_1 = [[1, 2], [1, 3], [1, 2, 3]]
    expected_1 = 4
    assert (
        total_proximity(arrays_1) == expected_1
    ), f"Тест 1 провален: ожидалось {expected_1}, получено {total_proximity(arrays_1)}"

    # Второй тестовый набор
    arrays_2 = [[5], [1, 2], [5, 1, 2]]
    expected_2 = 1
    assert (
        total_proximity(arrays_2) == expected_2
    ), f"Тест 2 провален: ожидалось {expected_2}, получено {total_proximity(arrays_2)}"

    print("Все тесты успешно пройдены!")


if __name__ == "__main__":
    # test_total_proximity()
    main()
