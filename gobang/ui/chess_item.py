
from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum

class ChessType(Enum):
    NOP = -1
    WHITE = 0
    BLACK = 1

# 显示棋子
class ChessItem(QtWidgets.QGraphicsItem):
    def __init__(self, chessType):
        super(ChessItem, self).__init__()
        self.chessIcon = QtGui.QPixmap("image/blackChess.png") \
            if chessType == ChessType.BLACK else QtGui.QPixmap("image/whiteChess.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessIcon)

# 鼠标移动时的提示线条
class ChessMove(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(ChessMove, self).__init__()
        self.chessLine = QtGui.QPixmap("image/redLine.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessLine)

# 下棋后显示的框
class ChessRect(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(ChessRect, self).__init__()
        self.chessLine = QtGui.QPixmap("image/chessRect.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessLine)

# 五点
class ChessFivePoint(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(ChessFivePoint, self).__init__()
        self.chessLine = QtGui.QPixmap("image/blackPoint.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessLine)
