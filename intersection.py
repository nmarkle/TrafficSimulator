import logger, traffic_light, street

class Intersection():
    def __init__(self):
        """
        The intersection class will represent the discrete intersections present where
        two streets converge. The intersection class will possess getters and setters
        for all of it's inherent class variables and methods to calculate relevant 
        metrics.

        Parameters
        ----------
            N/A

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
        """
        self._street_list = []
        self._traffic_light_list = []
        self._average_wait_time = None
        self._total_traffic_volume = None

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
            logger.write("Error! New Street cannot be a NoneType.")
        elif(type(new_street) != street.Street):
            logger.write("Error! New Street must be of type Street.")
        else:
            try:
                self._street_list.append(new_street)
            except Exception as e:
                logger.write("Error! Could not add the new Street object to list:\n %s" % e)
    
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
            logger.write("Error! Street list is empty.")
        else:
            try:
                return self._street_list
            except Exception as e:
                logger.write("Error! Unable to return the street list:\n %s" % e)

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
            logger.write("Error! Street to remove cannot be NoneType.")
        elif(type(street) != street.Street):
            logger.write("Error! Cannot remove non-Street type from list.")
        else:
            try:
                self._street_list.remove(street)
            except Exception as e:
                logger.write("Error! Could not remove street from list:\n %s" % e)

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
            logger.write("Error! Traffic light list is empty.")
        else:
            try:
                return self._traffic_light_list
            except Exception as e:
                logger.write("Error! Unable to return the traffic light list:\n %s" % e)

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
            logger.write("Error! New traffic light cannot be NoneType.")
        elif(type(new_traffic_light) != traffic_light.Traffic_Light):
            logger.write("Error! New traffic light must be of type Traffic_Light.")
        else:
            try:
                self._traffic_light_list.append(new_traffic_light)
            except Exception as e:
                logger.write("Error! Unable to add traffic light to traffic light list:\n %s" % e)

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
            logger.write("Error! New traffic light cannot be NoneType.")
        elif(type(traffic_light) != traffic_light.Traffic_Light):
            logger.write("Error! New traffic light must be of type Traffic_Light.")
        else:
            try:
                self._traffic_light_list.remove(traffic_light)
            except Exception as e:
                logger.write("Error! Could not remove traffic light from list:\n %s" % e)

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
            logger.write("Error! Cannot calculate average wait time of an intersection with no streets.")
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
            logger.write("Error! Cannot calculate traffic volume for an intersection with no streets.")
        else:
            for street in self._street_list:
                sum += street.calculate_street_volume()
            self._total_traffic_volume = sum