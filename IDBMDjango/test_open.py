file_path = r"D:\IDBM Django Study\name.basics1.tsv"

try:
    with open(file_path, encoding="utf-8") as f:
        print("✅ File opened successfully!")
        print(f.readline())  # Print just one line
except Exception as e:
    print("❌ Error opening file:", e)