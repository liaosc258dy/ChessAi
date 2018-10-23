# -*- coding: utf-8 -*-

# 获取棋子状态
def GetChessLives(chessMat):
    pass

def GetChessEffective(chessMat, x, y, chessKind):
    if x >= 0 and x <= 14 \
        and y >= 0 and y <= 14:
        if chessMat[x][y] == chessKind:
            return 1
    return 0

# 判断是否胜利,搜索当前落子的四个方向是否五连珠
def IsGobangWin(chessMat, x, y):
    chessKind = chessMat[x][y]
    # 横,竖,撇,捺
    chessDirection = [1 for n in range(4)]
    for i in range(5):
        if chessDirection[0] >= 5 \
                or chessDirection[1] >= 5 \
                or chessDirection[2] >= 5 \
                or chessDirection[3] >= 5:
            return True
        xLeftPos = x - i - 1
        xRightPos = x + i + 1
        yUpPos = y - i - 1
        yDownPos = y + i + 1

        chessDirection[0] = chessDirection[0] + GetChessEffective(chessMat,xRightPos,y,chessKind)
        chessDirection[0] = chessDirection[0] + GetChessEffective(chessMat, xLeftPos, y, chessKind)
        chessDirection[1] = chessDirection[1] + GetChessEffective(chessMat, x, yUpPos, chessKind)
        chessDirection[1] = chessDirection[1] + GetChessEffective(chessMat, x, yDownPos, chessKind)
        chessDirection[2] = chessDirection[2] + GetChessEffective(chessMat, xRightPos, yUpPos, chessKind)
        chessDirection[2] = chessDirection[2] + GetChessEffective(chessMat, xLeftPos, yDownPos, chessKind)
        chessDirection[3] = chessDirection[3] + GetChessEffective(chessMat, xLeftPos, yUpPos, chessKind)
        chessDirection[3] = chessDirection[3] + GetChessEffective(chessMat, xRightPos, yDownPos, chessKind)
    return False