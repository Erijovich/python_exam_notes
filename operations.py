import os
import json
from datetime import datetime

# временное список для хранения заметок в ОП во время работы с программой
notes = []

# грузим все заметки из файла (если он есть) во временный список
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r', encoding='utf-8') as file:
            notes.extend(json.load(file))

# пробегая по существующим заметкам, берём самый большой номер id. Это нужно, что бы избежать проблем при удалении заметок. Плюс, удобно понимать порядок создания
def get_last_id():
    id = 0
    for note in notes:
        if note['id'] > id:
            id = note['id']
    return id

# новая заметка
def new_note(title, body):
    timestamp = datetime.now().strftime('%d.%m.%Y %H:%M:%S') 
    note = {
        "id": get_last_id() + 1, # следующий после найденного 
        "title": title,
        "body": body,
        "created": timestamp,
        "edited": timestamp,
    }
    notes.append(note)
    save_notes()

# Проверяем существование заданного id
def check_id(possible_id):
    for note in notes:
        if note['id'] == possible_id:
            return True
    return False

def del_note(id):
    for i, note in enumerate(notes): # мда, чёт костыльное удаение получилось...
        if note['id'] == id:
            del notes[i]
            break 
    save_notes()

def save_notes():
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file)

def find_notes(string_to_find: str):
    # тут же можно в генератор всё засунуть, не?? что-то эта строчка не работает 
    # TODO разобраться, как её поправить!
    # all_titles = [title for title in notes['title']]
    all_titles = [] 
    for note in notes:
        all_titles.append(note['title'])
    return [index for index, title in enumerate(all_titles) if string_to_find.lower() in title.lower()]

def print_titles(indexes):
    for i in range(len(notes)):
        if i in indexes: # тож немного быдлокодом попахивает
            print(f"id: {notes[i]['id']}. Created at {notes[i]['created']}. Edited at {notes[i]['edited']}\nTitle: {notes[i]['title']}")

def read_note(id):
    # интересно было через генератор попробовать. Не уверен, что так читабельнее стало
    # return [note['body'] for note in notes if note['id'] == id][0]
    for note in notes:
        if note['id'] == id:
            return f"id: {note['id']}. Created at {note['created']}. Edited at {note['edited']}\nTitle: {note['title']}\n{note['body']}"
    return None

def edit_note(id):
    for i, note in enumerate(notes): # мда, чёт костыльное удаение получилось...
        if note['id'] == id:
            print(f"id: {notes[i]['id']}. Created at {notes[i]['created']}. Edited at {notes[i]['edited']}\nTitle: {notes[i]['title']}\n{notes[i]['body']}\n")
            note_title = input('Введите новый заголовок заметки, пустой ввод - оставить без изменения > ')
            note_body = input('Введите новый текст заметки, пустой ввод - оставить без изменения > ')
            flag = False
            if note_title.strip():
                notes[i]['title'] = note_title
                flag = True
            if note_body.strip():
                notes[i]['body'] = note_body
                flag = True
            if flag:
                notes[i]['edited'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                save_notes()
                print('Заметка успешно изменена')
            else:
                print('Заметка осталась без изменений')
            break 