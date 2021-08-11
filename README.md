**How to setup project locally**

1. Install python 3.9
1. Clone repo locally and navigate in terminal to the root of the project
1. In terminal type (for Linux):
    - `python3.9 -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
    - `python main.py`

<br />

**Simplifications**

1. For analysis I used just content of all paragraphs from *mw-parser-output* div.
1. I have not implemented *filtering out non-english words*. Instead I used regex-based logic to remove digits and punctuation.
1. Instead of *term frequency - inverse document frequency* I have implemented simple word counter.
I have just read about this issue (TF-IDF) on https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089
