# 📰 NewsSnap AI — News Article Summarizer

NewsSnap AI is a **beginner-level AI/NLP learning project** I built to explore text summarization, fine-tuning pretrained language models, and creating a simple web application.

The application uses a fine-tuned **T5-small model** to generate concise summaries from news articles. It provides a simple interface built with Streamlit.

> **Project status:** Learning and experimentation project. This is not a professional or production-ready summarization system.

## 🚀 Live Demo

🔗 **Try the application:** [Open NewsSnap AI](https://news-article-summarizer-gbc8vzxhtumm37bcu7chnk.streamlit.app/)

## ✨ Features

- Paste a news article into the application.
- Generate a concise summary using a fine-tuned T5-small model.
- View the original article alongside the generated summary.
- Simple and beginner-friendly Streamlit interface.

## 🛠️ Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- T5-small
- Streamlit
- Hugging Face Datasets
- ROUGE evaluation metrics

## ⚙️ How It Works

1. The user pastes a news article.
2. The article is tokenized and prepared for the model.
3. The fine-tuned T5-small model generates a summary.
4. The generated summary is displayed in the web application.

## 📊 Model Evaluation

The model was fine-tuned on the **CNN/DailyMail 3.0.0 dataset** and evaluated using ROUGE metrics on a sample of 100 validation examples.

| ROUGE Metric | Fine-tuned Model | Pretrained Baseline |
|---|---:|---:|
| ROUGE-1 | 0.3514 | 0.3227 |
| ROUGE-2 | 0.1611 | 0.1311 |
| ROUGE-L | 0.2611 | 0.2312 |
| ROUGE-Lsum | 0.3028 | 0.2727 |

*These scores are from a limited validation sample, not a full-dataset evaluation. ROUGE measures overlap between generated summaries and reference summaries; it does not guarantee factual accuracy or completeness.*

## ⚠️ Limitations

This is an early-stage learning project. The generated summaries may:

- Miss important announcements or key details.
- Focus on supporting information instead of the main point.
- Contain grammatical errors or awkward phrasing.
- Differ from the reference summary.

The output should not be treated as a fully accurate representation of the original article. Please refer to the original article when details matter.

## 🔮 Future Improvements

- Improve coverage of the main points in an article.
- Experiment with different summarization models and input lengths.
- Evaluate performance on a larger validation sample.
- Improve factual consistency and summary readability.

## 👩‍💻 Author

**Vashundthera Vashu**

- LinkedIn: [Connect with me](www.linkedin.com/in/vashundthera7/)
- GitHub: [View my repositories](https://github.com/purple279)

---

⭐ This project is part of my journey toward learning AI engineering, Natural Language Processing, and language model development.
