from PyQt6.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt6.QtGui import QTextCursor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTextEdit

def toggle_bold(editor):
    """
    Przełącza pogrubienie na zaznaczonym tekście oraz ustawia dla nowego tekstu.
    """
    cursor = editor.textCursor()
    fmt = QTextCharFormat()
    is_bold = not cursor.charFormat().fontWeight() == QFont.Weight.Bold
    fmt.setFontWeight(QFont.Weight.Bold if is_bold else QFont.Weight.Normal)
    cursor.mergeCharFormat(fmt)  # Zmiana dla zaznaczonego tekstu

    # Ustawienie domyślnego formatu dla nowego tekstu
    editor.setCurrentCharFormat(fmt)

def toggle_italic(editor):
    """
    Przełącza kursywę na zaznaczonym tekście oraz ustawia dla nowego tekstu.
    """
    cursor = editor.textCursor()
    fmt = QTextCharFormat()
    is_italic = not cursor.charFormat().fontItalic()
    fmt.setFontItalic(is_italic)
    cursor.mergeCharFormat(fmt)
    editor.setCurrentCharFormat(fmt)  # Domyślny format

def toggle_underline(editor):
    """
    Przełącza podkreślenie na zaznaczonym tekście oraz ustawia dla nowego tekstu.
    """
    cursor = editor.textCursor()
    fmt = QTextCharFormat()
    is_underlined = not cursor.charFormat().fontUnderline()
    fmt.setFontUnderline(is_underlined)
    cursor.mergeCharFormat(fmt)
    editor.setCurrentCharFormat(fmt)  # Domyślny format

def change_font_size(editor, size):
    """
    Zmienia rozmiar czcionki na zaznaczonym tekście oraz ustawia dla nowego tekstu.
    """
    print(f"[DEBUG] Zmieniamy rozmiar czcionki na: {size}")  # Log rozmiaru

    cursor = editor.textCursor()
    fmt = QTextCharFormat()
    fmt.setFontPointSize(size)

    if cursor.hasSelection():
        print("[DEBUG] Zaznaczony tekst, zmieniamy rozmiar dla zaznaczenia.")
        cursor.mergeCharFormat(fmt)
    else:
        print("[DEBUG] Brak zaznaczenia, ustawiamy domyślny format.")
        editor.setCurrentCharFormat(fmt)

    print("[DEBUG] Zmiana rozmiaru czcionki zakończona.")

def set_default_font_size(editor, size):
    """
    Ustawia domyślny rozmiar czcionki w edytorze.
    """
    fmt = editor.currentCharFormat()
    fmt.setFontPointSize(size)
    editor.setCurrentCharFormat(fmt)

def align_text_left(editor):
    editor.setAlignment(Qt.AlignmentFlag.AlignLeft)

def align_text_center(editor):
    editor.setAlignment(Qt.AlignmentFlag.AlignCenter)

def align_text_right(editor):
    editor.setAlignment(Qt.AlignmentFlag.AlignRight)

def align_text_justify(editor):
    editor.setAlignment(Qt.AlignmentFlag.AlignJustify)

def toggle_wrap_text(editor):
    if editor.lineWrapMode() == QTextEdit.LineWrapMode.NoWrap:
        editor.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
    else:
        editor.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)