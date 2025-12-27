# IPL Match Prediction 🏏

A data-driven IPL match prediction system built using historical IPL match data and probabilistic analysis.  
The project focuses on **team vs team win probabilities**, **season-wise learning**, and **prediction evaluation** without using heavy ML frameworks.

---

## 📌 Project Objective

The goal of this project is to:
- Analyze historical IPL match outcomes
- Compute team-wise winning probabilities
- Predict match winners for each season
- Evaluate prediction accuracy year by year

The approach is **statistics + probability based**, not black-box ML.

---

## 📂 Repository Files Explained (IMPORTANT)

This section explains **every file in this repository** and its role.

---

### 🐍 Python Source Files

#### `data_clean.py`
**Purpose:**  
Cleans and standardizes IPL raw data.

**What it does:**
- Reads `set1.csv`
- Filters seasons after **2017**
- Normalizes team names (e.g., *Royal Challengers Bangalore → RCB*)
- Ensures consistency across `team1`, `team2`, and `winner` columns
- Outputs cleaned data to `set2.csv`

➡️ This is the **data preprocessing step**.

---

#### `ipl.py`
**Purpose:**  
Core prediction engine of the project.

**What it does:**
- Builds **team-vs-team win percentage tables**
- Maintains:
  - Overall historical performance
  - Current season performance
- Uses a custom probabilistic algorithm (`ALGO`)
- Predicts match winners for each season
- Stores predictions in `Probs.csv`

➡️ This file contains the **entire prediction logic**.

---

#### `check_Predict.py`
**Purpose:**  
Evaluates prediction accuracy.

**What it does:**
- Compares predicted winners vs actual winners
- Computes:
  - Success rate
  - Failure rate
- Performs **year-wise evaluation**
- Appends results to `Summarize.csv`

➡️ This file answers: **“How good is the model?”**

---

#### `test.py`
**Purpose:**  
Final verification and boolean correctness tagging.

**What it does:**
- Reads `Probs.csv`
- Adds a column:
  - `BOOL_DATA = True` if prediction matches actual result
- Saves output to `prob2.csv`

➡️ Used for **final correctness checking and analysis**.

---

### 📊 Data Files

#### `set1.csv`
- Raw IPL match dataset
- Contains original team names and seasons
- Input for `data_clean.py`

---

#### `set2.csv`
- Cleaned IPL dataset
- Standardized team abbreviations
- Used by `ipl.py` for predictions

---

#### `Probs.csv`
- Stores match-wise predictions
- Columns include:
  - Year
  - team1, team2
  - Predicted Winner (`Win`)
  - Winning Probability (`Win_Prob`)
  - Actual Winner (`Actual_Win`)

➡️ This is the **main prediction output file**.

---

#### `prob2.csv`
- Enhanced prediction results
- Adds correctness flag:
  - `BOOL_DATA = True / False`

➡️ Useful for accuracy analysis.

---

#### `Summarize.csv`
- Year-wise performance summary
- Contains:
  - Success percentage
  - Failure percentage

➡️ Final evaluation report.

---

#### `prob_check_A.xlsx`
- Manual / external probability verification
- Used for validation or comparison

---

### 📄 Documentation Files

#### `IPL_PREDICTION.pdf`
- Detailed project report
- Explains methodology, results, and conclusions

---

#### `IPL_Simpler.pdf`
- Simplified explanation of the project logic
- Easy to understand overview

---

#### `title_page.pdf`
- Project title page (academic submission)

---

### 🖼️ Images

#### `summary.jpg`
- Visual summary or result snapshot
- Used for presentation or documentation

---

## 🔁 Project Workflow

```text
set1.csv
   ↓
data_clean.py
   ↓
set2.csv
   ↓
ipl.py
   ↓
Probs.csv
   ↓
check_Predict.py
   ↓
Summarize.csv
   ↓
test.py
   ↓
prob2.csv

▶️ How to Run the Project
Step 1: Data Cleaning
python data_clean.py

Step 2: Run Prediction Engine
python ipl.py

Step 3: Evaluate Accuracy
python check_Predict.py

Step 4: Final Validation
python test.py
