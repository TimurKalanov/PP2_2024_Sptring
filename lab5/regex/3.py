import re
def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    sequences = re.findall(pattern, text)
    return sequences

text = "privet america_usa"
sequences = find_sequences(text)
print("Found sequences:", sequences)