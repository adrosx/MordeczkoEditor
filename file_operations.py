from PyQt6.QtWidgets import QFileDialog
from helpers import hex_uuid, splitext

from helpers import hex_uuid, splitext

def open_file(editor):
    # Otwieramy dialog wyboru pliku
    path, _ = QFileDialog.getOpenFileName(editor, "Open file", "", "Text Files (*.txt);;All Files (*.*)")

    if not path:
        return

    ext = splitext(path)  # Wyciągamy rozszerzenie
    if ext != ".txt":
        editor.dialog_critical("Unsupported file format!")  # Prosta walidacja formatu
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            editor.editor.setText(f.read())
        editor.path = path
        editor.update_title()
    except Exception as e:
        editor.dialog_critical(f"Error opening file: {e}")

def save_file(editor):
    """
    Zapisuje aktualny plik (jeśli plik już istnieje).
    """
    if not editor.path:
        return save_file_as(editor)  # Jeśli brak ścieżki, używamy "Save As"

    try:
        with open(editor.path, "w", encoding="utf-8") as f:
            f.write(editor.editor.toPlainText())
    except Exception as e:
        editor.dialog_critical(f"Error saving file: {e}")

def save_file_as(editor):
    # Otwieramy dialog zapisu pliku
    path, _ = QFileDialog.getSaveFileName(editor, "Save file", f"file_{hex_uuid()}.txt", "Text Files (*.txt);;All Files (*.*)")

    if not path:
        return

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(editor.editor.toPlainText())
        editor.path = path
        editor.update_title()
    except Exception as e:
        editor.dialog_critical(f"Error saving file: {e}")
