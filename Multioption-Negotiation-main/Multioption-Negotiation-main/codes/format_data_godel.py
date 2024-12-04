import pandas as pd
import re

def extract_context_response(text):
    context = re.search(r'\[SOC\](.*?)\[EOC\]', text, re.DOTALL)
    response = re.search(r'\[SOR\](.*?)\[EOR\]', text, re.DOTALL)
    if context and response:
        context_text = context.group(1).strip().replace('[User]', 'EOS User:').replace('[Bot]', 'EOS Bot:')
        response_text = response.group(1).strip().replace('[User]', 'User:').replace('[Bot]', 'Bot:')
        return f"Instruction: given a dialog context, you need to respond to user to negotiate for a deal for hotel booking. [CONTEXT]  {context_text[4:]}", response_text
    return None, None



def format(input_file, output_file):
    # Read CSV file into a DataFrame
    data = pd.read_csv(input_file)

    # Apply extraction function to 'text' column
    data['context'], data['response'] = zip(*data['text'].apply(extract_context_response))

    # Write the extracted data to a new CSV file
    data[['context', 'response']].to_csv(output_file, index=False)

    print("Extraction completed. Output saved to", output_file)


format('data/train_data.csv', 'data/train_godel.csv')
format('data/val_data.csv', 'data/val_godel.csv')
format('data/test_data.csv', 'data/test_godel.csv')

