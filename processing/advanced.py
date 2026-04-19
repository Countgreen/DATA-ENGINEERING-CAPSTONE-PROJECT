def normalize(df):
    return df / df.max()

def aggregate(df):
    return df.mean()

def validate(df):
    return df.dropna()