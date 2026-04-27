class number_file_divider:

    def __init__(self, input_file_path, even_file_path, odd_file_path):
        self._input_file_path = input_file_path
        self._even_file_path = even_file_path
        self._odd_file_path = odd_file_path

    def process_numbers(self):
        