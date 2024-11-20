import sys
import os
from PyQt6.QtCore import Qt  # Import dla Align
from PyQt6.QtWidgets import QTextEdit  # Import dla LineWrapMode
from PyQt6.QtGui import QFont
from formatting import toggle_bold, toggle_italic, toggle_underline, change_font_size, set_default_font_size
from formatting import align_text_left, align_text_center, align_text_right, align_text_justify, toggle_wrap_text
from editor_window import MegasolidEditor
import pytest
from editor_window import MegasolidEditor
from constants import FONT_SIZES
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
def test_align_text_left():
    """
    Testuje wyrównanie tekstu do lewej.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    align_text_left(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignLeft

def test_align_text_center():
    """
    Testuje wyrównanie tekstu do środka.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    align_text_center(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignCenter

def test_align_text_right():
    """
    Testuje wyrównanie tekstu do prawej.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    align_text_right(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignRight

def test_align_text_justify():
    """
    Testuje wyrównanie tekstu do lewej i prawej.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    align_text_justify(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignJustify

def test_toggle_wrap_text():
    """
    Testuje włączanie i wyłączanie wrapowania tekstu.
    """
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")

    # Ustawiamy początkowy tryb na NoWrap
    editor.editor.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
    assert editor.editor.lineWrapMode() == QTextEdit.LineWrapMode.NoWrap

    # Włącz wrapowanie
    toggle_wrap_text(editor.editor)
    assert editor.editor.lineWrapMode() == QTextEdit.LineWrapMode.WidgetWidth

    # Wyłącz wrapowanie
    toggle_wrap_text(editor.editor)
    assert editor.editor.lineWrapMode() == QTextEdit.LineWrapMode.NoWrap

def test_align_left_save(tmp_path):
    """
    Testuje wyrównanie do lewej i zapis pliku.
    """
    test_file = tmp_path / "align_left.html"
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")

    # Ustaw wyrównanie do lewej
    align_text_left(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignLeft

    # Zapisz plik
    with open(test_file, "w") as f:
        f.write(editor.editor.toHtml())

    # Sprawdź zapis
    with open(test_file, "r") as f:
        content = f.read()
    # Sprawdzamy style Qt dla wyrównania do lewej
    assert '-qt-block-indent:0' in content and 'text-indent:0px' in content

def test_align_center_save(tmp_path):
    """
    Testuje wyrównanie do środka i zapis pliku.
    """
    test_file = tmp_path / "align_center.html"
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    
    # Ustaw wyrównanie do środka
    align_text_center(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignCenter

    # Zapisz plik
    with open(test_file, "w") as f:
        f.write(editor.editor.toHtml())
    
    # Sprawdź zapis
    with open(test_file, "r") as f:
        content = f.read()
    assert 'align="center"' in content or 'text-align: center' in content

def test_align_right_save(tmp_path):
    """
    Testuje wyrównanie do prawej i zapis pliku.
    """
    test_file = tmp_path / "align_right.html"
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    
    # Ustaw wyrównanie do prawej
    align_text_right(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignRight

    # Zapisz plik
    with open(test_file, "w") as f:
        f.write(editor.editor.toHtml())
    
    # Sprawdź zapis
    with open(test_file, "r") as f:
        content = f.read()
    assert 'align="right"' in content or 'text-align: right' in content

def test_align_justify_save(tmp_path):
    """
    Testuje wyrównanie do lewej i prawej (justyfikacja) i zapis pliku.
    """
    test_file = tmp_path / "align_justify.html"
    editor = MegasolidEditor()
    editor.editor.setPlainText("Test")
    
    # Ustaw wyrównanie do lewej i prawej
    align_text_justify(editor.editor)
    assert editor.editor.alignment() == Qt.AlignmentFlag.AlignJustify

    # Zapisz plik
    with open(test_file, "w") as f:
        f.write(editor.editor.toHtml())
    
    # Sprawdź zapis
    with open(test_file, "r") as f:
        content = f.read()
    assert 'align="justify"' in content or 'text-align: justify' in content
def test_font_sizes_in_combobox(qtbot):
    editor = MegasolidEditor()
    qtbot.addWidget(editor)
    
    combobox_items = [editor.font_size.itemText(i) for i in range(editor.font_size.count())]
    expected_items = [str(size) for size in FONT_SIZES]

    assert combobox_items == expected_items, "ComboBox nie łapie pełnej listy FONT_SIZES!"