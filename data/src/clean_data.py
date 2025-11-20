import pandas as pd
import re
import os

# =======================================================
#             DATA CLEANING HELPER FUNCTIONS
# =======================================================

def clean_cardcode(value):
    """
    Converts any CardCode like:
    C0001, C0002!, C0003$, 001, 1, A12
    → Into proper format: C001, C002, C003

    Steps:
    1. Remove everything except digits
    2. Pad numbers to 3 digits
    3. Add 'C' prefix
    """
    numbers = re.sub(r"[^0-9]", "", str(value))
    if numbers == "":
        return "INVALID"
    return "C" + numbers.zfill(3)


def clean_cardname(value):
    """
    CardName must contain:
    - Alphabet letters only
    - No quotes, no symbols, no numbers
    - First letter capitalized

    Example:
    Mary"DoubleQuotes" → Mary Doublequotes
    Omega'Quotes' → Omega Quotes
    """
    value = re.sub(r"[^A-Za-z ]", "", str(value))  # keep letters & space only
    value = value.strip()
    return value.title() if value else "INVALID"


def clean_email(email):
    """
    Fixes emails by:
    - Removing illegal characters: " ' ! $ &
    - Correcting wrong domains:
         mails.com → gmail.com
         test.com → outlook.com
         example.com → yahoo.com
    - Ensures email remains <username>@<domain>
    """
    email = str(email)

    # Remove unwanted characters
    email = re.sub(r"[\"'!$&]", "", email)

    # Ensure email contains '@'
    if "@" not in email:
        return "INVALID"

    username, domain = email.split("@")[0], email.split("@")[1]

    # Fix common domain mistakes
    domain = domain.replace("mails.com", "gmail.com")
    domain = domain.replace("test.com", "outlook.com")
    domain = domain.replace("example.com", "yahoo.com")

    # Remove any remaining bad chars
    domain = re.sub(r"[^A-Za-z0-9.]", "", domain)

    return f"{username}@{domain}"


def clean_phone(phone):
    """
    Phone must be:
    - Only digits
    - Exactly last 10 digits (remove +91, hyphens, spaces)
    
    Example:
    +91-9881396850 → 9881396850
    """
    phone = re.sub(r"[^\d]", "", str(phone))  # keep digits only
    return phone[-10:] if len(phone) >= 10 else "INVALID"


def clean_fax(fax):
    """
    Fax must follow format:
       +<country>-<area>-<number>

    Steps:
    1. Extract digits only
    2. Country code = first 2 digits
    3. Area code = next 4 digits
    4. Remaining digits = fax number
    """
    digits = re.sub(r"[^\d]", "", str(fax))

    if len(digits) < 8:
        return "INVALID"

    cc = digits[:2]      # country code
    area = digits[2:6]   # area code
    num = digits[6:]     # fax number

    return f"+{cc}-{area}-{num}"


def clean_balance(value):
    """
    Removes all symbols except digits and decimal:
    31727USD → 31727
    693USD → 693
    """
    cleaned = re.sub(r"[^0-9.]", "", str(value))
    return cleaned if cleaned else "0"


def clean_address(value):
    """
    Address allows:
    - Alphabets
    - Numbers
    - Spaces
    - Commas
    
    Removes all quotes and special characters.
    """
    return re.sub(r"[^A-Za-z0-9 ,]", "", str(value)).strip()


# =======================================================
#                 MAIN PROGRAM LOGIC
# =======================================================

def main():
    print("Scanning 'data/' folder for Excel files...")

    # 1. List all .xlsx files inside /data folder
    files = [f for f in os.listdir("data") if f.endswith(".xlsx")]

    if not files:
        print("No Excel (.xlsx) files found inside data/ folder.")
        return

    print("\nFound the following files:")
    for f in files:
        print(" -", f)

    # 2. User chooses which file to clean
    filename = input("\nEnter the EXACT file name you want to clean: ")

    filepath = f"data/{filename}"

    if not os.path.exists(filepath):
        print("The file does NOT exist. Check name and try again.")
        return

    print("\nLoading file:", filename)

    # 3. Read the Excel file
    df = pd.read_excel(filepath, engine="openpyxl")

    print("Cleaning data...")

    # 4. Apply cleaning as per available columns
    if "CardCode" in df:     df["CardCode"] = df["CardCode"].apply(clean_cardcode)
    if "CardName" in df:     df["CardName"] = df["CardName"].apply(clean_cardname)
    if "E_Mail" in df:       df["E_Mail"] = df["E_Mail"].apply(clean_email)
    if "Phone1" in df:       df["Phone1"] = df["Phone1"].apply(clean_phone)
    if "Fax" in df:          df["Fax"] = df["Fax"].apply(clean_fax)
    if "Balance" in df:      df["Balance"] = df["Balance"].apply(clean_balance)
    if "Address" in df:      df["Address"] = df["Address"].apply(clean_address)

    # 5. Generate a cleaned filename automatically
    base_name = filename.replace(".xlsx", "")
    output_name = base_name + "_cleaned.xlsx"

    output_path = f"data/{output_name}"

    print("\nSaving cleaned file as:", output_name)

    # 6. Write a cleaned Excel file
    df.to_excel(output_path, index=False, engine="openpyxl")

    print("\n🎉 Cleaning completed successfully!")
    print("Output saved at:", output_path)


# =======================================================
#            RUN MAIN FUNCTION WHEN FILE EXECUTES
# =======================================================

if __name__ == "__main__":
    main()
