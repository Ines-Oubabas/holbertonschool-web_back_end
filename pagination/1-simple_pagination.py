#!/usr/bin/env python3
''' Simple pagination '''

import csv
import math
from typing import List
from typing import Tuple


index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page from the dataset."""
        # Ensure page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the start and end indices for the requested page
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        data = self.dataset()

        # Return the slice of the dataset corresponding to the page
        return data[start_index:end_index] if start_index < len(data) else []
