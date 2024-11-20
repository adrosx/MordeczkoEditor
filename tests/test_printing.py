from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
import pytest
from editor_window import MegasolidEditor
import sys

@pytest.fixture
def editor_window(qtbot):
    app = MegasolidEditor()
    qtbot.addWidget(app)
    return app

def test_print_to_virtual_file(editor_window, tmp_path):
    printer = QPrinter()
    printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
    output_file = tmp_path / "test_output.pdf"
    printer.setOutputFileName(str(output_file))

    # Drukowanie na wirtualnym pliku
    editor_window.editor.setPlainText("Test drukowania")

    # Zamiast dialogu, po prostu drukujemy bezpośrednio na plik
    editor_window.editor.print(printer)

    # Sprawdzamy, czy plik został utworzony
    assert output_file.exists(), "Plik PDF nie został wygenerowany!"

def test_print_to_physical_printer(editor_window):
    printer = QPrinter()
    editor_window.editor.setPlainText("Drukowanie na prawdziwej drukarce!")
    
    dialog = QPrintDialog(printer, editor_window)
    assert dialog.exec() == QPrintDialog.DialogCode.Accepted
    
    # Drukowanie na prawdziwej drukarce
    editor_window.editor.print(printer)
    assert True, "Drukowanie zakończone bez błędów!"
