from transformers import AutoTokenizer
from collections import Counter


def count_unique_tokens(text_file, top_n=30):
    # Load a pre-trained tokenizer (e.g., BERT tokenizer)
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    # Read the text file
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Get the top 'n' most common tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens


# Example usage
top_tokens = count_unique_tokens('text1.txt', top_n=30)
print(top_tokens)
