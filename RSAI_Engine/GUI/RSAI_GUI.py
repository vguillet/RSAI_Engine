
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
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

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
        self.main_window.setWindowIcon(QIcon("RSAI_Engine/Data/GUI_assets/RSAI_icon.png"))

        # --> Create RSAI environment
        self.environment = RSAI_environment()

        # --> Create agent
        agent = Agent("Bob", (10, 10))
        self.main_window.agent_name.setText(agent.name)
        self.main_window.agent_pos_sim_coordinates.setText(str(agent.pos))

        # --> Initiate views trackers
        self.current_scale = "fit"

        # --> Set views
        self.update_views()

        # --> Connect buttons
        self.main_window.scale_toggle.clicked.connect(self.change_scale)

        # --> Display GUI
        self.main_window.show()

        sys.exit(app.exec())

    @property
    def scale(self):
        if self.current_scale == "fit":
            return 10000, 720
        else:
            return 10000, 1536

    def change_scale(self):
        if self.current_scale == "fit":
            self.current_scale = "full"
            self.update_views()

            # --> Adjust button text
            self.main_window.scale_toggle.setText("Scale view (Full screen)")

        else:
            self.current_scale = "fit"
            self.update_views()

            # --> Adjust button text
            self.main_window.scale_toggle.setText("Scale view (Fit screen)")

        return

    def update_views(self):
        # ----- Update map view
        # --> Create pixmap
        pixmap = QPixmap(self.environment.world_image_path)

        # --> Set view
        scene = self.create_scene(pixmap)
        self.main_window.map_view.setScene(scene)

        # ----- Update obstacle view
        # --> Create pixmap
        pixmap = QPixmap(self.environment.obstacle_image_path)

        # --> Set view
        scene = self.create_scene(pixmap)
        self.main_window.obstacle_view.setScene(scene)

        # ----- Update simulation view
        # --> Convert array to Qimage
        qimage = array2qimage(self.environment.sim_grid, normalize=True)
        pixmap = QPixmap(qimage)

        # --> Set view
        scene = self.create_scene(pixmap)
        self.main_window.sim_view.setScene(scene)

        return

    def create_scene(self, pixmap):
        # --> Scale pixmap
        x_scale, y_scale = self.scale
        pixmap_scaled = pixmap.scaled(x_scale, y_scale, Qt.KeepAspectRatio)

        # --> Create item
        item = QtWidgets.QGraphicsPixmapItem(pixmap_scaled)

        # --> Create scene
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        return scene
