# from Setting import save
# from crawler import datetime_handler
import datetime

class NotifCounter:

    def __init__(self, course, task, deadline):  # Should be obtained from crawler
        self.course = course
        self.task = task
        self.deadline = deadline


    def cur_datetime(self):
        get_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur_datetime = datetime.datetime.strptime(get_datetime, "%Y-%m-%d %H:%M:%S")
        return cur_datetime


    def notif_or_not(self):
        notif_dict = dict()
        notif_range = datetime.timedelta(days=3)  # Should be obtained from Setting

        deadline = datetime.datetime.strptime(self.deadline, "%Y-%m-%dT%H:%M:%SZ") # Should be consistent with the datatype from crawler
        if deadline - self.cur_datetime() <= notif_range:
            if notif_dict.get(self.course) == None:
                notif_dict[self.course] = self.task
            else:
                notif_dict[self.course] += self.task
        return notif_dict


"""
    def auto_refresh(self):
        refr_period = datetime.timedelta(hours=1)  # To be discussed
        init_time = "2022-06-03 17:26:20"  # Should be obtained from Setting

       while True:
        return 
"""


if __name__ == "__main__":
    n = NotifCounter("PBC", "HW1", "2022-06-06T12:30:00Z")
    n = n.notif_or_not()
    print(n)