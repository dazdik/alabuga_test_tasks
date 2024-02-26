def calculate_language_barriers(N: int, languages: str, hierarchy_structure: str):

    languages_dict = {i + 1: lang for i, lang in enumerate(languages.split())}

    parent_mapping = {i: None for i in range(N + 1)}
    children_mapping = {i: [] for i in range(N + 1)}

    stack = []
    for emp in hierarchy_structure.split():
        emp = int(emp)
        if stack and stack[-1] == emp:
            stack.pop()
        else:
            if stack:
                parent_mapping[emp] = stack[-1]
                children_mapping[stack[-1]].append(emp)
            stack.append(emp)

    def find_barrier(emp_id, target_language):
        if emp_id == 0 or languages_dict[emp_id] == target_language:
            return 0
        else:
            return 1 + find_barrier(parent_mapping[emp_id], target_language)

    barriers = {}
    for emp_id in range(1, N + 1):
        barriers[emp_id] = find_barrier(parent_mapping[emp_id], languages_dict[emp_id])

    return [barriers[i] for i in range(1, N + 1)]


def test_calculate_language_barriers():
    # Тест 1
    n1 = 5
    languages1 = "A B B A B"
    hierarchy_structure1 = "0 1 1 2 3 4 4 5 5 3 2 0"
    expected_output1 = [0, 0, 0, 2, 0]
    assert (
        calculate_language_barriers(n1, languages1, hierarchy_structure1)
        == expected_output1
    )
    print("Тест 1 пройден успешно!")

    # Тест 2
    n2 = 4
    languages2 = "A B A A"
    hierarchy_structure2 = "0 1 2 3 3 4 4 2 1 0"
    expected_output2 = [0, 1, 1, 1]
    assert (
        calculate_language_barriers(n2, languages2, hierarchy_structure2)
        == expected_output2
    )
    print("Тест 2 пройден успешно!")


def main():
    n = int(input())
    languages, hierarchy = input(), input()
    print(*calculate_language_barriers(n, languages, hierarchy))


if __name__ == "__main__":
    # test_calculate_language_barriers()
    main()
