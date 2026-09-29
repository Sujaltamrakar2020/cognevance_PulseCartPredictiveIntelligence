# Project Architecture

```text
CSV dataset
   |
   v
src/preprocess.py
   |
   +----> cleaned CSV
   |
   +----> SQLite database
   |
   +----> SQL analysis
   |
   v
src/train_models.py
   |
   +----> repeat-purchase model
   +----> revenue benchmark model
   |
   v
dashboard/app.py
   |
   v
Interactive analytics dashboard
```

## Beginner technology stack
- Python
- pandas
- NumPy
- SQLite
- scikit-learn
- Plotly
- Streamlit
- Power BI (optional dashboard recreation)
- GitHub
