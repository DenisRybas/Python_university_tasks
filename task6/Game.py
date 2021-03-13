import sys
import copy
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from Tetromino import Tetromino
from Game_service import GameService


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.rows = 20
        self.columns = 10
        self.point_tetromino = 10
        self.points_line = 100
        self.label = {}
        self.next_tetromino_label = {}
        self.score = 0
        self.lines = 0
        self.board = []
        self.next_tetromino_board = []
        self.board_color_hex = '#191919'
        self.grid_color_hex = '#7a7a6d'
        self.game_running = False
        self.message = "New game is loaded"
        self.best_score = GameService.get_best_score()
        self.setStyleSheet(f"background-color:{self.board_color_hex};")
        self.setWindowTitle("Tetris")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.main_page()

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)

        self.next_tetromino = Tetromino()
        self.new_tetromino = self.next_tetromino
        self.start_game()

    def main_page(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        horizontal_next_layout = QHBoxLayout()
        horizontal_next_layout.setSpacing(50)
        vertical_next_board = QVBoxLayout()
        horizontal_next_layout.addLayout(vertical_next_board)
        for row in range(0, 4):
            horizontal_next_board = QHBoxLayout()
            horizontal_next_board.setSpacing(0)
            for column in range(0, 4):
                self.next_tetromino_label[row, column] = self.create_cell()
                horizontal_next_board.addWidget(self.next_tetromino_label[row, column], 0, Qt.AlignTop)
            vertical_next_board.addLayout(horizontal_next_board)
            vertical_next_board.setSpacing(0)
        main_layout.addLayout(horizontal_next_layout)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(50)

        vertical_board = QVBoxLayout()
        horizontal_layout.addLayout(vertical_board)
        for row in range(0, self.rows):
            horizontal_board = QHBoxLayout()
            horizontal_board.setSpacing(0)
            for column in range(0, self.columns):
                self.label[row, column] = self.create_cell()
                horizontal_board.addWidget(self.label[row, column])
            vertical_board.addLayout(horizontal_board)
            vertical_board.setSpacing(0)

        main_layout.addLayout(horizontal_layout)
        self.show()
        self.setFixedSize(self.size())

    def create_cell(self):
        cell = QLabel(self)
        cell.setFixedHeight(60)
        cell.setFixedWidth(60)
        cell.setStyleSheet(f"background-color:{self.board_color_hex};"
                           f"border: 1px inset {self.grid_color_hex}")
        return cell

    def start_game(self):
        self.score = 0
        self.lines = 0
        self.board = []
        self.init_board()
        self.add_new_tetromino()
        self.update_tetromino()
        self.update_board()
        self.game_running = True

    def delete_tetromino(self):
        sheet = f"background-color:{self.board_color_hex};border: 1px inset {self.grid_color_hex}"
        origin_rows, origin_columns = self.new_tetromino.get_origin()
        for item in self.new_tetromino.get_relative_positions():
            self.label[origin_rows + item[0], origin_columns + item[1]].setStyleSheet(sheet)

    def update_tetromino(self):
        sheet = "background-color:" + self.new_tetromino.get_color() + f";border: 1px inset {self.grid_color_hex}"
        origin_rows, origin_columns = self.new_tetromino.get_origin()
        for item in self.new_tetromino.get_relative_positions():
            self.label[origin_rows + item[0], origin_columns + item[1]].setStyleSheet(sheet)

    def check_move_down(self):
        self.delete_tetromino()
        if self.new_tetromino.move_down(self.rows, self.columns, self.board):
            self.add_tetromino_to_board()
            self.check_full_lines()
            self.add_new_tetromino()
            self.update_tetromino()
            self.update_board()
            test_position = copy.deepcopy(self.new_tetromino.tetromino)
            test_position[4][0] += 1
            if GameService.check_existing_tetrominos(test_position, self.board) is False:
                self.game_over()
        self.update_tetromino()

    def add_new_tetromino(self):
        self.score += self.point_tetromino
        self.update_statusbar()
        self.new_tetromino = self.next_tetromino
        self.next_tetromino = Tetromino()
        self.draw_next_tetromino()

    def init_board(self):
        for row in range(self.rows):
            line = [None] * self.columns
            self.board.append(line)

    def add_tetromino_to_board(self):
        origin_rows, origin_columns = self.new_tetromino.get_origin()
        for item in self.new_tetromino.get_relative_positions():
            self.board[item[0] + origin_rows][item[1] + origin_columns] = self.new_tetromino.get_color()

    def update_board(self):
        for counter_row, row in enumerate(self.board):
            for counter_column, column in enumerate(row):
                if column is not None:
                    sheet = "background-color:" + column + f";border: 1px inset {self.grid_color_hex}"
                    self.label[counter_row, counter_column].setStyleSheet(sheet)
                else:
                    sheet = f"background-color:{self.board_color_hex};border: 1px inset {self.grid_color_hex}"
                    self.label[counter_row, counter_column].setStyleSheet(sheet)

    def check_full_lines(self):
        counter_row = self.rows - 1
        for row in reversed(self.board):
            if None not in row:
                for i in range(counter_row):
                    self.board[counter_row - i] = copy.deepcopy(self.board[counter_row - 1 - i])
                self.board[0] = [None] * self.columns
                self.check_full_lines()
                self.score += self.points_line
                self.lines += 1
                self.update_statusbar()
            counter_row -= 1

    def draw_next_tetromino(self):
        clear_sheet = "background-color:" + self.board_color_hex + f";border: 1px inset {self.grid_color_hex}"
        sheet = "background-color:" + self.next_tetromino.get_color() + f";border: 1px inset {self.grid_color_hex}"
        origin_rows, origin_columns = self.next_tetromino.get_origin()

        for row in range(0, 4):
            for column in range(0, 4):
                self.next_tetromino_label[row, column].setStyleSheet(clear_sheet)

        for item in self.next_tetromino.get_relative_positions():
            self.next_tetromino_label[origin_rows + item[0] + 1, origin_columns + item[1] - 3].setStyleSheet(sheet)

    def update_statusbar(self):
        speed = int(1000 * (1 - (self.lines // 5 / 10)))
        self.message = f'Score:{self.score} Number of lines: {self.lines} Best score: {self.best_score}'
        self.statusBar().setStyleSheet("color: rgb(255, 255, 255);")
        self.statusBar().showMessage(self.message)
        self.timer.start(speed)

    def game_over(self):
        self.game_running = False
        game_over = QMessageBox()
        game_over.setIcon(QMessageBox.Information)
        game_over.setText("Game over")
        game_over.setInformativeText("Score: " + str(self.score) + '\nNumber of lines: ' + str(self.lines))
        game_over.setWindowTitle("Game over")
        if self.score > self.best_score:
            GameService.save_best_score(score=self.score)
            self.best_score = self.score
        game_over.setStandardButtons(QMessageBox.Ok)
        game_over.buttonClicked.connect(self.start_game)
        game_over.exec_()

    def timer_event(self):
        if self.game_running is True:
            self.check_move_down()

    def keyPressEvent(self, event):
        pressedkey = event.key()
        if pressedkey == Qt.Key_P:
            if self.game_running is True:
                self.game_running = False
            else:
                self.game_running = True
            event.accept()
        if self.game_running is True:
            if pressedkey == Qt.Key_Up:
                self.delete_tetromino()
                self.new_tetromino.rotate(self.rows, self.columns, self.board)
                self.update_tetromino()
                event.accept()
            elif pressedkey == Qt.Key_Down:
                self.check_move_down()
                event.accept()
            elif pressedkey == Qt.Key_Left:
                self.delete_tetromino()
                self.new_tetromino.move_left(self.rows, self.columns, self.board)
                self.update_tetromino()
                event.accept()
            elif pressedkey == Qt.Key_Right:
                self.delete_tetromino()
                self.new_tetromino.move_right(self.rows, self.columns, self.board)
                self.update_tetromino()
                event.accept()
            else:
                event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
