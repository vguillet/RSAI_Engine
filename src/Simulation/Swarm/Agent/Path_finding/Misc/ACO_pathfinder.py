
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.Simulation.Swarm.Agent.Path_finding.Route import Route
from src.Simulation.Swarm.Agent.Path_finding.Misc.abc_pathfinder import Pathfinder

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class AOC_pathfinder(Pathfinder):
    def find_route_to_POI(self,
                          environments_grids,
                          swarm_grids,
                          start_coordinates,
                          POI,
                          show_path=False):
        return

    def find_route_to_coordinate(self, environments_grids, swarm_grids, start_coordinates, goal_coordinates, show_path=False):
        return

    @staticmethod
    def find_route(environments_grids, swarm_grids, start_coordinates, goal_coordinates):
        route = Route()

        current_pos = start_coordinates

        route.append(start_coordinates)

        while current_pos != goal_coordinates:
            possible_steps = []

            #   a b c
            #   d x e
            #   f g h

            # ----- a
            if environments_grids["Obstacle"][current_pos[0] - 1, current_pos[1] + 1] != 1:
                possible_steps.append([current_pos[0] - 1, current_pos[1] + 1])

            # --> b
            if environments_grids["Obstacle"][current_pos[0], current_pos[1] + 1] != 1:
                possible_steps.append([current_pos[0], current_pos[1] + 1])

            # --> c
            if environments_grids["Obstacle"][current_pos[0] + 1, current_pos[1] + 1] != 1:
                possible_steps.append([current_pos[0] + 1, current_pos[1] + 1])

            # --> d
            if environments_grids["Obstacle"][current_pos[0] - 1, current_pos[1]] != 1:
                possible_steps.append([current_pos[0] - 1, current_pos[1]])

            # --> e
            if environments_grids["Obstacle"][current_pos[0] + 1, current_pos[1]] != 1:
                possible_steps.append([current_pos[0] + 1, current_pos[1]])

            # --> f
            if environments_grids["Obstacle"][current_pos[0] - 1, current_pos[1] - 1] != 1:
                possible_steps.append([current_pos[0] - 1, current_pos[1] - 1])

            # --> g
            if environments_grids["Obstacle"][current_pos[0], current_pos[1] - 1] != 1:
                possible_steps.append([current_pos[0], current_pos[1] - 1])

            # --> h
            if environments_grids["Obstacle"][current_pos[0] + 1, current_pos[1] - 1] != 1:
                possible_steps.append([current_pos[0] + 1, current_pos[1] - 1])

            # --> Remove previous direction as option
            if len(route) > 1:
                possible_steps.remove(route[-1])

            possible_steps_pheromones = []

            for possible_step in possible_steps:
                possible_steps_pheromones.append(swarm_grids[possible_step])

            print(possible_steps)
            print(possible_steps_pheromones)

            

            # viable_steps = []
            # back_step = None
            # total_surrounding_pheromone = 0
            #
            # for s in possible_steps:
            #     if self.previous_direction_opposite is not None and s[1] == self.previous_direction_opposite:
            #         back_step = s
            #     else:
            #         total_surrounding_pheromone += s[2]
            #         viable_steps.append(s)
            #
            # # If no other steps are present, allow stepping back
            # if len(viable_steps) == 0:
            #     return back_step
            #
            # # Randomize the order in which possible steps will be evaluated
            # random.shuffle(viable_steps)
            #
            # # Pick a step to take
            # random_number = self.rand.random()
            # for step in viable_steps:
            #     # Compute probability this step should be taken
            #     relative_pheromone = step[2] / total_surrounding_pheromone
            #
            #     # Take this step if the probability roll picked this step
            #     if relative_pheromone >= random_number:
            #         return step
            #     else:
            #         random_number -= relative_pheromone
            #
            # # If for some reason no step was found, return the last step evaluated
            # print("found no step")
            # return viable_steps[len(viable_steps) - 1]
