from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMenuBar, QToolBar, QComboBox
from PyQt6.QtGui import QAction, QFont, QTextCursor
from PyQt6.QtCore import Qt
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from file_operations import open_file, save_file, save_file_as
from text_edit import TextEdit
from constants import FONT_SIZES
from formatting import (
    toggle_bold, toggle_italic, toggle_underline,
    change_font_size, set_default_font_size,
    align_text_left, align_text_center,
    align_text_right, align_text_justify,
    toggle_wrap_text
)

class MegasolidEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = TextEdit()
        self.path = None
        self.cursor_position = None  # Inicjalizacja miejsca na pozycję kursora

        # Rozmiar czcionki
        self.font_size = QComboBox()
        self.font_size.addItems([str(size) for size in FONT_SIZES])
        self.font_size.setFixedWidth(100)
        self.font_size.currentIndexChanged.connect(
            lambda: change_font_size(self.editor, int(self.font_size.currentText()))
        )

    def update_title(self):
        """
        Aktualizuje tytuł okna na podstawie bieżącej ścieżki pliku.
        """
        self.setWindowTitle(f"MordeczkoEditor - {self.path}" if self.path else "MordeczkoEditor - Nowy plik")

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

        # ComboBox do zmiany rozmiaru czcionki
        format_toolbar.addWidget(self.font_size)

        # Menu bar
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("File")

        # Opcja "Open"
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.file_open)
        file_menu.addAction(open_action)

        # Opcja "Save"
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.file_save)
        file_menu.addAction(save_action)

        # Opcja "Save As"
        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self.file_save_as)
        file_menu.addAction(save_as_action)

        # Opcja "Print"
        print_action = QAction("Print", self)
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)

        # Dodajemy pasek menu
        self.setMenuBar(menu_bar)

        # Dodajemy toolbar justowania
        align_left_action = QAction("Left", self)
        align_left_action.triggered.connect(lambda: align_text_left(self.editor))
        format_toolbar.addAction(align_left_action)

        align_center_action = QAction("Center", self)
        align_center_action.triggered.connect(lambda: align_text_center(self.editor))
        format_toolbar.addAction(align_center_action)

        align_right_action = QAction("Right", self)
        align_right_action.triggered.connect(lambda: align_text_right(self.editor))
        format_toolbar.addAction(align_right_action)

        align_justify_action = QAction("Justify", self)
        align_justify_action.triggered.connect(lambda: align_text_justify(self.editor))
        format_toolbar.addAction(align_justify_action)

        # Wrapowanie tekstu
        wrap_action = QAction("Wrap Text", self)
        wrap_action.triggered.connect(lambda: toggle_wrap_text(self.editor))
        format_toolbar.addAction(wrap_action)

    def file_print(self):
        """
        Wywołuje okno dialogowe drukowania.
        """
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.editor.print(printer)

    def file_open(self):
        from file_operations import open_file  # Import wewnątrz metody
        open_file(self)

    def file_save(self):
        from file_operations import save_file  # Import wewnątrz metody
        save_file(self)

    def file_save_as(self):
        from file_operations import save_file_as  # Import wewnątrz metody
        save_file_as(self)

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
