import time

# Manage logs, game clock, error handling
class GameModel():
    def __init__(self, logging, debug, start_time)
        self.logger = Logger(logging, start_time)
        self.debug = debug
        self.start_time = start_time


class Logger():
    def __init__(self, logging, start_time):
        self.log_queue = []
        self.start_time = start_time


    def write_log(self, log_text):
        self.log_queue.append(log_text)


    def write_elapsed_time(self):
        self.log_queue.append(str(time.time() - self.start_time))


    def flush_logs(self):
        self.log_queue.clear()


    # Print stored logs to terminal and flush log queue
    def log_dump(self):
        for log in log_queue:
            print(log)
        flush_logs()

