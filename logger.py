#!/usr/bin/env python3

__author__ = "Nathan Markle"
__created__ = "04-09-2021"
__editor__ = "Nathan Markle"
__edited__ = "04-09-2021"
__rationale___ = "Initial Creation"
__version__ = "0.0.1"
__maintainer__ = "Nathan Markle"
__email__ = "nmarkle@highpoint.edu"
__status__ = "In development"

from datetime import datetime
import os

class Logger:
    def __init__(self):
        """
        The ultimate logger for all error messages within the Traffic Simulator.

        Methods
        -------
            initialize() : Creates the logging directory and file to store data
            write()      : Writes the given message to the log file
        """
        #self._log_file_directory = "./log/"
        self._log_file_name = "logfile.log"
        #self._log_file_path = self._log_file_directory + self._log_file_name
        self._log_file_path =  self._log_file_name

    def initialize(self):
        """
        Creates the logging directory and file to store data.

        Parameters
        ----------
            N/A
        
        Returns
        -------
            N/A
        """
        os.mkdir(self._log_file_directory)
        temp = open(self._log_file_path, "x")
        temp.close()

    def write(self, message):
        """
        Writes the given message to the log file

        Parameters
        ----------
            message (str) : The message to be written to the log file

        Returns
        -------
            N/A
        """
        logfile = open(self._log_file_path, "a")
        logfile.write("%s: %s\n" % (datetime.utcnow(), message))
        logfile.close()