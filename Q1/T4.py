import spacy
from collections import Counter

# Load SpaCy models
nlp_sci = spacy.load("en_core_sci_sm")  # Small biomedical model
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")  # BC5CDR NER model for diseases and drugs


# Function to extract entities from a model
def extract_entities(text, model):
    doc = model(text)
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'CHEMICAL']
    return diseases, drugs


# Load the file and read the content
txt_path = 'text1.txt'  # Replace with actual file path
with open(txt_path, 'r') as file:
    text = file.read()

# Process the text using each model
diseases_sci, drugs_sci = extract_entities(text, nlp_sci)
diseases_bc5cdr, drugs_bc5cdr = extract_entities(text, nlp_bc5cdr)

# Get total entities
total_diseases_sci = len(diseases_sci)
total_drugs_sci = len(drugs_sci)
total_diseases_bc5cdr = len(diseases_bc5cdr)
total_drugs_bc5cdr = len(drugs_bc5cdr)

# Compare entities
common_diseases = set(diseases_sci).intersection(set(diseases_bc5cdr))
common_drugs = set(drugs_sci).intersection(set(drugs_bc5cdr))

# Print the comparison results
print(f"Total diseases detected by en_core_sci_sm: {total_diseases_sci}")
print(f"Total drugs detected by en_core_sci_sm: {total_drugs_sci}")
print(f"Total diseases detected by en_ner_bc5cdr_md: {total_diseases_bc5cdr}")
print(f"Total drugs detected by en_ner_bc5cdr_md: {total_drugs_bc5cdr}")

print("\nMost common diseases detected by both models:")
print(common_diseases)

print("\nMost common drugs detected by both models:")
print(common_drugs)

# Find differences between models
diff_diseases_bc5cdr_sci = set(diseases_bc5cdr).difference(set(diseases_sci))
diff_drugs_bc5cdr_sci = set(drugs_bc5cdr).difference(set(drugs_sci))

print(f"\nDiseases detected by en_ner_bc5cdr_md but not by en_core_sci_sm: {diff_diseases_bc5cdr_sci}")
print(f"Drugs detected by en_ner_bc5cdr_md but not by en_core_sci_sm: {diff_drugs_bc5cdr_sci}")

# Most common words among diseases and drugs
most_common_diseases_sci = Counter(diseases_sci).most_common(10)
most_common_drugs_sci = Counter(drugs_sci).most_common(10)

print("\nMost common diseases detected by en_core_sci_sm:")
print(most_common_diseases_sci)

print("\nMost common drugs detected by en_core_sci_sm:")
print(most_common_drugs_sci)

# Similarly, you can calculate most common entities for the other model as well
