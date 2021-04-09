import logger

__author__ = "Blake Vogel"
__created__ = "04-09-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-09-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Blake Vogel"
__email__ = "bvogel@highpoint.edu"
__status__ = "In development"

class Lane:
    def __init__(self):
        """
        The lane class will represent the discrete lanes present 
        at each street within the simulation software. The Lane 
        object will possess getters and setters for all of it’s
        inherent class variables.

        Parameters
        ----------
            N/A

        Methods
        -------
            get_length()                    : Getter for length
            set_length()                    : Setter for length
            get_types_of_actions()          : Getter for types_of_actions
            add_types_of_actions()          : Setter for types_of_actions
            delete_types_of_actions()       : Delete types_of_actions
            get_vehicle_list()              : Getter for vehicle_list
            add_vehicle_list()              : Add Vehicle to vehicle_list 
            move_position_vehicle_list()    : Move the position of a Vehicle in vehicle_list
            delete_vehicle_list()           : Delete Vehicle from vehicle_list
            get_max_vehicle_capacity()      : Getter for max_vehicle_capacity
            set_max_vehicle_capacity()      : Setter for max_vehicle_capacity
            get_total_lane_volume()         :
            set_total_lane_volume()         :
            get_total_lane_wait_time()      :
            set_total_lane_wait_time()      :
        """