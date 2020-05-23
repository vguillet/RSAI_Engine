
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import matplotlib.pyplot as plt

# Own modules
from RSAI_Engine.Environment.Grid_gen.Obstacle_grid_gen import Obstacle_grid_gen
from RSAI_Engine.Environment.Grid_gen.POI_grid_gen import POI_grid_gen


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class gen_RSAI_environment:
    def __init__(self,
                 image_path="RSAI_Engine\Data\Environment\Obstacle_image.png",
                 origin: "Exploded map coordinates" = (10, 10)):
        """
        RSAI environment class, used to generate RSAI-type Ingenium environments
        """
        # ----- Setup reference properties
        self.name = "RSAI environment"
        self.type = "Environment"
        self.origin = origin        # Origin coordinates of grid on the exploded map

        # --> Setup obstacle grid
        self.obstacles_grid = Obstacle_grid_gen(image_path)

        # --> Setup POI grid
        self.POI_grid, self.POI_dict = POI_grid_gen(self.obstacles_grid.shape, self.origin)

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

    @property
    def high(self):
        # --> Max x and y
        high_lst = [self.size[0], self.size[-1]]

        # --> Add max distance for each POI (diagonal of env)
        max_distance = (self.size[0] ** 2 + self.size[-1] ** 2) ** (1 / 2)
        for _ in self.POI_dict.keys():
            high_lst.append(max_distance)
        return high_lst

    @property
    def low(self):
        # --> Max x and y
        low_lst = [0, 0]

        # --> Add max distance for each POI (diagonal of env)
        for _ in self.POI_dict.keys():
            low_lst.append(0)
        return low_lst

    def visualise_environment(self):
        # TODO: Add visualiser
        plt.imshow(self.obstacle_grid)
        plt.colorbar()
        plt.show()
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
        return

    def remove_POI(self, POI: "POI Object"):
        del self.POI_dict[POI.name]
        return

    def __str__(self):
        return "RSAI environment"

    def __repr__(self):
        return self.__str__()

