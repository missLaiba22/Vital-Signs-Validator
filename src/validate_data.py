import sys
import csv

def check_vitals(file_path):
    print("--- STARTING VITAL SIGNS CHECK ---")
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hr = int(row['heart_rate'])
            pid = row['patient_id']

            # Clinical Rule: Heart Rate cannot be > 200
            if hr > 200:
                print(f"CRITICAL ERROR: Patient {pid} has Heart Rate {hr}. Impossible value!")
                sys.exit(1) # This tells GitHub "FAIL" (Red X)

    print("--- ALL CHECKS PASSED. DATA IS CLEAN. ---")
    sys.exit(0) # This tells GitHub "SUCCESS" (Green Check)

if __name__ == "__main__":
    check_vitals('data/dummy_patients.csv')
