
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from qimage2ndarray import array2qimage

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class Game_view_GUI:
    @staticmethod
    def dummy_view(gui):
        pix_gv = QPixmap("RSAI_Engine/Data/GUI_assets/random_game_view.png")

        # --> Create item
        item = QtWidgets.QGraphicsPixmapItem(pix_gv)

        # --> Create scene
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        # --> Set dummy game view
        gui.main_window.game_view.setScene(scene)