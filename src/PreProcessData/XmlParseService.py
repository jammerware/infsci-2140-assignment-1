import re


class XmlParseService:
    def __init__(self):
        # this dict holds compiled regexes to speed up matching
        self.regex_dict = {}

        # special case to catch non-tagged text content in the web collection
        self.regex_web = re.compile(r'</DOCHDR>([\s\S]+)<\/DOC>', flags=re.M)
        # replace regex to scrub HTML tags
        self.regex_html_tag = re.compile(r'<\/?.*?>', flags=re.M | re.DOTALL)

    def extract_element_content(self, tag, content):
        # compile a regex for this tag on demand
        if tag not in self.regex_dict:
            self.regex_dict[tag] = re.compile(rf'<{tag}>([\s\S]*?)<\/{tag}>', flags=re.M)

        regex = self.regex_dict[tag]
        match = regex.search(content).group(1).strip()

        return match

    def extract_html_text(self, content):
        raw_match = self.regex_web.search(content).group(1).strip()
        match_untagged = self.regex_html_tag.sub('', raw_match).strip()

        return match_untagged

    # def __parse_xml(self, xml_string):
    #     try:
    #         return et.fromstring(xml_string)
    #     except:
    #         return et.fromstring(f'<DOC><DOCNO>ERROR</DOCNO><BODY><TEXT>The xml contained an illegal entity.</TEXT></BODY></DOC>')
