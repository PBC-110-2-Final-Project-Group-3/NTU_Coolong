# Import libraries
import requests
from bs4 import BeautifulSoup as bs4
import json
import datetime
# Finish importing libraries


# Define classes
class NTUCoolCrawler:
    def _login(self, s, user, password):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67"
            " Safari/537.36"}
        pre_login_req = s.get("https://cool.ntu.edu.tw/login/saml",
                              headers=headers)
        form1 = bs4(pre_login_req.text, "html.parser").find("form")
        data1 = {}
        for inp in form1.find_all("input"):
            data1[inp.get("name")] = inp.get("value") or ""
        data1["ctl00$ContentPlaceHolder1$UsernameTextBox"] \
            = user
        data1["ctl00$ContentPlaceHolder1$PasswordTextBox"] \
            = password
        login_req = s.post("https://adfs.ntu.edu.tw/" + form1.get("action"),
                           data=data1, allow_redirects=True, headers=headers)
        form2 = bs4(login_req.text, "html.parser").find("form")
        data2 = {}
        for inp in form2.find_all("input"):
            data2[inp.get("name")] = inp.get("value") or ""
        post_login_req = s.post(form2.get("action"), data=data2,
                                allow_redirects=True, headers=headers)

    def _get_courses_id(self, s):
        """
        The parameter it takes is s,
        which is a requests.Session() context manager.

        It outputs a dictionary containing course
        id and the corresponding course name.

        Example:
        {"course_id_1": "course_name_1",
         "course_id_2": "course_name_2",...}
        """
        # Set up
        url = "https://cool.ntu.edu.tw/api/v1/courses?per_page=100000"
        courses = {}
        # Finish settin up

        # Crawl courses' id
        r = s.get(url)
        dt = json.loads(r.text)
        for course in dt:
            # Check the access to the course
            name = course.get("name")
            if not (name is None):
                id = course.get("id")
                courses[id] = name
            # Finish checking the access
        # Finish crawling id
        return courses

    def _get_unsubmitted_assignments(self, cid, s):
        """
        The parameters it takes is cid (course id) and s (context manager).
        It outputs a list containing Assignment objects.
        Example: [object_1, object_2, ...]
        And the function only crawls assignments that have not been submitted.
        """
        # Set up
        url = (f"https://cool.ntu.edu.tw/api/v1/courses/{cid}"
               "/assignments?per_page=100000000")
        assignments = []  # Store Assignments objects
        # Finish setting up

        # Crawl assignment by class id
        r = s.get(url)
        # print(r.text)
        dt = json.loads(r.text)
        for assi in dt:
            if not assi["has_submitted_submissions"]:
                name = assi["name"]
                deadline = assi["due_at"]
                if deadline is None:
                    continue
                assi_object = Assignment(name, deadline)
                assignments.append(assi_object)
        # print(cid, ": ok!")
        # Finish crawling assignment
        return assignments
    
    def _get_quizzes(self, cid, s):
        """
        The parameters it takes is cid (course id) and s (context manager).
        It outputs a list containing Quiz objects.
        Example: [object_1, object_2, ...]
        """
        # Set up
        url = ("https://cool.ntu.edu.tw/api/v1/courses/"
               f"{cid}/quizzes?per_page=100000000")
        quizzes = []
        # Finish setting up

        # Crawl quizzes by class id
        r = s.get(url)
        dt = json.loads(r.text)
        for quiz in dt:
            if quiz == "message":
                continue
            name = quiz["title"]
            deadline = quiz["due_at"]
            if deadline is None:
                continue
            quiz_object = Quiz(name, deadline)
            quizzes.append(quiz_object)
        # Finish crawling quizzes
        return quizzes

    def get_assignments_or_quizzes(self, course_data_type):
        """
        The function takes the parameter which decide
        the objective is assignment(0) or quiz(1).
        It outputs every unsubmitted assignments or upcoming quizzes.

        The output is a dictionary.
        The keys are courses' name, and the values are assignment
        or quiz object.

        Example 1:
            {course_1: [assignment_1, assignment_2, ...],
             course_2: [assignment_3, assignment_4, ...], ...}
        Example 2:
            {course_1: [quiz_1, quiz_2, ...],
             course_2: [quiz_3, quiz_4, ...], ...}
        """
        # Set up
        course_data = {}
        # Finish setting up

        with requests.Session() as s:
            self._login(s, user, password)
            courses = self._get_courses_id(s)
            for id in courses.keys():
                course_name = courses[id]
                if course_data_type in ("assignments", 0):
                    data = self._get_unsubmitted_assignments(id, s)
                elif course_data_type in ("quizzes", 1):
                    data = self._get_quizzes(id, s)
                if data != []:
                    course_data[course_name] = data
        return course_data


class Requirement:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = self.datetime_handler(deadline)

    def __repr__(self):
        name_str = "Name: " + str(self.name)
        dl_str = "Deadline: " + str(self.deadline)
        output_str = name_str + " , " + dl_str
        return output_str
    
    def datetime_handler(self, deadline):
        if deadline is None:
            return None
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        utc_8 = datetime.timedelta(hours=8)
        dl = datetime.datetime.strptime(deadline, fmt) + utc_8
        datetime_list = [dl.date, dl.time]
        return datetime_list


class Assignment(Requirement):
    submitted = False

class Quiz(Requirement):
    due = False
# Finish defining classes


# Test code
if __name__ == "__main__":
    # Set up
    # The user and password should be obtained from config
    user = ""  # Temporary
    password = ""  # Temporary
    # Finish setting up

    # Crawl!
    crawler = NTUCoolCrawler()
    adict = crawler.get_assignments_or_quizzes("assignments")  # It crawls quizzes
    for key in adict.keys():
        print(key + ":")
        print(adict[key], "\n===========")
    print("=======================\nFinish!\n=======================")
    # Finish crawling
# Finish testing code
