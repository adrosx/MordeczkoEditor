import os
import pypandoc
from PyQt6.QtWidgets import QMessageBox

def splitext(filename):
    """
    Rozdziela nazwę pliku na nazwę bazową i rozszerzenie.
    """
    base, ext = os.path.splitext(filename)
    return base, ext

def download_pandoc():
    """
    Pobiera Pandoc, jeśli jeszcze nie jest zainstalowany.
    """
    try:
        pypandoc.download_pandoc()
        print("[DEBUG] Pandoc został pobrany pomyślnie.")
    except Exception as e:
        print(f"[ERROR] Błąd przy pobieraniu Pandoca: {e}")

def convert_doc_to_txt(doc_path):
    """
    Konwertuje plik DOC lub DOCX na TXT.
    """
    try:
        download_pandoc()

        if not doc_path.lower().endswith(('.doc', '.docx')):
            raise ValueError("Supported formats are DOC and DOCX only.")

        output_path = os.path.splitext(doc_path)[0] + '.txt'
        pypandoc.convert_file(doc_path, 'plain', format='docx', outputfile=output_path)
        return output_path
    except Exception as e:
        print(f"[ERROR] Błąd konwersji: {e}")
        return None

def notify_user_about_conversion():
    """
    Wyświetla komunikat informujący o konwersji do formatu TXT.
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText("Plik musi zostać przekonwertowany na TXT. Wszelkie formatowanie i obrazy zostaną usunięte.")
    msg.setWindowTitle("Konwersja na TXT")
    msg.exec()
