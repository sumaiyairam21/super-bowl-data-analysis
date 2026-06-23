import pandas as pd
data = {
    "Team": ["Chiefs", "Patriots", "Eagles"],
    "Wins": [4, 6, 2]
}

df = pd.DataFrame(data)

print(df)

top_team = df.loc[df["Wins"].idxmax()]

print("Most successful team:", top_team["Team"])
