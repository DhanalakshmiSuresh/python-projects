# Requires: pip install pandas
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)
print("Average Score:", df["Score"].mean())