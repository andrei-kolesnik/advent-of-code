from typing import List
from operator import lt, gt


def assert_result(expected, actual):
    print(("PASS", actual) if actual == expected else ("FAIL", expected, actual))


def day_03_part_1(data: List[str]) -> int:
    counters = [0] * len(data[0])
    for number in data:
        for position, digit in enumerate(number):
            counters[position] += 1 if int(digit) else -1

    gamma = 0
    epsilon = 0
    for counter in counters:
        gamma *= 2
        epsilon *= 2
        if counter > 0:
            gamma += 1
        elif counter < 0:
            epsilon += 1
        else:
            print("ERROR in data: equal numbers of digits")

    return gamma * epsilon


def day_03_part_2_filter(data: List[str], position: int, operator, tie_breaker: int) -> List[str]:
    part_one = []
    part_zero = []
    for number in data:
        if int(number[position]):
            part_one.append(number)
        else:
            part_zero.append(number)
    if operator(len(part_zero), len(part_one)):
        return part_zero
    elif operator(len(part_one), len(part_zero)):
        return part_one
    return part_one if tie_breaker else part_zero


def day_03_part_2_for_digit(data: List[str], digit: int) -> int:
    for position in range(len(data[0])):
        data = day_03_part_2_filter(data=data, position=position, operator=gt if digit else lt, tie_breaker=digit)
        if len(data) == 1:
            return int(data[0], 2)
    print("ERROR in data: more than one answer")
    return 0


def day_03_part_2(data: List[str]) -> int:
    oxygen_generator_rating = day_03_part_2_for_digit(data=data, digit=1)
    co2_scrubber_rating = day_03_part_2_for_digit(data=data, digit=0)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    with open('03-test.txt', 'r') as test_data_file:
        with open('03.txt', 'r') as real_data_file:
            test_data = [x.strip() for x in test_data_file.readlines()]
            real_data = [x.strip() for x in real_data_file.readlines()]

            assert_result(198, day_03_part_1(data=test_data))
            assert_result(3969000, day_03_part_1(data=real_data))

            assert_result(230, day_03_part_2(data=test_data))
            assert_result(4267809, day_03_part_2(data=real_data))

