from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm
import torch

import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("godel-negotiator")
model = AutoModelForSeq2SeqLM.from_pretrained("godel-negotiator")
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model.to(torch.device(device))

df_test = pd.read_csv('data/test_godel.csv')

context = df_test['context'].to_list()
actual = df_test['response'].to_list()
response = []

for query in tqdm(context):

    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids.to(device)
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)

   
    response.append(output)


df = pd.DataFrame.from_dict({'Context':context, 'Actual':actual, 'Response':response})
df.to_csv('results/results-godel.csv', index=False)
