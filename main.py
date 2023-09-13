import user_interface as ui
import operations as ops


def main():
    # str = "   /add some note --    will be here"
    # parse1 = str.lstrip().split(" ",1)
    # print(parse1)
    # if parse1[0].strip().lower()[0] == "/":
    #     print(parse1[0][1:])

    
    ui.print_help()
    ops.load_notes()
    while ui.still_running(): pass
    print('Работа завершена')

if __name__ == '__main__':
    main()


# удаляя 4й мы удаляем 5й
# /new -- 
# это ошибка вылет нахуй