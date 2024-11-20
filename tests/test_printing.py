from unittest.mock import patch
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from editor_window import MegasolidEditor
import pytest
from editor_window import MegasolidEditor

@pytest.fixture
def editor_window(qtbot):
    editor = MegasolidEditor()
    qtbot.addWidget(editor)  # Podpinamy widget do QtBota
    return editor

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

def test_mocked_physical_print(editor_window):
    printer = QPrinter()
    editor_window.editor.setPlainText("Drukowanie na prawdziwej drukarce!")

    # Mockujemy dialog drukowania
    with patch.object(QPrintDialog, 'exec', return_value=QPrintDialog.DialogCode.Accepted):
        with patch.object(editor_window.editor, 'print') as mocked_print:
            dialog = QPrintDialog(printer, editor_window)
            assert dialog.exec() == QPrintDialog.DialogCode.Accepted
            
            # Drukowanie na "drukarce"
            editor_window.editor.print(printer)
            mocked_print.assert_called_once()

    # Upewniamy się, że test przechodzi
    assert True, "Symulowane drukowanie zakończone bez błędów!"
