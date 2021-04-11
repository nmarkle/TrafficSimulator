import logger

__author__ = "Blake Vogel"
__created__ = "04-10-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-10-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Blake Vogel"
__email__ = "bvogel@highpoint.edu"
__status__ = "In development"

class Street:
    def __init__(self):
        """
        The Street class is responsible for keeping track of information about a street.
         Particularly the name of the street, its orientation, and the lanes that compose the street.

        Parameters
        ----------
            N/A

        Methods
        -------
            set_name()                      : Setter for name
            get_name()                      : Getter for name
            set_orientation()               : Setter for orientation
            get_orientation()               : Getter for orientation
            get_lane_list()                 : Getter for lane_list
            add_lane()                      : Add lane to lane_list
            delete_lane()                   : Delete lane from lane_list
            calculate_street_wait_time()    : Street wait_time for all lanes 
            calculate_street_volume()       : Street volume for all lanes

        """
        
        self._name = None
        self._orientation = None
        self._lane_list = None
        self._average_street_wait_time = None
        self._average_street_volume = None

    def get_name(self):
        """
        Returns the value of the name class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            name (string) : the name of street
        """
        if(type(self._name) != str):
            logger.write("Error! name must be of type string")
        elif(self._name == None):
            logger.write("Error! name contains no value")
        else:
            try:
                return self._name
            except Exception as e:
                logger.write("Error! Could not fetch the value of name: \n %s" % e)
    
    def set_name(self, new_name):
        """
        Assigns name class variable the value of new_name variable. 

        Parameters
        ----------
            new_name (string) : The new value for name variable

        Returns
        -------
            N/A
        """
        if(new_name == None):
            logger.write("Error! new_name cannot be a NoneType")
        elif(type(new_name) != str):
            logger.write("Error! new_name must be of type string")
        else:
            try:
                self._name = new_name
            except Exception as e:
                logger.write("Error! Could not set the new name:\n %s" % e)

    def get_orientation(self):
        """
        Returns the value of the orientation class variable. 

        Parameters
        ----------
            N/A

        Returns
        -------
            orientation (string) : The orientation of the street
        """
        if(type(self._orientation) != str):
            logger.write("Error! orientation must be of type string")
        elif(self._orientation == None):
            logger.write("Error! orientation contains no value")
        else:
            try:
                return self._orientation
            except Exception as e:
                logger.write("Error! Could not fetch the value of orientation: \n %s" % e)
    
    def set_orientation(self, new_orientation):
        """
        Assigns orientation class variable the value of new_orientation variable. 

        Parameters
        ----------
            new_orientation (string) : The new value for orientation variable

        Returns
        -------
            N/A
        """
        if(new_orientation == None):
            logger.write("Error! new_orientation cannot be a NoneType")
        elif(type(new_orientation) != str):
            logger.write("Error! new_orientation must be of type string")
        else:
            try:
                self._orientation = new_orientation
            except Exception as e:
                logger.write("Error! Could not set the new orientation:\n %s" % e)

    def get_lane_list(self):
        """
        Returns the value of the lane_list class variable. 

        Parameters
        ----------
            N/A

        Returns
        -------
            lane_list (string) : List of lanes
        """
        if(type(self._lane_list) != str):
            logger.write("Error! lane_list must be of type string")
        elif(self._lane_list == None):
            logger.write("Error! lane_list contains no value")
        elif(len(self._lane_list) == 0):
            logger.write("Error! lane_list is empty")
        else:
            try:
                return self._lane_list
            except Exception as e:
                logger.write("Error! Could not fetch the value of lane_list: \n %s" % e)
    
    def add_lane(self, new_lane):
        """
        Appends new_lane to the lane_list class variable.

        Parameters
        ----------
            new_lane (string) : Lane object

        Returns
        -------
            N/A
        """

        if(type(new_lane) != str):
            logger.write("Error! new_lane must be of type string")
        elif(new_lane == None):
            logger.write("Error! new_lane contains no value")
        else:
            try:
                self._lane_list.append(new_lane)
            except Exception as e:
                logger.write("Error! Could add new_lane to lane_list: \n %s" % e)

    def delete_vehicle(self, lane):
        """
        If lane present in the lane_list class variable, remove it. Otherwise, provide an error message.

        Parameters
        ----------
            lane (string) : Lane Object

        Returns
        -------
            N/A
        """
        if(type(lane) != str):
            logger.write("Error! lane must be of type string")
        elif(vehicle == None):
            logger.write("Error! lane contains no value")
        elif(len(self._lane_list) == 0):
            logger.write("Error! lane_list is empty")
        else:
            try:
                self._lane_list.remove(lane)
            except Exception as e:
                logger.write("Error! could not remove lane from lane_list:\n %s" % e)
    
    def calculate_total_street_wait_time(self):
        """
        Gets the list of lanes and from each lane get the average lane wait time. 
        Then computes the average of all the lanes for the street.

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """

        if(type(self._lane_list) != str):
            logger.write("Error! lane_list must be of type string")
        elif(self._lane_list == None):
            logger.write("Error! lane_list contains no value")
        elif(len(self._lane_list) == 0):
            logger.write("Error! lane_list is empty")
        else:
            try:
                for l in self._lane_list:
                    self._average_street_wait_time += l.total_lane_wait_time

                self._average_street_wait_time = self._average_street_wait_time / len(self._lane_list)
            except Exception as e:
                logger.write("Error! Could not calculate average_street_wait_time: \n %s" % e)

    def calculate_street_volume(self):
        """
        Gets the list of lanes and from each lane get the total lane volume. 
        Then computes the total street volume by adding all the lane volumes together. 

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """

        if(type(self._lane_list) != str):
            logger.write("Error! lane_list must be of type string")
        elif(self._lane_list == None):
            logger.write("Error! lane_list contains no value")
        elif(len(self._lane_list) == 0):
            logger.write("Error! lane_list is empty")
        else:
            try:
                for l in self._lane_list:
                    self._average_street_volume += l.total_lane_volume 

                self._average_street_volume = self._average_street_volume / len(self._lane_list)
            except Exception as e:
                logger.write("Error! Could not calculate average_street_volume: \n %s" % e)