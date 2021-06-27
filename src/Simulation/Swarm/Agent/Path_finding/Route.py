
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Route(list):
    @property
    def reduced(self):
        """
        Reduces the cells visited in the route. If a cell is visited twice, all steps between the two visits are removed.
        For example: the route covering cells [a, b, c, d, e, b, f] will be reduced to [a, b, f].
        The reduced route is stored in self.reduced
        """

        def list_duplicates_of(seq, item):
            start_at = -1
            locs = []
            while True:
                try:
                    loc = seq.index(item, start_at + 1)
                except ValueError:
                    break
                else:
                    locs.append(loc)
                    start_at = loc
            return locs

        non_repeated_steps = []
        repeated_steps = []

        for index, i in enumerate(self):
            if i not in non_repeated_steps:
                non_repeated_steps.append(i)
            else:
                repeated_steps.append(i)

        reduced_route = self

        for _ in range(len(repeated_steps)):
            repeated_step_index = list_duplicates_of(reduced_route, repeated_steps.pop(0))

            if len(repeated_step_index) > 1:
                reduced_route = reduced_route[:repeated_step_index[0]] + reduced_route[repeated_step_index[-1]:]

        return reduced_route


if __name__ == "__main__":
    x = Route([1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5])

    print(x.reduced)
