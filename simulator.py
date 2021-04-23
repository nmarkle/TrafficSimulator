import configparser as c
from logger import Logger
from street import Street
from lane import Lane
from vehicle import Vehicle
from intersection import Intersection
from vpython import *

__author__ = "Vincent Fazio"
__created__ = "04-11-2021"
__editor__ = "Vincent Fazio"
__edited__ = "04-12-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Vincent Fazio"
__email__ = "vfazio@highpoint.edu"
__status__ = "In development"


class Simulator:
    def __init__(self):
        """
        The Simulator class will be responsible for keeping track of
        and controlling the state of the simulation.

        Parameters
        ----------
            N/A

        Methods
        -------
        set_running_state()             : Setter for running_state
        get_running_state()             : Getter for running_state
        set_paused_state()              : Setting for paused_state
        get_paused_state()              : Getter for paused_state
        set_stopped_state()             : Setting for stopped state
        get_stopped_state()             : Getter for stopped state
        add_intersection()              : Appends new_intersection to intersection_list
        delete_intersection()           : Deletes intersection from intersection_list (Is this suppose to be new_intersection object? -If so update the arch. design)
        get_intersection_list()         : Getter for intersection_list
        set_day_of_week()               : Setting for day_of_week
        get_day_of_week()               : Getter for day_of_week
        set_time_of_day()               : Setting for time_of_day
        get_time_of_day()               : Getter for time_of_day
        set_duration_of_simulation()    : Setting for duration_of_simulation
        get_duration_of_simulation()    : Getter for duration_of_simulation

        """
        # All class variables
        self._running_state = None
        self._paused_state = None
        self._stopped_state = None
        self._intersection_list = []
        self._day_of_week = None
        self._time_of_day = None
        self._duration_of_simulation = None
        self._logger = Logger()
        self._parser = c.ConfigParser()
        self._parser.read("config.ini")
        self._number_of_intersections = int(
            self._parser["simulation"]["number_of_intersections"])
        self._intersections = []

        # Build from the configuration file
        for i in range(0, self._number_of_intersections):
            # Create intersection key to access configuration file
            intersection_key = "intersection_" + str(i + 1)
            temp_intersection = Intersection()

            # Pull number of streets from the configuration file
            number_of_streets = int(
                self._parser[intersection_key]["number_of_streets"])

            # Iterate through number of streets in configuration file
            for j in range(0, number_of_streets):
                # Create street key
                street_key = "street_" + str(j + 1)

                # Generate temp street
                temp_street = Street()

                # Set the name of the temp street
                temp_street.set_name(self._parser[street_key]["name"])

                # Iterate through the number of endlanes
                for p in range(0, int(self._parser[street_key]["endlanes"])):
                    temp_lane = Lane()
                    temp_lane.set_max_vehicle_capacity(
                        int(self._parser[street_key]["queue_length"]))
                    # Add the temp lane to the temp street
                    temp_street.add_end_lane(temp_lane)

                # Iterates through the number of beginlanes
                for q in range(0, int(self._parser[street_key]["beginlanes"])):
                    temp_lane = Lane()
                    temp_lane.set_max_vehicle_capacity(
                        int(self._parser[street_key]["queue_length"]))
                    # Add the temp lane to the temp street
                    temp_street.add_begin_lane(temp_lane)
                    temp_vehicle = Vehicle()
                    temp_lane.enqueue(temp_vehicle)

                temp_street.set_lane_list()
                # Append temporary street to intersection
                temp_intersection.add_street(temp_street)
            # Add newly created intersection to intersection_list
            self.add_intersection(temp_intersection)

    def set_running_state(self, new_running_state):
        """
        Assigns new_running_state class variable the value of running_state variable.

        Parameters
        ----------
            new_running_state (boolean) : The new value for the 'running_state' variable

        Returns
        -------
            N/A
        """
        if(new_running_state == None):
            self._logger.write("Error! new_running_state cannot be a NoneType")
        elif(type(new_running_state) != bool):
            self._logger.write(
                "Error! new_running_state must be of type boolean")
        else:
            try:
                self._running_state = new_running_state
            except Exception as e:
                self._logger.write(
                    "Error! Could not set the new_running_state:\n %s" % e)

    def get_running_state(self):
        """
        Returns the value of the running_state of the Simulator Class.

        Parameters
        ----------
            N/A

        Returns
        -------
            running_state (boolean) : Class variable to store the state of 'running_state'
        """
        if(type(self._running_state) != bool):
            self._logger.write("Error! name must be of type boolean")
        elif(self._running_state == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._running_state
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of running_state: \n %s" % e)

    def set_paused_state(self, new_paused_state):
        """
        Assigns new_paused_state class variable the value of paused_state variable.

        Parameters
        ----------
            new_paused_state (boolean) : The new value for 'paused_state' variable

        Returns
        -------
            N/A
        """

        if(new_paused_state == None):
            self._logger.write("Error! new_paused_state cannot be a NoneType")
        elif(type(new_paused_state) != bool):
            self._logger.write(
                "Error! new_paused_state must be of type boolean")
        else:
            try:
                self._paused_state = new_paused_state
            except Exception as e:
                self._logger.write(
                    "Error! Could not set the new_paused_state:\n %s" % e)

    def get_paused_state(self):
        """
        Returns the value of the paused_state of the Simulator Class.

        Parameters
        ----------
            N/A

        Returns
        -------
            paused_state (boolean) : Class variable to store the state of 'paused_state'
        """
        if(type(self._paused_state) != bool):
            self._logger.write("Error! name must be of type boolean")
        elif(self._paused_state == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._paused_state
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of paused_state: \n %s" % e)

    def set_stopped_state(self, new_stopped_state):
        """
        Assigns new_stopped_state value to the stopped_state value in the Simulator Class.

        Parameters
        ----------
            new_stopped_state (boolean) : The new value for 'stopped_state' variable

        Returns
        -------
            N/A
        """
        if(new_stopped_state == None):
            self._logger.write("Error! new_stopped_state cannot be a NoneType")
        elif(type(new_stopped_state) != bool):
            self._logger.write(
                "Error! new_stopped_state must be of type boolean")
        else:
            try:
                self._stopped_state = new_stopped_state
            except Exception as e:
                self._logger.write(
                    "Error! Could not set the new_stopped_state:\n %s" % e)

    def get_stopped_state(self):
        """
        Returns the value of the stopped_state of the Simulator Class.

        Parameters
        ----------
            N/A

        Returns
        -------
            stopped_state (boolean) : Class variable to store the state of 'stopped_state'
        """
        if(type(self._stopped_state) != bool):
            self._logger.write("Error! name must be of type boolean")
        elif(self._stopped_state == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._stopped_state
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of stopped_state: \n %s" % e)

    def add_intersection(self, new_intersection):
        """
        Appends new_intersection to the intersection_list class variable.

        Parameters
        ----------
            new_intersection (string) : Intersection Object

        Returns
        -------
            N/A
        """
        if(new_intersection == None):
            self._logger.write("Error! new_intersection contains no value")
        else:
            try:
                self._intersection_list.append(new_intersection)
            except Exception as e:
                self._logger.write(
                    "Error! Could add new_intersection to intersection: \n %s" % e)

    def delete_intersection(self, intersection):
        """
        If intersection is present in the intersection_list class variable, remove it.
        Otherwise, provide an error message.

        Parameters
        ----------
            intersection (string): Intersection Object

        Returns
        -------
            N/A
        """
        if(type(intersection) != str):
            self._logger.write("Error! intersection must be of type string")
        elif(intersection == None):
            self._logger.write("Error! intersection contains no value")
        elif(len(self._intersection_list) == 0):
            self._logger.write("Error! intersection_list is empty")
        else:
            try:
                self._intersection_list.remove(intersection)
            except Exception as e:
                self._logger.write(
                    "Error! could not remove lane from intersection_list:\n %s" % e)

    def get_intersection_list(self):
        """
        Returns the value of the intersection_list class variable.

        Parameters
        ----------
            N/A

        Returns
        -------
            intersection_list (string) : List of intersections
        """
        if(type(self._intersection_list) != list):
            self._logger.write(
                "Error! intersection_list must be of type string")
        elif(self._intersection_list == None):
            self._logger.write("Error! intersection_list contains no value")
        elif(len(self._intersection_list) == 0):
            self._logger.write("Error! intersection_list is empty")
        else:
            try:
                return self._intersection_list
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of intersection_list: \n %s" % e)

    def set_day_of_week(self, new_day_of_week):
        """
        Assigns new_day_of_week value to the day_of_week value in the Simulator Class

        Parameters
        ----------
            new_day_of_week (string) : The new value for 'day_of_week' variable

        Returns
        -------
          N/A
        """
        if(new_day_of_week == None):
            self._logger.write("Error! new_day_of_week cannot be a NoneType")
        elif(type(new_day_of_week) != str):
            self._logger.write("Error! new_day_of_week must be of type string")
        else:
            try:
                self._day_of_week = new_day_of_week
            except Exception as e:
                self._logger.write(
                    "Error! Could not set the new_day_of_week:\n %s" % e)

    def get_day_of_week(self):
        """
        Returns the day_of_week variable in the Simulator Class.

        Parameters
        ----------
            N/A

        Returns
        -------
            day_of_week (string) : Class variable to store the state of 'day_of_week'
        """
        if(type(self._day_of_week) != str):
            self._logger.write("Error! name must be of type string")
        elif(self._day_of_week == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._day_of_week
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of day_of_week: \n %s" % e)

    def set_time_of_day(self, new_time_of_day):
        """
        Assigns new_time_of_day value to the time_of_day value in the Simulator Class.

        Parameters
        ----------
            new_time_of_day (string) : The new value for 'time_of_day' variable

        Returns
        -------
            N/A
        """
        if(new_time_of_day == None):
            self._logger.write("Error! new_time_of_day cannot be a NoneType")
        elif(type(new_time_of_day) != str):
            self._logger.write("Error! new_time_of_day must be of type string")
        else:
            try:
                self._time_of_day = new_time_of_day
            except Exception as e:
                self._logger.write(
                    "Error! Could not set the new_time_of_day:\n %s" % e)

    def get_time_of_day(self):
        """
        Returns the value of the time_of_day class variable of the Simulator Class.

        Parameters
        ----------
            N/A

        Returns
        -------
            time_of_day (string) : Class variable to store the state of 'time_of_day'
        """
        if(type(self._time_of_day) != str):
            self._logger.write("Error! name must be of type string")
        elif(self._time_of_day == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._time_of_day
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of time_of_day: \n %s" % e)

    def set_duration_of_simulation(self, new_duration_of_simulation):
        """
        Assigns new_duration_of_simulation value to the duration_of_simulation value in the Simulator Class.

        Parameters
        ----------
            new_duration_of_simulation (float) : The new value for 'duration_of_simulation' variable
        Returns
        -------
            N/A
        """
        if(new_duration_of_simulation == None):
            self._logger.write(
                "Error! new_duration_of_simulation cannot be a NoneType")
        elif(type(new_duration_of_simulation) != float):
            self._logger.write(
                "Error! new_duration_of_simulation must be of type string")
        else:
            try:
                self._duration_of_simulation = new_duration_of_simulation
            except Exception as e:
                self._logger.write(
                    "Error! Could not set the new_duration_of_simulation:\n %s" % e)

    def get_duration_of_simulation(self):
        """
        Returns the value of the duration_of_simulation class variable

        Parameters
        ----------
            N/A

        Returns
        -------
            duration_of_simulation (float) : Class varialbe to store the state of 'time_of_day'
        """
        if(type(self._duration_of_simulation) != float):
            self._logger.write("Error! name must be of type string")
        elif(self._duration_of_simulation == None):
            self._logger.write("Error! name contains no value")
        else:
            try:
                return self._duration_of_simulation
            except Exception as e:
                self._logger.write(
                    "Error! Could not fetch the value of duration_of_simulation: \n %s" % e)


if __name__ == "__main__":
    simulator = Simulator()
    simulator.set_running_state(True)
    while(simulator.get_running_state()):
        print(simulator.get_intersection_list())
        print(simulator._intersection_list[0].get_street_list())
        for i in range(0, len(simulator._intersection_list[0].get_street_list())):
            print(
                simulator._intersection_list[0]._street_list[i].get_end_lanes())
            print(
                simulator._intersection_list[0]._street_list[i].get_begin_lanes())
        # print(simulator._intersection_list[0]._street_list[0]._end_lanes[0].get_vehicle_list())
        # visually create intersection, street, and lane
        # create vehicles

        # For number of streets

        # for j in range(0, len(simulator._intersection_list[0].get_street_list())):
        # simulator._intersection_list[0].straight(j, 3)
        print("STRAIGHT TEST")
        print("Beginning State:\n--------------------------------")
        print(simulator._intersection_list[0]._street_list[0]._lane_list[3].get_vehicle_list())
        print(simulator._intersection_list[0]._street_list[2]._lane_list[1].get_vehicle_list())
        simulator._intersection_list[0].straight(0, 3)
        print("Beginning End State:\n--------------------------------")
        print(simulator._intersection_list[0]._street_list[0]._lane_list[3].get_vehicle_list())
        print(simulator._intersection_list[0]._street_list[2]._lane_list[1].get_vehicle_list())
        print()
        print()
        print("LEFT TEST")
        print("Beginning State:\n--------------------------------")
        print(simulator._intersection_list[0]._street_list[0]._lane_list[2].get_vehicle_list())
        print(simulator._intersection_list[0]._street_list[3]._lane_list[1].get_vehicle_list())
        simulator._intersection_list[0].left(0)
        print()
        print("Beginning End State:\n--------------------------------")
        print(simulator._intersection_list[0]._street_list[0]._lane_list[2].get_vehicle_list())
        print(simulator._intersection_list[0]._street_list[3]._lane_list[1].get_vehicle_list())

        break
