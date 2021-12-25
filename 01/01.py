from typing import List


def assert_result(expected, actual):
    print(("PASS", actual) if actual == expected else ("FAIL", expected, actual))


def day_01_part_1_brute(data: List[int]) -> int:
    previous_number = data[0]
    count = 0
    for number in data[1:]:
        if number > previous_number:
            count += 1
        previous_number = number
    return count


def day_01_part_1_comprehension(data: List[int]) -> int:
    return len([1 for (current, previous) in zip(data, [data[0]] + data[0:-1]) if current > previous])


def day_01_part_2_brute(data: List[int]) -> int:
    previous_number3 = data[0]
    previous_number2 = data[1]
    previous_number1 = data[2]
    count = 0
    for index, number in enumerate(data[3:], start=3):
        if data[index-2] + data[index-1] + data[index] > previous_number1 + previous_number2 + previous_number3:
            count += 1
        previous_number3 = previous_number2
        previous_number2 = previous_number1
        previous_number1 = number
    return count


def day_01_generic(data: List[int], window_size: int) -> int:
    window = data[0:window_size]
    count = 0
    for index, number in enumerate(data[window_size:], start=window_size):
        if sum(data[index-window_size+1:index+1]) > sum(window):
            count += 1
        window = window[1:] + [data[index]]
    return count


if __name__ == '__main__':
    with open('01-test.txt', 'r') as test_data_file:
        with open('01.txt', 'r') as real_data_file:
            test_data = [int(x) for x in test_data_file.readlines()]
            real_data = [int(x) for x in real_data_file.readlines()]

            assert_result(7, day_01_part_1_brute(data=test_data))
            assert_result(7, day_01_part_1_comprehension(data=test_data))
            assert_result(7, day_01_generic(data=test_data, window_size=1))
            assert_result(1446, day_01_part_1_brute(data=real_data))
            assert_result(1446, day_01_part_1_comprehension(data=real_data))
            assert_result(1446, day_01_generic(data=real_data, window_size=1))

            assert_result(5, day_01_part_2_brute(data=test_data))
            assert_result(5, day_01_generic(data=test_data, window_size=3))
            assert_result(1486, day_01_part_2_brute(data=real_data))
            assert_result(1486, day_01_generic(data=real_data, window_size=3))
