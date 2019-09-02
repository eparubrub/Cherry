import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

time_now = datetime.now().strftime("%H:%M:%S.%f")


class Timer:
    def __init__(self, launch_time):
        self.time_now = datetime.now().strftime("%H:%M:%S.%f")
        self.time_launch = launch_time
        self.timer_start = None
        self.timer_end = None

    def wait_until_start_time(self):
        while self.time_now < self.time_launch:
            time.sleep(.01)
            self.time_now = datetime.now().strftime("%H:%M:%S.%f")
        print('RELEASE')
        print("Current time: " + self.time_now)

    def start(self):
        self.timer_start = time.time()

    def end(self):
        self.timer_end = time.time()

    def print_time(self):
        if self.start and self.end is not None:
            print('Bot ran in ' + str(round(self.timer_end-self.timer_start, 3)) + ' seconds')
        else:
            print("Time was not recorded correctly, please make sure "
                  "the timer recorded start time and end time")
