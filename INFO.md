тут будет то что было добавлено в текущей версии и что мне предстоить сделать

**v 0.0.21 - ТЕКУЩАЯ**(16.08.2021)

__НОВОЕ__:

        Апгрейд версии 0.0.2. В ходе работы всплыла ошибка неработоспособности строк ввиду особенностей разделения на токены, поэтому я работал над тем, чтобы в функцию разделения на токены строки попадали отдельным элементом и не разбивались на отдельные элементы по пробелу, как это было раньше. Сама функция получила название normalSplit. Также добавил пару новых слов (Логическое ИЛИ и И), заменил запятую с 'И' на 'ДА', но планирую в итоге ее оставить просто запятой, посмотрим как пойдет.

__ЧТО ПРЕДСТОИТ СДЕЛАТЬ__:

        Все тоже самое, что и у версии 0.0.2.

**v 0.0.2 - ТЕКУЩАЯ** (13.08.2021)

__НОВОЕ__:

        Лексер начал делать то, для чего предназначался! Не уверен, что представленный в этой версии лексер - итоговый, но базовая часть должна остаться неизменной.
        На данный момент ошибки были реализованы просто обычным классом, не факт что останется в будущем
        Переименовал функцию _splitLine в _tokenize, стало звучать лучше
        Некоторые слова в синтаксисе были изменены на те, которые, по моему мнению, звучат лучше

__ЧТО ПРЕДСТОИТ СДЕЛАТЬ__:
        
        Все ещё добавить регулярки хотя бы к циклам for и while
        Заложить основу транслятора
        






**v 0.0.1** (11.08.21)

__НОВОЕ__:

        TrolleyScript переродился, так и не родившись! Пусть пока не полностью, но я планирую написать его так, чтобы он хотя бы отчасти
        напоминал нормальный язык программирования: TrolleyScript получит собственный лексер, что позволит ему быть чем-то более самобытным
        нежели чем просто синтаксис питона(хотя с технической точки зрения он все равно будет таким)

        Заложил основу лексера

__ЧТО ПРЕДСТОИТ СДЕЛАТЬ__:

        _SplitLine переименовать во что-то более адекватное
        Сделать разбиение на токены с использованием регулярок с помощью цикла
        Добавить регулярки к остальным выражениям языка

        