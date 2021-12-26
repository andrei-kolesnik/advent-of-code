from typing import List


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


if __name__ == '__main__':
    with open('03-test.txt', 'r') as test_data_file:
        with open('03.txt', 'r') as real_data_file:
            test_data = [x.strip() for x in test_data_file.readlines()]
            real_data = [x.strip() for x in real_data_file.readlines()]

            assert_result(198, day_03_part_1(data=test_data))
            assert_result(3969000, day_03_part_1(data=real_data))
