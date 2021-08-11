import json
import re

import urllib.request
import urllib.error
import urllib.parse

from bs4 import BeautifulSoup
from collections import Counter


urls = [
    "https://en.wikipedia.org/wiki/Exchange-traded_fund",
    "https://en.wikipedia.org/wiki/Investment_fund",
    "https://en.wikipedia.org/wiki/Stock_exchange",
    "https://en.wikipedia.org/wiki/Stock_market_index",
    "https://en.wikipedia.org/wiki/Index_fund",
    "https://en.wikipedia.org/wiki/Commodity",
    "https://en.wikipedia.org/wiki/Capital_gain",
    "https://en.wikipedia.org/wiki/Tf%E2%80%93idf",
    "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient",
    "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "https://en.wikipedia.org/wiki/Interpreter_(computing)",
    "https://en.wikipedia.org/wiki/C%2B%2B",
    "https://en.wikipedia.org/wiki/London",
    "https://en.wikipedia.org/wiki/England"
]

json_output_dict = dict()


for url in urls:
    try:
        response = urllib.request.urlopen(url)
        webContent = response.read()

        soup = BeautifulSoup(webContent, features="html.parser")
        div = soup.find("div", {"class": "mw-parser-output"})

        paragraphs = div.find_all("p")

        paragraphs_list = []

        for paragraph in paragraphs:
            paragraph = paragraph.get_text()
            paragraph = re.sub(r"[^a-zA-Z]", " ", paragraph)
            paragraph = re.sub(" +", " ", paragraph)
            paragraph = paragraph.lower()
            
            paragraphs_list.append(paragraph)

        webpage_words = [word for word in " ".join(paragraphs_list).split(" ") if word != ""]

        most_common_words = [tpl[0] for tpl in Counter(webpage_words).most_common(20)]

        json_output_dict[url] = most_common_words

    except urllib.error.HTTPError:
        json_output_dict[url] = "404 - Page Not Found"
        

with open('output.json', 'w') as f:
    json.dump(json_output_dict, f)
