# AutoEDA – AI Powered Data Quality Check 🧠📊

AutoEDA is an intelligent data quality assistant that automates Exploratory Data Analysis (EDA) on CSV files using Generative AI. It scans one or more datasets from a folder and produces detailed, file-specific suggestions in simple language. The system highlights outliers, missing values, data types, and more — offering tailored, actionable insights to help analysts clean and prepare their data efficiently.

---

## 🚀 Features

- 📁 **Folder-wise CSV Analysis**: Pass a folder path to analyze multiple CSVs at once.
- 📊 **Comprehensive EDA**: Detects missing values, outliers, duplicates, correlations, datatypes, and more.
- 🧠 **AI-Powered Recommendations**: Uses Gemini model to generate human-readable, file-specific suggestions (no generic output).
- 💡 **10 Tailored Suggestions**: Outputs exactly 10 clean, understandable, and meaningful data quality insights per file.
- 📝 **Report Generation**: Saves results in a markdown report under `/reports/` with timestamped filenames.

---

## 🎯 Objective

To assist data analysts, scientists, and ML engineers in quickly evaluating and preparing raw data by automating the EDA process and identifying potential data quality issues in a human-understandable format.

---

## 🛠️ How It Works

1. **Agent Setup**: A custom `EDAAgent` is defined using CrewAI and Google's Gemini model.
2. **Tool Execution**: For each CSV in the given folder, data profiling is done (e.g., nulls, outliers, types).
3. **LLM Understanding**: Results are passed to Gemini to interpret and write 10 useful suggestions.
4. **Report Generation**: Summary is saved as `analysis_<timestamp>.md` inside `/reports`.

   
## Tech Stack
1.**Python 3.10+**
2.**CrewAI**
3.**Google Gemini LLM**
4.**Pandas**
5.**dotenv**
