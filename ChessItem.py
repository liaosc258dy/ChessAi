
from PyQt5 import QtCore, QtGui, QtWidgets

# 显示棋子
class ChessItem(QtWidgets.QGraphicsItem):
    def __init__(self, chessKind):
        super(ChessItem, self).__init__()
        self.chessIcon = QtGui.QPixmap()
        if chessKind == 1:
            self.chessIcon.load("Image/blackChess.png")
        else:
            self.chessIcon.load("Image/whiteChess.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessIcon)

# 鼠标移动时的提示线条
class ChessMove(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(ChessMove, self).__init__()
        self.chessLine = QtGui.QPixmap("Image/redLine.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessLine)

# 下棋后显示的框
class ChessRect(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(ChessRect, self).__init__()
        self.chessLine = QtGui.QPixmap("Image/chessRect.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessLine)

# 五点
class ChessFivePoint(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(ChessFivePoint, self).__init__()
        self.chessLine = QtGui.QPixmap("Image/blackPoint.png")

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 50, 50)

    def paint(self, painter, styleOptionGraphicsItem, widget=None):
        painter.drawPixmap(self.boundingRect().topLeft(), self.chessLine)