import requests
from bs4 import BeautifulSoup
import pprint

# grabbing the url with GET request
res1 = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')
# print(res.text)

# using BeautifulSoup to parse text od the website to html
soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# using find methods you can find specific elements of the html file
# ex. soup.a/soup.find('a') - first link, soup.find_all('a') - all links
# print(soup.find('title'))

# css selector - select an element or a specific class in this case by .class_name
# print(soup.select('.score')[0])

# for id #id_name
# print(soup.select('#score_39426341'))

# we want to grab title and link of a story with over 100 points
links1 = soup1.select('.titleline > a') # grabbing the a tag that is a child of a tag with titleline class
links2 = soup2.select('.titleline > a')
subtext1 = soup1.select('.subtext')
subtext2 = soup2.select('.subtext')
#print(votes[0].get('id')) chaining is possible

links = links1 + links2 
subtext = subtext1 + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText() # getting title
        href = item.get('href', None) # adding default value, in case of no link
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title,
                        'link': href,
                        'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))