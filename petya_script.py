def calculate_result(rows, keys, values, constraints):

    res = 0
    for i_row in range(rows):
        row = values[i_row]

        # Проверка для каждой строки
        if all(
            check_constraint(row, var, sign, val, keys)
            for var, sign, val in constraints
        ):
            res += sum(row)

    return res


def check_constraint(
    row: list[int], column_name: str, sign: str, value: int, keys: list[str]
) -> bool:

    column_index = keys.index(column_name)

    if sign == ">" and not (row[column_index] > value):
        return False
    if sign == "<" and not (row[column_index] < value):
        return False
    return True


def main():
    rows, columns, constr = map(int, input().split())

    keys = input().split()
    values = [[int(num) for num in input().split()] for _ in range(rows)]
    constraints = [
        (var, sign, int(num))
        for _ in range(constr)
        for var, sign, num in [input().split()]
    ]
    print(calculate_result(rows, keys, values, constraints))


def test_calculate_result():
    rows, columns, constr = (2, 2, 3)
    keys = ["a", "b"]
    values = [[1, 1], [2, 2]]
    constraints = [("a", "<", 3), ("b", ">", 1), ("b", "<", 3)]

    expected_output = 4
    assert calculate_result(rows, keys, values, constraints) == expected_output
    print("Тест успешно пройден!")


if __name__ == "__main__":
    # test_calculate_result()
    main()
