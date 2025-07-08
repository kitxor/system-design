from abc import ABC, abstractmethod

"""
each work flow, be it simple or corporate 
has different rules. define contract for workflow specific methods
"""


class WorkFlowStrategy(ABC):

    @abstractmethod
    def get_next_possible_statuses(self, status):
        return

    @abstractmethod
    def change_status(self, task, new_status):
        return

    @abstractmethod
    def check_status_change_validation(self, old_status, new_status):
        return

    @abstractmethod
    def send_notification(self, task, msg):
        return
