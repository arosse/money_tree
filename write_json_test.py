# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:22:55 2024

@author: Antoine
"""

import json

class CompactJSONEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, list):
            # Join list elements with commas in a single line
            return '[' + ', '.join(self.encode(el) for el in obj) + ']'
        elif isinstance(obj, dict):
            # Pretty-print dictionaries with indented formatting
            items = []
            for key, value in obj.items():
                items.append(f'"{key}": {self.encode(value)}')
            return '{\n    ' + ',\n    '.join(items) + '\n}'
        else:
            return super().encode(obj)

def write_data_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        # Use our custom encoder to format JSON
        json_file.write(CompactJSONEncoder().encode(data))


# Example data to write
data = {
    "x1": [1, 2, 3, 4],
    "x2": [0, 5, 8, 10],
    "x3": [0, 5, 8, 10],
    "y1": [10, 15, 13, 17],
    "y2": [7, 15, 10, 12],
    "y3": [1, 1.1, 1, 0.9]
}

write_data_to_json("C:/Users/Antoine/Documents/Projects/Stock Market/Python/Money_Tree/data.json", data)