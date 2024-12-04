
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments

import nltk
from datasets import load_dataset
import evaluate
import numpy as np

dataset = load_dataset('csv', data_files={'train': 'data/train_godel.csv', 'eval':'data/val_godel.csv', 'test': 'data/test_godel.csv'})

tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

# Setup evaluation
nltk.download("punkt", quiet=True)
metric = evaluate.load("rouge")

#===============================================Format Data===============================================================

prefix = "Response: "

def preprocess_function(examples):
    inputs = [prefix + doc for doc in examples["context"]]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)

    labels = tokenizer(text_target=examples["response"], max_length=128, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)



def compute_metrics(eval_preds):
    preds, labels = eval_preds

    # decode preds and labels
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # rougeLSum expects newline after each sentence
    decoded_preds = ["\n".join(nltk.sent_tokenize(pred.strip())) for pred in decoded_preds]
    decoded_labels = ["\n".join(nltk.sent_tokenize(label.strip())) for label in decoded_labels]

    result = metric.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
    return result

#===============================================Train Model===============================================================


training_args = Seq2SeqTrainingArguments(
    f"godel-negotiator",
    evaluation_strategy = "epoch",
    save_strategy = "epoch",
    num_train_epochs=30,
    save_total_limit=3,
    per_device_train_batch_size=6,
    per_device_eval_batch_size=6,
    learning_rate=2e-5,
    load_best_model_at_end=True,
    weight_decay=0.01,
    predict_with_generate=True
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["eval"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

trainer.train()
trainer.save_model()
tokenizer.save_pretrained("godel-negotiator")