
__author__ = 'Kevin Carbone'

from neural.datasets.dataset import Dataset
import lxml.html
import string


class LanguageDataset(Dataset):
    """Builds a dataset of language documents, using relative frequency of letters"""
    def __init__(self, languages=None, offline=True, ndocuments=10):
        Dataset.__init__(self)
        self.languages = []
        if not languages:
            self.languages.extend(["en", "it", "nl"])
        self.build_dataset(ndocuments)
        print "Dataset Built"

    def extract_features(self, data):
        d = dict(zip(string.letters, (0 for x in range(0, len(string.letters)))))
        for ch in data:
            if d.get(ch, None) != None:
                d[ch] += 1.0
        total = sum(d.values())
        result = []
        for k in sorted(d.keys()):
            if total == 0:
                result.append(0)
            else:
                result.append(float(d[k])/float(total))
        return result

    def add_text(self, text):
        input = self.extract_features(text)
        output = [0, 0, 0]
        self.add(input, output, text)

    def build_dataset(self, ndocuments=10):
        for l, lang in enumerate(self.languages):
            segments = self.retrieve_segments(lang, ndocuments)
            for seg in segments:
                for text in seg[1]:
                    input = self.extract_features(text)
                    # norm_input = normalize(input.values())
                    output = [1 if l==x else 0 for x in range(len(self.languages))]
                    if sum(input) > .1:
                        self.add(input, output, text)

    def retrieve_segments(self, lang, n=10):
        dataset = []
        for i in range(n):
            url = "http://%s.wikipedia.org/wiki/Special:Random" % lang
            actual_url, data = self.retrieve_segment(url)
            dataset.append((actual_url, data))

        return dataset

    @classmethod
    def retrieve_segment(cls, url, min_chars=30):
        html_tree = lxml.html.parse(url)
        if not html_tree:
            return cls.retrieve_segment(url, min_chars)
        try:
            p_tags = html_tree.xpath('//p')
        except AssertionError, e:
            return cls.retrieve_segment(url, min_chars)
        p_content = [p.text_content() for p in p_tags
                     if len(filter(lambda c: not c.isdigit(), p.text_content())) > min_chars]
        s_content = []
        for p in p_content:
            sentences = p.split(".")
            s_content.extend(sentences)
        if len(p_content) <= 0:
            return cls.retrieve_segment(url, min_chars)
        return html_tree.docinfo.URL, s_content
