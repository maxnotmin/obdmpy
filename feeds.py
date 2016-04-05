import feedparser
import re
import time


rawNews = feedparser.parse('https://www.instapaper.com/rss/1365552/HbE1CixNWJJVshSUOEiVhEpdHsk')

rawPod = feedparser.parse('http://ourbigdumbmouth.libsyn.com/rss')


# newsEntries = rawNews.entries
podEntries = rawPod.entries

newsEntries = rawNews.entries



newsList = []
def BuildNews():
    for i in newsEntries:
        #print(i.title)
        #print("news url", i.links[0].href)
        #print(i.published)
        newsList.append({
            'newsTitle': i.title,
            'newsURL': i.links[0].href,
            'newsDate': i.published
        })
    return newsList



podList = []
def BuildPod():
    for j in podEntries[0 : 100]:

        podList.append({
            'podTitle': j.title,
            'podURL': j.links[1].href,
            'podDate': str(j.published).replace('+0000', ''),
            'podSummary': re.sub("<.*?>", "", j.summary)
        })
    return podList








"""
def makePodList():
    return podEntries
"""

"""
print('Pod Entries: ', podEntries[0])

print(podEntries[0].title)
print(podEntries[0].subtitle)
print(podEntries[0].published)
print("mp3: ", podEntries[0].links[1].href)
print(podEntries[0].summary)



for post in podEntries[0 : 100]:
    print(post.title)
    print(post.published)
    print(post.links[1].href)
    print(post.summary)
"""


