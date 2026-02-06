# Vital Signs Validator: A Clinical CI/CD Demo 🏥 🤖

**"Building a Medical Device, Not Just Scripts"**

This repository is a demonstration of **Engineering Protocols** in Clinical Data Science. It simulates a "Digital Safety Net" that prevents bad data from entering a research study.

---

## 📂 1. The Scaffold (The Housing)
Just like a hospital crash cart is organized so anyone can find tools in an emergency, our project follows a strict **Standardized Scaffold**.

| Folder/File | The Clinical Analogy | Purpose |
| :--- | :--- | :--- |
| **`data/`** | **The Specimen Fridge** | Contains raw data (`dummy_patients.csv`). It is strictly read-only to prevent contamination. |
| **`src/`** | **Surgical Instruments** | Contains the Python scripts (`validate_data.py`) that perform the operation. |
| **`.github/`** | **The Safety Robot** | Contains the automation rules that check our work every time we save. |
---

## 🤖 2. The Safety Circuit (CI/CD)
We do not rely on humans to remember safety checks. We rely on **Continuous Integration (CI)**.

* **The Trigger:** Every time you "Push" (save) code to this repository.
* **The Robot:** GitHub Actions wakes up a virtual computer.
* **The Test:** It runs `src/validate_data.py` to check for "Medical Errors" in the data.
* **The Rule:** *If any patient has a Heart Rate > 200, stop the process immediately.*

---

## 🧪 3. Lab Protocol: How to Run This Experiment

Follow these steps to see the "Digital Safety Net" in action.

### **Phase A: The Failure (Catching the Error)**
1.  Navigate to the **`Actions`** tab at the top of this page.
2.  Look at the previous run. You will see a **Red X ❌**.
3.  Click on the failure and look at the logs. You will see:
    > `CRITICAL ERROR: Patient 103 has Heart Rate 450. Impossible value!`
4.  **Conclusion:** The Robot successfully quarantined the bad data.

### **Phase B: The Fix (Treating the Patient)**
1.  Go to the file `data/dummy_patients.csv`.
2.  Click the **Pencil Icon ✏️** to edit the file.
3.  Change Patient 103's heart rate from `450` to a normal value (e.g., `90`).
4.  Scroll down and click **Commit changes** (Save).

### **Phase C: The Success (Discharge)**
1.  Immediately go back to the **`Actions`** tab.
2.  You will see a yellow circle (The Robot is working).
3.  Wait 30 seconds. It will turn into a **Green Check ✅**.
4.  **Conclusion:** The data is now clean, verified, and safe for analysis.

---

## 💰 4. Feasibility Check (Budget)
Before launching this on the cloud, we must prove we can afford it.
* **View the Estimate:** Open (https://calculator.aws/#/addService) to see our AWS calculation.

---

### 📝 Capstone Requirements
For your final Capstone project, you must replicate this structure:
1.  **Organize** your files using this folder structure.
2.  **Protect** your code using a simple GitHub Action.
3.  **Estimate** your costs using the AWS Calculator.
