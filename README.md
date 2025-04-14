# 🧾 ExpenseTrackerV1

A simple, CLI-based Python app to track your monthly expenses and stay within budget. It allows you to enter individual expenses, categorize them, and then gives you a summary of how much you’ve spent and how much budget you have left for the month.

---

## 📦 Features

- Prompt user for monthly budget
- Add and categorize expenses (`Food`, `Rent`, `Transport`, `Misc`)
- Store expenses in a CSV file
- Calculate and display:
  - Total spent
  - Remaining budget
  - Per-category spending
  - Daily budget based on days left in the month

---

## 🚀 How to Run

1. Clone the repo or download the files.
2. Make sure you have Python 3 installed.
3. Run the script from the terminal:

```bash
python expenseTracker.py
```

> 🔄 You’ll be prompted for:
> - Your monthly budget
> - Expense name, amount, and category

---

## 🗃️ File Structure

```bash
ExpenseTrackerV1/
│
├── expenseTracker.py       # Main script that runs the app
├── expense.py              # Class definition for Expense
├── expenses.csv            # (Ignored by .gitignore) Stores user expenses
└── .gitignore              # Ignores virtual environment, CSV, etc.
```

---

## 🧠 How It Works

1. **User inputs budget**
2. **User adds an expense** (name, amount, and selects category)
3. Expense is saved to `expenses.csv`
4. The script reads the file and:
   - Groups expenses by category
   - Shows total spent vs. budget
   - Shows remaining budget and days left in the month
   - Calculates your allowed daily spend

---

## ❌ Files Excluded from Git

This project excludes the following files from version control:

- `.venv/` – Virtual environment
- `expenses.csv` – Personal expense data
- `.idea/` – PyCharm project files
- `__pycache__/` – Python cache

---

## ✍️ Author

Created by [N-Sh00](https://github.com/N-Sh00)

---

