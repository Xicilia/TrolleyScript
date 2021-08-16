import sys


from re import A

class Error:

    def __init__(self,ErrorName,Code,ErrorText):

        self.ErrorName = ErrorName
        self.Code = Code
        self.ErrorText = ErrorText

        self.target = None

    def ShowError(self):
        #shows the error if target was added or returns None
        if self.target:
            print(str(self.Code) + '.' + str(self.ErrorName) + " : " + self.target)
            #sys.exit() will uncommented letter, maybe
        else:
            return None

    def setTarget(self,target):
        self.target = target


SyntError = Error('Синтаксическая ошибка',0,' Синтаксическая ошибка в строке')