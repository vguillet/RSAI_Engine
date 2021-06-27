
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

    @staticmethod
    def update_views_dict(gui):
        if gui.current_view == "world":
            gui.views_dict["world"]["Map"] = QPixmap(gui.simulation.world_image_path)
            gui.views_dict["world"]["Obstacles"] = QPixmap(gui.simulation.obstacle_image_path)
            return

        else:
            if gui.current_sim_view == "Overview":
                gui.views_dict["simulation"]["Overview"] = QPixmap(array2qimage(gui.views.overview, normalize=True))
                return

            elif gui.current_sim_view == "Obstacles":
                gui.views_dict["simulation"]["Obstacles"] = QPixmap(array2qimage(gui.views.obstacle_view, normalize=True))
                return

            elif gui.current_sim_view == "POIs":
                gui.views_dict["simulation"]["POIs"] = QPixmap(array2qimage(gui.views.POI_view, normalize=True))
                return

            elif gui.current_sim_view == "Agent":
                gui.views_dict["simulation"]["Agent"] = QPixmap(array2qimage(gui.views.agent_view, normalize=True))
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
            # --> Update agent labels
            gui.main_window.map_agent_name.setText(gui.simulation.swarm.population[0].name)
            gui.main_window.agent_pos_world_coordinates.setText(str(gui.simulation.swarm.population[0].world_pos))
            gui.main_window.agent_pos_simulation_coordinates.setText(str(gui.simulation.swarm.population[0].simulation_pos))

            # --> If goal is set
            if gui.simulation.agent.goal is not None:
                # --> Set step text
                gui.main_window.step_pos_world_coordinates.setText(str(gui.simulation.swarm.population[0].world_path_to_goal[0]))
                gui.main_window.step_pos_simulation_coordinates.setText(str(gui.simulation.swarm.population[0].simulation_path_to_goal[0]))

                # --> Set name text
                if gui.simulation.agent.goal_type == "POI":
                    gui.main_window.goal_name.setText(str(gui.simulation.swarm.population[0].goal.name))

                elif gui.simulation.agent.goal_type == "Coordinates":
                    gui.main_window.goal_name.setText("Coordinates")

                # --> Set goal coordinates
                gui.main_window.goal_pos_world_coordinates.setText(str(gui.simulation.swarm.population[0].goal.world_pos))
                gui.main_window.goal_pos_simulation_coordinates.setText(str(gui.simulation.swarm.population[0].goal.simulation_pos))

                # --> Set path text
                gui.main_window.total_path_length.setText(str(gui.simulation.swarm.population[0].total_path_len))
                gui.main_window.steps_to_goal.setText(str(len(gui.simulation.swarm.population[0].simulation_path_to_goal) - 1))

                return
        else:
            return

"""   
1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 if __name__ == "__main__":x 
   6 
   7     app = QApplication(sys.argv)
   8     
   9     if len(app.arguments()) < 2:
  10     
  11         sys.stderr.write("Usage: %s <image file> <overlay file>\n" % sys.argv[0])
  12         sys.exit(1)
  13     
  14     image = QImage(app.arguments()[1])
  15     if image.isNull():
  16         sys.stderr.write("Failed to read image: %s\n" % app.arguments()[1])
  17         sys.exit(1)
  18     
  19     overlay = QImage(app.arguments()[2])
  20     if overlay.isNull():
  21         sys.stderr.write("Failed to read image: %s\n" % app.arguments()[2])
  22         sys.exit(1)
  23     
  24     if overlay.size() > image.size():
  25     
  26         overlay = overlay.scaled(image.size(), Qt.KeepAspectRatio)
  27     
  28     painter = QPainter()
  29     painter.begin(image)
  30     painter.drawImage(0, 0, overlay)
  31     painter.end()
  32     
  33     label = QLabel()
  34     label.setPixmap(QPixmap.fromImage(image))
  35     label.show()
  36     
  37     sys.exit(app.exec_())
  """