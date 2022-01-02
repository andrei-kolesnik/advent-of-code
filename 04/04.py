from typing import List
import numpy as np


def assert_result(expected, actual):
    print(("PASS", actual) if actual == expected else ("FAIL", expected, actual))


def parse_input(data: List[str]) -> tuple[list[int], list[np.array]]:
    drawn_numbers_data = data.pop(0)
    drawn_numbers = [int(x) for x in drawn_numbers_data.split(',')]

    boards = []
    board = []

    for line in data:
        if not line:
            if board:
                boards.append(np.array(board))
            board = []
            continue
        board.append([int(x) for x in line.split()])

    if board:
        boards.append(np.array(board))

    return drawn_numbers, boards


def play_number_on_board(drawn_number: int, board: np.array) -> np.array:
    return np.where(board == drawn_number, 0, board)


def check_board(board: np.array) -> bool:
    bool_board = (board == 0)
    if any(bool_board.all(axis=0)):
        return True
    if any(bool_board.all(axis=1)):
        return True
    return False


def play_game(drawn_numbers: List[int], boards: list[np.array]) -> int:
    for drawn_number in drawn_numbers:
        for index, board in enumerate(boards):
            boards[index] = play_number_on_board(drawn_number=drawn_number, board=board)
            if check_board(boards[index]):
                return np.sum(boards[index]) * drawn_number
    return 0


def day_04_part_1(data: List[str]) -> int:
    drawn_numbers, boards = parse_input(data=data)
    result = play_game(drawn_numbers=drawn_numbers, boards=boards)
    return result


if __name__ == '__main__':
    with open('04-test.txt', 'r') as test_data_file:
        with open('04.txt', 'r') as real_data_file:
            test_data = [x.strip() for x in test_data_file.readlines()]
            real_data = [x.strip() for x in real_data_file.readlines()]

            assert_result(4512, day_04_part_1(data=test_data))
            assert_result(44088, day_04_part_1(data=real_data))
