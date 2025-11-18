import pandas as pd
import re
def clean_text(value):
    if pd.isna(value):
        return value

    value = str(value).strip()

    # Remove special characters
    value = re.sub(r"[^a-zA-Z0-9@\.\s]", "", value)

    # Replace multiple spaces with single space
    value = re.sub(r"\s+", " ", value)

    return value
def clean_email(email):
    if pd.isna(email):
        return email

    email = email.lower().strip()

    # Basic email validation
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return email

    return ""
def clean_dataset(df):
    for column in df.columns:
        if "email" in column.lower():
            df[column] = df[column].apply(clean_email)
        else:
            df[column] = df[column].apply(clean_text)
    
    # Remove duplicate rows
    df = df.drop_duplicates()

    return df
def main():
    print("Loading raw data...")
    df = pd.read_excel("data/raw_data.xlsx")

    print("Cleaning data...")
    cleaned_df = clean_dataset(df)

    print("Saving cleaned file...")
    cleaned_df.to_excel("data/cleaned_data.xlsx", index=False)

    print("Cleaning completed successfully!")

if __name__ == "__main__":
    main()

