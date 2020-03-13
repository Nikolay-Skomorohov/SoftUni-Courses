class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        secs = self.seconds
        if len(str(self.seconds)) == 1:
            secs = "0" + str(self.seconds)
        mins = self.minutes
        if len(str(self.minutes)) == 1:
            mins = "0" + str(self.minutes)
        hours = self.hours
        if len(str(self.hours)) == 1:
            hours = "0" + str(self.hours)
        return f"{hours}:{mins}:{secs}"

    def next_second(self):
        self.seconds += 1
        if self.seconds >= self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours >= self.max_hours:
                    self.hours = 0
        return self.get_time()


time = Time(24, 0, 0)
print(time.next_second())

