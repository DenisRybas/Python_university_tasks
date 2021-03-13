class GameService:
    @staticmethod
    def get_best_score():
        f = open('bestscore.txt', 'r')
        score = f.readline()
        f.close()
        return int(score) if isinstance(score, str) else 0

    @staticmethod
    def save_best_score(score):
        if not isinstance(score, int) \
                and not isinstance(score, str):
            raise ValueError('Invalid type of score!')
        f = open('bestscore.txt', 'w+')
        f.truncate()
        f.write(str(score))
        f.close()

    @staticmethod
    def check_position(test_position, rows, columns):
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

    @staticmethod
    def check_existing_tetrominos(test_position, board):
        origin_rows = test_position[-2][0]
        origin_columns = test_position[-2][1]
        for item in test_position[:-2]:
            if board[origin_rows + item[0]][origin_columns + item[1]] is not None:
                return False
        return True
