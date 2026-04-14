from parser import parse
from collections import defaultdict
from datetime import datetime


class LogAnalyzer:
    analyzer_count = 0
    def __init__(self, logs):
        self.logs = logs
        LogAnalyzer.analyzer_count += 1

    def count_by_level(self):
        err, war, inf = 0, 0, 0
        for log in self.logs:
            match log["level"]:
                case "INFO": inf += 1
                case "ERROR": err += 1
                case "WARNING": war += 1
        return {"i": inf, "e": err, "w": war}

    def most_common_error(self):
        common_errors = defaultdict(int)
        for log in self.logs:
            if log["level"] == "ERROR":
                common_errors[log["message"]] += 1
        return max(common_errors, key=common_errors.get)

    def errors_per_hour(self):
        errors = self.count_by_level()["e"]
        # starting time in ms
        date, time = self.logs[0]["timestamp"].split(" ")
        year, month, day = map(int, date.split("-"))
        hour, minute, second = map(int, time.split(":"))
        start_seconds = datetime(year, month, day, hour, minute, second).timestamp()
        # final time in ms
        date_e, time_e = self.logs[-1]["timestamp"].split(" ")
        year_e, month_e, day_e = map(int, date_e.split("-"))
        hour_e, minute_e, second_e = map(int, time_e.split(":"))
        start_seconds_1 = datetime(year_e, month_e, day_e, hour_e, minute_e, second_e).timestamp()
        # difference in time in s
        time_gone = (start_seconds_1 - start_seconds) / 3600
        return round(errors / time_gone, 2)

    def __str__(self):
        mcerrot = self.most_common_error()
        levels = self.count_by_level()
        eph = self.errors_per_hour()
        return f"Levels breakdown:\n\tINFO: {levels['i']}\n\tERROR: {levels['e']}\n\tWARNING: {levels['w']}\nMost common error: '{mcerrot}'\nErrors per hour: {eph}"

    def __len__(self):
        return len(self.logs)

l = parse()
analyze = LogAnalyzer(l)
eph = analyze.errors_per_hour()
print(analyze)
