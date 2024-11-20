import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication
from editor_window import MegasolidEditor

app = QApplication([])  # Musimy stworzyć aplikację dla PyQt

def test_file_open(tmp_path):
    """
    Testuje otwieranie pliku i sprawdza, czy tekst jest poprawnie wczytany.
    """
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, Mordeczko!")

    editor = MegasolidEditor()
    editor.path = str(test_file)  # Ustawiamy ścieżkę bez dialogu
    with open(editor.path, "r") as f:
        editor.editor.setPlainText(f.read())  # Wczytujemy tekst do edytora

    assert editor.editor.toPlainText() == "Hello, Mordeczko!"

def test_file_save(tmp_path):
    """
    Testuje zapisywanie pliku i sprawdza, czy tekst jest poprawnie zapisany.
    """
    test_file = tmp_path / "test_save.txt"

    editor = MegasolidEditor()
    editor.editor.setPlainText("Save me, Mordeczko!")
    editor.path = str(test_file)  # Ustawiamy ścieżkę bez dialogu
    with open(editor.path, "w") as f:
        f.write(editor.editor.toPlainText())  # Zapisujemy tekst z edytora

    assert test_file.read_text() == "Save me, Mordeczko!"
