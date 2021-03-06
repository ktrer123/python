# 1. 페이지 가져오기
# 2. requests 만들기
# 3. 정보 추출하기

from cgi import print_directory
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs/companies?q=python&"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}


def get_last_page():
    result =  requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)
    
get_last_page()

def extract_job(html):
    title = html.find("h2", {"class" : "mb4"}).find("a")["title"]
    company, location = html.find("h3", {"class":"fc-black-700"}).find_all("span",recursive=0)
    company = company.get_text(strip=1)
    location = location.get_text(strip=1)
    job_id = html['data-jobid']
    return {'title' : title, 'company' : company, 'location' : location, 'link' : f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            job = extract_job(result)  
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs