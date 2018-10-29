
import gobang.ui.main_window as window
import gobang.ui.chess_item as ChessIcon

from gobang.ui.chess_item import ChessType
from gobang.algorithm.strategy_interface import StrategyInterface
from gobang.algorithm.strategy_factory import StrategyFactory
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from enum import Enum

class GameStatus(Enum):
    STOP = 0
    PLAYING = 1

class GameType(Enum):
    PLAYINGSINGLE = 1
    PLAYINGMULTI = 2

class ChessApplication(QMainWindow):
    def __init__(self):
        super(ChessApplication, self).__init__()
        # 棋盘开始位置
        self.chessStartPos = 20
        # 棋盘结束位置
        self.chessEndPos = 770
        # 棋盘线条偏移量
        self.chessLineOffset = (self.chessEndPos - self.chessStartPos) / 14
        # 棋子半径
        self.chessRadius = 13
        self.chessMove = None
        self.chessRect = None
        # 棋盘矩阵,初始化为-1, 0为白子, 1为黑子
        self.chessMat = [[]]
        self.currentChessType = ChessType.BLACK
        self.playerChessType = ChessType.BLACK
        # ui
        self.ui = window.Ui_MainWindow()
        self.chessScene = QtWidgets.QGraphicsScene()
        self.InitWidgets()
        # Application
        self.strategyInstance = StrategyFactory.ProvideInstance()
        self.gameStatus = GameStatus.STOP
        self.gameType = GameType.PLAYINGSINGLE
        self.InitGame()

    def InitWidgets(self):
        self.ui.setupUi(self)
        # 棋盘
        self.chessScene.setSceneRect(self.chessStartPos, self.chessStartPos,
                                     self.chessEndPos, self.chessEndPos)
        self.ui.chessView.setScene(self.chessScene)
        self.ui.chessView.setEnabled(False)
        self.ui.chooseBlack.setChecked(True)

        self.ui.startButton.clicked.connect(self.StartButtonClick)
        self.ui.failButton.clicked.connect(self.FailButtonClick)
        self.ui.exitButton.clicked.connect(self.ExitButtonClick)
        self.ui.chooseBlack.clicked.connect(self.ChessTypeClick)
        self.ui.chooseWhite.clicked.connect(self.ChessTypeClick)

    # 绘制棋盘
    def InitChessView(self):
        self.chessMove = None
        self.chessRect = None
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

    # 初始化游戏
    def InitGame(self):
        self.InitChessView()
        self.chessMat = [[-1 for i in range(15)] for n in range(15)]
        self.currentChessType = ChessType.BLACK
        self.ui.resultLabel.setText("")
        self.ui.blackNums.setText("")
        self.ui.whiteNums.setText("")
        self.ui.actionLabel.setText("")

    def StopGame(self):
        self.gameStatus = GameStatus.STOP
        self.ui.startButton.setEnabled(True)
        self.ui.chooseWhite.setEnabled(True)
        self.ui.chooseBlack.setEnabled(True)

    # 下一步棋
    def PutOneChess(self, indexX, indexY, chessType):
        if self.gameStatus is not GameStatus.PLAYING \
                or self.chessMat[indexX][indexY] !=  ChessType.NOP.value:
            return

        chessItem = ChessIcon.ChessItem(chessType)
        chessItem.setPos(self.chessStartPos + indexX * self.chessLineOffset - self.chessRadius,
                         self.chessStartPos + indexY * self.chessLineOffset - self.chessRadius)
        chessItem.show()
        self.chessScene.addItem(chessItem)
        if self.chessRect is not None:
            self.chessScene.removeItem(self.chessRect)
        self.chessRect = ChessIcon.ChessRect()
        self.chessRect.setPos(self.chessStartPos + indexX * self.chessLineOffset - self.chessRadius,
                              self.chessStartPos + indexY * self.chessLineOffset - self.chessRadius)
        self.chessRect.show()
        self.chessScene.addItem(self.chessRect)
        self.chessMat[indexX][indexY] = chessType.value
        self.currentChessType = ChessType.BLACK if self.currentChessType is ChessType.WHITE else ChessType.WHITE
        numsView = self.ui.blackNums if chessType == ChessType.BLACK else self.ui.whiteNums
        gobangNums = 1 if numsView.text() == "" else int(numsView.text()) + 1
        numsView.setText(str(gobangNums))

        if StrategyInterface.IsGobangWin(self.chessMat, indexX, indexY):
            self.StopGame()
            if chessType == ChessType.BLACK:
                self.ui.resultLabel.setText("五连珠黑胜!")
            else:
                self.ui.resultLabel.setText("五连珠白胜!")
        else:
            if self.playerChessType is not self.currentChessType:
                self.strategyInstance.DecideNext(self.chessMat, self.currentChessType, self.CallBackPlaying)

    # AI 异步回调
    def CallBackPlaying(self, indexX, indexY):
        self.PutOneChess(indexX, indexY, self.currentChessType)

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

    """ 
        Ui CallBack Function
    """
    # 开始
    def StartButtonClick(self):
        if self.gameStatus is GameStatus.STOP:
            self.gameStatus = GameStatus.PLAYING
            self.ui.startButton.setEnabled(False)
            self.ui.chooseWhite.setEnabled(False)
            self.ui.chooseBlack.setEnabled(False)
            self.InitGame()
            if self.playerChessType is not self.currentChessType:
                self.ui.actionLabel.setText("..电脑下棋..")
                self.strategyInstance.DecideNext(self.chessMat, self.currentChessType, self.CallBackPlaying)
            else:
                self.ui.actionLabel.setText("..玩家下棋..")

    # 认输
    def FailButtonClick(self):
        if self.gameStatus is GameStatus.PLAYING:
            self.StopGame()
            failer = "黑" if self.playerChessType is ChessType.BLACK else "白"
            self.ui.resultLabel.setText(failer + "方已认输")

    # 退出
    def ExitButtonClick(self):
        self.StopGame()
        self.close()

    # 选先手
    def ChessTypeClick(self):
        if self.ui.chooseWhite.isChecked():
            self.playerChessType = ChessType.WHITE
        else:
            self.playerChessType = ChessType.BLACK

    def mouseMoveEvent(self, event):
        super(ChessApplication, self).mouseMoveEvent(event)
        if not self.IsMouseInChessView(event.x(), event.y()):
            return

        indexX, indexY = self.GetClickChessIndex(event.x(), event.y())
        if self.chessMove is not None:
            self.chessScene.removeItem(self.chessMove)
        self.chessMove = ChessIcon.ChessMove()
        self.chessMove.setPos(self.chessStartPos + indexX * self.chessLineOffset - self.chessRadius,
                              self.chessStartPos + indexY * self.chessLineOffset - self.chessRadius)
        self.chessMove.show()
        self.chessScene.addItem(self.chessMove)

    def mouseReleaseEvent(self, event):
        super(ChessApplication, self).mouseMoveEvent(event)
        if not self.IsMouseInChessView(event.x(), event.y()) \
                or self.currentChessType is not self.playerChessType:
            return
        indexX, indexY = self.GetClickChessIndex(event.x(), event.y())
        self.PutOneChess(indexX, indexY, self.currentChessType)
