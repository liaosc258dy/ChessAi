# -*- coding: utf-8 -*-

# @Author   : Shichao Liao
# @Email    : liaosc@liaoshichao.com
# @Site     : https://liaoshichao.com/
# @Github   : https://github.com/liaoscdy

from PyQt5.QtWidgets import QApplication
from gobang.chess_application import ChessApplication
import sys

if __name__ == "__main__":
    process = QApplication(sys.argv)
    app = ChessApplication()
    app.show()
    sys.exit(process.exec())
