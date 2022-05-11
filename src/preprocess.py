import pandas as pd

# Import data
basic = pd.read_csv("data/basic_info.csv")
detailed = pd.read_csv("data/detailed_info.csv")

# Merge the two datasets
df = basic\
    .merge(detailed, on="ID", how="left")

# drop unneeded columns
bad_cols = ['Unnamed: 0_x', 'Unnamed: 0_y']
df = df.drop(bad_cols, axis=1)

# fix column names (replace spaces with underscores; change to lower case)
df.columns = [i.replace(" ", "_").lower() for i in df.columns]

# drop weird "</label>" value in the release_clause field
df["release_clause"] = df["release_clause"]\
    .replace("</label>", None)

# fix datatype of wages and value
df[["wage", "value", "release_clause"]] = df[["wage", "value", "release_clause"]]\
    .replace("(€|K|M)", "", regex=True)\
    .astype("float")
df = df.rename(columns={"wage": "wage_thousands", "value": "value_millions"})

# fix DOB datatype
df["dob"] = pd.to_datetime(df["dob"])

# save processed data
df.to_csv("data/main.csv", index=False)
