import requests
import re
from bs4 import BeautifulSoup
import webbrowser


class Job:
    def __init__(self, name, link, *description):
        self.name = name
        self.link = link
        self.description = description

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description


jobs = []


def get_jobs_from_ejobs():
    URL = "https://www.ejobs.ro/locuri-de-munca/remote/no-experience/it---telecom"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    job_elements = soup.find_all("div", class_="JobCard")

    for job_element in job_elements:
        title = job_element(class_="JCContentMiddle__Title")
        title_extracted = re.findall(">(.*?)<", str(title))
        job_link = re.findall("href=\"(.*?)\"", str(title))
        # company = job_element("h3", class_="JCContentMiddle__Info JCContentMiddle__Info--Darker")
        # company_extracted = re.findall(">(.*?)<", str(company))
        for item in title_extracted:
            title_extracted = list(filter(None, title_extracted))
        job_link = "https://www.ejobs.ro" + str(job_link[0])
        jobs.append(Job(title_extracted[0], job_link))
        # for item in company_extracted:
        # company_extracted = list(filter(None, company_extracted))
        # print(title_extracted, company_extracted)
        # TODO Figure out how to extract the company thing


def get_job_extended_info():
    for link in jobs:
        URL = link.get_link()
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        job_summaries = soup.find_all("div", class_="JDSummaries")
        job_descriptions = soup.find("div", class_="JMDContent")

        # for job_summary in job_summaries:
        # info = job_summary("a", class_="JDSummary__Link")
        # info = str(info)
        # info_extracted = re.findall("(.*?)</a>", info)

        link.set_description(str(job_descriptions))


get_jobs_from_ejobs()
get_job_extended_info()

if input("Kellenek-e a munkak?(y/n)") == 'y':
    f = open("jobFinder.html", "w")
    f.write("""<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>HTML 5 Boilerplate</title>
        <style>
            .center {
                    margin: auto;
                    width: 50%;
                    padding: 10px;
                    text-align: center;
            }
        </style>
      </head>
      <body>""")
    f.close()
    for job in jobs:
        f = open("jobFinder.html", "a", encoding="utf-8")
        f.write(f"""<h1 class=center><a href="{job.get_link()}"> {job.get_name()}</a></h1>
      <p class=description center> {job.get_description()} </p>""")
        f.close()
    f = open("jobFinder.html", "a")
    f.write("""  </body>
</html>""")
    f.close()
    webbrowser.open("file://f:/pythonStuff/test/pythonStuff/pageScraper/jobFinder.html", new=2)
