# Tokenizer Comparison Tool
This project compares how different NLP tokenizers split text.
Supported models:
- bert-base-cased
- bert-base-uncased
- gpt2
- roberta-base

## Installation
pip install -r requirements.txt

## Run
python main.py

## Example Output

Input: Transformers are unbelievable
Model                Token Count   Tokens
------------------------------------------------------------
bert-base-cased      4             ['Transformers','are','un','##believable']
gpt2                 3             ['Transformers','Ġare','Ġunbelievable']