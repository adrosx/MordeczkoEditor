from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMenuBar, QToolBar, QComboBox, QTextEdit
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from file_operations import open_file, save_file, save_file_as, open_txt_file
from helpers import splitext, convert_doc_to_txt, notify_user_about_conversion
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
        self.editor = None
        self.path = None
        self.cursor_position = None

        # Rozmiar czcionki
        self.font_size = QComboBox()
        self.font_size.addItems([str(size) for size in FONT_SIZES])
        self.font_size.setFixedWidth(100)
        self.font_size.currentIndexChanged.connect(
            lambda: change_font_size(self.editor, int(self.font_size.currentText()))
        )

        # Ustawienia UI
        self.reset()

    def reset(self):
        """
        Resetuje okno edytora do początkowego stanu.
        """
        # Usuń istniejące toolbary, jeśli są zdublowane
        for toolbar in self.findChildren(QToolBar):
            self.removeToolBar(toolbar)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("MordeczkoEditor")

        # Layout główny
        layout = QVBoxLayout()
        self.editor = QTextEdit()  # Poprawione: użycie QTextEdit zamiast QWidget
        layout.addWidget(self.editor)

        # Widget kontenera
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Toolbar formatowania
        format_toolbar = QToolBar("Formatowanie")
        self.addToolBar(format_toolbar)

        # Akcje Toolbaru
        self.add_toolbar_actions(format_toolbar)

        # Menu bar
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("File")

        # Opcja "Open"
        file_menu.addAction(self.create_action("Open", self.file_open))

        # Opcja "Save"
        file_menu.addAction(self.create_action("Save", self.file_save))

        # Opcja "Save As"
        file_menu.addAction(self.create_action("Save As", self.file_save_as))

        # Dodajemy pasek menu
        self.setMenuBar(menu_bar)

    def add_toolbar_actions(self, toolbar):
        """
        Dodaje akcje do toolbaru.
        """
        bold_action = QAction("Bold", self)
        bold_action.setCheckable(True)
        bold_action.triggered.connect(lambda: toggle_bold(self.editor))
        toolbar.addAction(bold_action)

        italic_action = QAction("Italic", self)
        italic_action.setCheckable(True)
        italic_action.triggered.connect(lambda: toggle_italic(self.editor))
        toolbar.addAction(italic_action)

        underline_action = QAction("Underline", self)
        underline_action.setCheckable(True)
        underline_action.triggered.connect(lambda: toggle_underline(self.editor))
        toolbar.addAction(underline_action)

        # ComboBox do zmiany rozmiaru czcionki
        toolbar.addWidget(self.font_size)

        align_left_action = QAction("Left", self)
        align_left_action.triggered.connect(lambda: align_text_left(self.editor))
        toolbar.addAction(align_left_action)

        align_center_action = QAction("Center", self)
        align_center_action.triggered.connect(lambda: align_text_center(self.editor))
        toolbar.addAction(align_center_action)

        align_right_action = QAction("Right", self)
        align_right_action.triggered.connect(lambda: align_text_right(self.editor))
        toolbar.addAction(align_right_action)

        align_justify_action = QAction("Justify", self)
        align_justify_action.triggered.connect(lambda: align_text_justify(self.editor))
        toolbar.addAction(align_justify_action)

        wrap_action = QAction("Wrap Text", self)
        wrap_action.triggered.connect(lambda: toggle_wrap_text(self.editor))
        toolbar.addAction(wrap_action)

    def create_action(self, name, callback):
        """
        Tworzy akcję dla menu lub toolbara.
        """
        action = QAction(name, self)
        action.triggered.connect(callback)
        return action

    def update_title(self):
        """
        Aktualizuje tytuł okna na podstawie bieżącej ścieżki pliku.
        """
        self.setWindowTitle(f"MordeczkoEditor - {self.path}" if self.path else "MordeczkoEditor - Nowy plik")

    def file_open(self):
        """
        Obsługuje otwieranie plików z obsługą konwersji DOC do TXT.
        """
        print("[DEBUG] Otwieranie pliku...")
        path = open_file(self)
        if not path:
            return

        ext = splitext(path)[1].lower()
        if ext in [".docx", ".doc"]:
            notify_user_about_conversion()
            converted_path = convert_doc_to_txt(path)
            if converted_path:
                print(f"[DEBUG] Plik skonwertowany: {converted_path}")
                open_txt_file(self, converted_path)
            else:
                print("[ERROR] Konwersja się wykrzaczyła!")
        elif ext == ".txt":
            open_txt_file(self, path)
        else:
            QMessageBox.critical(self, "Błąd", "Unsupported file format!")

    def file_save(self):
        """
        Obsługuje zapis pliku.
        """
        save_file(self)

    def file_save_as(self):
        """
        Obsługuje zapis pliku pod nową nazwą.
        """
        save_file_as(self)

    def file_print(self):
        """
        Wywołuje okno dialogowe drukowania.
        """
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.editor.print(printer)
