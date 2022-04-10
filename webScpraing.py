
import requests
from bs4  import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def scrape():
  baseUrl = "https://www.washingtonpost.com/world/2022/04/03/russia-ukraine-war-news-putin-live-updates/"
  req = requests.get(baseUrl)
  htmlPost = req.content
  soup= BeautifulSoup(htmlPost, 'html.parser')
  return(soup.get_text())
if __name__=="__main__" :
  app.run(debug=True)  