class number_file_divider:

    def __init__(self, input_file_path, even_file_path, odd_file_path):
        self._input_file_path = input_file_path
        self._even_file_path = even_file_path
        self._odd_file_path = odd_file_path

    def process_numbers(self):
        with open(self._input_file_path, "r") as cosmic_input_stream, \
             open(self._even_file_path, "w") as azure_even_stream, \
             open(self._odd_file_path, "w") as crimson_odd_stream:

            for nebula_line in cosmic_input_stream:
                stellar_number = int(nebula_line.strip())