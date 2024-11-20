import uuid
import os

def hex_uuid():
    """
    Generuje unikalny identyfikator w formacie szesnastkowym (UUID).
    """
    return uuid.uuid4().hex


def splitext(filename):
    """
    Rozdziela nazwę pliku na nazwę bazową i rozszerzenie.
    """
    base, ext = os.path.splitext(filename)
    return base, ext
