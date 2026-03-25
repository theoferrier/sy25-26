import glob

# Get all .txt files in the directory
files = glob.glob("server_dump/*.txt")

status_counts = {"OK": 0, "WARN": 0, "ERROR": 0}
status_files = {"OK": [], "WARN": [], "ERROR": []}

for filename in files:
    with open(filename, "r") as f:
        content = f.read()
        if "OK" in content:
            status_counts["OK"] += 1
            status_files["OK"].append(filename)
        elif "WARN" in content:
            status_counts["WARN"] += 1
            status_files["WARN"].append(filename)
        elif "ERROR" in content:
            status_counts["ERROR"] += 1
            status_files["ERROR"].append(filename)

print("OK:", status_counts["OK"])
print("WARN:", status_counts["WARN"])
print("ERROR:", status_counts["ERROR"])