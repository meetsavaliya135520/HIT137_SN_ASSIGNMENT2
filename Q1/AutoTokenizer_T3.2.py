from collections import Counter
from transformers import AutoTokenizer


def count_and_get_top_tokens(file_path, model_name, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))

    token_counts = Counter(tokens)

    top_tokens = token_counts.most_common(top_n)

    top_words = [(token, count) for token, count in top_tokens]

    return top_words


file_path = 'D:/CDU/STUDY/SEM 1/SN HIT137/Assignment 2/New folder/text1.txt'
model_name = 'bert-base-uncased'
top_words = count_and_get_top_tokens(file_path, model_name)

for token, count in top_words:
    print(f'{token}: {count}')
