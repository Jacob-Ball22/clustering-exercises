#df_summary function gives a look into the data we will be using
def df_summary(df):
    #Shows the columns and the amount of non-null data in them
    print("Info:")
    print(df.info(show_counts=True))
    #Gives statistical descriptions for the data
    print("\nDescribe:")
    print(df.describe())
    #Gives a sorted count of the amount that is in each gender for the data
    print("\nGender Counts:")
    return df['Gender'].value_counts(sort=True)