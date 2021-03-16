import urllib.request

import bs4 as bs
import requests
from fastapi import FastAPI, HTTPException
from gensim.summarization.summarizer import summarize

# from scraper import get_data, get_status_code

app = FastAPI()


def get_status_code(url):
    request = requests.get(url)
    return request.status_code


def get_data(url):
    scraped_data = urllib.request.urlopen(url)
    print('Done')
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article, 'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    return article_text


@app.get("/scrape_wiki/{wiki_url:path}")
def scrape_wikipedia(wiki_url: str):
    if get_status_code(wiki_url) == 404:
        raise HTTPException(status_code=404, detail="Invalid URL")
    text = get_data(wiki_url)
    return {text}


@app.get("/summarize_wiki/{wiki_url:path}/{ratio:float}")
def summarize_wikipedia_article(wiki_url: str, ratio: float):
    # Check if the URL is a valid Wiki Link
    if get_status_code(wiki_url) == 404:
        raise HTTPException(status_code=404, detail="Invalid URL")

    text = get_data(wiki_url)
    summary = summarize(text, ratio=ratio)
    return {summary}
