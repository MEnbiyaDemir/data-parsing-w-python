#import what we need
from requests_html import HTMLSession
import csv

print("(start)")


session = HTMLSession()
url='https://doaj.org/search/articles?ref=homepage-box&source=%7B%22query%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22terms%22%3A%7B%22index.schema_codes_tree.exact%22%3A%5B%22LCC%3AQH301-705.5%22%5D%7D%7D%5D%7D%7D%2C%22size%22%3A%22200%22%2C%22from%22%3A1200%2C%22track_total_hits%22%3Atrue%7D'
#use session to get the page
r = session.get(url)

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r.html.render(sleep=1, scrolldown=5)


#find all the articles by using inspect element and create blank list
articles = r.html.find('article')
newslist = []

#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newsitem2 = item.find('.doaj-public-search-abstracttext', first=True)
        title = newsitem.text
        abstract = newsitem2.text
        

        newsarticle = [title, abstract]
        newslist.append(newsarticle)
        #newslist.append(newsarticle)
    except:
       pass

#print the length of the list

fields = ['title', 'abstract'] 

with open('file.csv', 'a',encoding="utf-8") as f:
      
   # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(newslist)

print("Finished")
# print(title)
# print("")
# print(abstract)