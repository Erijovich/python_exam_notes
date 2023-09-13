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


def del_note(id: int):
    for i, note in enumerate(notes): # мда, чёт костыльное удаение получилось...
        if note['id'] == id:
            del notes[i]
            break 
    save_notes()

def save_notes():
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file)

