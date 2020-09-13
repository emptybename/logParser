class Log:
    def __init__(self, timestamp, url, method, response_time, response_code):
        self.timestamp = timestamp
        self.url = url
        self.method = method
        self.response_time = response_time
        self.response_code = response_code
