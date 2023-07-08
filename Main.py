import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from loginUser import login


class main(QMainWindow):
           
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = login()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())

