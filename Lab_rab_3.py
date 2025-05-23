from collections import deque, defaultdict, namedtuple
from timeit import timeit


# Способ 1
def knight_moves_array(start, end):
    start_col, start_row = ord(start[0].upper()) - ord('A'), int(start[1]) - 1
    end_col, end_row = ord(end[0].upper()) - ord('A'), int(end[1]) - 1

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[start_row][start_col] = 0

    q = deque()
    q.append((start_row, start_col))

    while q:
        row, col = q.popleft()

        if row == end_row and col == end_col:
            return board[row][col]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col] == -1:
                board[new_row][new_col] = board[row][col] + 1
                q.append((new_row, new_col))

    return -1


# Способ 2
def build_knight_graph():
    graph = defaultdict(list)
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for row in range(8):
        for col in range(8):
            for dr, dc in moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    graph[(row, col)].append((new_row, new_col))

    return graph


def knight_moves_linked_list(start, end):
    start_col, start_row = ord(start[0].upper()) - ord('A'), int(start[1]) - 1
    end_col, end_row = ord(end[0].upper()) - ord('A'), int(end[1]) - 1

    visited = {}
    q = deque()
    q.append((start_row, start_col))
    visited[(start_row, start_col)] = 0
    graph = build_knight_graph()

    while q:
        row, col = q.popleft()

        if row == end_row and col == end_col:
            return visited[(row, col)]

        for neighbor in graph[(row, col)]:
            if neighbor not in visited:
                visited[neighbor] = visited[(row, col)] + 1
                q.append(neighbor)

    return -1


# Способ 3
def knight_moves_library(start, end):
    Position = namedtuple('Position', ['row', 'col'])

    start_col, start_row = ord(start[0].upper()) - ord('A'), int(start[1]) - 1
    end_col, end_row = ord(end[0].upper()) - ord('A'), int(end[1]) - 1

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    visited = {}
    q = deque()
    q.append(Position(start_row, start_col))
    visited[Position(start_row, start_col)] = 0

    while q:
        current = q.popleft()

        if current.row == end_row and current.col == end_col:
            return visited[current]

        for dr, dc in moves:
            new_pos = Position(current.row + dr, current.col + dc)
            if 0 <= new_pos.row < 8 and 0 <= new_pos.col < 8 and new_pos not in visited:
                visited[new_pos] = visited[current] + 1
                q.append(new_pos)

    return -1


def main():

    print("======================================")
    print("Выполнил: Борисов Данила Александрович")
    print("Группа:   090304-РПИа-o24")
    print("======================================")

    start, end = "A5", "C2"

    print(knight_moves_array(start, end))

    print(knight_moves_linked_list(start, end))

    print(knight_moves_library(start, end))

    # Сравнение производительности способов
    test_cases = [("A1", "H8"), ("B3", "G5"), ("D4", "D4")]

    implementations = [
     ("Array", knight_moves_array),
     ("Linked List", knight_moves_linked_list),
     ("Library", knight_moves_library)]

    for name, impl in implementations:
        print(f"\nTesting {name}:")
        for test in test_cases:
            t = timeit(lambda: impl(*test), number=10000)
            print(f"{test}: {impl(*test)} moves, time: {t:.5f}s")


if __name__ == "__main__":
    main()
