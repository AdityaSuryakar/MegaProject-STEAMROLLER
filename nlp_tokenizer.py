import os
import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# Base directory (same folder as this script)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Input and Output folders
input_folder = os.path.join(base_dir, "transcripts")
output_folder = os.path.join(base_dir, "tokens")

os.makedirs(output_folder, exist_ok=True)

# Get all .txt transcript files
txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

for file in txt_files:

    input_path = os.path.join(input_folder, file)

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Sentence tokenization
    sentences = nltk.sent_tokenize(text)

    output_file = os.path.join(
        output_folder,
        os.path.splitext(file)[0] + "_tokens.txt"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in sentences:
            f.write(sentence.strip() + "\n")

    print(f"Processed sentence tokens saved: {output_file}")

print("NLP processing completed successfully.")
