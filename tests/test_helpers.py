from helpers import hex_uuid

def test_hex_uuid():
    """
    Testuje, czy funkcja hex_uuid generuje unikalny identyfikator w formacie szesnastkowym.
    """
    uuid1 = hex_uuid()
    uuid2 = hex_uuid()

    # Sprawdzamy, czy UUID ma długość 32 znaków
    assert len(uuid1) == 32
    assert len(uuid2) == 32

    # Sprawdzamy, czy UUID są unikalne
    assert uuid1 != uuid2

    # Sprawdzamy, czy UUID zawiera tylko znaki szesnastkowe
    assert all(c in "0123456789abcdef" for c in uuid1)
    assert all(c in "0123456789abcdef" for c in uuid2)
from helpers import splitext

def test_splitext():
    """
    Testuje funkcję splitext, która rozdziela nazwę pliku na nazwę bazową i rozszerzenie.
    """
    # Przykładowe pliki
    file1 = "example.txt"
    file2 = "archive.tar.gz"
    file3 = "no_extension"

    # Sprawdzamy poprawność rozdzielania
    assert splitext(file1) == ("example", ".txt")
    assert splitext(file2) == ("archive.tar", ".gz")
    assert splitext(file3) == ("no_extension", "")
