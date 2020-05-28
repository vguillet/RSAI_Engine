
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


class Map_view_GUI:
    @staticmethod
    def gen_views_dict(gui):
        return {"world": {"Map": QPixmap(gui.simulation.world_image_path),
                          "Obstacles": QPixmap(gui.simulation.obstacle_image_path)},

                "simulation": {"Overview": QPixmap(array2qimage(gui.views.overview, normalize=True)),
                               "Obstacles": QPixmap(array2qimage(gui.views.obstacle_view, normalize=True)),
                               "POIs": QPixmap(array2qimage(gui.views.POI_view, normalize=True)),
                               "Agent": QPixmap(array2qimage(gui.views.agent_view, normalize=True))}
                }

    def update_map_view(self, gui):
        try:
            if gui.main_window.enable_render.isChecked():
                gui.views_dict = self.gen_views_dict(gui)

                # --> Scale pixmap
                x_scale, y_scale = gui.scale
                pixmap_scaled = gui.view_pixmap.scaled(x_scale, y_scale, Qt.KeepAspectRatio)

                # --> Create item
                item = QtWidgets.QGraphicsPixmapItem(pixmap_scaled)

                # --> Create scene
                scene = QtWidgets.QGraphicsScene()
                scene.addItem(item)

                # --> Set map view
                gui.main_window.map_view.setScene(scene)

        except:
            pass

            return

        else:
            return

    @staticmethod
    def update_position_summary(gui):
        if gui.main_window.enable_render.isChecked():
            # --> Update agent labels
            gui.main_window.map_agent_name.setText(gui.simulation.agent.name)
            gui.main_window.agent_pos_world_coordinates.setText(str(gui.simulation.agent.world_pos))
            gui.main_window.agent_pos_simulation_coordinates.setText(str(gui.simulation.agent.simulation_pos))

            # --> If goal is set
            if gui.simulation.agent.goal is not None:
                # --> Set step text
                gui.main_window.step_pos_world_coordinates.setText(str(gui.simulation.agent.world_path_to_goal[0]))
                gui.main_window.step_pos_simulation_coordinates.setText(str(gui.simulation.agent.simulation_path_to_goal[0]))

                # --> Set name text
                if gui.simulation.agent.goal_type == "POI":
                    gui.main_window.goal_name.setText(str(gui.simulation.agent.goal.name))

                elif gui.simulation.agent.goal_type == "Coordinates":
                    gui.main_window.goal_name.setText("Coordinates")

                # --> Set goal coordinates
                gui.main_window.goal_pos_world_coordinates.setText(str(gui.simulation.agent.goal.world_pos))
                gui.main_window.goal_pos_simulation_coordinates.setText(str(gui.simulation.agent.goal.simulation_pos))

                # --> Set path text
                gui.main_window.total_path_length.setText(str(gui.simulation.agent.total_path_len))
                gui.main_window.steps_to_goal.setText(str(len(gui.simulation.agent.simulation_path_to_goal) - 1))

                return
        else:
            return
