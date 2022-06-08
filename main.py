# Import libraries
import os
import yaml
import datetime
# Finish importing libraries

# Import classes
from crawler import NTUCoolCrawler, Assignment, Quiz
from Setting import Setting
from NotifCounter import NotifCounter
from window import window
from notification.notifi import notification
# Finish importing classes


# Define functions
def login_crawl():
    # Set up
    crawl_success = False
    # Finish setting up

    # Read the setting in the Config.yaml and crawl data
    while not crawl_success:
        is_config = os.path.isfile('./Config.yaml')
        if is_config:
            with open("./Config.yaml", "r") as f:
                config = yaml.safe_load(f)
                account = config["account"]
                password = config["password"]
                remind_day = int(config["remindDay"])
        try:
            crawler = NTUCoolCrawler(account, password)
            assignments = crawler.get_assignments_or_quizzes(0)
            quizzes = crawler.get_assignments_or_quizzes(1)
        except:
            setting = Setting()
            setting.mainloop()
            if setting.exit:
                raise RuntimeError("Exit the login window!")
        else:
            crawl_success = True
    # Finish crawling courses' data
    assignments = deadline_checking(assignments)
    quizzes = deadline_checking(quizzes)
    return remind_day, assignments, quizzes


def deadline_checking(list_1):
    # Set up
    return_list = []
    # Finish setting up

    # Time checking
    now = datetime.datetime.now()
    for obj in list_1:
        if obj.deadline > now:
            return_list.append(obj)
    # Finish time checking
    return return_list


def notification_count(assignments, quizzes):
    # Decide which tasks to be notified
    counter_1 = NotifCounter(assignments, remind_day)
    counter_2 = NotifCounter(quizzes, remind_day)
    return counter_1.notif_or_not() + counter_2.notif_or_not()
# Finish defining funcition


if __name__ == "__main__":
    # Crawl data for the first time
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    remind_day, assignments, quizzes = login_crawl()
    # Finish crawling data

    # To see the deadline is within "remind_day"
    n_assi_quiz = notification_count(assignments, quizzes)

    # Set up
    update_time = datetime.datetime.now()
    ori_assignments = ori_quizzes = ori_n_assi_quiz = None
    win_refresh = False
    win_first_time = True
    # Finish setting up

    while True:
        # Crawl data hourly
        now = datetime.datetime.now()
        if now - update_time >= datetime.timedelta(hours=1):
            remind_day, assignments, quizzes = login_crawl()
            n_assi_quiz = notification_count(assignments, quizzes)
            update_time = now
        # Finish crawling data hourly

        # Notification window
        if ori_n_assi_quiz != n_assi_quiz:
            ori_n_assi_quiz = n_assi_quiz
            if len(ori_n_assi_quiz) > 0:
                noti_assi = notification(remind_day, ori_n_assi_quiz)
                noti_assi.mainloop()
        # Finish notification window

        # All the assignments and quizzes
        if win_first_time:
            win_first_time = False
            win = window(ori_assignments, ori_quizzes)
            win.mainloop()
        elif win_refresh:
            win_refresh = False
            win = window(ori_assignments, ori_quizzes)
            win.mainloop()
        if (ori_assignments != assignments) or (ori_quizzes != quizzes):
            ori_assignments = assignments
            ori_quizzes = quizzes
            win = window(ori_assignments, ori_quizzes)
            win.mainloop()
        # Finish the whole assignments and quizzes
