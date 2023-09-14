import operations as ops
import user_interface as ui
import parserer as prs


def choose_action(action, user_input):
    match action:
        
        case '/new':
            if user_input == '':
                user_input = input(msg['to_add'])
            title, body = prs.parser_to_add(user_input)
            ops.new_note(title, body)
            print(msg['added'])

        case '/find': 
            if user_input == '':
                user_input = input(msg['to_find'])
            found_notes = ops.find_notes(user_input)
            if found_notes: # список, если пустой, то будет False
                print(msg['found'])
                ops.print_titles(found_notes)
            else:
                print(msg['not_found'])   

        case '/read': 
            id = input_id(user_input, msg['to_read'])
            if id:
                print(ops.read_note(id))

        case '/edit':
            id = input_id(user_input, msg['to_edit'])
            if id:
                ops.edit_note(id)

        case '/del':
            id = input_id(user_input, msg['to_del'])
            if id:
                ops.del_note(id)

        case '/help':
            ui.print_help()

        case '/stop': # возврат в основное, если можно так сказать, меню
            return True
        
        case '/exit':
            return False # выход
        
        case _:
            print(msg['error']) # если что-то не учли

    return True

# тут запрашиваем у юзера айдишник, проверяем, что он является числом и то, что он есть среди уже существующих
def input_id(user_input, message):
    if user_input != '':
        id = prs.parser_id(user_input)
    else:
        id = prs.parser_id(input(message))
    if id: # если парсер не вернул False
        if ops.check_id(id): # проверка, есть ли указанный id в списке заметок
            return id
        else:
            print(msg['id_not_found'])
            return False
    else:
        print(msg['invalid_id'])
        return False

msg = {
        'error':        'Invalid command! Что бы вывести на экран помощь по командам нажмите "/help"',
        'found':        'Вот, что было найдено:',
        'to_find':      'Укажите слово или часть слова для поиска по заголовкам > ',
        'to_add':       'Заголовок и тело заметки через двойной дефис > ',
        'not_found':    'Ничего не найдено',
        'id_not_found': 'Заметки с указанным id не существует',
        'to_del':       'Укажите id заметки для удаления > ',
        'to_edit':      'Укажите id заметки для изменения > ',
        'to_read':      'Укажите id заметки для чтения > ',
        'added':        'Заметка успешно добавлена!',
        'deleted':      'Заметка успешно удалена!',
        'invalid_id':   'id заметки - это натуральное число!'
      }