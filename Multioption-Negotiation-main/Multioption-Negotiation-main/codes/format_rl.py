import pandas as pd
import re

def extract_context_response(text):
    context = text.split('[SOR]')[0]
    response = '[SOR]' + text.split('[SOR]')[1]

    return context, response



def format(input_file, output_file):
    # Read CSV file into a DataFrame
    data = pd.read_csv(input_file)

    # Apply extraction function to 'text' column
    data['context'], data['response'] = zip(*data['text'].apply(extract_context_response))

    # Write the extracted data to a new CSV file
    data[['context', 'response']].to_csv(output_file, index=False)

    print("Extraction completed. Output saved to", output_file)


format('data/train_data.csv', 'data/train_rl.csv')
format('data/val_data.csv', 'data/val_rl.csv')
format('data/test_data.csv', 'data/test_rl.csv')