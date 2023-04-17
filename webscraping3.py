from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
count=1
for job in jobs:
    print()
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ", "")
    skills = job.find('span', class_="srp-skills").text.replace(" ", "")
    # job_time = job.find('span', class_='sim-posted').span.text.replace(" ","")
    # location =  job.find('ul', class_="top-jd-dtl clearfix").text.replace(" ","")
    more_info = job.header.h2.a['href']
    print(f'{count}.company: {company_name.strip()}')
    print(f'skills:  {skills.strip()}')
    count+=1
    print()
    print('-' * 50)
    with open('pyjobs.txt','a') as jobs1:
        content = jobs1.writelines(company_name)

        content2 = jobs1.writelines(skills)

        content4 = jobs1.writelines(more_info)

        content3 = jobs1.writelines('-'*50)


print(f" we found {count-1} results for you")