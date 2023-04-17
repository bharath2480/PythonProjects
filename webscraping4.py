from bs4 import BeautifulSoup
import requests
import time
print("some Skill that you are not familar with")
unfamilar_skill = input('>')
print(f'Filtering out {unfamilar_skill}.....')
def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')


    for index,job in enumerate(jobs):
        print()
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ", "")
        skills = job.find('span', class_="srp-skills").text.replace(" ", "")
        # job_time = job.find('span', class_='sim-posted').span.text.replace(" ","")
        # location =  job.find('ul', class_="top-jd-dtl clearfix").text.replace(" ","")
        more_info=job.header.h2.a['href']
        if unfamilar_skill not in skills:
            with open('pyjobs1.txt', 'a') as f:
               f.writelines(f'{index}.company: {company_name.strip()}\n')
               f.writelines(f'skills:  {skills.strip()}\n')
               f.writelines( more_info)

               f.write(" ")
               f.write('-' * 50)
        else:
            pass

    print(f" we found {index} results for you")
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*1)
