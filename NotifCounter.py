# from Setting import save
# from crawler import datetime_handler
import datetime

class NotifCounter:

    def __init__(self, data_list, remind_day):
        self.data_list = data_list
        self.remind_day = remind_day


    def notif_or_not(self):
        return_list = []
        notif_range = datetime.timedelta(days=self.remind_day)
        for one_assi in self.data_list:
            if one_assi.deadline - datetime.datetime.now() <= notif_range:
                return_list.append(one_assi)
        return return_list


"""
if __name__ == "__main__":
    n = NotifCounter(, 3)
    n = n.notif_or_not()
    print(n)
# trying to recreate a Assignment(course, task, deadline) was a disaster
"""