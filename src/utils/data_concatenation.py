import pandas as pd

class FileConcatenation():
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def file_concatenation(self, sep, encoding):
        self.file1 = pd.read_csv(self.file1, sep=';', encoding="cp1252")
        self.file2 = pd.read_csv(self.file2, sep=';', encoding="cp1252")
        concatenated_file = pd.concat([self.file1, self.file2])
        df = pd.DataFrame(concatenated_file)
        df.to_excel(r'output\Goodreads_data_2004_2025.xlsx', index=False)
        print('file has been concatenated')
        return concatenated_file


concatenation = FileConcatenation(r'output\Goodreads_2004_2024_merged_06.csv', r'output\books_data_2004_2025.csv')
concatenate_files = concatenation.file_concatenation(sep=';', encoding="cp1252")

