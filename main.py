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

if __name__ == "__main__":
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
            assiments = crawler.get_assignments_or_quizzes(0)
            quizzes = crawler.get_assignments_or_quizzes(1)
        except:
            setting = Setting()
            setting.mainloop()
        else:
            crawl_success = True
    # Finish crawling courses' data
