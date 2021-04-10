import logger

__author__ = "Blake Vogel"
__created__ = "04-09-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-10-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Blake Vogel"
__email__ = "bvogel@highpoint.edu"
__status__ = "In development first 4 methods need work"

class Vehicle:
    def __init__(self):
        """
        The vehicle class will be the blueprint for each vehicle 
        that appears within the simulation. Vehicles will travel 
        on a set path from one location to another. In order to do this, 
        it will be given a path, or a list of actions that will be performed 
        in order in order to get from point A to point B. The vehicle will also 
        have a wait time that is updated each time the vehicle waits at an intersection.
        These variables can be accessed using getter and setter functions

        Parameters
        ----------
            N/A

        Methods
        -------
            choose_action()         : Get an action from action_list
            perform_action()        : Performs an action
            update_action_list()    : 
            update_position()       :
            get_x_pos()             : Getter for x_pos
            set_x_pos()             : Setter for x_pos
            get_y_pos()             : Getter for y_pos
            set_y_pos()             : Setter for y_pos
            get_wait_time()         : Getter for wait_time
            reset_wait_time()       : Reset for wait_time
        """
        self._path = []
        self._x_pos = None
        self._y_pos = None
        self._action_list = []
        self._wait_time = None
        self._time_entered_queue = None
    
    def choose_action(self):
        """
        Gets the top action from the action_list

        Parameters
        ----------
            N/A

        Returns
        -------
            action (string) : an action that a vehicle will make
        """
        if(len(self._action_list) == 0):
            logger.write("Error! The action_list is empty")
        elif(type(self._action_list) != str):
            logger.write("Error! The action_list must be of type string")
        else:
            try:
                return self._action_list[0]
            except Exception as e:
                logger.write("Error! could not fetch an action:\n %s" % e)

        
    def perform_action(self, action):
        """
        performs the action from the choose action function

        Parameters
        ----------
            N/A

        Returns
        -------
           N/A
        """

        if(type(action) != str):
            logger.write("Error! Action must be of type string")

    def update_action_list(self):
        """
        

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
    def update_position(self):
        """
        

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
    
    def get_x_pos(self):
        """
        Gets the x_pos value

        Parameters
        ----------
            N/A

        Returns
        -------
            x_pos (float) : the x position of the vehicle 
        """
        if(type(self._x_pos) != float):
            logger.write("Error! x_pos must be of type float")
        elif(self._x_pos == None):
            logger.write("Error! x_pos contains no value")
        else:
            try:
                return self._x_pos
            except Exception as e:
                logger.write("Error! Could not fetch the x_pos: \n %s" % e)

    def set_x_pos(self, new_x_pos):
        """
        Setter for x_pos.

        Parameters
        ----------
            new_x_pos (float) : The new value for x_pos variable

        Returns
        -------
            N/A
        """
        if(new_x_pos == None):
            logger.write("Error! new_x_pos cannot be a NoneType")
        elif(type(new_x_pos) != float):
            logger.write("Error! new_x_pos must be of type float")
        else:
            try:
                self._x_pos = new_x_pos
            except Exception as e:
                logger.write("Error! Could not set the new x_pos:\n %s" % e)
    
    def get_y_pos(self):
        """
        Gets the y_pos value

        Parameters
        ----------
            N/A

        Returns
        -------
            y_pos (float) : the x position of the vehicle 
        """
        if(type(self._y_pos) != float):
            logger.write("Error! y_pos must be of type float")
        elif(self._y_pos == None):
            logger.write("Error! y_pos contains no value")
        else:
            try:
                return self._y_pos
            except Exception as e:
                logger.write("Error! Could not fetch the y_pos: \n %s" % e)

    def set_y_pos(self, new_y_pos):
        """
        Setter for y_pos.

        Parameters
        ----------
            new_y_pos (float) : The new value for y_pos variable

        Returns
        -------
            N/A
        """
        if(new_y_pos == None):
            logger.write("Error! new_y_pos cannot be a NoneType")
        elif(type(new_y_pos) != float):
            logger.write("Error! new_y_pos must be of type float")
        else:
            try:
                self._y_pos = new_y_pos
            except Exception as e:
                logger.write("Error! Could not set the new y_pos:\n %s" % e)

    def get_wait_time(self):
        """
        Gets the wait_time value

        Parameters
        ----------
            N/A

        Returns
        -------
            wait_time (float) : the wait time of the vehicle at an intersection
        """
        if(self._wait_time == None):
            logger.write("Error! wait_time contains no value")
        elif(type(self._wait_time) != float):
            logger.write("Error! wait_time must be type float")
        else:
            try:
                return self._wait_time
            except Exception as e:
                logger.write("Error! Could not fetch the wait_time:\n %s" % e)
    
    def reset_wait_time(self):
        """
        Resets the wait_time to 0.0

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
        try:
            self._wait_time = 0.0
        except Exception as e:
            logger.write("Error! Could not reset wait_time: \n %s" % e)
