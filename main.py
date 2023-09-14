import user_interface as ui
import operations as ops


def main():
    ui.print_help()
    ops.load_notes()
    while ui.still_running(): pass
    print('Работа завершена')

if __name__ == '__main__':
    main()