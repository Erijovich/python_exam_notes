def still_running():
    operation = input(msg['next_input']).strip().lower()
    while operation not in (oper_list):
        print(msg['error'])
        operation = input(msg['next_input']).strip().lower()
    # return controller.choose_action(operation) # choose action возвращает только тру или фолс

def print_help():
    print()
    print(msg['help'])
    for i in oper_list:
        print(f'   {i} - {oper_list[i]}')
    print()



# список доступных команд
oper_list = {
            '/add': 'Добавить новую заметку',
            '/save': 'Сохранить заметку',
            '/redo': 'Отменить ввод последней строки',
            '/clear': 'Отчистить текущую заметку',
            '/find': 'Найти заметку',
            '/read': 'Прочитать заметку',
            '/del': 'Удалить заметку',
            '/edit': 'Изменить заметку',
            '/help': 'Вывести на экран помощь по командам',
            '/end': 'Закончить работу и выйти из программы',
            }

# некоторые вспомогательные сообщения 
msg = {
        'next_input':   '> ',
        'error':        'Команда - инвалид! Что бы вывести на экран помощь по командам введите /help',
        'help':         'Список доступных команд:'
      }   

