import logger

__author__ = "Blake Vogel"
__created__ = "04-09-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-10-2021"
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
            add_vehicle()                   : Add Vehicle to vehicle_list 
            move_position_vehicle_list()    : Move the position of a Vehicle in vehicle_list
            delete_vehicle_list()           : Delete Vehicle from vehicle_list
            get_max_vehicle_capacity()      : Getter for max_vehicle_capacity
            set_max_vehicle_capacity()      : Setter for max_vehicle_capacity
            get_total_lane_volume()         : Getter for total_lane_volume
            set_total_lane_volume()         : Setter for total_lane_volume
            get_total_lane_wait_time()      : Getter for total_lane_wait_time
            calculate_total_lane_wait_time(): Setter for total_lane_wait_time
        """
        
        self._length = None
        self._types_of_actions = []
        self._vehicle_list = []
        self._max_vehicle_capacity = None
        self._total_lane_volume = None
        self._total_lane_wait_time = None
    
    def get_length(self):
        """
        Gets the float value of the length of the lane.

        Parameters
        ----------
            N/A

        Returns
        -------
            length (float) : the length of a lane
        """
        if(type(self._length) != float):
            logger.write("Error! length must be of type float")
        elif(self._length == None):
            logger.write("Error! length contains no value")
        else:
            try:
                return self._length
            except Exception as e:
                logger.write("Error! Could not fetch the value of length: \n %s" % e)
    
    def set_length(self, new_length):
        """
        Assigns length variable new_length. 

        Parameters
        ----------
            new_length (float) : The new value for length variable

        Returns
        -------
            N/A
        """
        if(new_length == None):
            logger.write("Error! new_length cannot be a NoneType")
        elif(type(new_length) != float):
            logger.write("Error! new_length must be of type float")
        else:
            try:
                self._length = new_length
            except Exception as e:
                logger.write("Error! Could not set the new length:\n %s" % e)
    
    def get_types_of_actions(self):
        """
        Gets the list of types_of_actions that a car will make.

        Parameters
        ----------
            N/A

        Returns
        -------
            types_of_action (list of strings) : list of types of actions that a vehicle can make the lane
        """
        if(type(self._types_of_actions) != str):
            logger.write("Error! types_of_action must be of type string")
        elif(self._types_of_actions == None):
            logger.write("Error! types_of_action contains no value")
        elif(len(types_of_actions) == 0):
            logger.write("Error! types_of_actions list is empty")
        else:
            try:
                return self._types_of_actions
            except Exception as e:
                logger.write("Error! Could not fetch the list of types_of_actions: \n %s" % e)
    
    def add_types_of_actions(self, new_type_of_action):
        """
        Adds a new_type_of_action to the list of types_of_actions.

        Parameters
        ----------
            new_type_of_action (string) : A new type of action a vehicle can make in this lane

        Returns
        -------
            N/A
        """
        if(new_type_of_action == None):
            logger.write("Error! new_type_of_action cannot be a NoneType")
        elif(type(new_type_of_action) != str):
            logger.write("Error! new_type_of_action must be of type string")
        else:
            try:
                self._types_of_actions.append(new_type_of_action)
            except Exception as e:
                logger.write("Error! Could not add a new type of action to the types_of_actions list:\n %s" % e)
    
    def delete_action(self, type_of_action):
        """
        Delete type_of_action from the list of types_of_actions.

        Parameters
        ----------
            type_of_action : string

        Returns
        -------
            N/A
        """
        if(type(type_of_action) != str):
            logger.write("Error! type_of_action must be of type string")
        elif(type_of_action == None):
            logger.write("Error! type_of_action contains no value")
        elif(len(self._types_of_actions) == 0):
            logger.write("Error! types_of_actions list is empty")
        else:
            try:
                self._types_of_actions.remove(type_of_action)
            except Exception as e:
                logger.write("Error! could not remove type_of_action from types_of_actions list:\n %s" % e)
    
    def get_vehicle_list(self):
        """
        Gets the list of vehicle_list vehicle objects

        Parameters
        ----------
            N/A

        Returns
        -------
            vehicle_list (list of string) : list of Vehicle objects
        """
        if(type(self._vehicle_list) != str):
            logger.write("Error! vehicle_list must be of type string")
        elif(self._vehicle_list == None):
            logger.write("Error! vehicle_list contains no value")
        elif(len(self._vehicle_list) == 0):
            logger.write("Error! vehicle list is empty")
        else:
            try:
                return self._vehicle_list
            except Exception as e:
                logger.write("Error! Could not fetch the vehicle_list: \n %s" % e)

    def add_vehicle(self, new_vehicle):
        """
        Adds a new_vehicle to the list of vehicle_list.

        Parameters
        ----------
            new_vehicle (string) : Vehicle object

        Returns
        -------
            N/A
        """
        if(type(new_vehicle) != str):
            logger.write("Error! new_vehicle must be of type string")
        elif(new_vehicle == None):
            logger.write("Error! new_vehicle contains no value")
        else:
            try:
                self._vehicle_list.append(new_vehicle)
            except Exception as e:
                logger.write("Error! Could add new_vehicle to vehicle_list: \n %s" % e)
    
    def delete_vehicle(self, vehicle):
        """
        Delete vehicle from vehicle_list.

        Parameters
        ----------
            vehicle : string

        Returns
        -------
            N/A
        """
        if(type(vehicle) != str):
            logger.write("Error! vehicle must be of type string")
        elif(vehicle == None):
            logger.write("Error! vehicle contains no value")
        elif(len(self._vehicle_list) == 0):
            logger.write("Error! vehicle_list list is empty")
        else:
            try:
                self._vehicle_list.remove(vehicle)
            except Exception as e:
                logger.write("Error! could not remove vehicle from vehicle_list:\n %s" % e)

    def move_position_vehicle_list(self, vehicle_to_be_moved, position_to_be_moved):
        """
        Move vehicle_to_be_moved to position_to_be_moved in vehicle_list.

        Parameters
        ----------
            vehicle_to_be_moved : string
            position_to_be_moved : int

        Returns
        -------
            N/A
        """

        if(type(vehicle_to_be_moved) != str):
            logger.write("Error! vehicle_to_be_moved must be of type string")
        elif(type(position_to_be_moved) != int):
            logger.write("Error! position_to_be_moved must be of type int")
        elif(vehicle_to_be_moved == None):
            logger.write("Error! vehicle_to_be_moved contains no value")
        elif(position_to_be_moved == None):
            logger.write("Error! position_to_be_moved contains no value")
        elif(len(self._vehicle_list) == 0):
            logger.write("Error! vehicle_list is empty")
        else:
            try:
                self._vehicle_list[position_to_be_moved] = vehicle_to_be_moved
            except Exception as e:
                logger.write("Error! could not move vehicle_to_be_moved to position_to_be_moved:\n %s" % e)
    
    def get_max_vehicle_capacity(self):
        """
        Gets the integer value of max_vehicle_capacity.

        Parameters
        ----------
            N/A

        Returns
        -------
            max_vehicle_capacity (int) : the maximum number of vehicle allowed in a lane
        """
        if(type(self._max_vehicle_capacity) != int):
            logger.write("Error! max_vehicle_capacity must be of type int")
        elif(self._max_vehicle_capacity == None):
            logger.write("Error! max_vehicle_capacity contains no value")
        else:
            try:
                return self._max_vehicle_capacity
            except Exception as e:
                logger.write("Error! Could not fetch the value of max_vehicle_capacity: \n %s" % e)

    def set_max_vehicle_capacity(self, new_max_vehicle):
        """
        Assigns max_vehicle_capacity variable new_max_vehicle_capacity.

        Parameters
        ----------
            new_max_vehicle (int) : The new value for max_vehicle_capacity variable

        Returns
        -------
            N/A
        """
        if(new_max_vehicle == None):
            logger.write("Error! new_max_vehicle cannot be a NoneType")
        elif(type(new_max_vehicle) != int):
            logger.write("Error! new_max_vehicle must be of type int")
        else:
            try:
                self._max_vehicle_capacity = new_max_vehicle
            except Exception as e:
                logger.write("Error! Could not set the new max_vehicle:\n %s" % e)

    def get_total_lane_volume(self):
        """
        Gets the integer value of total_lane_volume.

        Parameters
        ----------
            N/A

        Returns
        -------
            total_lane_volume (int) : the total number of lanes
        """
        if(type(self._total_lane_volume) != int):
            logger.write("Error! total_lane_volume must be of type int")
        elif(self._total_lane_volume == None):
            logger.write("Error! total_lane_volume contains no value")
        else:
            try:
                return self._total_lane_volume
            except Exception as e:
                logger.write("Error! Could not fetch the value of total_lane_volume: \n %s" % e)
                
    def set_total_lane_volume(self, new_total_lane_volume):
        """
        Assigns total_lane_volume variable new_total_lane_volume.

        Parameters
        ----------
            new_total_lane_volume (int) : The new value for total_lane_volume variable

        Returns
        -------
            N/A
        """
        if(new_total_lane_volume == None):
            logger.write("Error! new_total_lane_volume cannot be a NoneType")
        elif(type(new_total_lane_volume) != int):
            logger.write("Error! new_total_lane_volume must be of type int")
        else:
            try:
                self._total_lane_volume = new_total_lane_volume
            except Exception as e:
                logger.write("Error! Could not set the new total_lane_volume:\n %s" % e)
    
    def get_total_lane_wait_time(self):
        """
        Gets the float value of total_lane_wait_time.

        Parameters
        ----------
            N/A

        Returns
        -------
            total_lane_wait_time (float) : the total lane wait time
        """
        if(type(self._total_lane_wait_time) != float):
            logger.write("Error! total_lane_volume must be of type int")
        elif(self._total_lane_wait_time == None):
            logger.write("Error! total_lane_wait_time contains no value")
        else:
            try:
                return self._total_lane_wait_time
            except Exception as e:
                logger.write("Error! Could not fetch the value of total_lane_wait_time: \n %s" % e)

    def calculate_total_lane_wait_time(self):
        """
        Calculates the total lane wait time by iterating through each object in the vehicle_list.  

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """

        if(type(self._vehicle_list) != str):
            logger.write("Error! vehicle_list must be of type string")
        elif(self._vehicle_list == None):
            logger.write("Error! vehicle_list contains no value")
        elif(len(self._vehicle_list) == 0):
            logger.write("Error! vehicle_list is empty")
        else:
            try:
                for v in self._vehicle_list:
                    self._total_lane_wait_time += v._wait_time
            except Exception as e:
                logger.write("Error! Could not calculate total_lane_wait_time: \n %s" % e)

