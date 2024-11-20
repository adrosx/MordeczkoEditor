# file_operations.py
from constants import SUPPORTED_EXTENSIONS
from dialogs import dialog_critical, open_file_dialog, save_file_dialog
from helpers import splitext

def open_file(editor):
    path = open_file_dialog(editor)
    if not path:
        return

    ext = splitext(path)  # Wyciągamy rozszerzenie
    if ext not in SUPPORTED_EXTENSIONS:
        dialog_critical(editor, "Unsupported file format!")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            editor.editor.setText(f.read())
        editor.path = path
        editor.update_title()
    except Exception as e:
        dialog_critical(editor, f"Error opening file: {e}")

def save_file(editor):
    if not editor.path:
        return save_file_as(editor)

    try:
        with open(editor.path, "w", encoding="utf-8") as f:
            f.write(editor.editor.toPlainText())
    except Exception as e:
        dialog_critical(editor, f"Error saving file: {e}")

def save_file_as(editor):
    path = save_file_dialog(editor)
    if not path:
        return

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(editor.editor.toPlainText())
        editor.path = path
        editor.update_title()
    except Exception as e:
        dialog_critical(editor, f"Error saving file: {e}")
