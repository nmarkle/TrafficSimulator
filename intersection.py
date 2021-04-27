__author__ = "Blake Vogel"
__created__ = "04-20-2021"
__editor__ = "Blake Vogel"
__edited__ = "04-26-2021"
__rationale___ = "Created"
__version__ = "0.0.3"
__maintainer__ = "Blake Vogel"
__email__ = "bvogel@highpoint.edu"
__status__ = "In development"

from vehicle import Vehicle
from lane import Lane
from logger import Logger
from street import Street


class Intersection():
    def __init__(self):
        """
        The intersection class will represent the discrete intersections present where
        two streets converge. The intersection class will possess getters and setters
        for all of it's inherent class variables and methods to calculate relevant 
        metrics.

        Attributes
        ----------
            street_list (list of Street objects) : List to hold all the Streets of an Intersection
            average_wait_time                    : average wait time 
            traffic_light_list (list)            : list of traffic lights
            total_traffic_volume                 : total traffic volume
            logger = logger.Logger()             : logger object

        Methods
        -------
            add_street()                  : Adds an additional street to the intersection's street list
            get_street_list()             : Returns the intersection's street list
            delete_street()               : Deletes the street from the list of streets
            get_traffic_light_list()      : Returns the intersection's traffic light list
            add_traffic_light()           : Adds an additional traffic light to the intersection's traffic light list
            delete_traffic_light()        : Removes a traffic light from the intersection's traffic light list
            calculate_average_wait_time() : Calculates the average wait time for the intersection based off the
                                            average wait time of every street.
            calculate_traffic_volume()    : Calculates the traffic volume based off the volumes of every street
            left()                        : Have a vehicle make a left turn
            straight()                    : Have a vehicle go straight
            right()                       : Have a vehicle make a right turn
            move_vehicle()                : Move a vehicle from one lane to another
            logger()                      : Logger object for error handling
        """
        self._street_list = []
        self._average_wait_time = None
        self._traffic_light_list = []
        self._total_traffic_volume = None
        self._logger = Logger()

    def add_street(self, new_street):
        """
        Adds an additional street to the intersection's street list

        Parameters
        ----------
            new_street (Street) : The new street to be added to this intersection

        Returns
        -------
            N/A
        """
        if(new_street == None):
            self._logger.write("Error! New Street cannot be a NoneType.")
        else:
            try:
                self._street_list.append(new_street)
            except Exception as e:
                self._logger.write("Error! Could not add the new Street object to list:\n %s" % e)

    def get_street_list(self):
        """
        Returns the intersection's street list

        Parameters
        ----------
            N/A

        Returns
        -------
            street_list (list of Street objects) : The list representing the streets of the intersection
        """
        if(len(self._street_list) == 0):
            self._logger.write("Error! Street list is empty.")
        else:
            try:
                return self._street_list
            except Exception as e:
                self._logger.write("Error! Unable to return the street list:\n %s" % e)

    def delete_street(self, street):
        """
        Deletes the street from the list of streets

        Parameters
        ----------
            street (Street) : The street to be removed from the list of streets

        Returns
        -------
            N/A
        """
        if(street == None):
            self._logger.write("Error! Street to remove cannot be NoneType.")
        elif(type(street) != street.Street):
            self._logger.write("Error! Cannot remove non-Street type from list.")
        else:
            try:
                self._street_list.remove(street)
            except Exception as e:
                self._logger.write("Error! Could not remove street from list:\n %s" % e)

    def get_traffic_light_list(self):
        """
        Gets the list of traffic lights

        Parameters
        ----------
            N/A

        Returns
        -------
            traffic_light_list (list of Traffic_Light objects) : The list representing the traffic lights of the intersection
        """
        if(len(self._traffic_light_list) == 0):
            self._logger.write("Error! Traffic light list is empty.")
        else:
            try:
                return self._traffic_light_list
            except Exception as e:
                self._logger.write("Error! Unable to return the traffic light list:\n %s" % e)

    def add_traffic_light(self, new_traffic_light):
        """
        Adds an additional Traffic_Light to the intersection's traffic light list

        Parameters
        ----------
            new_traffic_light (Traffic_Light) : New Traffic_Light to be added to the intersection

        Returns
        -------
            N/A
        """
        if(new_traffic_light == None):
            self._logger.write("Error! New traffic light cannot be NoneType.")
        elif(type(new_traffic_light) != traffic_light.Traffic_Light):
            self._logger.write("Error! New traffic light must be of type Traffic_Light.")
        else:
            try:
                self._traffic_light_list.append(new_traffic_light)
            except Exception as e:
                self._logger.write("Error! Unable to add traffic light to traffic light list:\n %s" % e)

    def delete_traffic_light(self, traffic_light):
        """
        Removes the traffic light from the intersections Traffic_Light list

        Parameters
        ----------
            traffic_light (Traffic_Light) : The Traffic_Light to be removed

        Returns
        -------
            N/A
        """
        if(traffic_light == None):
            self._logger.write("Error! New traffic light cannot be NoneType.")
        elif(type(traffic_light) != traffic_light.Traffic_Light):
            self._logger.write("Error! New traffic light must be of type Traffic_Light.")
        else:
            try:
                self._traffic_light_list.remove(traffic_light)
            except Exception as e:
                self._logger.write("Error! Could not remove traffic light from list:\n %s" % e)

    def calculate_average_wait_time(self):
        """
        Calculates the average wait time at every intersection

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
        sum = 0
        total_streets = len(self._street_list)
        if(total_streets == 0):
            self._logger.write("Error! Cannot calculate average wait time of an intersection with no streets.")
        else:
            for street in self._street_list:
                sum += street.calculate_street_wait_time()
            self._average_wait_time = (sum / total_streets)

    def calculate_traffic_volume(self):
        """
        Calculates the total traffic volume for the intersection

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
        sum = 0
        total_streets = len(self._street_list)
        if(total_streets == 0):
            self._logger.write(
                "Error! Cannot calculate traffic volume for an intersection with no streets.")
        else:
            for street in self._street_list:
                sum += street.calculate_street_volume()
            self._total_traffic_volume = sum

    def left(self, street_index):
        """
        Move a vehicle to take a left turn at an intersection

        Parameters
        ----------
            street_index
        Returns
        -------
            N/A
        """
        if street_index is None:
            self._logger.write('Error! street_index in left is None')
        elif type(street_index) != int:
            self._logger.write('Error! street_index in left is not of type int')
        else:
            try:
                left_lane_index = len(self._street_list[street_index]._end_lanes)
                if street_index == 0:
                    street_to_be_moved = len(self._street_list)-1
                else:
                    street_to_be_moved = street_index - 1
                self.move_vehicle(street_index, left_lane_index, street_to_be_moved, len(self._street_list[street_index]._end_lanes)-1)
            except Exception as e:
                self._logger.write('Error! failed to move_vehicle in left:\n %s' % e)

    def straight(self, street_index, lane_index):
        """
        Moves a vehicle straight through an intersection 

        Parameters
        ----------
            street_index
            lane_index

        Returns
        -------
            N/A
        """
        if street_index is None:
            self._logger.write('Error! street_index in straight is None')
        elif type(street_index) != int:
            self._logger.write('Error! street_index in straight is not of type int')
        elif type(lane_index) != int:
            self._logger.write('Error! lane_index in straight is not of type int')
        else:
            try:
                if street_index <= 1:
                    destination_street = street_index+2
                else:
                    destination_street = street_index-2
                straight_lane_recipient = len(self._street_list[destination_street].get_lane_list()) - (lane_index + 1)
                self.move_vehicle(street_index, lane_index, destination_street, straight_lane_recipient)
            except Exception as e:
                self._logger.write('Error! failed to move vehicle in straight:\n %s' % e)

    def right(self, street_index):
        """
        Moves a vehicle to take a right turn

        Parameters
        ----------
            street_index

        Returns
        -------
            N/A
        """
        if street_index is None:
            self._logger.write('Error! street_index in right is None')
        elif type(street_index) != int:
            self._logger.write('Error! street_index in right is not of type int')
        else:
            try:
                right_lane_index = len(self._street_list[street_index]._lane_list)-1
                if street_index == len(self._street_list)-1:
                    street_to_be_moved = 0
                else:
                    street_to_be_moved = street_index + 1
                self.move_vehicle(street_index, right_lane_index, street_to_be_moved, 0)
            except Exception as e:
                self._logger.write('Error! failed to move vehicle in right:\n %s' % e)

    def move_vehicle(self, origin_street, origin_lane, destination_street, destination_lane):
        """
        Move a vehicle from one lane to another 

        Parameters
        ----------
            origin_street
            origin_lane
            destination_street
            destination_lane

        Returns
        -------
            N/A
        """
        if origin_street is None:
            self._logger.write('Error! origin_street is None')
        elif origin_lane is None:
            self._logger.write('Error! origin_lane is None')
        elif destination_street is None:
            self._logger.write('Error! destination_street is None')
        elif destination_lane is None:
            self._logger.write('Error! destination_lane is None')
        elif type(origin_street) != int:
            self._logger.write('Error! origin_street needs to be of type int')
        elif type(origin_lane) != int:
            self._logger.write('Error! origin_lane needs to be of type int')
        elif type(destination_street) != int:
            self._logger.write('Error! destination_street needs to be of type int')
        elif type(destination_lane) != int:
            self._logger.write('Error! destination_lane needs to be of type int')
        try:
            v = self._street_list[origin_street]._lane_list[origin_lane].dequeue()
            if v is None:
                print('vehicle queue is empty')
            self._street_list[destination_street]._lane_list[destination_lane].enqueue(v)
        except Exception as e:
            self._logger.write('Error! failed to removed vehicle from origin_lane and move it to destination_lane:\n %s' % e)