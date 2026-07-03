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

├── data/
│   ├── vedaz.jsonl
│   └── train.jsonl
│
├── prepare_dataset.py
├── finetune.py
├── inference.py
├── requirements.txt
├── README.md
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

## Notes

The repository contains the complete fine-tuning pipeline, dataset preparation scripts, inference example, and configuration required to train the model on compatible GPU hardware.
"# vedaz-qwen-finetuning-assessment" 
