
################################################################################################################
"""
A converter sub-class specialising in exchanging items for money (agent selling and buying)
"""

# Built-in/Generic Imports

# Libs

# Own modules
from Ingenium_Engine.Environment.Converters.Converter_gen import Converter
from Ingenium_Engine.Tools.Inventory_tools import Inventory_tools
from Ingenium_Engine.Tools.Interests_tools import Interests_tools

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class gen_transaction:
    def __init__(self, date, transaction_type, item_type, item, item_quantity, price_per_item):
        # --> Record transaction information
        self.date = date
        self.transaction_type = transaction_type

        self.item_type = item_type
        self.item = item
        self.item_quantity = item_quantity
        self.price_per_item = price_per_item

    def __str__(self):
        if self.transaction_type == "buy":
            return "Transaction --> " + self.item_type + ": " + self.item + " -" + str(self.item_quantity) + " units at " + str(self.price_per_item) + "$ (Net: +" + str(self.item_quantity * self.price_per_item) + "$)    " + self.date
        else:
            return "Transaction --> " + self.item_type + ": " + self.item + " +" + str(self.item_quantity) + " units at " + str(self.price_per_item) + "$ (Net: -" + str(self.item_quantity * self.price_per_item) + "$)    " + self.date

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    from datetime import date
    print(gen_transaction(date.today().strftime('%d/%m/%Y'), "Sell", "Resouces", "Iron", 10, 10))

