
__author__ = 'Kevin Carbone'

from neural.datasets.dataset import Dataset
from neural.utilities import *
import lxml.html
import string
import re



class LanguageDataset(Dataset):
    """docstring for Dataset"""
    def __init__(self,languages=None,offline=True):
        Dataset.__init__(self)
        self.languages = []
        if not languages:
            self.languages.extend(["en","it","nl"])
        self.build_dataset()
        print "Dataset Built"

    def extract_features(self,data):
        d = dict(zip(string.ascii_lowercase, (0 for x in range(0,27))))
        for ch in data:
            if d.get(ch.lower(),None) != None:
                d[ch.lower()] += 1.0
        total = sum(d.values())
        for k in d.keys():
            if total == 0:
                d[k] = 0
            else:
                d[k] = float(d[k])/float(total)
        return d


    def build_dataset(self):
        for l,lang in enumerate(self.languages):
            segments = self.retrieve_segments(lang,10)
            for seg in segments:
                for text in seg[1]:
                    input = self.extract_features(text)
                    # norm_input = normalize(input.values())
                    output = [1 if l==x else 0 for x in range(len(self.languages))]
                    if sum(input.values()) > .1:
                        self.add(input.values(),output,text)



    def retrieve_segments(self, lang, n=10):
        dataset = []
        for i in range(n):
            url = "http://%s.wikipedia.org/wiki/Special:Random" % lang
            actual_url,data = self.retrieve_segment(url)
            dataset.append((actual_url,data))
        return dataset

    @classmethod
    def retrieve_segment(cls, url, min_chars=150):
        html_tree = lxml.html.parse(url)
        p_tags = html_tree.xpath('//p')
        p_content = [p.text_content() for p in p_tags if len(p.text_content())>min_chars]
        if len(p_content) <=0:
            return cls.retrieve_segment(url, min_chars)
        return html_tree.docinfo.URL,p_content


def remove_bad_chars(str):
    return re.findall("[a-z]+", str.lower())

remove_bad_chars("Alkjlk567670-!@")