import json

input_file = r"C:\Users\MAIMI\Downloads\archive\arxiv-metadata-oai-snapshot.json"
output_file = "healthcare_papers.json"

keywords = [
    "health", "medical", "medicine", "disease",
    "cancer", "covid", "patient", "clinical",
    "bioinformatics", "hospital", "diagnosis"
]

count = 0

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        paper = json.loads(line)

        text = (
            paper.get("title", "") + " " +
            paper.get("abstract", "")
        ).lower()

        if any(keyword in text for keyword in keywords):

            record = {
                "title": paper.get("title"),
                "abstract": paper.get("abstract"),
                "authors": paper.get("authors")
            }

            outfile.write(json.dumps(record) + "\n")

            count += 1

            if count >= 10000:
                break

print(f"Saved {count} healthcare papers.")