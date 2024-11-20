#text_edit.py
from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QFont, QColor


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def toggle_bold(self):
        """
        Przełącza pogrubienie na zaznaczonym tekście.
        """
        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Weight.Bold if not cursor.charFormat().fontWeight() == QFont.Weight.Bold else QFont.Weight.Normal)
        cursor.mergeCharFormat(fmt)

    def toggle_italic(self):
        """
        Przełącza kursywę na zaznaczonym tekście.
        """
        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontItalic(not cursor.charFormat().fontItalic())
        cursor.mergeCharFormat(fmt)

    def toggle_underline(self):
        """
        Przełącza podkreślenie na zaznaczonym tekście.
        """
        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontUnderline(not cursor.charFormat().fontUnderline())
        cursor.mergeCharFormat(fmt)

    def change_font_size(self, size: int):
        """
        Zmienia rozmiar czcionki na zaznaczonym tekście.
        """
        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontPointSize(size)
        cursor.mergeCharFormat(fmt)

    def change_text_color(self, color: QColor):
        """
        Zmienia kolor tekstu na zaznaczonym obszarze.
        """
        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setForeground(color)
        cursor.mergeCharFormat(fmt)
