import re

class Lexer:

    def __init__(self,source_code):

        self.source_lines = []

        self.sourceDict = []

        #get content from source file
        with open(source_code,'r',encoding='UTF-8') as file:

            for line in file:
                self.source_lines.append(line)

            self._createDict()

    def _createDict(self):
        
        for line in self.source_lines:
            self.sourceDict.append(self._splitLine(line))

    def _splitLine(self,line):
        #will be split string to a list of tokens
        splittedString = []

        res = re.search('//',line)
        if res:
            splittedString.append(['comment',res])
            line = line.replace(line[res.start():len(line)],'')

        res = re.search(r'\$\w+',line)
        if res:
            splittedString.append(['var',res])
            line = line.replace(res.group(0),'')

        res = re.search('запомни как',line) 
        if res:
            splittedString.append(['operation',res])
            line = line.replace(res.group(0),'')

        res = re.search(r'\d+',line)
        if res:
            splittedString.append(['value',res])
            line = line.replace(res.group(0),'')

        splittedString.sort(key=lambda val: val[1].start())

        for string in splittedString:
            string[1] = string[1].group(0)

        print(splittedString)


        

    def _setContext(self,line):
        #get current line then use this as arg to func
        return self.source_lines[self.source_lines.index(line)]

Lexer('test.txt')
