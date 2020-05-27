
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import sys
import traceback
import time

# Libs
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThreadPool
from PyQt5.QtGui import QIcon

from qimage2ndarray import array2qimage

# Own modules
from RSAI_Engine.GUI.GUI_elements.Map_view_gui import Map_view_GUI
from RSAI_Engine.GUI.GUI_elements.Game_view_gui import Game_view_GUI

from RSAI_Engine.Simulation.RSAI_simulation import RSAI_simulation
from RSAI_Engine.Simulation.Tools.Views_generator import Views

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '7/02/2020'

##################################################################################################################


class RSAI_GUI():
    def __init__(self):
        app = QtWidgets.QApplication([])

        # --> Setting up thread pool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # --> Load RSAI GUI layout
        self.main_window = uic.loadUi("RSAI_Engine/GUI/Layouts/Layout_2.ui")
        self.main_window.setWindowIcon(QIcon("RSAI_Engine/Data/GUI_assets/RSAI_icon.png"))

        # --> Create RSAI sim
        self.simulation = RSAI_simulation()

        # ============================== Initiate map view
        # --> Load gui element
        self.map_view_gui = Map_view_GUI()

        # --> Initiate views trackers
        self.current_scale = "fit"
        self.current_view = "world"

        self.current_world_view = "Map"
        self.current_sim_view = "Overview"

        # --> Create map views
        self.views = Views(self.simulation)
        self.views_dict = self.map_view_gui.gen_views_dict(self)

        # --> Initiate view
        self.map_view_gui.update_map_view(self)

        # --> Update labels
        self.map_view_gui.update_position_summary(self)

        # --> Connect buttons
        self.main_window.scale_toggle.clicked.connect(self.change_scale)

        self.main_window.world_toggle.clicked.connect(self.toggle_world_view)
        self.main_window.simulation_toggle.clicked.connect(self.toggle_simulation_view)

        self.main_window.run_button.clicked.connect(self.run_simulation)

        # --> Connect comb boxes
        self.main_window.world_combo.currentIndexChanged.connect(self.change_world_sub_view)
        self.main_window.simulation_combo.currentIndexChanged.connect(self.change_sim_sub_view)

        # ============================== Initiate game view
        # --> Load gui element
        self.game_view_gui = Game_view_GUI()

        # --> Set dummy game view
        self.game_view_gui.dummy_view(self)

        # ============================== Display GUI
        self.main_window.show()

        sys.exit(app.exec())

    def update_gui(self, s):
        self.map_view_gui.update_map_view(self)
        self.map_view_gui.update_position_summary(self)

    def run_simulation(self):
        worker = Worker(self.simulation.run_simulation)
        worker.signals.progress.connect(self.update_gui)

        self.threadpool.start(worker)

        return

    # =======================================================================================================
    @property
    def scale(self):
        if self.current_scale == "fit":
            return 10000, 660
        else:
            return 10000, 1536

    @property
    def view_pixmap(self):
        if self.current_view == "world":
            return self.views_dict[self.current_view][self.current_world_view]
        else:
            return self.views_dict[self.current_view][self.current_sim_view]

    def change_scale(self):
        if self.current_scale == "fit":
            self.current_scale = "full"
            self.map_view_gui.update_map_view(self)

            # --> Adjust button text
            self.main_window.scale_toggle.setText("Scale view (Full screen)")

        else:
            self.current_scale = "fit"
            self.map_view_gui.update_map_view(self)

            # --> Adjust button text
            self.main_window.scale_toggle.setText("Scale view (Fit screen)")

        return

    def toggle_world_view(self):
        self.current_view = "world"
        self.map_view_gui.update_map_view(self)
        return

    def toggle_simulation_view(self):
        self.current_view = "simulation"
        self.map_view_gui.update_map_view(self)
        return

    def change_world_sub_view(self):
        self.current_world_view = self.main_window.world_combo.currentText()

        if self.current_view == "world":
            self.map_view_gui.update_map_view(self)
        return

    def change_sim_sub_view(self):
        self.current_sim_view = self.main_window.simulation_combo.currentText()

        if self.current_view == "simulation":
            self.map_view_gui.update_map_view(self)
        return


# =======================================================================================================
class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done