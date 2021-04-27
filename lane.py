from logger import Logger
from vehicle import Vehicle

__author__ = "Blake Vogel"
__created__ = "04-09-2021"
__editor__ = "Blake Vogel, Nathan Markle"
__edited__ = "04-26-2021"
__rationale___ = "Fixed errors"
__version__ = "0.0.3"
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

        Attributes
        ----------
            length (int)                    : Length of the lane
            types_of_actions (list of str)  : List of valid actions for the lane
            max_vehicle_capacity (int)      : Max number of vehicles per lane
            total_lane_volume (int)         : Metric for the number of cars that passed through the lane
            total_lane_wait_time (float)    : Metric for the amount of time each car waited in the lane
            vehicle_list (list of Vehicle)  : The Vehicles present in this lane
            light_status (bool)             : Whether the light is on or not
            logger (Logger)                 : The Logger to handle errors within the Lane
            starting_coordinate (tuple)     : A tuple to keep track of the coordinate

        Methods
        -------
            get_length()                    : Getter for length
            set_length()                    : Setter for length
            get_types_of_actions()          : Getter for types_of_actions
            add_types_of_actions()          : Setter for types_of_actions
            delete_types_of_actions()       : Delete types_of_actions
            get_max_vehicle_capacity()      : Getter for max_vehicle_capacity
            set_max_vehicle_capacity()      : Setter for max_vehicle_capacity
            get_total_lane_volume()         : Getter for total_lane_volume
            set_total_lane_volume()         : Setter for total_lane_volume
            get_total_lane_wait_time()      : Getter for total_lane_wait_time
            calculate_total_lane_wait_time(): Setter for total_lane_wait_time
            enqueue()                       : Adds a vehicle to the bottom of end_list
            dequeue()                       : Removes a vehicle from the top of vehicle_list 
            get_vehicle_list                : Gets the vehicle_list
            get_light_status()              : Getter for light_status
            set_light_status()              : Setter for light_status
            change_light()                  : Inverses the current boolean status
            set_starting_coordinate()       : Setter for starting_coordinate
            get_starting_coordinate()       : Getter for starting_coordinate
        """
        
        self._length = None
        self._types_of_actions = []
        self._max_vehicle_capacity = None
        self._total_lane_volume = None
        self._total_lane_wait_time = None
        self._vehicle_list = []
        self._light_status = None
        self._logger = Logger()
        self._starting_coordinate = None
        
    
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
            self._logger.write("Error! length must be of type float")
        elif(self._length == None):
            self._logger.write("Error! length contains no value")
        else:
            try:
                return self._length
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of length: \n %s" % e)
    
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
            self._logger.write("Error! new_length cannot be a NoneType")
        elif(type(new_length) != float):
            self._logger.write("Error! new_length must be of type float")
        else:
            try:
                self._length = new_length
            except Exception as e:
                self._logger.write("Error! Could not set the new length:\n %s" % e)
    
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
        if(self._types_of_actions == None):
            self._logger.write("Error! types_of_action contains no value")
        elif(len(self._types_of_actions) == 0):
            self._logger.write("Error! types_of_actions list is empty")
        else:
            try:
                return self._types_of_actions
            except Exception as e:
                self._logger.write("Error! Could not fetch the list of types_of_actions: \n %s" % e)
    
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
            self._logger.write("Error! new_type_of_action cannot be a NoneType")
        elif(type(new_type_of_action) != str):
            self._logger.write("Error! new_type_of_action must be of type string")
        else:
            try:
                self._types_of_actions.append(new_type_of_action)
            except Exception as e:
                self._logger.write("Error! Could not add a new type of action to the types_of_actions list:\n %s" % e)
    
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
            self._logger.write("Error! type_of_action must be of type string")
        elif(type_of_action == None):
            self._logger.write("Error! type_of_action contains no value")
        elif(len(self._types_of_actions) == 0):
            self._logger.write("Error! types_of_actions list is empty")
        else:
            try:
                self._types_of_actions.remove(type_of_action)
            except Exception as e:
                self._logger.write("Error! could not remove type_of_action from types_of_actions list:\n %s" % e)
    
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
            self._logger.write("Error! max_vehicle_capacity must be of type int")
        elif(self._max_vehicle_capacity == None):
            self._logger.write("Error! max_vehicle_capacity contains no value")
        else:
            try:
                return self._max_vehicle_capacity
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of max_vehicle_capacity: \n %s" % e)

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
            self._logger.write("Error! new_max_vehicle cannot be a NoneType")
        elif(type(new_max_vehicle) != int):
            self._logger.write("Error! new_max_vehicle must be of type int")
        else:
            try:
                self._max_vehicle_capacity = new_max_vehicle
            except Exception as e:
                self._logger.write("Error! Could not set the new max_vehicle:\n %s" % e)

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
            self._logger.write("Error! total_lane_volume must be of type int")
        elif(self._total_lane_volume == None):
            self._logger.write("Error! total_lane_volume contains no value")
        else:
            try:
                return self._total_lane_volume
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of total_lane_volume: \n %s" % e)
                
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
            self._logger.write("Error! new_total_lane_volume cannot be a NoneType")
        elif(type(new_total_lane_volume) != int):
            self._logger.write("Error! new_total_lane_volume must be of type int")
        else:
            try:
                self._total_lane_volume = new_total_lane_volume
            except Exception as e:
                self._logger.write("Error! Could not set the new total_lane_volume:\n %s" % e)
    
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
            self._logger.write("Error! total_lane_volume must be of type int")
        elif(self._total_lane_wait_time == None):
            self._logger.write("Error! total_lane_wait_time contains no value")
        else:
            try:
                return self._total_lane_wait_time
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of total_lane_wait_time: \n %s" % e)

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

        if(self._vehicle_list == None):
            self._logger.write("Error! vehicle_list contains no value")
        elif(len(self._vehicle_list) == 0):
            self._logger.write("Error! vehicle_list is empty")
        else:
            try:
                for v in self._vehicle_list:
                    self._total_lane_wait_time += v._wait_time
            except Exception as e:
                self._logger.write("Error! Could not calculate total_lane_wait_time: \n %s" % e)

    def enqueue(self, vehicle):
        """
        Adds a vehicle to the to the bottom of end_list

        Parameters
        ----------
            vehicle (Vehicle Object) : vehicle to be added to end_list

        Returns
        -------
            N/A
        """

        if(vehicle == None):
            self._logger.write("Error! vehicle cannot be a NoneType")
        else:
            try:
                self._vehicle_list.append(vehicle)
            except Exception as e:
                self._logger.write("Error! Could not add vehicle to end_list:\n %s" % e)
    
    def dequeue(self):
        """
        Removes a vehicle from the top of the vehicle_list

        Parameters
        ----------
            N/A

        Returns
        -------
            vehicle (Vehicle Object) : a vehicle that is being removed from a lane
        """

        if(len(self._vehicle_list) == 0):
            self._logger.write("Error! Vehicle list is empty")
        else:
            try:
                return self._vehicle_list.pop(0)
            except Exception as e:
                self._logger.write("Error! failed to pop the top vehicle off vehicle list")
                
    def get_vehicle_list(self):
        """
        Getter for the vehicle_list

        Parameters
        ----------
            N/A

        Returns
        -------
            vehicle_list (list) : a vehicle_list in a lane
        """
        if(self._vehicle_list == None):
            self._logger.write("Error! _vehicle_list contains no value")
        elif(len(self._vehicle_list) == 0):
            self._logger.write("Error! _vehicle_list list is empty")
        else:
            try:
                return self._vehicle_list
            except Exception as e:
                self._logger.write("Error! Could not fetch the list of _vehicle_list: \n %s" % e)
                
    def get_light_status(self):
        """
        Return the status of light_status
        
        Parameters
        ----------
            N/A
        Returns
        -------
            light_status : boolean
        """
        return self._light_status
    
    def set_light_status(self, new_light_status):
        """
        Setter for the light_status

        Parameters
        ----------
            new_light_status (bool) : The new status for the light
        
        Returns
        -------
            N/A
        """
        if type(new_light_status) != bool:
            self._logger.write("Error! new_light_status should be of type bool")
        try:
            self._light_status = new_light_status
        except Exception as e:
            self._logger.write("Error! could not set light status")
   
    def change_light(self):
        """
        Changes the status of the light

        Parameters
        ----------
            N/A
        Returns
        -------
            N/A
        """
        self._light_status = not self._light_status

    def set_starting_coordinate(self, new_coordinate):
        """
        Sets the starting coordinate for the first Vehicle in the lane list

        Parameters
        ----------
            new_coordinate (tuple) : A tuple containing the x and y value of the starting coordinate of the lane

        Returns
        -------
            N/A
        """
        if type(new_coordinate) != tuple:
            self._logger.write("Error! new_coordinate should be a tuple")
        elif new_coordinate == None:
            self._logger.write("Error! new_coordinate does not contain a value")
        else:
            try:
                self._starting_coordinate = new_coordinate
            except Exception as e:
                self._logger.write("Error! could not set _starting_coordinate: %s" % e)

    def get_starting_coordinate(self):
        """
        Gets the starting coordinate for the first Vehicle in the lane list

        Parameters
        ----------
            N/A

        Returns
        -------
            new_coordinate (tuple) : A tuple containing the x and y value of the starting coordinate of the lane
        """
        if type(self._starting_coordinate) != tuple:
            self._logger.write("Error! starting_coordinate should be a tupple")
        elif self._starting_coordinate == None:
            #this is dead code
            self._logger.write("Error! starting_coordinate does not contain a value")
        else:
            try:
                return self._starting_coordinate
            except Exception as e:
                self._logger.write("Error! could not get starting_coordinate: %s" % e)