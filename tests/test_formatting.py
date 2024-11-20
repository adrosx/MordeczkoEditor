import sys
import os
from PyQt6.QtGui import QFont
from formatting import toggle_bold
from editor_window import MegasolidEditor
from formatting import toggle_bold, toggle_italic, toggle_underline, change_font_size, set_default_font_size

# Dodajemy folder główny projektu do PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from editor_window import MegasolidEditor  # Importujemy główną klasę

def test_toggle_bold():
    """
    Testuje funkcję pogrubienia w edytorze.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")

    # Zaznaczamy tekst
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    editor.editor.setTextCursor(cursor)

    # Wywołujemy funkcję pogrubienia
    toggle_bold(editor.editor)

    # Pobieramy formatowanie z kursora
    fmt = editor.editor.textCursor().charFormat()
    assert fmt.fontWeight() == QFont.Weight.Bold

from formatting import toggle_italic
from editor_window import MegasolidEditor

def test_toggle_italic():
    """
    Testuje funkcję kursywy w edytorze.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")

    # Zaznaczamy tekst
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    editor.editor.setTextCursor(cursor)

    # Wywołujemy funkcję kursywy
    toggle_italic(editor.editor)

    # Pobieramy formatowanie z kursora
    fmt = editor.editor.textCursor().charFormat()
    assert fmt.fontItalic() is True

from formatting import change_font_size
from editor_window import MegasolidEditor

def test_change_font_size():
    """
    Testuje funkcję zmiany rozmiaru czcionki.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Hello, Mordeczko!")

    # Zaznaczamy tekst
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    editor.editor.setTextCursor(cursor)

    # Zmieniamy rozmiar czcionki
    new_size = 16
    change_font_size(editor.editor, new_size)

    # Sprawdzamy rozmiar czcionki w zaznaczeniu
    fmt = editor.editor.textCursor().charFormat()
    assert fmt.fontPointSize() == new_size


def test_open_bold_save(tmp_path):
    """
    Otwiera plik, ustawia bold, zapisuje i sprawdza zapis.
    """
    test_file = tmp_path / "test_bold.txt"
    test_file.write_text("Hello, Mordeczko!")  # Przygotowanie pliku

    editor = MegasolidEditor()
    editor.path = str(test_file)

    # Otwórz plik
    with open(editor.path, "r") as f:
        editor.editor.setPlainText(f.read())

    # Zaznaczamy tekst
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    editor.editor.setTextCursor(cursor)

    # Wywołujemy pogrubienie
    toggle_bold(editor.editor)
    # Sprawdzamy formatowanie
    fmt = editor.editor.textCursor().charFormat()
    assert fmt.fontWeight() == QFont.Weight.Bold

    # Zapisz
    with open(editor.path, "w") as f:
        f.write(editor.editor.toHtml())

    # Sprawdź zapis – szukamy stylu CSS dla bold
    assert 'font-weight' in test_file.read_text()

def test_open_underline_save(tmp_path):
    """
    Otwiera plik, ustawia underline, zapisuje i sprawdza zapis.
    """
    test_file = tmp_path / "test_underline.txt"
    test_file.write_text("Hello, Mordeczko!")  # Przygotowanie pliku

    editor = MegasolidEditor()
    editor.path = str(test_file)

    # Otwórz plik
    with open(editor.path, "r") as f:
        editor.editor.setPlainText(f.read())

    # Zaznaczamy cały tekst
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    editor.editor.setTextCursor(cursor)

    # Ustaw underline
    toggle_underline(editor.editor)
    # Sprawdź podkreślenie w charFormat
    fmt = editor.editor.textCursor().charFormat()
    assert fmt.fontUnderline() is True  # Sprawdzamy podkreślenie

    # Zapisz
    with open(editor.path, "w") as f:
        f.write(editor.editor.toHtml())

    # Debug: wypisz zawartość pliku HTML
    print(f"\nDEBUG: HTML content for underline test:\n{test_file.read_text()}")

    # Sprawdź zapis
    assert "text-decoration: underline" in test_file.read_text()

def test_open_italic_save(tmp_path):
    """
    Otwiera plik, ustawia kursywę, zapisuje i sprawdza zapis.
    """
    test_file = tmp_path / "test_italic.txt"
    test_file.write_text("Hello, Mordeczko!")  # Przygotowanie pliku

    editor = MegasolidEditor()
    editor.path = str(test_file)

    # Otwórz plik
    with open(editor.path, "r") as f:
        editor.editor.setPlainText(f.read())

    # Ustaw italic
        toggle_italic(editor.editor)
        assert editor.editor.fontItalic() is True

    # Zapisz
    with open(editor.path, "w") as f:
        f.write(editor.editor.toHtml())

    # Debug: wypisz zawartość pliku HTML
    print(f"\nDEBUG: HTML content for italic test:\n{test_file.read_text()}")

    # Sprawdź zapis – szukamy stylu CSS dla italic
    assert 'font-style' in test_file.read_text()

def test_change_font_size():
    """
    Testuje funkcję zmiany rozmiaru czcionki.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Hello, Mordeczko!")  # Przygotowanie tekstu

    # Zaznaczamy tekst
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    editor.editor.setTextCursor(cursor)

    # Zmieniamy rozmiar czcionki
    new_size = 16
    change_font_size(editor.editor, new_size)

    # Sprawdzamy rozmiar czcionki w zaznaczeniu
    fmt = editor.editor.textCursor().charFormat()
    assert fmt.fontPointSize() == new_size

def test_set_default_font_size():
    """
    Testuje ustawianie domyślnego rozmiaru czcionki.
    """
    editor = MegasolidEditor()
    new_size = 18
    set_default_font_size(editor.editor, new_size)

    # Wstawiamy nowy tekst i sprawdzamy, czy ma domyślny rozmiar czcionki
    editor.editor.insertPlainText("Nowy tekst")
    cursor = editor.editor.textCursor()
    cursor.select(cursor.SelectionType.Document)
    fmt = cursor.charFormat()
    assert fmt.fontPointSize() == new_size

def test_cursor_restoration():
    """
    Testuje przywracanie pozycji kursora po zamknięciu listy rozmiarów.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Hello, Mordeczko!")

    # Ustawiamy kursor w środku tekstu
    cursor = editor.editor.textCursor()
    cursor.setPosition(6)  # Po "Hello,"
    editor.editor.setTextCursor(cursor)

    # Symulujemy zapisanie pozycji kursora
    editor.save_cursor_position()

    # Symulujemy zamknięcie listy rozmiarów
    editor.restore_cursor_position()

    # Sprawdzamy, czy kursor wrócił na swoje miejsce
    restored_cursor = editor.editor.textCursor()
    assert restored_cursor.position() == 6
