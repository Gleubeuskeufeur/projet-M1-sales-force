from os import environ
from PyQt6.QtWidgets import QWidget, QComboBox, QGridLayout, QLabel
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from models.model import serializeCSVDB
from controller.controller import sortAllPrices

class ProjectP6Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projet P6")
        self.json_db_data = sortAllPrices(serializeCSVDB(environ['DATA_DIRECTORY']))

        layout = QGridLayout(self)
        layout.addWidget(QLabel("Choisissez une parcelle"),0,0,1,3,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        layout.addWidget(QLabel("Ville"),1,0,1,1,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.city_combobox = QComboBox(self)
        self.city_combobox.currentTextChanged.connect(self.citySelected)
        layout.addWidget(self.city_combobox,2,0,1,1,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        layout.addWidget(QLabel("Section"),1,1,1,1,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.section_combobox = QComboBox(self)
        self.section_combobox.currentTextChanged.connect(self.sectionSelected)
        layout.addWidget(self.section_combobox,2,1,1,1,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        layout.addWidget(QLabel("Parcelle"),1,2,1,1,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.parcelle_combobox = QComboBox(self)
        self.parcelle_combobox.currentTextChanged.connect(self.parcelleSelected)
        layout.addWidget(self.parcelle_combobox,2,2,1,1,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.canvas = FigureCanvas(Figure())
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        layout.addWidget(self.canvas,3,0,1,3,Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.city_combobox.addItems(self.json_db_data)


    def citySelected(self,city):
        if city:
            self.section_combobox.clear()
            self.section_combobox.addItems(self.json_db_data[city])


    def sectionSelected(self,section):
        if section and self.city_combobox.currentText():
            self.parcelle_combobox.clear()
            self.parcelle_combobox.addItems(self.json_db_data[self.city_combobox.currentText()][section])


    def parcelleSelected(self,parcelle):
        if parcelle and self.city_combobox.currentText() and self.section_combobox.currentText():
            parcelle_plot_data = self.json_db_data[self.city_combobox.currentText()][self.section_combobox.currentText()][parcelle]
            self.plot(parcelle_plot_data)


    def plot(self, parcelle_plot_data):
        self.canvas.axes.clear()
        self.canvas.axes.plot(parcelle_plot_data[0],parcelle_plot_data[1],marker='*',linestyle='-',color='green')
        self.canvas.axes.set_xticklabels(parcelle_plot_data[0], rotation='vertical')
        self.canvas.draw()
