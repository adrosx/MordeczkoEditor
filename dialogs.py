from PyQt6.QtWidgets import QMessageBox, QFileDialog

def dialog_critical(editor, message):
    """
    Wyświetla krytyczny komunikat w oknie dialogowym.
    """
    dlg = QMessageBox(editor)
    dlg.setText(message)
    dlg.setIcon(QMessageBox.Icon.Critical)
    dlg.show()

def open_file_dialog(editor):
    """
    Dialog do wyboru pliku do otwarcia.
    """
    path, _ = QFileDialog.getOpenFileName(editor, "Open file", "", "Text Files (*.txt);;All Files (*.*)")
    return path

def save_file_dialog(editor):
    """
    Dialog do wyboru pliku do zapisania.
    """
    path, _ = QFileDialog.getSaveFileName(editor, "Save file", "file.txt", "Text Files (*.txt);;All Files (*.*)")
    return path
