import logger

__author__ = "Nathan Markle"
__created__ = "04-06-2021"
__editor__ = "Nathan Markle, Blake Vogel"
__edited__ = "04-16-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Nathan Markle, Blake Vogel"
__email__ = "nmarkle@highpoint.edu, bvogel@highpoint.edu"
__status__ = "In development"

class Traffic_Light:
    def __init__(self):
        """
        The traffic light class will represent the discrete traffic lights
        present at each intersection within the simulation software. The
        Traffic_Light object will possess getters and setter for all of it's
        inherent class variables.

        Parameters
        ----------
            N/A

        Methods
        -------
            get_blinking_arrow_status()  : Getter for blinking_arrow_status
            set_blinking_arrow_status()  : Setter for blinking_arrow_status
            get_blinking_status()        : Getter for blinking_status
            set_blinking_status()        : Setter for blinking_status
            get_left_arrow_status()      : Getter for left_arrow_status
            set_left_arrow_status()      : Setter for left_arrow_status
            get_right_arrow_status()     : Getter for right_arrow_status
            set_right_arrow_status()     : Setter for right_arrow_status
            get_green_status()           : Getter for green_arrow_status
            set_green_status()           : Setter for green_arrow_status
            get_yellow_status()          : Getter for yellow_arrow_status
            set_yellow_status()          : Setter for yellow_arrow_status
            get_red_status()             : Getter for red_status
            set_red_status()             : Setter for red_status
            get_x_pos()                  : Getter for x_pos
            set_x_pos()                  : Setter for x_pos
            get_y_pos()                  : Getter for y_pos
            set_y_pos()                  : Setter for y_pos
            get_interval()               : Getter for interval
            set_interval()               : Setter for interval
            check_interval()             : Checks to see the status of interval
            change_light()               : Changes light 
        """
        self._blinking_arrow_status = None
        self._blinking_status = None
        self._left_arrow_status = None
        self._right_arrow_status = None
        self._green_status = None
        self._yellow_status = None
        self._red_status = None
        self._x_pos = None
        self._y_pos = None
        self._interval = None

    def get_blinking_arrow_status(self):
        """
        Getter for blinking_arrow_status.

        Parameters
        ----------
            N/A

        Returns
        -------
            blinking_arrow_status (bool) : Class variable to store the state of the blinking arrow
        """
        if(self._blinking_arrow_status == None):
            logger.write("Error! The blinking_arrow_status contains no value.")
        elif(type(self._blinking_arrow_status) != bool):
            logger.write("Error! The blinking_arrow_status must be of type bool.")
        else:
            try:
                return self._blinking_arrow_status
            except Exception as e:
                logger.write("Error! Could not fetch the blinking_arrow_status:\n %s" % e)

    def set_blinking_arrow_status(self, new_blinking_arrow_status):
        """
        Setter for blinking_arrow_status.

        Parameters
        ----------
            new_blinking_arrow_status (bool) : The new status for the blinking_arrow_status variable

        Returns
        -------
            N/A
        """
        if(new_blinking_arrow_status == None):
            logger.write("Error! New blinking_arrow_status cannot be a NoneType")
        elif(type(new_blinking_arrow_status) != bool):
            logger.write("Error! New blinking_arrow_status must be of type bool.")
        else:
            try:
                self._blinking_arrow_status = new_blinking_arrow_status
            except Exception as e:
                logger.write("Error! Could not set the new blinking_arrow_status:\n %s" % e)
        
    def get_blinking_status(self):
        """
        Getter for blinking_status.

        Parameters
        ----------
            N/A

        Returns
        -------
            blinking_status (bool) : Class variable to store the state of the blinking status
        """
        if(self._blinking_status == None):
            logger.write("Error! The blinking_status contains no value.")
        elif(type(self._blinking_status) != bool):
            logger.write("Error! The blinking_status must be of type bool.")
        else:
            try:
                return self._blinking_status
            except Exception as e:
                logger.write("Error! Could not fetch the blinking_status: \n %s" % e)

    def set_blinking_status(self, new_blinking_status):
        """
        Setter for blinking_status.
        
        Parameters
        ----------
            new_blinking_status (bool) : New state of the blinking status

        Returns
        -------
            N/A
        """
        if(new_blinking_status == None):
            logger.write("Error! New blinking_status cannot be a NoneType.")
        elif(type(new_blinking_status) != bool):
            logger.write("Error! New blinking status must be of type bool.")
        else:
            try:
                self._blinking_status = new_blinking_status
            except Exception as e:
                logger.write("Error! Could not set the new blinking_status:\n %s" % e)

    def get_left_arrow_status(self):
        """
        Getter for left_arrow_status.

        Parameters
        ----------
            N/A

        Returns
        -------
            left_arrow_status (bool) : Class variable to store the state of the left_arrow_status
        """
        if(self._left_arrow_status == None):
            logger.write("Error! The left_arrow_status contains no value.")
        elif(type(self._left_arrow_status) != bool):
            logger.write("Error! The left_arrow_status must be of type bool.")
        else:
            try:
                return self._left_arrow_status
            except Exception as e:
                logger.write("Error! Could not fetch the left_arrow_status:\n %s" % e)

    def set_left_arrow_status(self, new_left_arrow_status):
        """
        Setter for left_arrow_status.

        Parameters
        ----------
            new_left_arrow_status (bool) : New state of the left_arrow_status

        Returns
        -------left
            N/A
        """
        if(new_left_arrow_status == None):
            logger.write("Error! New left_arrow_status cannot be NoneType.")
        elif(type(new_left_arrow_status) != bool):
            logger.write("Error! new left_arrow_status must be of type bool")
        else:
            try:
                self._left_arrow_status = new_left_arrow_status
            except Exception as e:
                logger.write("Error! Could not set the new left_arrow_status:\n %s" % e)

    def get_right_arrow_status(self):
        """
        Getter for right_arrow_status.

        Parameters
        ----------
            N/A

        Returns
        -------
            right_arrow_status (bool) : Class variable to store the state of the right_arrow_status
        """
        if(self._right_arrow_status == None):
            logger.write("Error! The right_arrow_status contains no value.")
        elif(type(self._right_arrow_status) != bool):
            logger.write("Error! The right_arrow_status must be of type bool.")
        else:
            try:
                return self._right_arrow_status
            except Exception as e:
                logger.write("Error! Could not fetch the right_arrow_status:\n %s" % e)

    def set_right_arrow_status(self, new_right_arrow_status):
        """
        Setter for right_arrow_status.

        Parameters
        ----------
            new_right_arrow_status (bool) : New state of the right_arrow_status

        Returns
        -------
            N/A
        """
        if(new_right_arrow_status == None):
            logger.write("Error! New right_arrow_status cannot be NoneType.")
        elif(type(new_right_arrow_status) != bool):
            logger.write("Error! New right_arrow_status must be of type bool")
        else:
            try:
                self._right_arrow_status = new_right_arrow_status
            except Exception as e:
                logger.write("Error! Could not set the new right_arrow_status:\n %s" % e)

    def get_green_status(self):
        """
        Getter for the green_status.

        Parameters
        ----------
            N/A

        Returns
        -------
            green_status (bool) : Class variable to store the state of the green_status
        """
        if(self._green_status == None):
            logger.write("Error! The green_status contains no value.")
        elif(type(self._green_status) != bool):
            logger.write("Error! The green_status must be of type bool.")
        else:
            try:
                return self._green_status
            except Exception as e:
                logger.write("Error! Could not fetch the green_status:\n %s" % e)

    def set_green_status(self, new_green_status):
        """
        Setter for the green_status

        Parameters
        ----------
            new_green_status (bool) : New state of the green_status

        Returns
        -------
            N/A
        """
        if(new_green_status == None):
            logger.write("Error! New green_status cannot be NoneType.")
        elif(type(new_green_status) != bool):
            logger.write("Error! New green_status must be of type bool.")
        else:
            try:
                return self._green_status
            except Exception as e:
                logger.write("Error! Could not set the new green_status:\n %s" % e)

    def get_yellow_status(self):
        """
        Getter for the yellow_status.

        Parameters
        ----------
            N/A

        Returns
        -------
            yellow_status (bool) : Class variable to store the state of the yellow_status
        """
        if(self._yellow_status == None):
            logger.write("Error! The yellow_status contains no value.")
        elif(type(self._yellow_status) != bool):
            logger.write("Error! The yellow_status must be of type bool.")
        else:
            try:
                return self._yellow_status
            except Exception as e:
                logger.write("Error! Could not fetch the yellow_status:\n %s" % e)

    def set_yellow_status(self, new_yellow_status):
        """
        Setter for the yellow_status

        Parameters
        ----------
            new_yellow_status (bool) : New state of the yellow_status

        Returns
        -------
            N/A
        """
        if(new_yellow_status == None):
            logger.write("Error! New yellow_status cannot be NoneType.")
        elif(type(new_yellow_status) != bool):
            logger.write("Error! New yellow_status must be of type bool.")
        else:
            try:
                return self._yellow_status
            except Exception as e:
                logger.write("Error! Could not set the new yellow_status:\n %s" % e)

    def get_red_status(self):
        """
        Getter for the red_status

        Parameters
        ----------
            N/A

        Returns
        -------
            red_status (bool) : Class variable to store the state of the red_status
        """
        if(self._red_status == None):
            logger.write("Error! The red_status contains no value.")
        elif(type(self._red_status) != bool):
            logger.write("Error! The yellow_status must be of type bool")
        else:
            try:
                return self._red_status
            except Exception as e:
                logger.write("Error! Could not fetch the red_status:\n %s" % e)

    def set_red_status(self, new_red_status):
        """
        Setter for the red_status

        Parameters
        ----------
            new_red_status (bool) : New state of the red_status

        Returns
        -------
            N/A
        """
        if(new_red_status == None):
            logger.write("Error! New red_status cannot be NoneType.")
        elif(type(new_red_status) != bool):
            logger.write("Error! New red_status must be of type bool.")
        else:
            try:
                self._red_status = new_red_status
            except Exception as e:
                logger.write("Error! Could not set the red_status:\n %s" % e)

    def get_x_pos(self):
        """
        Getter for the x_pos

        Parameters
        ----------
            N/A

        Returns
        -------
            x_pos (int) : The x position of the Traffic Light
        """
        if(self._x_pos == None):
            logger.write("Error! The x_pos contains no value.")
        elif(type(self._x_pos) != int):
            logger.write("Error! The x_pos must be of type int.")
        else:
            try:
                return self._x_pos
            except Exception as e:
                logger.write("Error! Could not fetch the x_pos:\n %s" % e)

    def set_x_pos(self, new_x_pos):
        """
        Setter for the x_pos

        Parameters
        ----------
            new_x_pos (int) : The new value of the x_pos

        Returns
        -------
            N/A
        """
        if(new_x_pos == None):
            logger.write("Error! New x_pos cannot be NoneType.")
        elif(type(new_x_pos) != int):
            logger.write("Error! New x_pos must be of type int.")
        else:
            try:
                self._x_pos = new_x_pos
            except Exception as e:
                logger.write("Error! Could not set the x_pos:\n %s" % e)

    def get_y_pos(self):
        """
        Getter for the y_pos

        Parameters
        ----------
            N/A

        Returns
        -------
            y_pos (int) : The y position of the Traffic Light
        """
        if(self._y_pos == None):
            logger.write("Error! The y_pos contains no value.")
        elif(type(self._y_pos) != int):
            logger.write("Error! The y_pos must be of type int.")
        else:
            try:
                return self._y_pos
            except Exception as e:
                logger.write("Error! Could not fetch the y_pos:\n %s" % e)

    def set_y_pos(self, new_y_pos):
        """
        Setter for the y_pos

        Parameters
        ----------
            new_y_pos (int) : The new value of the y_pos

        Returns
        -------
            N/A
        """
        if(new_y_pos == None):
            logger.write("Error! New y_pos cannot be NoneType.")
        elif(type(new_y_pos) != int):
            logger.write("Error! New y_pos must be of type int.")
        else:
            try:
                self._y_pos = new_y_pos
            except Exception as e:
                logger.write("Error! Could not set the y_pos:\n %s" % e)
    
    def get_interval(self):
        """
        Getter for the interval

        Parameters
        ----------
            N/A

        Returns
        -------
            interval (int) : The interval of a Traffic Light
        """
        if(self._interval == None):
            logger.write("Error! The interval contains no value.")
        elif(type(self._interval) != int):
            logger.write("Error! The y_pos must be of type int.")
        else:
            try:
                return self._get_interval
            except Exception as e:
                logger.write("Error! Could not fetch the interval:\n %s" % e)

    def set_interval(self, new_interval):
        """
        Setter for the interval

        Parameters
        ----------
            new_interval (int) : The new value of the interval

        Returns
        -------
            N/A
        """
        if(new_interval == None):
            logger.write("Error! New interval cannot be NoneType.")
        elif(type(new_y_pos) != int):
            logger.write("Error! New interval must be of type int.")
        else:
            try:
                self._interval = new_interval
            except Exception as e:
                logger.write("Error! Could not set the interval:\n %s" % e)

    def check_interval():
        """
        Checks the status of intervals

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
        if self.get_interval() > 0:
            try:
                self.set_interval(self.get_interval()-1)
            except Exception as e:
                logger.write("Error! failed ot set interval")
        else:
            try:
                change_light()
            except Exception as e:
                logger.write("Error! failed to change light:\n %s" % e)
    
    def change_light():
        """
        Changes the light status

        Parameters
        ----------
            N/A

        Returns
        -------
            N/A
        """
        if self._green_status:
            self.set_green_status(False)
            self.set_yellow_status(True)
            self.set_interval(3)
            return
        elif self._yellow_status:
            self.set_yellow_status(False)
            self.set_red_status(True)
            self.set_interval(30)
            return
        elif self._red_status:
            self.set_red_status(False)
            self.set_green_status(True)
            self.set_interval(30)
            return