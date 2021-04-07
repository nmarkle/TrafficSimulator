import logger

__author__ = "Nathan Markle"
__created__ = "04-06-2021"
__editor__ = "Nathan Markle"
__edited__ = "04-07-2021"
__rationale___ = "Updated constructor"
__version__ = "0.0.1"
__maintainer__ = "Nathan Markle"
__email__ = "nmarkle@highpoint.edu"
__status__ = "In development"

class Traffic_Light:
    def __init__(self):
        """
        The traffic light class will represent the discrete traffic lights 
        present at each intersection within the simulation software. The 
        Traffic_Light object will possess getters and setters for all of it’s 
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