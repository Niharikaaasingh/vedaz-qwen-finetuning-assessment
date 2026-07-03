from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments
)

from peft import LoraConfig
from trl import SFTTrainer
from datasets import load_dataset

MODEL = "Qwen/Qwen2.5-7B-Instruct"

dataset = load_dataset(
    "json",
    data_files="data/train.jsonl"
)

tokenizer = AutoTokenizer.from_pretrained(MODEL)

model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    device_map="auto"
)

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

training_args = TrainingArguments(
    output_dir="./outputs",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    logging_steps=10,
    save_strategy="epoch"
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    args=training_args,
    peft_config=peft_config,
)

trainer.train()
trainer.save_model("./vedaz-qwen")