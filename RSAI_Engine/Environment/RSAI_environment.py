
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import matplotlib.pyplot as plt
import cv2

# Own modules
from RSAI_Engine.Environment.Grid_gen.Obstacle_grid_gen import gen_obstacle_grid
from RSAI_Engine.Environment.Grid_gen.POI_grid_gen import gen_POI_grid

from RSAI_Engine.Visualiser.Visualiser import Visualiser
from RSAI_Engine.Visualiser.Visualiser_tools import Visualiser_tools


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class RSAI_environment:
    def __init__(self,
                 image_path="RSAI_Engine\Data\Environment\Obstacle_image.png",
                 origin: "Exploded map coordinates" = (3136, 3136)):
        """
        RSAI environment class, used to generate RSAI environments
        """
        # ----- Setup reference properties
        self.name = "RSAI environment"
        self.type = "Environment"
        self.origin = origin        # Origin coordinates of grid on the exploded map

        # --> Load map image
        self.map_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        # --> Setup obstacle grid
        self.obstacle_grid = gen_obstacle_grid(self.map_image)

        # --> Setup POI grid
        self.POI_grid, self.POI_dict = gen_POI_grid(self.obstacle_grid.shape, self.origin)

        self.shape = self.obstacle_grid.shape

    # =============================================================================== Getters

    @property
    def converters_dict(self):
        converters_lst = []
        for POI in self.POI_dict.keys():
            if self.POI_dict[POI].label == "Converter":
                converters_lst.append(POI)
        return converters_lst

    @property
    def sources_dict(self):
        sources_dict = {}
        for POI in self.POI_dict.keys():
            for source in self.POI_dict[POI].ef_dict["Sources"].keys():
                sources_dict[source] = self.POI_dict[POI].ef_dict["Sources"][source]
        return sources_dict

    def visualise_environment(self, run_name, agents_dict, press_start=True):
        # # TODO: Add visualiser
        # visu = self.obstacle_grid.copy()
        #
        # visu += self.POI_grid * 5
        #
        # plt.imshow(visu)
        # plt.colorbar()
        # plt.show()

        Visualiser(run_name, self, agents_dict, press_start=press_start)

        return

    def get_POI_at_pos(self, pos: tuple):
        for POI in self.POI_dict.keys():
            if self.POI_dict[POI].pos == pos:
                return POI
            else:
                print("!!! No POI at provided pos !!!")
                return

    def get_label_of_name(self, name: str):
        for POI in self.POI_dict.keys():
            if POI == name:
                return self.POI_dict[POI].label
            else:
                for ef in self.POI_dict[POI].ef_dict.keys():
                    if ef == name:
                        return self.POI_dict[POI].ef_dict[ef].label
                    else:
                        pass
        print("!!! Name not found !!!")

    # =============================================================================== Setters
    def add_POI(self, POI: "POI Object"):
        self.POI_dict[POI.name] = POI
        self.POI_grid[POI.pos[1]][POI.pos[1]] = 1
        return

    def remove_POI(self, POI: "POI Object"):
        del self.POI_dict[POI.name]
        self.POI_grid[POI.pos[1]][POI.pos[1]] = 0
        return

    def __str__(self):
        return "RSAI environment"

    def __repr__(self):
        return self.__str__()

