from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMenuBar, QToolBar, QComboBox
from PyQt6.QtGui import QAction, QFont, QTextCursor, QTextCharFormat
from PyQt6.QtCore import Qt
from file_operations import open_file, save_file, save_file_as
from text_edit import TextEdit
from helpers import hex_uuid, splitext
from formatting import toggle_bold, toggle_italic, toggle_underline, change_font_size, set_default_font_size

class MegasolidEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = TextEdit()
        self.path = None
        self.cursor_position = None  # Inicjalizacja miejsca na pozycję kursora

        # Rozmiar czcionki - zdefiniowane tutaj
        self.font_size = QComboBox()
        self.font_size.addItems([str(s) for s in [8, 10, 12, 14, 16, 18, 20, 24]])
        self.font_size.setFixedWidth(100)
        self.font_size.currentIndexChanged.connect(
            lambda: change_font_size(self.editor, int(self.font_size.currentText()))
)

    # Funkcje obsługi plików
    def file_open(self):
        open_file(self)

    def file_save(self):
        save_file(self)

    def file_save_as(self):
        save_file_as(self)

    def update_title(self):
        """
        Aktualizuje tytuł okna na podstawie aktualnej ścieżki do pliku.
        """
        self.setWindowTitle(f"{self.path if self.path else 'Untitled'} - MordeczkoEditor")

    def dialog_critical(self, message):
        """
        Wyświetla krytyczny komunikat w oknie dialogowym.
        """
        from PyQt6.QtWidgets import QMessageBox
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.show()

    def reset(self):
        """
        Resetuje okno edytora do początkowego stanu.
        """
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("MordeczkoEditor")

        # Layout główny
        layout = QVBoxLayout()
        layout.addWidget(self.editor)

        # Widget kontenera
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Toolbar formatowania
        format_toolbar = QToolBar("Formatowanie")
        self.addToolBar(format_toolbar)

        # Bold
        bold_action = QAction("Bold", self)
        bold_action.setCheckable(True)
        bold_action.triggered.connect(lambda: toggle_bold(self.editor))
        format_toolbar.addAction(bold_action)

        # Italic
        italic_action = QAction("Italic", self)
        italic_action.setCheckable(True)
        italic_action.triggered.connect(lambda: toggle_italic(self.editor))
        format_toolbar.addAction(italic_action)

        # Underline
        underline_action = QAction("Underline", self)
        underline_action.setCheckable(True)
        underline_action.triggered.connect(lambda: toggle_underline(self.editor))
        format_toolbar.addAction(underline_action)

        # Dodajemy ComboBox do zmiany rozmiaru czcionki
        format_toolbar.addWidget(self.font_size)

    def save_cursor_position(self):
        """
        Zapisuje aktualną pozycję kursora.
        """
        self.cursor_position = self.editor.textCursor()

    def restore_cursor_position(self):
        """
        Przywraca pozycję kursora.
        """
        if self.cursor_position:
            self.editor.setFocus()
            self.editor.setTextCursor(self.cursor_position)