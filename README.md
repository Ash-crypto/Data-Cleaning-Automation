# Data-Cleaning-Automation

A Python-based data cleaning automation tool designed to clean and transform unstructured Excel datasets into clean, structured files ready for SAP B1 DTW import or any downstream processing.

This project showcases backend data handling, Python automation, regex-based transformations, and dynamic file processing.

---

## 🚀 Features

* Clean ANY Excel file dynamically (no hardcoded filename)
* Fixes messy customer/vendor master data
* Cleans:

  * CardCode → Converts to standard format (C001, C002, ...)
  * CardName → Removes special characters, capitalizes properly
  * Email Fixing → Corrects wrong domains, removes illegal symbols
  * Phone Numbers → Extracts valid 10-digit numbers
  * Fax → Converts to +CC-AREA-NUMBER format
  * Balance → Removes currencies & symbols, keeps numeric values
  * Address → Allows only alphabets, digits, spaces, commas
* Automatically generates output filenames:

  * `raw_data.xlsx` → `raw_data_cleaned.xlsx`
  * `sap_unstructured.xlsx` → `sap_unstructured_cleaned.xlsx`
* Protects previous outputs—no overwriting
* Works for unlimited files inside the `/data` folder

---

## 🧠 Tech Stack

**Language:** Python 3.8+
**Libraries:** Pandas, OpenPyXL, Regex (re)
**Environment:** VS Code
**Version Control:** Git + GitHub

---

## 📂 Project Structure

```
Data-Cleaning-Automation/
│
├── src/
│   └── clean_data.py        # Main data cleaning script
│
├── data/
│   ├── raw_data.xlsx        # (User uploads unstructured file here)
│   └── *anyname.xlsx        # Script detects all files
│
├── LICENSE                  # All Rights Reserved License
└── README.md                # Project documentation
```

---

## 🛠 How to Use

### **Step 1 — Place your raw Excel file**

Put ANY unstructured file inside:

```
data/
```

Example:

```
raw_data.xlsx
sapb1_unstructured.xlsx
vendor_list.xlsx
```

---

### **Step 2 — Run the script**

In terminal (inside project root):

```
python src/clean_data.py
```

---

### **Step 3 — Select the filename**

Script will list all files in the `data` folder.
You type the exact filename you want to clean.

Example:

```
Enter the file name to clean: raw_data.xlsx
```

---

### **Step 4 — Get the cleaned output**

The cleaned file will be saved as:

```
raw_data_cleaned.xlsx
sapb1_unstructured_cleaned.xlsx
```

inside the same `data/` folder.

---

## 🧽 Cleaning Rules Applied

### ✔ CardCode

* Removes symbols
* Keeps digits only
* Converts to `C001`, `C002`, ...

### ✔ CardName

* Removes numbers & special characters
* Converts to Proper Case

### ✔ Email

* Removes illegal characters (`"'!$&`)
* Fixes wrong domains:

  * mails.com → gmail.com
  * test.com → outlook.com
  * example.com → yahoo.com

### ✔ Phone

* Removes +91, spaces, hyphens
* Extracts last 10 digits

### ✔ Fax

Format:

```
+CC-AREA-NUMBER
```

### ✔ Balance

* Removes USD, INR, EUR
* Keeps digits and decimals only

### ✔ Address

* Allows letters, digits, spaces, commas
* Removes quotes & special characters

---

## 📌 Example Before & After

### **Before:**

```
CardCode: C0002!
CardName: Global"DoubleQuotes"
E_Mail: global"doublequotes"@test.com
Phone1: +91-6092582489
Balance: 10496.72USD
```

### **After:**

```
CardCode: C002
CardName: Global Doublequotes
E_Mail: globaldoublequotes@outlook.com
Phone1: 6092582489
Balance: 10496.72
```

---

## 📜 License

This project is **NOT open source**.
All rights reserved © 2025 **Ashwini Khandare**.

Unauthorized copying, modification, or reuse of the code is strictly prohibited.
This repository is public only for **portfolio and recruiter evaluation purposes**.

---

## 📧 Contact

**Author:** Ashwini Khandare
**Email:** [akhandare981@gmail.com](mailto:akhandare981@gmail.com)
**GitHub:** [https://github.com/Ash-crypto](https://github.com/Ash-crypto)
**LinkedIn:** [https://www.linkedin.com/in/ashwini-khandare-176ba91bb](https://www.linkedin.com/in/ashwini-khandare-176ba91bb)

---

