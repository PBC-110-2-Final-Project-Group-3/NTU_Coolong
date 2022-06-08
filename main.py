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
    return remind_day, assignments, quizzes


def notification_count(assignments, quizzes):
    # Decide which tasks to be notified
    counter_1 = NotifCounter(assignments, remind_day)
    counter_2 = NotifCounter(quizzes, remind_day)
    return counter_1.notif_or_not(), counter_2.notif_or_not()
# Finish defining funcition


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    remind_day, assignments, quizzes = login_crawl()
    n_assi, n_quiz = notification_count(assignments, quizzes)
    ori_n_assi = ori_n_quiz = None

    # Set up
    update_time = datetime.datetime.now()
    while True:
        now = datetime.datetime.now()
        if now - update_time >= datetime.timedelta(hours=1):
            remind_day, assignments, quizzes = login_crawl()
            n_assi, n_quiz = notification_count(assignments, quizzes)
            update_time = now
        # win = window()
        if ori_n_assi != n_assi:
            ori_n_assi = n_assi
            if len(ori_n_assi) > 0:
                print(f"Number of assignments: {len(ori_n_assi)}")
                noti_assi = notification(remind_day, ori_n_assi)
                noti_assi.mainloop()
            else:
                print("No assignments!")

        if ori_n_quiz != n_quiz:
            ori_n_quiz = n_quiz
            if len(ori_n_quiz) > 0:
                print(f"Number of quizzes: {len(ori_n_quiz)}")
                noti_quiz = notification(remind_day, ori_n_quiz)
                noti_quiz.mainloop()
            else:
                print("No quizzes!")

    # print(n_assi)
    # Finish deciding tasks
    # print(assignments)
