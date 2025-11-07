# 🤖 T5 Abstractive Text Summarizer (Fine-Tuned on CNN/DailyMail)

## Project Overview
This project demonstrates an end-to-end Machine Learning pipeline for **abstractive text summarization**, a core Natural Language Processing (NLP) task. I successfully fine-tuned the **T5-small transformer model** on a subset of the industry-standard CNN/DailyMail dataset to generate concise, coherent, and human-readable summaries from news articles.

This repository contains the full, reproducible training notebook, evaluation artifacts, and code used to deploy the model as a live web application.

---

## 🚀 Live Demo & Deployment
The model is deployed on the Hugging Face ecosystem, showcasing mastery of the full MLOps cycle from training to production.

| Component | Status | Details |
| :--- | :--- | :--- |
| **Live Web App** | **Running** | Interactive Gradio demo for immediate testing. |
| **Deployment Link** | **[T5-CNN-DailyMail-Summarizer-Demo](https://huggingface.co/spaces/benjose51/T5-CNN-DailyMail-Summarizer-Demo)** | Click to try the model now. |
| **Model Used** | **T5-small** | Selected for balance between high performance and computational efficiency. |

---

## 🏆 Key Performance Metrics (ROUGE Score)
The model's performance was evaluated on a validation set using **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**, the industry standard for summarization quality.

| Metric | **Score (Fine-Tuned Model)** | Technical Implication |
| :--- | :--- | :--- |
| **ROUGE-1** | **$31.5125\%$** | Measures unigram overlap, indicating the presence of key topics and keywords. |
| **ROUGE-2** | **$14.2222\%$** | Measures bigram overlap, indicating phrase structure and better coherence. |
| **ROUGE-L** | **$23.2637\%$** | Measures the longest common subsequence, confirming fluency and content preservation. |

---

## ✨ Technical and Business Achievements

### 1. Model Development & Optimization
* **Transformer Fine-Tuning:** Successfully leveraged the Hugging Face `transformers` library to fine-tune the T5-small model using the `Seq2SeqTrainer`.
* **Efficient Training:** Utilized **Mixed Precision Training (`fp16`)** via the `accelerate` library to significantly speed up training time and reduce GPU memory consumption, demonstrating resource management skills.
* **Inference Strategy:** Employed **Beam Search (`num_beams=4`)** during text generation to ensure high-quality, fluent summaries and avoid common failure modes like repetitive or generic output.

### 2. Deployment and MLOps
* **Containerized Demo:** Deployed the model using **Gradio** on **Hugging Face Spaces**, creating a simple, functional, and publicly accessible web interface.
* **Dependency Management:** Maintained a clean, minimal deployment environment using a `requirements.txt` file.
* **Portfolio Management:** Structured the repository to **exclude large model binaries**, linking instead to the Hugging Face Model Hub for the weights, which keeps the GitHub repo lightweight and focused on code.

---

## 📂 Repository Contents
| File/Folder | Description |
| :--- | :--- |
| `Text_Summarizer` | **The Complete Notebook:** The fully executable Google Colab notebook containing all steps: data loading, tokenization, training, evaluation, and artifact generation. |
| `examples.csv` | **Evaluation Artifacts:** A CSV file showing side-by-side examples of the **Article**, the **Human Reference Summary**, and the **Model's Generated Prediction** for visual quality assessment. |
| `app.py` | * The file used to deploy the live demo on Hugging Face Spaces. |
| `LLM Text Summarizer Demo` |* Screenshot of the live demo on Hugging Face Spaces. |

---

## 🧑‍💻 Author and Contact Information
This project was developed by:

* **Name:** BEN JOSE
* **LinkedIn:** [https://www.linkedin.com/in/ben-jose-aa9537190/](https://www.linkedin.com/in/ben-jose-aa9537190/)
* **GitHub:** [https://github.com/BENJOSE51](https://github.com/BENJOSE51)
* **Email:** benjose51@gmail.com
