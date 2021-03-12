import copy
from collections import namedtuple
from random import choice


class Tetromino:

    def __init__(self):
        '''
        T shape
        long
        square
        L right
        L left
        S shape
        Z - left shape
        '''
        shapes = [[[0, -1], [0, 0], [0, 1], [1, 0], [0, 4], '#9816F4'],
                  [[0, -1], [0, 0], [0, 1], [0, 2], [0, 4], '#65ECF0'],
                  [[0, 0], [0, 1], [1, 0], [1, 1], [0, 4], '#EEF200'],
                  [[0, -1], [0, 0], [0, 1], [1, 1], [0, 4], '#1E00F0'],
                  [[0, -1], [0, 0], [0, 1], [1, -1], [0, 4], '#E5A50E'],
                  [[0, -1], [0, 0], [1, 0], [1, 1], [0, 4], '#61ED00'],
                  [[1, -1], [1, 0], [0, 0], [0, 1], [0, 4], '#DF3516'],
                  ]
        self.tetromino = choice(shapes)

    def __str__(self):
        return 'Positions: {}, {}, {}, {}, Origin: {}, Color: {}'.format(self.tetromino[0], self.tetromino[1], self.tetromino[2],
                                                                         self.tetromino[3], self.tetromino[4], self.tetromino[5])

    def __repr__(self):
        return 'Tetromino: ' + str(self.tetromino)

    def move_down(self, rows, columns, board):
        test_position = copy.deepcopy(self.tetromino)
        test_position[4][0] += 1
        if self.check_position(test_position, rows, columns) and self.check_existing_tetrominos(test_position, board):
            self.tetromino = copy.deepcopy(test_position)
        else:
            return True

    def move_right(self, rows, columns, board):
        test_position = copy.deepcopy(self.tetromino)
        test_position[4][1] += 1
        if self.check_position(test_position, rows, columns):
            if self.check_existing_tetrominos(test_position, board):
                self.tetromino = copy.deepcopy(test_position)

    def move_left(self, rows, columns, board):
        test_position = copy.deepcopy(self.tetromino)
        test_position[4][1] -= 1
        if self.check_position(test_position, rows, columns):
            if self.check_existing_tetrominos(test_position, board):
                self.tetromino = copy.deepcopy(test_position)

    def rotate(self, rows, columns, board):
        if self.tetromino[-1] != '#EEF200':
            test_position = copy.deepcopy(self.tetromino)
            for item in test_position[:-2]:
                item[0], item[1] = item[1], -item[0]
            if self.check_position(test_position, rows, columns):
                if self.check_existing_tetrominos(test_position, board):
                    self.tetromino = copy.deepcopy(test_position)

    def check_position(self, test_position, rows, columns):
        origin_rows = test_position[-2][0]
        origin_columns = test_position[-2][1]
        for item in test_position[:-2]:
            if origin_columns + item[1] < 0:
                return False
            elif origin_columns + item[1] > columns - 1:
                return False
            elif origin_rows + item[0] < 0:
                return False
            elif origin_rows + item[0] > rows - 1:
                return False
        return True

    def check_existing_tetrominos(self, test_position, board):
        origin_rows = test_position[-2][0]
        origin_columns = test_position[-2][1]
        for item in test_position[:-2]:
            if board[origin_rows + item[0]][origin_columns + item[1]] is not None:
                return False
        return True

    def get_origin(self):
        return self.tetromino[-2][0], self.tetromino[-2][1]

    def get_color(self):
        return self.tetromino[-1]

    def get_relative_positions(self):
        return self.tetromino[:-2]
