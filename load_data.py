import json

file_path = r"C:\Users\MAIMI\Downloads\archive\arxiv-metadata-oai-snapshot.json"

count = 0

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        paper = json.loads(line)

        print("Title:", paper.get("title"))
        print("Abstract:", paper.get("abstract", "")[:200])
        print("-" * 50)

        count += 1

        if count == 5:
            break