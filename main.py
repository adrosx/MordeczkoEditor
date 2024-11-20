#main.py
from PyQt6.QtWidgets import QApplication
from editor_window import MegasolidEditor
import sys
import os

sys.path.append(os.path.dirname(__file__))  # Dodaje folder główny projektu
if __name__ == "__main__":
    print("Tworzenie aplikacji...")
    app = QApplication(sys.argv)
    app.setApplicationName("MordeczkoEditor")
    print("Aplikacja utworzona.")

    print("Tworzenie okna...")
    window = MegasolidEditor()
    print("Okno utworzone.")

    print("Resetowanie okna...")
    window.reset()
    print("Okno zresetowane.")

    print("Wyświetlanie okna...")
    window.show()
    print("Okno wyświetlone.")

    print("Uruchamianie aplikacji...")
    app.exec()
    print("Aplikacja zakończyła działanie.")
