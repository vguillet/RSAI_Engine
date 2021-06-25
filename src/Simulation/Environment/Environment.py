
################################################################################################################
"""

"""

# Built-in/Generic Imports
import sys

# Libs
import matplotlib.pyplot as plt

# Own modules
from src.Simulation.Environment.Grids.Obstacle_grid_gen import gen_obstacle_grid
from src.Simulation.Environment.Grids.POI_grid_gen import gen_POI_grid
from src.Simulation.Environment.Grids.Path_grid_gen import gen_path_grid

# from src.Visualiser.Visualiser import Visualiser
# from src.Visualiser.Visualiser_tools import Visualiser_tools


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Environment:
    def __init__(self,
                 world_image=None,
                 obstacle_image_path="src\Data\Assets\Environment\Obstacle_image.png",
                 path_image_path="src\Data\Assets\Environment\Path_image.png",

                 sim_origin: "World coordinates tuple" = (3136, 3136)):
        """
        RSAI environment class, used to generate RSAI environments
        """
        # ----- Setup reference properties
        self.name = "RSAI environment"
        self.type = "Environment"
        self.origin = sim_origin        # Origin coordinates of grid on the exploded map

        if world_image is None:
            print("!!!!! Environment image is not provided !!!!!")
            sys.exit()

        # --> Setup obstacle grid
        # obstacle_grid = gen_obstacle_grid(world_image=world_image,
        #                                   obstacle_image_path=obstacle_image_path)

        # --> Setup path grid
        path_grid = gen_path_grid(world_image=world_image,
                                  path_image_path=path_image_path)

        # --> Setup POI grid and dict
        POI_grid, self.POI_dict = gen_POI_grid(simulation_origin=self.origin,
                                               simulation_size=obstacle_grid.shape)

        self.shape = obstacle_grid.shape

        # --> Setup grids dictionary
        self.grids_dict = {"Obstacle": obstacle_grid,
                           "Path": path_grid,
                           "POI": POI_grid}

        print("- Environment initiated:", self)

    def __str__(self):
        return "RSAI environment"

    def __repr__(self):
        return self.__str__()

    @property
    def converter_lst(self):
        converters_lst = []
        for POI in self.POI_dict.keys():
            if self.POI_dict[POI].label == "Converter":
                converters_lst.append(POI)
        return converters_lst

    @property
    def source_lst(self):
        sources_lst = []
        for POI in self.POI_dict.keys():
            if self.POI_dict[POI].label == "Source":
                sources_lst.append(POI)
        return sources_lst

    @property
    def sink_lst(self):
        sinks_lst = []
        for POI in self.POI_dict.keys():
            if self.POI_dict[POI].label == "Sink":
                sinks_lst.append(POI)
        return sinks_lst

    # def visualise_environment(self):
    #     # TODO: Add visualiser
    #     # Visualiser(run_name, self, agents_dict, press_start=press_start)
    #
    #     plt.imshow(self.sim_grid)
    #     plt.colorbar()
    #     plt.show()
    #
        # return

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
        self.grids_dict["POI"][POI.pos[1]][POI.pos[1]] = 1
        return

    def remove_POI(self, POI: "POI Object"):
        del self.POI_dict[POI.name]
        self.grids_dict["POI"][POI.pos[1]][POI.pos[1]] = 0
        return
