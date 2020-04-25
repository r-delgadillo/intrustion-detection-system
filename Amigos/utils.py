import pandas as pd

def read_csv_chunked(filepath):
    """
        This method is used to prevent memory issues
        with large filed csv files. It will incrementally read
        the csv file rather than reading the whole file in memory
        at once.
    """
    print('-------------------------------------------------------')
    data_frames = []
    
    print(f"Reading file {filepath}")
    # Read the csv file in chunks. Chunksize was chosen arbitrarily 
    for chunk in pd.read_csv(filepath, iterator=True, chunksize= 1000000):
        # append the chunks to array of data frames
        data_frames.append(chunk)
    
    # Combine the data frames into single one and return the result
    df = pd.concat(data_frames)
    
    print(f"Number of rows and columns {df.shape}")

    return df


# Read rows from data frame
# df.loc[0:2]

# Print columns values in data frame
# df["column1"]

# Print column values
# df["column1"].values

# Convert columns values to list
# df["column1"].tolist()

############################## Inspecting DataFrames #################################
# Summary
# df.info()

# Get the list of columns
# df.columns
# df.columns.tolist()

# Get the index
# data_df.index

# Sneak peek, prints out first 5 cases
# df.head()

# Sneak peek, prints out last 5 cases
# df.tail()

# Summary statistics - gives mean, std, min, max, etc
# df.describe()

# Print the value of 75% of the data
# df.describe().loc["75%"]

# Number of tows in a dataframe
# len(df)

# Number of rows in a column
# len(df["column1"])

# Print available objects in data frame
# dir(df)

# Print help
# help(df.loc)

# Print unique values
# df["column1"].unique()

############################## Filtering data #################################
# Check if something is contained in something
# df["column1"].str.contains("Fog")
# df["column1"].str.contains("Fog").mean()
# df["column1"].str.contains("Fog").head()


# Find rows that has weather value as "Fog"
# df[df["column1"] == "Fog"]

# df[(df["column1"] > 10) & (df["column2"].isin(["Cloudy"]))]