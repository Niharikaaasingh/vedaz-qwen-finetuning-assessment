import json
import sys

# Fix Hindi/Unicode display on Windows
sys.stdout.reconfigure(encoding='utf-8')

with open("data/vedaz.jsonl", "r", encoding="utf-8") as f:
    content = f.read()

decoder = json.JSONDecoder()

dataset = []
idx = 0

while idx < len(content):
    try:
        # Decode one JSON object at a time
        obj, end = decoder.raw_decode(content, idx)

        # Store only valid conversations
        if isinstance(obj, dict) and "messages" in obj:
            dataset.append(obj)

        idx = end

        # Skip whitespace/newlines
        while idx < len(content) and content[idx].isspace():
            idx += 1

    except json.JSONDecodeError:
        idx += 1

print("=" * 50)
print("Total conversations:", len(dataset))
print("=" * 50)

# Show first conversation safely
if dataset:
    print("\nFirst conversation loaded successfully!\n")

    for i, msg in enumerate(dataset[0]["messages"], 1):
        print(f"Message {i}")
        print("Role:", msg.get("role", "Unknown"))
        print("Content Preview:")

        content = msg.get("content", "")

        # Print only first 100 characters to avoid terminal issues
        if len(content) > 100:
            print(content[:100] + "...")
        else:
            print(content)

        print("-" * 50)
else:
    print("No conversations found.")