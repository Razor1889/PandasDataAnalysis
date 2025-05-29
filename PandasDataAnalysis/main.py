
import pandas as pd
import matplotlib.pyplot as plt

def versionCheck():
    print("Pandas Version: " + pd.__version__)

#General data Input into DF
#Simple example to create a manual df
def manualDataFrameTest():
    myData = {
        'Fruit': ["Apple", "Orange", "Banana"],
        'Rating': ["8", "6", "9"]
    }
    myDataSet = pd.DataFrame(myData)
    printDF(myDataSet)

def dfFromJSON(filename):
    df = pd.read_json(filename)
    return df

def dfFromCSV(filename):
    df = pd.read_csv(filename)
    return df

#Simple Analysis and Lookup Functions
#Print Dataframe
def printDF(df: pd.DataFrame):
    #print(df)   This returns only top and bottom 5(based on pandas options)
    print(df.to_string())

#Extract a row (prints as a single (column))
#Assumes non-named normal indexes (0->infinity)
def extractRow(df: pd.DataFrame, rowNumber):
    print("DataFrame row number: ", rowNumber)
    print(df.loc[rowNumber])


#Return top limit number of entries(rows)
def quickHead(df: pd.DataFrame, limit):
    print(df.head(limit))

#Return bottom limit number of entries(rows)
def quickTail(df: pd.DataFrame, limit):
    print(df.tail(limit))

#Return general information of column names, datatypes, memory usage, NON_NULL COLUMNS etc.
def dataInfo(df: pd.DataFrame):
    print(df.info())

#Functions to Clean Data
#Remove empty cells (rows with null data, only good for large datasets)
def removeNullCellRows(df: pd.DataFrame):
    new_df = df.dropna()
    #return df.dropna(inplace=True)    Use this if you want to manipulate the original dataset
    return new_df                      #This returns a new df

#Replace empty cells with (value)
def replaceNullCellRows(df: pd.DataFrame, value):
    new_df = df.fillna(value)
    #df.fillna({"ColumnName": value}) Use this if you want to replace nulls for a specific column
    return new_df

def replaceNullCellWithColMean(df: pd.DataFrame, colName):
    mean = df[colName].mean()
    new_df = df.fillna({colName: mean})
    return new_df

def replaceNullCellWithColMode(df: pd.DataFrame, colName):
    mode = df[colName].mode()[0]
    new_df = df.fillna({colName: mode})
    return new_df

def replaceNullCellWithColMedian(df: pd.DataFrame, colName):
    median = df[colName].median()
    new_df = df.fillna({colName: median})
    return new_df

def formatDate(df: pd.DataFrame, dateCol):
    df[dateCol] = pd.to_datetime(df[dateCol], errors='coerce')
    #Non-Date entries turn into Not a Time (NaT) values, they handle as null so remove them after.
    return df


def boundToColRange(df: pd.DataFrame, colName, min, max):
    #Convert to numeric, turn errors into NaN
    df[colName] = pd.to_numeric(df[colName], errors='coerce')
    #Apply Range (between min and max)
    df[colName] = df[colName].clip(lower=min, upper=max)
    return df

def deleteOutOfColRange(df: pd.DataFrame, colName, max, min):
    for i in df.index:
        if df.loc[i, colName] > max:
            df.drop(i, inplace=True)
        if df.loc[i, colName] < min:
            df.drop(i, inplace=True)
    return df

def deleteDuplicates(df: pd.DataFrame):
    print("Duplicate rows: ", df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    return df

def correlation(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include='number')
    #Ignores non-numeric columns
    #Shows the correlation between data across columns.
    print("Correlation:\n", numeric_df.corr())

def plotDF(df: pd.DataFrame):
    df.plot()
    plt.show()

def plotScatter(df: pd.DataFrame, xcol, ycol):
    df.plot(kind='scatter', x=xcol, y=ycol)
    plt.show()

def plotHistogram(df: pd.DataFrame, colName):
    df[colName].plot(kind='hist')
    plt.show()

#Example Run that incorporates usage
versionCheck()

print("\n-- Manual DataFrame Test --")
manualDataFrameTest()

print("\n-- Original DataFrame --")
df = dfFromCSV('data.csv')
printDF(df)

print("\n-- Data Info --")
dataInfo(df)

print("\n-- Extract Row 1 --")
extractRow(df, 1)

print("\n-- Head(3) --")
quickHead(df, 3)

print("\n-- Tail(3) --")
quickTail(df, 3)

print("\n-- Replace Nulls with 'Unknown' --")
df_unknowns = replaceNullCellRows(df, 'Unknown')
printDF(df_unknowns)

print("\n-- Replace Null Score with Mean --")
df_mean = replaceNullCellWithColMean(df, 'Score')
printDF(df_mean)

print("\n-- Format Date Column --")
df_formatted = formatDate(df, 'Date')
printDF(df_formatted)

print("\n-- Drop Invalid Dates --")
df_cleaned = removeNullCellRows(df_formatted)
printDF(df_cleaned)

print("\n-- Correlation --")
correlation(df_cleaned)

print("\n-- Plot Histogram of Score --")
plotHistogram(df_cleaned, 'Score')