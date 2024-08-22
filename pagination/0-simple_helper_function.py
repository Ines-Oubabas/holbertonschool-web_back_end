#!/usr/bin/env python3
"""
Module simple_helper_function
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retourne un tuple contenant le début et la fin de la plage d'indices
    correspondant à la pagination.
    
    :param page: numéro de la page (1-indexé)
    :param page_size: taille de la page (nombre d'éléments par page)
    :return: tuple (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
