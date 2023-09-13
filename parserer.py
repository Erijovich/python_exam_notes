import controller as ctr
import user_interface as ui

def parser_command(user_input: str):
    command_list = user_input.lstrip().split(" ",1) # берём первое слово введённой строки
    if command_list[0].strip().lower()[0] == "/": # проверяем наличие старта команды в первом элементе массива строк
        if command_list[0] in ui.oper_list: # если да, то проверяем, является ли слово зарезервированной командой
            if len(command_list) < 2:
                command_list.append('')
            print(command_list)
            return ctr.choose_action(command_list[0],command_list[1]) # отправляем команду и всю остальную строку
        else:
            print(f'{command_list[0]} не является зарегистрированной командой. Введите /help для вывода списка доступных команд')
    else:
        print('Необходимо ввести команду, начинающуюся с символа "/". Введите /help для вывода списка доступных команд')
        return True

        
# метод парсит строку для добавления и проверяет наличие заголовка. если его нет - то добавляет из первых слов самой заметки посредством метода get_title()
# вызывается только один раз для каждой команды /add
def parser_to_add(user_input: str):
    string_to_add = user_input.strip().split("--",1)
    print(f'list = {string_to_add}')
    if len(string_to_add) > 1: # если разбивка произошла
        title = string_to_add[0].strip()
        body = string_to_add[1].strip()
        if not is_empty(title): # проверка не пустое ли название
            return(title, body) # возвращаем кортеж из заданного заголовока и тела заметки
        elif not is_empty(body):
            return (get_title(body), body) # возвращаем кортеж из созданного заголовока и тела заметки
        else:
            return ('не задано','не задано')
    else:       # если разделителя не было
        body = string_to_add[0].strip()
        if not is_empty(string_to_add[0].strip()): # проверка не пустое ли тело заметки
            return (get_title(body), body) # возвращаем кортеж из созданного заголовока и тела заметки
        else:
            return ('не задано','не задано')

# метод проверяет , является ли введённая строка числом
def parser_id(some_string: str):
    id_to_search = some_string.lstrip().split()[0].strip() # берём первый элемент введённой строки, обрезаем от всех пробелов, остальное - в игнор
    print("to check:", end=" ")
    print(id_to_search)
    if id_to_search.isnumeric(): # isnumeric() всё-таки не на 100% проверяет на число, в особых случаях могут возникать ошибки конвертации
        try:
            return int(id_to_search)
        except:
            return False
    return False

    

def parser_to_search(some_string: str):
    pass

# метод проверяет, не является ли строка пустой
def is_empty(some_string: str):
    if some_string == "":
        return True
    return False

# метод создаёт заголовок из первых слов тела заметки
def get_title(body: str):
    words = body.split(" ")
    if len(words) >= 3:
        return " ".join([words[0],words[1],words[2]]) # склеиваем пробелами первые 3 слова
    else:
        return " ".join(words) # берём существующие слова в качестве заголовка заметки