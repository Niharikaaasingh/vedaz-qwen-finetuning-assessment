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

            conversation = ""

            for msg in obj["messages"]:
                role = msg["role"]
                text = msg["content"]

                conversation += f"<|{role}|>\n{text}\n"

            dataset.append({
                "text": conversation
            })

        idx = end

        while idx < len(content) and content[idx].isspace():
            idx += 1

    except:
        idx += 1

with open("data/train.jsonl", "w", encoding="utf-8") as f:
    for item in dataset:
        f.write(
            json.dumps(item, ensure_ascii=False)
            + "\n"
        )

print("Created:", len(dataset), "training samples")