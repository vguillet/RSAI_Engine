
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
                          "Obstacle": QPixmap(gui.simulation.obstacle_image_path),
                          "Paths": QPixmap(gui.simulation.path_image_path)},

                "simulation": {"Overview": QPixmap(array2qimage(gui.views.overview(gui.POI_selection, gui.agent_selection), normalize=True)),
                               "POIs": QPixmap(array2qimage(gui.views.POI_view(gui.POI_selection, gui.agent_selection), normalize=True)),
                               "Appeal": QPixmap(array2qimage(gui.views.appeal_map_view(gui.POI_selection, gui.agent_selection), normalize=True)),
                               "Pheromone": QPixmap(array2qimage(gui.views.pheromone_map_view(gui.POI_selection, gui.agent_selection), normalize=True)),
                               "Obstacles": QPixmap(array2qimage(gui.views.obstacle_view(gui.POI_selection, gui.agent_selection), normalize=True)),
                               "Paths": QPixmap(array2qimage(gui.views.path_view(gui.POI_selection, gui.agent_selection), normalize=True))}
                }

    @staticmethod
    def update_views_dict(gui):
        if gui.current_view == "world":
            gui.views_dict["world"]["Map"] = QPixmap(gui.simulation.world_image_path)
            gui.views_dict["world"]["Obstacles"] = QPixmap(gui.simulation.obstacle_image_path)
            gui.views_dict["world"]["Paths"] = QPixmap(gui.simulation.path_image_path)

            return

        else:
            if gui.current_sim_view == "Overview":
                gui.views_dict["simulation"]["Overview"] = \
                    QPixmap(array2qimage(gui.views.overview(gui.POI_selection, gui.agent_selection), normalize=True))
                return

            elif gui.current_sim_view == "POIs":
                gui.views_dict["simulation"]["POIs"] = \
                    QPixmap(array2qimage(gui.views.POI_view(gui.POI_selection, gui.agent_selection), normalize=True))
                return

            elif gui.current_sim_view == "Appeal":
                gui.views_dict["simulation"]["Appeal"] = \
                    QPixmap(array2qimage(gui.views.appeal_map_view(gui.POI_selection, gui.agent_selection), normalize=True))
                return

            elif gui.current_sim_view == "Pheromone":
                gui.views_dict["simulation"]["Pheromone"] = \
                    QPixmap(array2qimage(gui.views.pheromone_map_view(gui.POI_selection, gui.agent_selection), normalize=True))
                return

            elif gui.current_sim_view == "Obstacles":
                gui.views_dict["simulation"]["Obstacles"] = \
                    QPixmap(array2qimage(gui.views.obstacle_view(gui.POI_selection, gui.agent_selection), normalize=True))
                return

            elif gui.current_sim_view == "Paths":
                gui.views_dict["simulation"]["Paths"] = \
                    QPixmap(array2qimage(gui.views.path_view(gui.POI_selection, gui.agent_selection), normalize=True))
                return

    def update_map_view(self, gui):
        self.update_views_dict(gui)

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

        return

    @staticmethod
    def update_position_summary(gui):
        if gui.main_window.enable_render.isChecked():
            if gui.agent_selection == "All":
                selected_agent = gui.simulation.swarm.population[0]

            else:
                # --> Find selected agent
                for agent in gui.simulation.swarm.population:
                    if agent.name == gui.agent_selection:
                        selected_agent = agent
                        break

            # --> Update agent labels
            gui.main_window.map_agent_name.setText(selected_agent.name)
            gui.main_window.agent_pos_world_coordinates.setText(str(selected_agent.world_pos))
            gui.main_window.agent_pos_simulation_coordinates.setText(str(selected_agent.simulation_pos))

            # --> If goal is set
            if selected_agent.goal is not None:
                # --> Set name text
                gui.main_window.goal_name.setText(selected_agent.goal.name)

                # # --> Set prev goal coordinates
                # gui.main_window.prev_goal_pos_world_coordinates.setText(str(selected_agent.goal_history[-1].world_pos))
                # gui.main_window.prev_goal_pos_simulation_coordinates.setText(str(selected_agent.goal_history[-1].simulation_pos))

                # --> Set goal coordinates
                gui.main_window.goal_pos_world_coordinates.setText(str(selected_agent.goal.world_pos))
                gui.main_window.goal_pos_simulation_coordinates.setText(str(selected_agent.goal.simulation_pos))

            else:
                # --> Set name text
                gui.main_window.goal_name.setText("None")

                # # --> Set prev goal coordinates
                # gui.main_window.prev_goal_pos_world_coordinates.setText("-")
                # gui.main_window.prev_goal_pos_simulation_coordinates.setText("-")

                # --> Set goal coordinates
                gui.main_window.goal_pos_world_coordinates.setText("-")
                gui.main_window.goal_pos_simulation_coordinates.setText("-")

        else:
            return
