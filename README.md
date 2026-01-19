# 🕵️‍♂️ Fake News Detector AI

A machine learning–based web application that helps students identify **fake, real, or uncertain news** related to **education, exams, jobs, and viral academic messages**.  
The application is built using **Python, NLP, Machine Learning, and Streamlit**.

---

## 🚀 Project Overview

With the rapid spread of misinformation on social media, students often face confusion regarding exams, results, scholarships, and job opportunities.  
This project aims to provide a simple tool that analyzes textual news content and predicts whether it is:

- ❌ Fake  
- ✅ Real  
- 🤔 Uncertain (needs verification)

---

## ✨ Features
* **High Accuracy:** 94% accuracy using Logistic Regression.
* **Interactive Web App:** Built with Streamlit for easy testing.
* **Fast Processing:** Checks any news article in under a second.

> ⚠️ **Disclaimer:**  
> This system predicts the likelihood of misinformation based on language patterns.  
> It does **not replace official fact-checking sources**.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Web UI)
- **Scikit-learn**
- **Natural Language Processing (NLP)**
- **Pickle** (Model & Vectorizer storage)

---

## 📊 Dataset

- The dataset used to train this model is **sourced from Kaggle**
- It focuses on **education-related news**
- Initially, US-based datasets were explored, but the final training was done using **India-related education news data from Kaggle**

> Dataset Source: **Kaggle (Indian education-related dataset)**

---

## 🖥️ Application Features

- Simple and clean UI
- Real-time prediction
- Confidence score display
- Handles ambiguous cases as *Uncertain*
- Designed specifically for **students**

---

## 🛠️ How to Run Locally

```bash
#Install requirements
pip install -r requirements.txt

# Run the Streamlit app
 streamlit run app.py

├── app.py
├── Fake News Detection.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

📌 Limitations

Model accuracy depends on dataset quality

Limited availability of high-quality Indian education datasets

Cannot guarantee 100% correctness

## 🧠 Model
The model was trained on the ISOT Fake News Dataset using TF-IDF Vectorization.
