import re
from Error import SyntError

tokens = {
    'equals': r'^будет',
    'comment':r'//.*',
    'var':r'\$\w+',
    'integer':r'^\d+',
    'ifOperation':r'^это',
    'string':r'\'.+\'',
    'ifCondition':r'^если',
    'printFunction':r'^базарить',
    'funcDeclare':r'^мутка',
    'argBlockStart':r'^номерочки',
    'stateBlockStart':r'^епт',
    'booleanTrue':r'^Пиздато',
    'booleanFalse':r'^Хуево',
    'lineEnd':'\n',
    'space':r' *'

}

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

            self.sourceDict.append(self._tokenize(line))

    def _tokenize(self,line):
        #will be split string to a list of tokens

        splittedLine = line.split(' ') # list of all words
        errorGettingLine = line #line which will be get any syntax error
        resultList = [] #will contain information about every word in program as token: [key:value]

        for element in splittedLine:

            for key in tokens:

                res = re.search(tokens[key],element)

                if res:
                    value = res.group(0)

                    resultList.append([key,value])

                    if key == 'comment':
                        #delete all comments from error getting line

                        start = splittedLine.index(value)
                        commentSection = splittedLine[start:len(splittedLine)]

                        errorGettingLine = errorGettingLine.replace(value,'')

                        for commentStuff in commentSection:
                            errorGettingLine = errorGettingLine.replace(commentStuff,'')

                        continue

                    errorGettingLine = errorGettingLine.replace(value,'')
                    
        errorGettingLine = errorGettingLine.replace(' ','')

        if errorGettingLine:
            
            SyntError.setTarget(str(self.source_lines.index(line)))
            SyntError.ShowError()

        print(resultList)
        return resultList

Lexer('test.txt')
input()