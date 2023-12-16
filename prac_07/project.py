"""
Project Management Program
Estimate: 50 minutes
Actual:   52 minutes
"""
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {str(self.priority)}, " \
               f"estimate: ${float(self.cost_estimate):.2f}, completion: {self.percent_complete}%"

    def update_project(self, percent_complete="", priority=""):
        if percent_complete:
            self.percent_complete = percent_complete
        if priority:
            self.priority = priority

    def is_after_date(self, date):
        project_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        return project_date > date