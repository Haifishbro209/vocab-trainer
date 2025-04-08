
---

# French Vocabulary Trainer

A personalized French vocab trainer that uses **Exponentially Weighted Moving Average (EWMA)** to prioritize difficult words based on recent mistakes.

### How It Works:

The algorithm tracks mistakes using the formula:

```
Eₜ = α·eₜ + (1−α)·Eₜ₋₁
```

It combines current and previous errors, giving more weight to recent mistakes, helping the trainer prioritize challenging words for faster learning.

---

### Setup:

1. **Clone the Repo**  
   ```bash
   git clone https://github.com/haifishbro209/vocab-trainer.git
   cd vocab-trainer
   ```

2. **Create or Modify Your Vocabulary Database**  
   Edit `Database.py` to use your own French-German words.

3. **Get a Linguistic Expert**  
   Ensure your vocabulary is accurate by consulting an expert.

---

### Features:
- Smart word selection based on errors.
- Customizable vocabulary database.
- Open-source and free to use.

---

### Installation:

1. Clone the repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the trainer:
   ```bash
   python main.py
   ```

---
