import os
import traceback
import xml.etree.ElementTree as et
import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class TrectextCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!

        self.file = open(Path.DataTextDir, 'r')

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.

        read_line = None
        doc_xml = ''

        try:
            while True:
                read_line = self.file.readline()

                if read_line is None:
                    self.__cleanup()
                    return None

                doc_xml += read_line

                if read_line.strip() == "</DOC>":
                    break

            # BEN: temporary fix for the malformatted xml
            parsed_xml = self.__parse_xml(doc_xml)

            docNo = parsed_xml.find('DOCNO').text.strip()
            content = parsed_xml.find('BODY').find('TEXT').text.strip()

            return [docNo, content]
        except:
            self.__cleanup()
            return None

    def __parse_xml(self, xml_string):
        try:
            return et.fromstring(xml_string)
        except:
            return et.fromstring(f'<DOC><DOCNO>ERROR</DOCNO><BODY><TEXT>The xml contained an illegal entity.</TEXT></BODY></DOC>')

    def __cleanup(self):
        ex = traceback.format_exc()
        print('ERROR:', ex)

        if self.file:
            self.file.close()
