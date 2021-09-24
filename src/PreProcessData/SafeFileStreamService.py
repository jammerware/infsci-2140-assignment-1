import traceback


class SafeFileStreamService:
    def __init__(self, path, delimiter):

        # open the file and record the delimiter
        self.delimiter = delimiter
        self.file = open(path, 'r', encoding="utf-8")

    def next(self):
        content = ''

        try:
            while True:
                read_line = self.file.readline()

                if read_line == '':
                    self.__cleanup()
                    return None

                content += read_line

                if read_line.strip() == self.delimiter:
                    return content
        except:
            self.__cleanup(is_error=True)

        return None

    def __cleanup(self, is_error=False):
        if is_error:
            ex = traceback.format_exc()
            print('ERROR:', ex)

        if self.file:
            self.file.close()
