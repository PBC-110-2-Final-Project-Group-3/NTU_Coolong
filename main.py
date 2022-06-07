# Import libraries
import os
import yaml
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
    print(n_assi)
    # Finish deciding tasks
    # print(assignments)
