
################################################################################################################
"""

"""

# Built-in/Generic Imports
from distutils import util

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Shop_prints:
    def __init__(self):
        with open("src/Settings/Settings_cache/Print_settings", "r") as cache:
            for line in cache:
                if line.split()[0] == "Environment_prints":
                    environment_print_setting = bool(util.strtobool(line.split()[-1]))
                    break

        if environment_print_setting is False:
            self.transaction_recap = self.__monkey_patch_pass
            self.successful_buy_transaction_recap = self.__monkey_patch_pass
            self.successful_sell_transaction_recap = self.__monkey_patch_pass
            self.print_1 = self.__monkey_patch_pass
            self.print_2 = self.__monkey_patch_pass
            self.print_3 = self.__monkey_patch_pass
            self.print_4 = self.__monkey_patch_pass
            self.print_5 = self.__monkey_patch_pass
            self.print_6 = self.__monkey_patch_pass
            self.print_7 = self.__monkey_patch_pass
            self.print_8 = self.__monkey_patch_pass
            self.print_9 = self.__monkey_patch_pass

    @staticmethod
    def __monkey_patch_pass(*args, **kwargs):
        return

    @staticmethod
    def transaction_recap(name,
                          transaction_type,
                          item_type,
                          item,
                          quantity_requested,
                          agent_expectation,
                          market_expectation):
        print("Transaction request recap:")
        print("Agent trading:", name)
        print("Transaction type:", transaction_type)
        print("Requested item:", item_type, item)
        print("Quantity requested: " + quantity_requested)
        print("(Agent price) " + agent_expectation + " - " + market_expectation + " (Market price)\n")

    @staticmethod
    def successful_buy_transaction_recap(item_quantity, item_type, item, price_per_item):
        print(f"Transaction successful, {item_quantity} units of {item} {item_type} brought at {price_per_item}$ per unit")

    @staticmethod
    def successful_sell_transaction_recap(item_quantity, item_type, item, price_per_item):
        print(f"Transaction successful, {item_quantity} units of {item} {item_type} sold at {price_per_item}$ per unit")

    @staticmethod
    def print_1():
        print("Agent money too low for item")

    @staticmethod
    def print_2():
        print("Market expectation too high")

    @staticmethod
    def print_3(item, available_item_count):
        print(f"Requested {item} quantity not available (max available: {available_item_count} )")

    @staticmethod
    def print_4(item):
        print(f"Requested " + item + " not available")

    @staticmethod
    def print_5(item_type):
        print(f"{item_type} not tradable in this market")

    @staticmethod
    def print_6():
        print("Market funds insufficient")

    @staticmethod
    def print_7():
        print("Market expectation too low")

    @staticmethod
    def print_8():
        print("Invalid transaction type")

    @staticmethod
    def print_9():
        print("item not in inventory")
