#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary with pagination details that is resilient to deletions.

        :param index: The current start index of the return page.
        :param page_size: The current page size.
        :return: A dictionary with keys 'index', 'next_index', 'page_size', 'data'.
        """
        # Validate the index
        assert index is not None and 0 <= index < len(self.dataset()), "Index out of range"

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index

        # Iterate to collect `page_size` items starting from `index`
        while len(data) < page_size and next_index < len(self.dataset()):
            item = indexed_data.get(next_index)
            if item is not None:
                data.append(item)
            next_index += 1

        # If we reached the end of the dataset, there is no next index
        if next_index >= len(self.dataset()):
            next_index = None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index,
        }
