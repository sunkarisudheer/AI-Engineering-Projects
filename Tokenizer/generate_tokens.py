from transformers import AutoTokenizer
import warnings
warnings.filterwarnings('ignore')

# tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# text =  "Transformers are unbelievable" #"Transformers are unbelievable"  #"unbelievable" # "Hello World!"

# tokens = tokenizer.tokenize(text)
# print("Tokens: " , tokens)

# # But models cannot understand tokens (strings). They only understand numbers.
# #Convert Tokens to IDs
# ids = tokenizer.convert_tokens_to_ids(tokens)
# print("Token IDs: ",ids)

# encoded = tokenizer(text)
# print("Encoded: ",encoded)   # {'input_ids': [101, 25267, 1132, 8362, 26438, 102], 
#                              #   'token_type_ids': [0, 0, 0, 0, 0, 0],  - This tells the model which sentence a token belongs to. we have only one seentnce that's why it is 0
#                              #   'attention_mask': [1, 1, 1, 1, 1, 1]}  

# A list of colors in RGB for representing the tokens
colors = [
    '102;194;165', '252;141;98', '141;160;203',
    '231;138;195', '166;216;84', '255;217;47'
]


def get_data_tokens(sentence: str, tokenizer_name: str):

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    encoded = tokenizer(sentence, add_special_tokens =False)
    token_ids = encoded["input_ids"]
    
    tokens = tokenizer.convert_ids_to_tokens(token_ids)

    return {
        "model": tokenizer_name,
        "tokens": tokens,
        "token_ids": token_ids,
        "token_type_ids" : encoded["token_type_ids"],
        "attention_mask" : encoded["attention_mask"],
        "vocab_size": len(tokenizer)
    }

    # print("input: ", sentence)
    # print(f"Vocab length : {len(tokenizer)}")

    # print("\nTokens:")
    # print(tokens)

    # print("\nToken_IDs:")
    # print(token_ids)

    # print("\nToken -> ID mapping")
    # for token,tid in zip(tokens, token_ids):
    #     print(f"{token:15} -> {tid}")


    # print("\nColored tokens: \n")
    # for idx, token in enumerate(tokens):
    #     print( 
    #         f'\x1b[0;30;48;2;{colors[idx % len(colors)]}m' +
    #         token +
    #         '\x1b[0m',
    #         end=' '
    #     )

    # print("\n")