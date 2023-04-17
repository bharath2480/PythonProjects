from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name=job.find('h3',class_='joblist-comp-name').text.replace(" ","")
    skills=job.find('span',class_="srp-skills").text.replace(" ","")
    job_time = job.find('span', class_='sim-posted').span.text.replace(" ","")
    location =  job.find('ul', class_="top-jd-dtl clearfix").text.replace(" ","")
    if 'webtechnologies' in skills:
        print(f'''{company_name} 
            skills - {skills}  
            time posted {job_time}
            salaray {location}''')

        print('-'*50)
