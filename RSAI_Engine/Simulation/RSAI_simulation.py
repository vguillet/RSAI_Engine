
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import time
import random

# Libs
import cv2
from faker import Faker

# Own modules
from RSAI_Engine.Simulation.Environment.RSAI_environment import RSAI_environment
from RSAI_Engine.Simulation.Agent.RSAI_agent import RSAI_agent
from RSAI_Engine.Simulation.Items.Item import Item

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class RSAI_simulation:
    def __init__(self,
                 sim_origin: "World coordinates tuple" = (2944, 3072),  # (2944, 3519) (3136, 3136), from bottom left
                 world_image_path="RSAI_Engine\Data\Assets\Environment\World_image_L.png",
                 obstacle_image_path="RSAI_Engine\Data\Assets\Environment\Obstacle_image.png"):

        # --> Record image paths
        self.world_image_path = world_image_path
        self.obstacle_image_path = obstacle_image_path

        # --> Load images
        self.world_image = cv2.imread(world_image_path, cv2.IMREAD_UNCHANGED)

        # --> Create environment
        self.environment = RSAI_environment(world_image=self.world_image,
                                            obstacle_image_path=self.obstacle_image_path,
                                            sim_origin=sim_origin)
        # --> Create agentS
        self.agent_lst = []

        fake = Faker()

        for _ in range(5):
            self.agent_lst.append(RSAI_agent(name=fake.name(),
                                             simulation_origin=self.environment.origin,
                                             simulation_shape=self.environment.shape,
                                             start_world_pos=(3216, 3219)))

        # --> Equip some items
        equipment = [Item("Helm", "Med_helm", "Iron"),
                     Item("Chest", "Platebody", "Iron"),
                     Item("Legs", "Platelegs", "Iron"),
                     Item("Boots", "Boots", "Iron"),
                     Item("Gloves", "Gloves", "Iron"),
                     Item("Shield", "Kiteshield", "Black"),
                     Item("Weapon", "Scimitar", "Mithril")]

        for agent in self.agent_lst:
            for item in equipment:
                agent.inventory.add_item_to_inventory(item=item)
                agent.equipment.equip_item(inventory_dict=agent.inventory(),
                                           states_dict=agent.states(),
                                           item=item)

                agent.inventory.add_item_to_inventory(item=item)

    def run_simulation(self, progress_callback):
        print("---------------------- Simulation started ----------------------")
        for agent in self.agent_lst:
            agent.goal = None

        while True:
            for agent in self.agent_lst:
                if agent.goal is None:
                    while agent.goal is None:
                        # --> Pick random goal
                        goal = random.choice(list(self.environment.POI_dict.keys()))

                        # --> Set goal
                        agent.set_goal_POI(grids_dict=self.environment.grids_dict,
                                           POI=self.environment.POI_dict[goal])

                    print(f"- {agent.name} - New Goal:", agent.goal)

                else:
                    agent.move()

            time.sleep(0.005)
            progress_callback.emit()
