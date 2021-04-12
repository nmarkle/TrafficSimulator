import logger, os

__author__ = "Vincent Fazio"
__created__ = "04-12-2021"
__editor__ = "Vincent Fazio"
__edited__ = "04-12-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Vincent Fazio"
__email__ = "vfazio@highpoint.edu"
__status__ = "In development"

class Reporter:
    def __init__(self):
        """

        HAVING TROUBLE CREATING THESE FUNCTIONS, DONT THEY HAVE TO CALL EACH OTHER?
            WHATS THE POINT IN SETTING AND GETTING THE FILE PATH?
                ISNT IT SO OPEN/CLOSE CAN USE THOSE GETTER/SETTERS TO OPEN AND CLOSE THE FILE PATH?
            HOW DO I DECLARE REPORT_FILE PATH? IS THAT RIGHT
            FAILED TO OPEN FILE - WHAT DOES THIS MEAN HOW DO I WRITE THIS ERROR
                SYNTAX ERRORS, WHATS THE PROPER SYNTAX IF ITS A STRING
                ALSO IF THE PATH IS CODED INTO SELF._report_file_path = "./report/report.log", DOES IT EVEN MATTER
            DONT I ALSO NEED TO PASS THE BOOLEAN FILE_OPENED AROUND IN GENERATE REPORT,open/close functions MEANING GENERATE REPORT NEEDS ACCESS TO OPEN/CLOSE
                AND OPEN/CLOSE NEEDS ACCESS TO SETTER/GETTERS

            WE NEED TO ADD MORE SHIT AND REDESIGN, I DONT UNDERSTAND WHY WE HAVE THESE SETTER/GETTERS BUT WE NEVER CALL THEM/USE THEM?

            MAY NEED TO ADD A FILE OBJECT? OPEN/CLOSE NEED TO ACCESS THE FILE OBJECT THAT IS CREATED TO F.OPEN() / F.CLOSE()

        The reporter class will be responsible for accessing the intersection class in order to pull the metrics stored there. 
        With these metrics, the reporter class will then open the output file specified at the report_file_path 
        and print relevant metric data from the simulation.
        
        Parameters
        ----------
            N/A
        
        Methods
        -------
            generate_report()       : Gathers Metrics and writes a report to report.log
            open_report_file()      : Opens report.log for writing 
            close_report_file()     : Closes the report.log file for writing
            set_file_path()         : Setter for report_file_path
            get_file_path()         : Getter for report_file_path
        """

        self._report_file_path = "./report/report.log"
        self._report_file_size = None
        self._viewing_report_state = None
        self._file_opened = None
    
    def generate_report(self):
    
    def open_report_file(self): """ Dont we need to pass in report_file_path"""
       """
       Open_report_file will open the report.log file for writing and set the file_opened variable to True. 
       If the opening of the report.log file was a success, return True. Otherwise, return false.

        Parameters
        ----------
            N/A
        Returns
        -------
            file_opened (boolean) : Class variable to store the state of 'File_opened'
        """
        
        fName = "./report/report.log"

        if os.path.exists(fName):
            f = open(fName, 'w')
            try:
                return self._file_opened
            except Exception as e:
                logger.write("Error! Failed to open report file:\n %s" % e)

    
    def close_report_file(self):
        """
       close_report_file will close the previously report.log file and set the file_opened variable to False. 
       If closing the report.log file was a success, return True. Otherwise, return false.

        Parameters
        ----------
            N/A ??
        Returns
        -------
            N/A ??
        """
        fName = "./report/report.log"
        
        if os.path.exists(fName):
            try:
                self._file_opened = False
                f.close() #need to pass in file object to close it here
                return True
            except Exception as e:
                logger.write("Error! Failed to close report file:\n %s" % e)
        else:
            logger.write("Report file was not open close")
            return False

    def set_file_path(self, new_file_path):
        """
        Assigns new_file_path class variable the value of file_path variable. 

        Parameters
        ----------
            new_file_path (string) : The new value for the 'file_path' variable

        Returns
        -------
            N/A
        """
        if(new_file_path == None):
            logger.write("Error! new_file_path cannot be a NoneType")
        elif(type(new_file_path) != string):
            logger.write("Error! A string value representing the file path should be provided")
        else:
            try:
                self._report_file_path = new_file_path
            except Exception as e:
                logger.write("Error! Failed to set the report_file_path:\n %s" % e)

    def get_file_path(self):
        """
        Returns the value of the report_file_path of the Reporter Class.

        Parameters
        ----------
            N/A

        Returns
        -------
            report_file_path (boolean) : Class variable to store the state of 'report_file_path'
        """
        if(type(self._report_file_path) != str):
            logger.write("Error! File path name is not assigned")
        elif(self._report_file_path == None):
            logger.write("Error! name contains no value")
        else:
            try:
                return self._report_file_path
            except Exception as e:
                logger.write("Error! Failed to fetch the value of report_file_path: \n %s" % e)