from datetime import datetime
import calendar


SECONDS_IN_DAY = 24 * 60 * 60


def calculate_days_and_seconds(
    start_date: datetime, end_date: datetime
) -> tuple[int, int]:

    # подсчет количества високосных дней по григорианскому календарю
    leap_days = calendar.leapdays(start_date.year, end_date.year + 1)

    corrected_days = (end_date - start_date).days - leap_days
    seconds_difference = SECONDS_IN_DAY - (start_date - end_date).seconds

    return corrected_days, seconds_difference


def simple_test():
    # Тест 1
    date_1 = datetime(980, 2, 12, 10, 30, 1)
    date_2 = datetime(980, 3, 1, 10, 31, 37)
    assert calculate_days_and_seconds(date_1, date_2) == (17, 96), "Тест 1 провален"

    # Тест 2
    date_1 = datetime(1001, 5, 20, 14, 15, 16)
    date_2 = datetime(9009, 9, 11, 12, 21, 11)
    assert calculate_days_and_seconds(date_1, date_2) == (
        2923033,
        79555,
    ), "Тест 2 провален"

    print("Все тесты пройдены успешно!")


def main():
    date_1 = datetime(*map(int, input().split()))
    date_2 = datetime(*map(int, input().split()))
    print(*calculate_days_and_seconds(date_1, date_2))


if __name__ == "__main__":
    # simple_test()
    main()
