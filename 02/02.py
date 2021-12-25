from typing import List


def assert_result(expected, actual):
    print(("PASS", actual) if actual == expected else ("FAIL", expected, actual))


def day_02_part_1(data: List[str]) -> int:
    x = 0
    y = 0

    for instruction in data:
        words = instruction.split()
        direction = words[0]
        distance = int(words[1])
        if direction == 'forward':
            x += distance
        elif direction == 'down':
            y += distance
        elif direction == 'up':
            y -= distance

    return x * y


def day_02_part_2(data: List[str]) -> int:
    x = 0
    y = 0
    aim = 0

    for instruction in data:
        words = instruction.split()
        direction = words[0]
        distance = int(words[1])
        if direction == 'forward':
            x += distance
            y += aim * distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

    return x * y

if __name__ == '__main__':
    with open('02-test.txt', 'r') as test_data_file:
        with open('02.txt', 'r') as real_data_file:
            test_data = test_data_file.readlines()
            real_data = real_data_file.readlines()

            assert_result(150, day_02_part_1(data=test_data))
            assert_result(1728414, day_02_part_1(data=real_data))

            assert_result(900, day_02_part_2(data=test_data))
            assert_result(1765720035, day_02_part_2(data=real_data))
