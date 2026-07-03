import json

with open("data/vedaz.jsonl", "r", encoding="utf-8") as f:
    content = f.read()

decoder = json.JSONDecoder()

dataset = []
idx = 0

while idx < len(content):
    try:
        obj, end = decoder.raw_decode(content, idx)

        if isinstance(obj, dict) and "messages" in obj:
            text = ""

            for msg in obj["messages"]:
                role = msg.get("role", "")
                message = msg.get("content", "")
                text += f"{role}: {message}\n"

            dataset.append({"text": text})

        idx = end

        while idx < len(content) and content[idx].isspace():
            idx += 1

    except:
        idx += 1

print("=" * 50)
print("Total training samples:", len(dataset))
print("=" * 50)

print("\nFirst training sample:\n")
print(dataset[0]["text"][:500])