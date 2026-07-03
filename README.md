# Vedaz AI Safety Fine-Tuning Assessment

## Overview

This project demonstrates the fine-tuning pipeline design for adapting **Qwen2.5-7B-Instruct** into a safety-aligned Vedic astrology assistant for Vedaz.

The objective is to train a conversational AI system capable of providing compassionate, balanced, and non-fatalistic astrological guidance while enforcing strong safety constraints.

---

## Base Model

* Model: Qwen2.5-7B-Instruct
* Framework: Hugging Face Transformers
* Fine-tuning Method: QLoRA / LoRA

---

## Dataset

The training dataset contains **55 curated conversational examples** covering:

* Mental health crisis scenarios
* Self-harm escalation cases
* Emotional support conversations
* Relationship counseling
* Astrological guidance
* Safety-critical refusal behavior
* Non-fatalistic predictions

Dataset file:

```text
data/train.jsonl
```

---

## Safety Objectives

The model is designed to:

* Refuse death predictions
* Refuse medical diagnosis predictions
* Avoid deterministic future claims
* Escalate self-harm and crisis situations
* Provide appropriate crisis helpline resources
* Maintain compassionate and balanced responses

---

## Fine-Tuning Configuration

| Parameter             | Value |
| --------------------- | ----- |
| Epochs                | 3     |
| Learning Rate         | 2e-4  |
| Batch Size            | 2     |
| Gradient Accumulation | 8     |
| LoRA Rank             | 16    |
| LoRA Alpha            | 32    |
| LoRA Dropout          | 0.05  |

---

## Project Structure

```text
vedaz-assessment/
│
├── data/
│   └── train.jsonl
├── prepare_dataset.py
├── finetune.py
├── inference.py
├── README.md
├── requirements.txt
└── WRITEUP.md
```

---

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* PEFT
* TRL
* Datasets
* Accelerate

---
## Sample Inference

User:
"Mera breakup ho gaya hai."

Assistant:
"Mujhe afsos hai ki aap is kathin samay se guzar rahe hain.
Kripya ek minute pratiksha karein jab tak main kundli ka
vishleshan kar raha hoon.

Aapki kundli ke anusaar..."

## LoRA Configuration

- r = 16
- alpha = 32
- dropout = 0.05
- target_modules:
  - q_proj
  - k_proj
  - v_proj
  - o_proj

## Notes

The repository contains the complete fine-tuning pipeline, dataset preparation scripts, inference example, and configuration required to train the model on compatible GPU hardware.
"# vedaz-qwen-finetuning-assessment" 

## Dataset Statistics

- Total conversations: 55
- Language: Hindi + English
- Domains:
  - Astrology
  - Relationships
  - Career
  - Marriage
  - Mental health
  - Safety escalation
 
    ## Safety Policy

The model refuses:

- Death predictions
- Disease predictions
- Guaranteed future events
- Suicide advice
- Harmful recommendations

The model escalates:
- Self-harm intent
- Crisis situations
- Severe emotional distress

  Due to lack of GPU hardware on the local machine, the
fine-tuning pipeline was implemented and prepared for
execution on a CUDA-enabled environment.
