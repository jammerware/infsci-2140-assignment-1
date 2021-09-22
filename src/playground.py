import xml.etree.ElementTree as ET
from xml import sax
from xml.sax.handler import ContentHandler

from os import path


class SaxContentHandler(ContentHandler):
    def __init__(self):
        self.count = 0

    def startElement(self, tag, attributes):
        return

    def endElement(self, tag):
        if tag == "DOC":
            self.count += 1

    def get_count(self):
        return self.count


def count(file_path):
    count = 0

    # PULL PARSER
    # parser = ET.XMLPullParser(['end'])

    # with open(rf'{file_path}', 'rb', buffering=32) as f:
    #     while True:
    #         line = f.read()

    #         if line is None:
    #             break

    #         parser.feed(line)

    # print('reading events')
    # return sum(1 for _ in parser.read_events())

    # ITERPARSE
    # context = ET.iterparse(file_path, events=('end',))
    # prior_element = None

    # for action, elem in context:
    #     if elem.tag == 'DOC':
    #         if prior_element is not None:
    #             prior_element.clear()
    #         prior_element = elem
    #         count += 1

    #     while elem.getprevious() is not None:
    #         del elem.getparent()[0]

    # SAX
    handler = SaxContentHandler()
    parser = sax.make_parser(['xml.sax.IncrementalParser'])
    parser.setContentHandler(handler)

    with open(rf'{file_path}', 'rb', buffering=32) as f:
        for chunk in f:
            parser.feed(chunk)
            count = handler.get_count()

    return count


# total = count('E:/School/Grad/infsci-2140/assignment-1/data/output/docset.trectext')
total = count('E:/School/Grad/infsci-2140/assignment-1/data/output/docset.edited.trectext')
print('total', total)
