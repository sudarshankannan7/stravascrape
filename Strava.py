
# coding: utf-8

# In[122]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

#trying to use a headless browser; not quite sure how to implement
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


# In[123]:


base_url = "https://www.strava.com"
featured_running_races = 'https://www.strava.com/featured-running-races'
id_list = []


# In[ ]:


#trying to use a headless browser + webdriver tools; not quite sure how to implement
opts = Options()
opts.set_headless()
browser = Chrome(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class('playbutton').click()


# In[126]:


#doesn't work, probably for the same reason that pullActivities doesn't 
def pullRaceStravaLinks(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    #list_td = soup.find_all('a', {'class':'minimal'})
    #return list_td
    links = soup.find_all('tr', {'class': 'race-row'})
#list_races = pullRaceStravaLinks(featured_running_races)
#list_races
list_races = ['https://www.strava.com/running-races/2019-brass-monkey-half-marathon',
             'https://www.strava.com/running-races/2019-buff-winter-trail',
              'https://www.strava.com/running-races/2019-circuito-do-sol-so-paulo-10k',
            'https://www.strava.com/running-races/2019-walt-disney-world-marathon',
            'https://www.strava.com/running-races/2019-houston-marathon']


# In[134]:


#modifies global id_list (will need for later reference when foldering stuff) and returns links to athlete profiles
def pullAthleteIDs(race_url):
    page = requests.get(race_url)
    soup = BeautifulSoup(page.content,'html.parser')
    #list_td = soup.find_all('a', {'class':'minimal'})
    #return list_td
    global id_list
    links_with_text = []
    for a in soup.find_all('a', {'class': 'minimal'}, href=True): 
        if a.text: 
            links_with_text.append(base_url + a['href'])
            id_list.append(a['href'].replace('/athletes/',''))
    return links_with_text
#compile list of athlete homepages
athlete_list = []
for i in list_races:
    athlete_list+=pullAthleteIDs(i)
athlete_list


# In[67]:


#list of links to athlete homepages
link_list = []
for i in list_races:
    link_list+=pullAthleteIDs(i)
link_list

#list of IDs, will need for reference later


# In[135]:


len(athlete_list)


# In[103]:


#doesn't work
from urllib.request import urlopen as uReq
test_url = 'https://www.strava.com/athletes/1254606'

def pullActivitiesPerPage(athlete_homepage):
    requests.get(athlete_homepage,{'_strava4_session':'pgmn1hsokcs5s6nsv5d4v2v8iajj5lmj'})
    soup = BeautifulSoup(client.read(),'html.parser')
    #list_td = soup.find_all('a', {'class':'bar'})
    #return list_td
    links = soup.find_all('div', {'class':'page container'})
    return links

pullActivitiesPerPage(test_url)


# In[136]:


#the cookie
'''
optimizelyEndUserId=oeu1514687259714r0.5192151439467816;
                    optimizelySegments=%7B%7D;
                    optimizelyBuckets=%7B%7D;
                    _ga=GA1.2.1681880105.1514687261;
                    sp=4bb5833a-37b7-4de7-a60d-08100f9ac6c7;
                    strava_wv2_fonts_loaded=1;
                    _strava_cookie_banner=true;
                    mp_b36aa4f2a42867e23d8f9907ea741d91_mixpanel=%7B%22distinct_id%22%3A%20%22d46c37ec-577c-2744-3971-4ad8e339a04b%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D;
                    _gid=GA1.2.738712934.1548828502;
                    experiment_session=6cc3fc80f9f78f8badfcb28ae6f3adbd;
                    _strava4_session=mf1nh8bvn895tvt410g7j0m7k6gbrard;
                    ajs_user_id=16394677;
                    ajs_anonymous_id=%22c886ae9b-ca0e-4704-8f95-c17c3c40ea45%22;
                    fbm_284597785309=base_domain=.www.strava.com;
                    _sp_ses.047d=*;
                    _sp_id.047d=4ff3fd70-fbe8-4d49-9e4f-8851a04ab79d.1535492186.187.1548879443.1548855213.3963ff4b-a9d0-428d-b017-44a74f9f1f35;
                    ajs_group_id=null;
'''


# In[121]:


login = {'inUserName': '{my_email}', 'inUserPass': {'my_password'}}

example_url = 'https://www.strava.com/athletes/16394677/prs'

p = requests.get('https://www.strava.com/athletes/16394677/prs')
p = BeautifulSoup(p.content,'html.parser')

