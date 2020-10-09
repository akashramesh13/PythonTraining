# requests
import requests as request
url = "https://www.google.com"
# getting response by requesting to that url
response = request.get(url)
# taking the content of the page from the response 
page = response.text
# some str splicing to get the title alone 
# fails for fb because of their script between title tag
title = page[page.find('<title>') + 7: page.find('</title>')]

print(f"Title of the page is: {title}")