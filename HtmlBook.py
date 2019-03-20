#!/usr/bin/python
import readline

readline.parse_and_bind('set editing-mode vi')

class text:
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'
    DARK_BLUE = '\x1b[34m'
    PURPUR = '\x1b[35m'
    LIGHT_BLUE = '\x1b[36m'
    
    INVERT = '\x1b[7m'
    GLITCH = '\x1b[5m'
    LINE = '\x1b[4m'
    STRONG = '\x1b[1m'

    END = '\x1b[0m'

    NEWLINE = '\n'

TagDict = {}
DictFile = "dict.txt"


def AllTags():
	list(TagDict.keys())
	startkey=0
	print(text.RED + text.STRONG + "			Все доступные теги")
	for key in TagDict.keys():
		startkey += 1
		print(text.LIGHT_BLUE+"["+str(startkey)+"] "+ text.YELLOW + key)
	print(text.END)


def PrintHelp():
	print(text.RED + text.STRONG + '''			Помощь
''' + text.LIGHT_BLUE + '''[1] Для получения помощи используй''' + text.YELLOW + ''' 'help' ''' + text.NEWLINE +
text.LIGHT_BLUE + '''[2] Для поиска нужного тега воспользуяся командой''' + text.YELLOW + ''' 'tag тег' ''' + text.NEWLINE +
text.LIGHT_BLUE + '''[3] Для составления словаря используется разделитель''' + text.YELLOW + ''' '|' ''' + text.LIGHT_BLUE + '''текущий файл словаря: ''' + text.YELLOW + DictFile + text.END)



def TagSearch(tag):
	if(tag in TagDict):
		print(text.LIGHT_BLUE + text.STRONG + "Тег " + text.YELLOW + "<" + tag + ">" + text.LIGHT_BLUE + " - " + TagDict[tag][0])
	else:
		print(text.RED + text.STRONG + "Тег " + text.YELLOW + "<" + tag + ">" + text.RED + " не найден" + text.END)



def core():
	while(True):

		string = input(text.YELLOW + text.STRONG + "[BookCmd]~> " + text.GREEN).split(' ')

		print(text.END)

		if(string[0] == "exit"):
			exit(text.RED + text.STRONG + "Выходим" + text.END)
		elif(string[0] == "tag"):
			TagSearch(string[1])
		elif(string[0] == "help"):
			PrintHelp()
		elif(string[0] == "all"):
			AllTags()
		else:
			print(text.RED + text.STRONG + "Команда '" + str(string[0]) +"' не найдена" + text.END)



def LoadingDict():
	with open(DictFile) as file:
		for line in file:
			key, *value = line.split('|')
			TagDict[key] = value




if __name__ == '__main__':
	LoadingDict()
	print(text.LIGHT_BLUE + text.STRONG +'''
	Тебя притествует HtmlBook
	Если требуется помощь то пиши''' + text.YELLOW + ''' help''' + text.LIGHT_BLUE + '''
	Для выхода используй''' + text.YELLOW + ''' exit''' + text.END)
	core()