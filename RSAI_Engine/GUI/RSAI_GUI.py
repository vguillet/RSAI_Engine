
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import sys

# Libs
import numpy as np

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets

from qimage2ndarray import array2qimage

# Own modules
from RSAI_Engine.Environment.RSAI_environment import RSAI_environment
from RSAI_Engine.Agent.RSAI_agent import Agent

from RSAI_Engine.GUI.Table_model import TableModel

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '7/02/2020'

##################################################################################################################


class RSAI_GUI:
    def __init__(self):
        app = QtWidgets.QApplication([])

        # --> Load RSAI GUI layout
        self.main_window = uic.loadUi("RSAI_Engine/GUI/Layout_1.ui")

        # --> Create RSAI environment
        self.environment = RSAI_environment()

        # --> Create agent
        agent = Agent("Bob", (10, 10))
        self.main_window.agent_name.setText(agent.name)
        self.main_window.agent_pos_sim_coordinates.setText(str(agent.pos))

        # --> Initiate view tracker
        self.view = "obstacle"

        # --> Set image to map
        self.change_view()

        # --> Set array to sim array
        self.set_array_view()

        # --> Connect buttons
        self.main_window.view_toggle.clicked.connect(self.change_view)

        # --> Display GUI
        self.main_window.show()

        sys.exit(app.exec())

    def set_array_view(self):
        # --> Set image to fill graphics view
        # self.main_window.sim_view.setScaledContents(True)

        # --> Convert array to Qimage
        qimage = array2qimage(self.environment.sim_grid, normalize=True)

        # --> Create pixmap
        pix = QPixmap(qimage)
        item = QtWidgets.QGraphicsPixmapItem(pix)

        # --> Create scene
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.main_window.sim_view.setScene(scene)

        # self.main_window.sim_view.fitInView(scene.sceneRect())
        return

    def change_view(self):
        if self.view == "obstacle":
            # ----- Set image to map
            # --> Create pixmap
            pix = QPixmap(self.environment.world_image_path)
            item = QtWidgets.QGraphicsPixmapItem(pix)

            # --> Create scene
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.main_window.map_view.setScene(scene)

            # --> Update text to view
            self.main_window.view_toggle.setText("Switch view (Map)")

            # --> Update view tracker
            self.view = "map"

        else:
            # ----- Set image to obstacle
            # --> Create pixmap
            pix = QPixmap(self.environment.obstacle_image_path)
            item = QtWidgets.QGraphicsPixmapItem(pix)

            # --> Create scene
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.main_window.map_view.setScene(scene)

            # --> Update text to view
            self.main_window.view_toggle.setText("Switch view (Obstacles)")

            # --> Update view tracker
            self.view = "obstacle"

        return
