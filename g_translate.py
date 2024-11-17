from googletrans import Translator as Tr
import pandas as pd
# Initialize the translator , setting up.
translator = Tr()

# taking dynamic input and translating to the desired output
text_to_translate = input("Give the lines to be translated:\t")
# saved the gathered daRead the Excel file
with open('Google_Languages.xlsx', 'rb') as fxlsx:  # Use 'rb' mode for binary reading
    reader = pd.read_excel(fxlsx, sheet_name='Sheet1')

# Iterate over the rows and print the first and second columns
for index, row in reader.iterrows():
    # Check if the first or second cell is empty (NaN)
    if pd.isna(row[0]) or pd.isna(row[1]):
        break
    print("for"+ row[0] +": pick :"+ row[1].upper())
source_Lang_in = input("enter the source language's code #for example 'en for english'")
dest_Lang_out = input("enter the destination language's code #for example 'es for espanol'")

source_Lang_in, dest_Lang_out  = source_Lang_in.lower(), dest_Lang_out.lower()

# Translate the text
translated = translator.translate(text_to_translate, src=source_Lang_in, dest=dest_Lang_out)

# Print the translated text
print("Original Text:", text_to_translate)
print("Translated Text:", translated.text)

