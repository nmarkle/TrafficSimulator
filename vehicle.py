from logger import Logger

__author__ = "Blake Vogel"
__created__ = "04-09-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-26-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.2"
__maintainer__ = "Blake Vogel"
__email__ = "bvogel@highpoint.edu"
__status__ = "In development need to still go over perform_action method"

class Vehicle:
    def __init__(self):
        """
        The vehicle class will be the blueprint for each vehicle 
        that appears within the simulation. Vehicles will travel 
        on a set path from one location to another. In order to do this, 
        it will be given a path, or a list of actions that will be performed 
        in order in order to get from point A to point B. The vehicle will also 
        have a wait time that is updated each time the vehicle waits at an intersection.
        These variables can be accessed using getter and setter functions.

        Attributes
        ----------
            x_pos (float)               : x position of where a vehicle is
            y_pos (float)               : y position of where a vehicle is 
            action_list (list)          : a list of actions
            wait_time (float)           : the wait time a vehicle experiences at a light

        Methods
        -------
            choose_action()         : Get an action from action_list
            perform_action()        : Performs an action
            get_x_pos()             : Getter for x_pos
            set_x_pos()             : Setter for x_pos
            get_y_pos()             : Getter for y_pos
            set_y_pos()             : Setter for y_pos
            get_wait_time()         : Getter for wait_time
            reset_wait_time()       : Reset for wait_time
            add_action()            : Add action to action_list
            delete_action()         : Delete action from action_list
        """
        self._x_pos = None
        self._y_pos = None
        self._action_list = []
        self._wait_time = None
        self._logger = Logger()
    
    def choose_action(self):
        """
        Returns the next action to be performed by choosing from the action_list class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            action (string) : an action that a vehicle will make
        """
        if(len(self._action_list) == 0):
            self._logger.write("Error! The action_list is empty")
        else:
            try:
                return self._action_list[0]
            except Exception as e:
                self._logger.write("Error! could not fetch an action:\n %s" % e)
        
    def perform_action(self, action):
        """

        Parameters
        ----------
            N/A

        Returns
        -------
           N/A
        """
        pass
 
    def get_x_pos(self):
        """
        Returns the value of the x_pos class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            x_pos (float) : the x position of the vehicle 
        """
        if(type(self._x_pos) != float):
            self._logger.write("Error! x_pos must be of type float")
        elif(self._x_pos == None):
            self._logger.write("Error! x_pos contains no value")
        else:
            try:
                return self._x_pos
            except Exception as e:
                self._logger.write("Error! Could not fetch the x_pos: \n %s" % e)

    def set_x_pos(self, new_x_pos):
        """
        Assigns x_pos variable the value of new_x_pos.

        Parameters
        ----------
            new_x_pos (float) : The new value for x_pos variable

        Returns
        -------
            N/A
        """
        if(new_x_pos == None):
            self._logger.write("Error! new_x_pos cannot be a NoneType")
        elif(type(new_x_pos) != float):
            self._logger.write("Error! new_x_pos must be of type float")
        else:
            try:
                self._x_pos = new_x_pos
            except Exception as e:
                self._logger.write("Error! Could not set the new x_pos:\n %s" % e)
    
    def get_y_pos(self):
        """
        Returns the value of the y_pos class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            y_pos (float) : the x position of the vehicle 
        """
        if(type(self._y_pos) != float):
            self._logger.write("Error! y_pos must be of type float")
        elif(self._y_pos == None):
            self._logger.write("Error! y_pos contains no value")
        else:
            try:
                return self._y_pos
            except Exception as e:
                self._logger.write("Error! Could not fetch the y_pos: \n %s" % e)

    def set_y_pos(self, new_y_pos):
        """
       Assigns y_pos variable the value of new_y_pos.

        Parameters
        ----------
            new_y_pos (float) : The new value for y_pos variable

        Returns
        -------
            N/A
        """
        if(new_y_pos == None):
            self._logger.write("Error! new_y_pos cannot be a NoneType")
        elif(type(new_y_pos) != float):
            self._logger.write("Error! new_y_pos must be of type float")
        else:
            try:
                self._y_pos = new_y_pos
            except Exception as e:
                self._logger.write("Error! Could not set the new y_pos:\n %s" % e)

    def get_wait_time(self):
        """
        Returns the value of the wait_time class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            wait_time (float) : the wait time of the vehicle at an intersection
        """
        if(self._wait_time == None):
            self._logger.write("Error! wait_time contains no value")
        elif(type(self._wait_time) != float):
            self._logger.write("Error! wait_time must be type float")
        else:
            try:
                return self._wait_time
            except Exception as e:
                self._logger.write("Error! Could not fetch the wait_time:\n %s" % e)
    
    def reset_wait_time(self):
        """
        Assigns the value of 0 to the wait_time variable. 
        This should happen when a vehicle begins waiting in a queue. (leaves an intersection)

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
            self._logger.write("Error! Could not reset wait_time: \n %s" % e)\
    
    def add_action(self, new_action):
        """
        This function appends the value of new_action to the class variable action_list.

        Parameters
        ----------
            new_action : string

        Returns
        -------
            N/A
        """

        if(type(new_action) != str):
            self._logger.write("Error! action must be of type string")
        elif(new_action == None):
            self._logger.write("Error! action contains no value")
        else:
            try:
                self._action_list.append(new_action)
            except Exception as e:
                self._logger.write("Error! could not add new_action to action_list:\n %s" % e)

    def delete_action(self, action):
        """
        This function removes an element of the same value as action from the action_list class variable.
        If there are no elements that match the value of action, then it throws an error.

        Parameters
        ----------
            action : string

        Returns
        -------
            N/A
        """
        if(type(action) != str):
            self._logger.write("Error! action must be of type string")
        elif(action == None):
            self._logger.write("Error! action contains no value")
        elif(len(self._action_list) == 0):
            self._logger.write("Error! action_list is empty")
        else:
            try:
                self._action_list.remove(action)
            except Exception as e:
                self._logger.write("Error! could not remove action from action_list:\n %s" % e)