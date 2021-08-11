# -*- ansi
import os
import shutil


langDict = {
    'типа': '',
    'запомни':'=',
    'как':'',
    'епт':'\n',
    'слыш':'=',
    'базарить':'print',
    'если':'if ',
    'зачмырить':'for',
    'каждого':'',
    'в':'in',
    
    'нахуй':':\n',
    'без_корешей':'()',
    'кореша':'(',
    'нах':')',
    'ептыть':'):\n',
    'похуй':'\n',
    'это':'==',
    'иначе':'else',
    'поясни':'input()',
    'отдыхай':'pass',
    'мутка':'def ',
    'по_понятиям':'True',
    'не_по_понятиям':'False',

}
errors = {

    'NameError': 'Мутные у тебя контактики, перепроверь номерки'


}
keys = langDict.keys()

def countSub(text, target):
    count = 0
    i = -1
    while True:
        i = text.find(target, i+1)
        if i == -1:
            return count
        count += 1

class Lex:

    def __init__(self,source_file):

        self.source_text = ''
        try:
            with open(source_file,'r',encoding='ANSI') as f:
                for line in f:
                    self.source_text += line
        except:
            pass

        self.source_text += ' '

        self._textAsList()
        self._translate()
        self._normalize()
        self.setup()

    def _textAsList(self):

        self.source_text_list = []

        while self.source_text.find('\n') != -1:
            self.source_text = self.source_text.replace('\n',' ',1)

        line = ''

        tempList = []

        for letter in self.source_text:
            if letter == ' ':
                self.source_text_list.append(line)
                tempList.append(line)
                line = ''
                continue
            line += letter

        for word in self.source_text_list:
            
            if '\t' in word:

                tabCount = countSub(word,'\t')

                tempList.insert(tempList.index(word),tempList[tempList.index(word)][0:tabCount])
                tempList[tempList.index(word)] = tempList[tempList.index(word)][tabCount:len(tempList[tempList.index(word)])]

                #tempList[tempList.index(word)] = tempList[tempList.index(word)].replace('\t','')
                #tempList.insert(self.source_text_list.index(word),'\t')

        self.source_text_list = tempList

        #print(self.source_text_list) 

    def _translate(self):
        
        self.translated_text_List = self.source_text_list

        for word in self.translated_text_List:

            for key in keys:

                if word == key:
                    
                    self.translated_text_List[self.translated_text_List.index(word)] = langDict[key]

        tempList = self.source_text_list
        #print(tempList)

        self.translated_text_List = tempList

        #print(self.translated_text_List)

    def _normalize(self):

        self.translated_text = ''

        for word in self.translated_text_List:
            self.translated_text += word

        #print(self.translated_text)

    def setup(self):

        with open('temp.txt','w',encoding='UTF-8') as f:

            f.write(self.translated_text)

print('\nприва) вводи название файлика ептаа только он в папочке должен быть: ')

filename = input()

Lex(filename)
shutil.copy(r'temp.txt',r'temp.py')

try:    
    exec(open('temp.py').read())
except Exception as e:
    print(errors[str(type(e). __name__)])
else:
    #os.system('python temp.txt')
    pass

os.remove('temp.txt')
#os.remove('temp.py')

input()