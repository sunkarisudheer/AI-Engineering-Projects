from generate_tokens import get_data_tokens
import warnings
warnings.filterwarnings('ignore')


models =[
    "bert-base-cased",
    "bert-base-uncased",
    "gpt2",
    "roberta-base"
]
text = input("Enter input to get tokens: ")

print(f"\ninput: {text}")
print("-" * 80)

print(f"{'Model':20} {'Token_Count':15} {'Tokens'}")
print("-" * 80)
for model in models:
    data = get_data_tokens(text , model)

    tokens = data['tokens']
    print(f"{model:20} {len(tokens):<15}  {tokens}")