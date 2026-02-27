# 🚀 Streamlit Basics Demo

A comprehensive demonstration of Streamlit's core display functions, featuring a premium dark-themed UI and interactive data components.

## 📋 Features Covered
- **Core Display Functions**: `st.write`, `st.title`, `st.header`, `st.subheader`, `st.markdown`, `st.caption`, `st.code`.
- **Data Visualization**: `st.dataframe` (Interactive), `st.table` (Static).
- **KPI Reporting**: `st.metric` with delta indicators.
- **Media & Structure**: `st.image` and `st.json` viewer.

---

## 🛠️ Setup and Installation

Since `streamlit` was not found in your global path, it's recommended to install it using `python3 -m pip`.

### 1. Install Dependencies
Run the following command in your terminal to install Streamlit and its requirements:

```bash
python3 -m pip install -r requirements.txt
```

### 2. Run the Application
After installation, launch the app using:

```bash
python3 -m streamlit run basics.py
```

---

## 📁 Project Structure
- `basics.py`: Main application code with all Streamlit display examples.
- `requirements.txt`: List of dependencies (Streamlit, Pandas, NumPy).
- `banner.png`: Generated asset used for the `st.image` demonstration.

## 💡 Troubleshooting
If you still see "command not found", ensure you are using the full python path as shown above:
`python3 -m streamlit run basics.py`
