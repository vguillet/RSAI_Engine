
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
        self.main_window = uic.loadUi("RSAI_Engine/GUI/Layout_2.ui")
        self.main_window.setWindowIcon(QIcon("RSAI_Engine/Data/GUI_assets/RSAI_icon.png"))

        # --> Create RSAI environment
        self.environment = RSAI_environment()

        # --> Create agent
        agent = Agent("Bob", (10, 10))
        self.main_window.agent_name.setText(agent.name)
        self.main_window.agent_pos_sim_coordinates.setText(str(agent.pos))

        # --> Set views
        self.views_dict = {"world": {"Map": QPixmap(self.environment.world_image_path),
                                     "Obstacles": QPixmap(self.environment.obstacle_image_path)},

                           "sim": {"Overview": QPixmap(array2qimage(self.environment.sim_grid, normalize=True))}
                           }

        # --> Initiate views trackers
        self.current_scale = "fit"
        self.current_view = "world"

        self.current_world_view = "Map"
        self.current_sim_view = "Overview"

        # --. Initiate view
        self.update_map_view()

        # --> Connect buttons
        self.main_window.scale_toggle.clicked.connect(self.change_scale)

        self.main_window.world_toggle.clicked.connect(self.toggle_world_view)
        self.main_window.simulation_toggle.clicked.connect(self.toggle_simulation_view)

        # --> Connect comb boxes
        self.main_window.world_combo.currentIndexChanged.connect(self.change_world_sub_view)
        self.main_window.simulation_combo.currentIndexChanged.connect(self.change_sim_sub_view)

        # --> Display GUI
        self.main_window.show()

        sys.exit(app.exec())

    @property
    def scale(self):
        if self.current_scale == "fit":
            return 10000, 720
        else:
            return 10000, 1536

    @property
    def view_pixmap(self):
        if self.current_view == "world":
            return self.views_dict[self.current_view][self.current_world_view]
        else:
            return self.views_dict[self.current_view][self.current_sim_view]

    def change_scale(self):
        if self.current_scale == "fit":
            self.current_scale = "full"
            self.update_map_view()

            # --> Adjust button text
            self.main_window.scale_toggle.setText("Scale view (Full screen)")

        else:
            self.current_scale = "fit"
            self.update_map_view()

            # --> Adjust button text
            self.main_window.scale_toggle.setText("Scale view (Fit screen)")

        return

    def toggle_world_view(self):
        self.current_view = "world"
        self.update_map_view()
        return

    def toggle_simulation_view(self):
        self.current_view = "sim"
        self.update_map_view()
        return

    def change_world_sub_view(self):
        self.current_world_view = self.main_window.world_combo.currentText()

        if self.current_view == "world":
            self.update_map_view()
        return

    def change_sim_sub_view(self):
        self.current_sim_view = self.main_window.simulation_combo.currentText()

        if self.current_view == "sim":
            self.update_map_view()
        return

    def update_map_view(self):
        # --> Scale pixmap
        x_scale, y_scale = self.scale
        pixmap_scaled = self.view_pixmap.scaled(x_scale, y_scale, Qt.KeepAspectRatio)

        # --> Create item
        item = QtWidgets.QGraphicsPixmapItem(pixmap_scaled)

        # --> Create scene
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        # --> Set map view
        self.main_window.map_view.setScene(scene)

        return
