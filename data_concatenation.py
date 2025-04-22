import pandas as pd

def file_concatenation(file1:str, file2:str):
    file1 = pd.read_csv(file1, sep=';', encoding="cp1252")
    file2 = pd.read_csv(file2, sep=';', encoding="cp1252")
    concatenated_file = pd.concat([file1, file2])
    df = pd.DataFrame(concatenated_file)
    df.to_excel('Goodreads_data_2004_2025.xlsx', index=False)
    print('file has been concatenated')
    return concatenated_file


file_concatenation(r'output\Goodreads_2004_2024_merged_06.csv', r'output\books_data_2004_2025.csv')
