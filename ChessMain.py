import sys
import ChessAi.ChessMainWindow as window
import ChessAi.ChessItem as ChessIcon
import ChessAi.Tools as tools

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class ChessApplication(QMainWindow):
    def __init__(self):
        super(ChessApplication, self).__init__()
        # 棋盘开始位置
        self.chessStartPos = 20
        # 棋盘结束位置
        self.chessEndPos = 770
        # 棋盘线条偏移量
        self.chessLineOffset = (self.chessEndPos - self.chessStartPos)/14
        # 棋子半径
        self.chessRadius = 13
        self.playerBlack = False
        self.chessMove = ChessIcon.ChessMove()
        self.chessRect = ChessIcon.ChessRect()
        # 棋盘矩阵,初始化为-1, 0为白子, 1为黑子
        self.chessMat = [[-1 for i in range(15)] for n in range(15)]
        self.CHESS_WHITE = 0
        self.CHESS_BLACK = 1
        self.InitWidgets()

    def InitWidgets(self):
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        # 棋盘
        self.chessScene = QtWidgets.QGraphicsScene()
        self.chessScene.setSceneRect(self.chessStartPos, self.chessStartPos,
                                     self.chessEndPos, self.chessEndPos)
        self.ui.ChessView.setScene(self.chessScene)
        self.ui.ChessView.setEnabled(False)

        self.ui.StartButton.clicked.connect(self.StartButtonClick)
        self.ui.FailButton.clicked.connect(self.FailButtonClick)
        self.ui.ExitButton.clicked.connect(self.ExitButtonClick)
        self.ui.ChooseBlack.clicked.connect(self.ChooseBlackClick)
        self.InitChessView()

    # 绘制棋盘
    def InitChessView(self):
        self.chessScene.clear()
        for i in range(15):
            self.chessScene.addLine(self.chessStartPos, self.chessStartPos + self.chessLineOffset * i,
                                    self.chessEndPos, self.chessStartPos + self.chessLineOffset * i)
            self.chessScene.addLine(self.chessStartPos + self.chessLineOffset * i, self.chessStartPos,
                                    self.chessStartPos + self.chessLineOffset * i, self.chessEndPos)
        # 棋盘上的五个点
        points = [None for i in range(5)]
        points[0] = ChessIcon.ChessFivePoint()
        points[1] = ChessIcon.ChessFivePoint()
        points[2] = ChessIcon.ChessFivePoint()
        points[3] = ChessIcon.ChessFivePoint()
        points[4] = ChessIcon.ChessFivePoint()
        points[0].setPos(self.chessStartPos + 3 * self.chessLineOffset - self.chessRadius,
                         self.chessStartPos + 3 * self.chessLineOffset - self.chessRadius)
        points[1].setPos(self.chessStartPos + 11 * self.chessLineOffset - self.chessRadius,
                      self.chessStartPos + 3 * self.chessLineOffset - self.chessRadius)
        points[2].setPos(self.chessStartPos + 7 * self.chessLineOffset - self.chessRadius,
                      self.chessStartPos + 7 * self.chessLineOffset - self.chessRadius)
        points[3].setPos(self.chessStartPos + 3 * self.chessLineOffset - self.chessRadius,
                      self.chessStartPos + 11 * self.chessLineOffset - self.chessRadius)
        points[4].setPos(self.chessStartPos + 11 * self.chessLineOffset - self.chessRadius,
                      self.chessStartPos + 11 * self.chessLineOffset - self.chessRadius)
        for point in points:
            point.show()
            self.chessScene.addItem(point)

    # 下一步棋
    def PutOneChess(self, indexX, indexY, chessKind):
        if self.chessMat[indexX][indexY] != -1:
            return
        chessItem = ChessIcon.ChessItem(chessKind)
        chessItem.setPos(self.chessStartPos + indexX * self.chessLineOffset - self.chessRadius,
                         self.chessStartPos + indexY * self.chessLineOffset - self.chessRadius)
        chessItem.show()
        self.chessScene.addItem(chessItem)
        self.chessScene.removeItem(self.chessRect)
        self.chessRect.setPos(self.chessStartPos + indexX * self.chessLineOffset - self.chessRadius,
                              self.chessStartPos + indexY * self.chessLineOffset - self.chessRadius)
        self.chessRect.show()
        self.chessScene.addItem(self.chessRect)
        self.chessMat[indexX][indexY] = chessKind
        if tools.IsGobangWin(self.chessMat, indexX, indexY):
            self.ui.ResultLabel.setText("五连珠黑胜!")


# Ui CallBack Function
    # 开始
    def StartButtonClick(self):
        print('Button Clicked!')
    # 认输
    def FailButtonClick(self):
        print('Fail Button!')
    # 退出
    def ExitButtonClick(self):
        self.close()
    # 选先手
    def ChooseBlackClick(self):
        self.playerBlack = self.ui.ChooseBlack.isChecked()
        print(self.playerBlack)

    def mouseMoveEvent(self, event):
        if not self.IsMouseInChessView(event.x(), event.y()):
            super(ChessApplication, self).mouseMoveEvent(event)
            return
        indexX, indexY = self.GetClickChessIndex(event.x(), event.y())
        self.chessScene.removeItem(self.chessMove)
        self.chessMove.setPos(self.chessStartPos + indexX * self.chessLineOffset - self.chessRadius,
                              self.chessStartPos + indexY * self.chessLineOffset - self.chessRadius)
        self.chessMove.show()
        self.chessScene.addItem(self.chessMove)
        super(ChessApplication, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if not self.IsMouseInChessView(event.x(), event.y()):
            super(ChessApplication, self).mouseMoveEvent(event)
            return
        indexX,indexY = self.GetClickChessIndex(event.x(), event.y())
        #if self.chessMat[indexX][indexY] not

        self.PutOneChess(indexX, indexY, self.CHESS_BLACK)
        super(ChessApplication, self).mouseReleaseEvent(event)

# Tools Func
    # 判断鼠标是否在棋盘中
    def IsMouseInChessView(self, x, y):
        if x < 1 or x > self.chessEndPos + 10\
                or y < 1 or y > self.chessEndPos + 10:
            return False
        return True
    # 返回点击时,鼠标指向的棋子
    def GetClickChessIndex(self, x, y):
        posX = abs(x - self.chessStartPos)
        posY = abs(y - self.chessStartPos)
        indexX = round(posX / self.chessLineOffset)
        indexY = round(posY / self.chessLineOffset)
        return indexX, indexY

if __name__ == '__main__':
    process = QApplication(sys.argv)
    app = ChessApplication()
    app.show()
    sys.exit(process.exec())
