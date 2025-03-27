import pandas as pd

file_path = r"C:\Users\Yogin\dev10-classwork\week-08\assessment\boardGameData_team4\boardgames_ranks.csv"

df = pd.read_csv(file_path)

df.fillna(0, inplace=True)

output_path = r"C:\Users\Yogin\dev10-classwork\week-08\assessment\boardGameData_team4\boardgames_ranks_cleaned.csv"
df.to_csv(output_path, index=False)

