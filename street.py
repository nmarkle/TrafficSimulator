from logger import Logger
from lane import Lane

__author__ = "Blake Vogel"
__created__ = "04-10-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-26-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.2"
__maintainer__ = "Blake Vogel"
__email__ = "bvogel@highpoint.edu"
__status__ = "In development"


class Street:
    def __init__(self):
        """
        The Street class is responsible for keeping track of information about a street.
         Particularly the name of the street, its orientation, and the lanes that compose the street.

        Attributes
        ----------
            name (string)                       : the name of a street
            orientation (string)                : the orientation of a street i.e. (N,S) or (E,W)
            lane_list (list)                    : list of lanes
            average_street_wait_time (float)    : average street wait time
            average_street_volume (float)       : average street volume over a certain time
            begin_lanes (list)                  : list of begin lanes where begins wait in to move through an intersection
            end_lanes (list)                    : list of end lanes where vehicles turn into

        Methods
        -------
            set_name()                          : Setter for name
            get_name()                          : Getter for name
            set_orientation()                   : Setter for orientation
            get_orientation()                   : Getter for orientation
            get_lane_list()                     : Getter for lane_list
            set_lane_list()                     : Setter for lane_list
            get_begin_lanes()                   : Getter for being_lanes
            add_begin_lane()                    : Adds begin_lane to begin_lanes
            add_end_lane()                      : Adds end_lane to end_lanes
            get_end_lane()                      : Getter for end_lanes
            delete_end_lane()                   : Delete lane from end_lanes
            delete_begin_lane()                 : Delete lane from begin_lanes
            calculate_total_street_wait_time()  : Street wait_time for all lanes
            calculate_street_volume()           : Street volume for all lanes            
        """

        self._name = None
        self._orientation = None
        self._lane_list = []
        self._average_street_wait_time = None
        self._average_street_volume = None
        self._begin_lanes = []
        self._end_lanes = []
        self._logger = Logger()

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
            self._logger.write("Error! name must be of type string")
        elif(self._name == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._name
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of name: \n %s" % e)

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
            self._logger.write("Error! new_name cannot be a NoneType")
        elif(type(new_name) != str):
            self._logger.write("Error! new_name must be of type string")
        else:
            try:
                self._name = new_name
            except Exception as e:
                self._logger.write("Error! Could not set the new name:\n %s" % e)

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
            self._logger.write("Error! orientation must be of type string")
        elif(self._orientation == None):
            self._logger.write("Error! orientation contains no value")
        else:
            try:
                return self._orientation
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of orientation: \n %s" % e)

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
            self._logger.write("Error! new_orientation cannot be a NoneType")
        elif(type(new_orientation) != str):
            self._logger.write("Error! new_orientation must be of type string")
        else:
            try:
                self._orientation = new_orientation
            except Exception as e:
                self._logger.write("Error! Could not set the new orientation:\n %s" % e)

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
        if(self._lane_list == None):
            self._logger.write("Error! lane_list contains no value")
        elif(len(self._lane_list) == 0):
            self._logger.write("Error! lane_list is empty")
        else:
            try:
                return self._lane_list
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of lane_list: \n %s" % e)

    def set_lane_list(self):
        """
        combines begin and end lane lists into lane_list

        Parameters
        ----------
            N/A

        Returns
        -------
            lane_list (string) : List of lanes
        """
        if(self._lane_list == None):
            self._logger.write("Error! lane_list contains no value")
        else:
            try:
                self._lane_list = self._end_lanes + self._begin_lanes
            except Exception as e:
                self._logger.write("Error! Could not set lane_list: \n %s" % e)

    def get_begin_lanes(self):
        """
        Returns the value of the begin_lanes class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            begin_lanes (string) : List of lanes
        """
        if(self._begin_lanes == None):
            self._logger.write("Error! begin_lanes contains no value")
        elif(len(self._begin_lanes) == 0):
            self._logger.write("Error! begin_lanes is empty")
        else:
            try:
                return self._begin_lanes
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of begin_lanes: \n %s" % e)

    def add_begin_lane(self, new_begin_lane):
        """
        Appends new_begin_lane to begin_lanes

        Parameters
        ----------
            new_begin_lane (Lane) : Lane object

        Returns
        -------
            N/A
        """
        if(new_begin_lane == None):
            self._logger.write("Error! new_begin_lane contains no value")
        else:
            try:
                self._begin_lanes.append(new_begin_lane)
            except Exception as e:
                self._logger.write("Error! Could add new_begin_lane to _begin_lanes: \n %s" % e)

    def add_end_lane(self, new_end_lane):
        """
        Appends new_end_lane to the end_lanes class variable.

        Parameters
        ----------
            new_end_lane (Lane) : Lane object

        Returns
        -------
            N/A
        """
        if(new_end_lane == None):
            self._logger.write("Error! new_end_lane contains no value")
        else:
            try:
                self._end_lanes.append(new_end_lane)
            except Exception as e:
                self._logger.write("Error! Could add new_end_lane to _end_lanes: \n %s" % e)

    def get_end_lanes(self):
        """
        Returns the value of the end_lanes class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            end_lanes (Lane) : List of lanes
        """
        if(self._end_lanes == None):
            self._logger.write("Error! end_lanes contains no value")
        elif(len(self._end_lanes) == 0):
            self._logger.write("Error! end_lanes is empty")
        else:
            try:
                return self._end_lanes
            except Exception as e:
                self._logger.write("Error! Could not fetch the value of end_lanes: \n %s" % e)

    def delete_begin_lane(self, lane):
        """
        If lane present in the begin_lanes class variable, remove it. Otherwise, provide an error message.

        Parameters
        ----------
            lane (Lane) : Lane Object

        Returns
        -------
            N/A
        """

        if(lane == None):
            self._logger.write("Error! lane contains no value")
        elif(len(self._lane_list) == 0):
            self._logger.write("Error! begin_lanes is empty")
        else:
            try:
                self._begin_lanes.remove(lane)
            except Exception as e:
                self._logger.write("Error! could not remove lane from begin_lanes:\n %s" % e)

    def delete_end_lane(self, lane):
        """
        If lane present in the end_lanes class variable, remove it. Otherwise, provide an error message.

        Parameters
        ----------
            lane (Lane) : Lane Object

        Returns
        -------
            N/A
        """

        if(lane == None):
            self._logger.write("Error! lane contains no value")
        elif(len(self._lane_list) == 0):
            self._logger.write("Error! end_lanes is empty")
        else:
            try:
                self._end_lanes.remove(lane)
            except Exception as e:
                self._logger.write("Error! could not remove lane from end_lanes:\n %s" % e)

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
            self._logger.write("Error! lane_list must be of type string")
        elif(self._lane_list == None):
            self._logger.write("Error! lane_list contains no value")
        elif(len(self._lane_list) == 0):
            self._logger.write("Error! lane_list is empty")
        else:
            try:
                for l in self._lane_list:
                    self._average_street_wait_time += l.total_lane_wait_time

                self._average_street_wait_time = self._average_street_wait_time/len(self._lane_list)
            except Exception as e:
                self._logger.write("Error! Could not calculate average_street_wait_time: \n %s" % e)

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
            self._logger.write("Error! lane_list must be of type string")
        elif(self._lane_list == None):
            self._logger.write("Error! lane_list contains no value")
        elif(len(self._lane_list) == 0):
            self._logger.write("Error! lane_list is empty")
        else:
            try:
                for l in self._lane_list:
                    self._average_street_volume += l.total_lane_volume
                    self._average_street_volume = self._average_street_volume/ len(self._lane_list)
            except Exception as e:
                self._logger.write("Error! Could not calculate average_street_volume: \n %s" % e)