from collections import Counter


def calculate_diversity(player_a: list, player_b: list, changes: list) -> list:
    diversity_after_changes = []
    a_counter = Counter(player_a)
    b_counter = Counter(player_b)

    for change in changes:
        type_change, player, card = change
        if player == "A":
            if type_change == 1:
                a_counter[card] += 1
            else:
                a_counter[card] -= 1
                if a_counter[card] == 0:
                    del a_counter[card]
        else:
            if type_change == 1:
                b_counter[card] += 1
            else:
                b_counter[card] -= 1
                if b_counter[card] == 0:
                    del b_counter[card]

        common_cards = sum((a_counter & b_counter).values())
        diversity = sum(a_counter.values()) + sum(b_counter.values()) - 2 * common_cards
        diversity_after_changes.append(diversity)

    return diversity_after_changes


def simple_test():
    # Тестовые данные
    player_a = [1, 2]
    player_b = [1, 2, 3, 4, 5]
    changes = [
        (1, "A", 3),
        (1, "A", 4),
        (1, "A", 5),
        (1, "A", 6),
        (1, "A", 7),
        (-1, "A", 1),
        (1, "B", 7),
        (-1, "A", 6),
        (-1, "B", 1),
        (1, "A", 7),
    ]
    expected_output = [2, 1, 0, 1, 2, 3, 2, 1, 0, 1]

    test_output = calculate_diversity(player_a, player_b, changes)
    assert (
        test_output == expected_output
    ), f"Тест провален: ожидалось {expected_output}, получено {test_output}"
    print("Тест успешно пройден!")


def main():
    _, _, Q = map(int, input().split())
    collection_player_a = list(map(int, input().split()))
    collection_player_b = list(map(int, input().split()))
    changes_of_cards = [
        (int(type_k), player_k, int(card_k))
        for _ in range(Q)
        for type_k, player_k, card_k in [input().split()]
    ]

    variety_of_collections = calculate_diversity(
        collection_player_a, collection_player_b, changes_of_cards
    )
    print(*variety_of_collections)


if __name__ == "__main__":
    # simple_test()
    main()
