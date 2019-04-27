from bs4 import BeautifulSoup 
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#just declaring a url string
url="https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html"

#get response object for that url
web_response= requests.get(url)

#content of the response is stored into var webpage
webpage = web_response.content

#parse the webpage content and store it as bs4 object into var soup
soup = BeautifulSoup(web_response.content,"html.parser")

#all the tags with attribute "Rating" are stored in var rating
#rating contains tags
rating=soup.find_all(attrs={"class": "Rating"})
company=soup.find_all(attrs={"class": "Company"})
cocoa=soup.find_all(attrs={"class": "CocoaPercent"})

#print(rating)
#create a ratings list variable 
ratings = []
companys =[]
cocoas =[]

#loop through rating varible,extract the text from tags,convert it to float, append it to ratings list
#The first element is a heading, so begin from 1st index in array
for r in rating[1:]:
  ratings.append(float(r.get_text()))

for r in company[1:]:
  companys.append(r.get_text())

for r in cocoa[1:]:
  cocoas.append(r.get_text().replace("%", ""))

#print(ratings)
#print(companys)

#plot a histogram of collected ratings, use plt.show() to view the histogram
plt.hist(ratings)
plt.show()
#use plt.clf() to clear the field
#create a dictionary and store the lists
d={"Company": companys,"Rating": ratings,"Cocoa": cocoas}

#create a dataframe from the dictionary
df= pd.DataFrame.from_dict(d)
print(df)

#get the average rating
mean=df.groupby("Company").Rating.mean()

#get the top ten largest rating values
topten=mean.nlargest(10)
print(topten)

# this is for plotting purpose

#index = np.arange(len(companys))
#plt.bar(index, ratings)
#plt.xlabel('Company', fontsize=5)
#plt.ylabel('Ratings', fontsize=5)
#plt.xticks(index, companys, fontsize=5, rotation=30)
#plt.title('Chocolate Company Ratings')
#plt.clf
#plt.show()






