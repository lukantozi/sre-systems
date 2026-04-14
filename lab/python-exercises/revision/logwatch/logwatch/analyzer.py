from parser import parse

class LogAnalyzer:
    analyzer_count = 0
    def __init__(self, logs):
        self.logs = logs
        LogAnalyzer.analyzer_count += 1

    def count_by_level(self):
        err = 0
        war = 0
        inf = 0
        for log in self.logs:
            match log["level"]:
                case "INFO": inf += 1
                case "ERROR": err += 1
                case "WARNING": war += 1

        return {"i": inf, "e": err, "w": war}


l = parse()
anlz = LogAnalyzer(l)
d = anlz.count_by_level()
print(d)
