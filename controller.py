import operations as ops
import user_interface as ui
import parserer as prs


def choose_action(action, user_input):
    match action:
        case '/new':
            if user_input != '':
                 title, body = prs.parser_to_add(user_input)
            else:
                 title, body = prs.parser_to_add(input('Заголовок и тело заметки через двойной дефис > '))
            ops.new_note(title, body)
            print(msg['added'])
        case '/find': 
           pass
        case '/read': 
            pass
        case '/edit':
            pass
        case '/del':
            # id_to_del = 0
            if user_input != '':
                id_to_del = prs.parser_id(user_input)
            else:
                id_to_del = prs.parser_id(input(msg['to_del']))

            if id_to_del: # если парсер не вернул False
                if ops.check_id(id_to_del): # проверка, есть ли указанный id в списке
                    ops.del_note(id_to_del)
                    print(msg['deleted'])
                else:
                    print(msg['id_not_found'])
            else:
                print('id заметки - это натуральное число!')
        case '/help':
            ui.print_help()
        case '/stop': # возврат в основное, есл можно так сказать, меню
            return True
        case '/exit':
            return False # Сохранение и выход
        case _:
            print(msg['error'])
    return True




msg = {
        'error':        'Invalid command! Что бы вывести на экран помощь по командам нажмите "/help"',
        'found':        'Вот, что было найдено:',
        'to_find':      'Укажите слово или часть слова для поиска по заголовкам > ',
        'not_found':    'Ничего не найдено',
        'id_not_found': 'Заметки с указанным id не существует',
        'to_del':       'Укажите id заметки для удаления > ',
        'to_change':    'Укажите id заметки для изменения > ',
        'added':        'Заметка успешно добавлена!',
        'deleted':      'Заметка успешно удалена!'
      }
