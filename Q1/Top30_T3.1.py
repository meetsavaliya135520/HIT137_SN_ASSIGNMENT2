from collections import Counter
import csv

file_path = 'C:/Users/saval/PycharmProjects/pythonProject/SE/HIT137_SN_Assignment2/text1.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()

words = text.split()

word_counts = Counter(words)

top_30_words = word_counts.most_common(30)

for word, count in top_30_words:
    print(f'{word}: {count}')

csv_file_path = 'C:/Users/saval/PycharmProjects/pythonProject/SE/HIT137_SN_Assignment2/top30.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word', 'Count'])
    csv_writer.writerows(top_30_words)
print(f'Top 30 words and their counts saved to {csv_file_path}')
