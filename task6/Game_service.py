class GameService:
    @staticmethod
    def get_best_score():
        f = open('bestscore.txt', 'r')
        score = f.readline()
        f.close()
        return int(score) if isinstance(score, str) else 0

    @staticmethod
    def save_best_score(score):
        if not isinstance(score, int)\
                and not isinstance(score, str):
            raise ValueError('Invalid type of score!')
        f = open('bestscore.txt', 'w+')
        f.truncate()
        f.write(str(score))
        f.close()
