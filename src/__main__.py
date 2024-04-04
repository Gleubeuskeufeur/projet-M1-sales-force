from os import environ
from os.path import join, dirname

environ['DATA_DIRECTORY'] = join(dirname(dirname(__file__)), 'data')

from view.view import ProjectP6Window
from PyQt6.QtWidgets import QApplication

app = QApplication([])

window = ProjectP6Window()
window.show()

app.exec()
