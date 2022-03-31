import requests
from bs4 import BeautifulSoup

START = 10
URL = "https://kr.indeed.com/jobs?q=python"

def get_last_page():
    result = requests.get(URL)
# print(indeed_result)
# <Response [200]> : 오케이
# print(indeed_result.text)
# html 출력, 이 안에서 정보를 출력해야 됨.

    soup = BeautifulSoup(result.text, "html.parser")
# beautifulsoup로 html내에서 데이터를 탐색함

    pagination = soup.find("div",{"class":"pagination"})
# 사이트 내의 pagination class를 갖는 요소 찾기 / 페이지 순서
    links = pagination.find_all('a')
# pagination class를 가진 요소 중에서 'a'(링크)에 해당하는 html요소들 모두 찾기 / 페이지 버튼

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))
    max_pages = pages[-1]
    return max_pages
# link.find("span") : 리스트 형태로 생선된 pages에서 span을 포함하는 내용 모두 찾아서 pages 리스트에 넣어주기
# link.find("span").string : 그 중에서 "str"(텍스트) 부분만 찾아서 추출
# link.string만해도 잘 추출됨
# int(정수형)으로 변형시 마지막 요소(다음) 식별 불가, 미리 마지막 요소를 빼서 방지

def extrac_job(html):
    title = html.find("h2", {"class":"jobTitle"}).find("span", title=True).string
    company = html.find("span", {"class": "companyName"}).string
    location = html.find("div", {"class": "companyLocation"}).string
    job_id = html.parent['data-jk']
    return {'title': title, 'company': company, 'location': location, 
    'link':f"https://www.indeed.com/viewjob?jk={job_id}&from=serp&vjs=3"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping INDEED page:{page}")
        result = requests.get(f"{URL}&start={page*START}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"slider_container"})
        for result in results:
            job = extrac_job(result)
            jobs.append(job)
    return jobs    
        
# reqests를 자옹으로 계속 실행해주는 함수.
# 추출한 페이지 정보를 토대로 페이지 바다 변하는 숫자를 이용해 반복 request
# 그 중에서 공고 모집의 '제목'에 해당하는 부분을 find해서 출력 되도록 코딩.  

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs