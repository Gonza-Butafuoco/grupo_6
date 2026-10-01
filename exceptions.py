"""Excepciones de dominio para las reglas de ElPlagio."""


class EmptyTextError(Exception):
    """Se intenta guardar o procesar un texto vacío."""


class TextLimitError(Exception):
    """Se intenta guardar más textos de los admitidos."""


class NotEnoughTextsError(Exception):
    """No hay dos textos disponibles para comparar."""


class TextNotFoundError(Exception):
    """Se intenta eliminar un texto que no fue cargado."""
