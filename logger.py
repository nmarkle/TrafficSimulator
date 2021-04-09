#!/usr/bin/env python3

from datetime import datetime


class Logger:
    def __init__(self):
        self._log_file_path = "./log/"

    def write(self, message):
        logfile = open(self._log_file_path + "logfile.log", "a")
        logfile.write("%s: %s\n" % (datetime.utcnow(), message))