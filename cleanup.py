# Import libraries
import glob
import pandas as pd

# Get all the data in a DataFrame
df = pd.concat(map(pd.read_csv, glob.glob('./data' + "/*.csv")))

# Take only the "pink morsel" data
df = df[df['product'] == "pink morsel"].reset_index(drop=True)

# Make a Sales column
df["sales"] = df["price"].str[1:].astype('float32') * df["quantity"]
df.drop(["product", "price", "quantity"], axis=1, inplace=True)

# Save the file
df.to_csv("./data/pink_morsel.csv", index=False)
