# 🎓 Student Result Management System

A desktop application built with **Python (Tkinter)** and **SQLite** that lets an
administrator manage student academic records — adding, updating, deleting and
searching students, while automatically calculating totals, percentage, grade
and pass/fail status.

Built as a hands-on project to practice **GUI development, database design,
and clean code organization** in Python.

---

## ✨ Features

- 🔐 **Secure admin login** — passwords are stored as SHA-256 hashes, not plain text
- ➕ **Add student records** with roll number, name, class and marks for 5 subjects (English, Mathematics, Science, Social Science, Hindi — standard 10th/12th board subjects)
- ✏️ **Update existing records** by selecting a row from the table
- 🗑️ **Delete records** with a confirmation prompt
- 🔍 **Search by Roll Number**
- 📊 **Automatic result calculation** — total marks, percentage, grade (A+ to F), and pass/fail status
- 📋 **All records displayed in a sortable, scrollable table**
- 📁 **Export all records to CSV** for use in Excel or Google Sheets
- ✅ **Input validation** on every field (empty values, invalid marks, duplicate roll numbers, etc.)
- 💬 **Clear success/error messages** for every action
- 🎨 **Modern, clean GUI** with a consistent color theme
- 📐 **Responsive window layout** that resizes gracefully

---

## 🛠️ Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| Language   | Python 3               |
| GUI        | Tkinter (standard library) |
| Database   | SQLite3 (standard library) |
| Data Export| CSV (standard library) |

No external/third-party packages are required — everything runs on Python's
standard library, which makes the project easy to set up and run anywhere.

---

## 📂 Project Structure

```
student-result-management-system/
│
├── main.py                     # Application entry point
│
├── database/
│   ├── db_manager.py           # All SQLite setup and CRUD operations
│   └── results.db              # Auto-created on first run (not committed to git)
│
├── gui/
│   ├── login_window.py         # Admin login screen
│   ├── main_window.py          # Main dashboard (form, table, actions)
│   └── styles.py                # Shared colors and fonts
│
├── utils/
│   ├── validators.py            # Input validation functions
│   └── grade_calculator.py      # Total / percentage / grade / pass-fail logic
│
├── seed_data.py                # Optional: fills the database with sample students
├── requirements.txt
├── .gitignore
└── README.md
```

This separation (GUI / database / utils) keeps each file focused on a single
responsibility, which makes the project easier to read, extend and debug.

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher installed on your system
- Tkinter (included with most Python installations by default)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/codingdivyanshi/Student-Result-Management-System.git
   cd student-result-management-system
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Run the application**
   ```bash
   python main.py
   ```
   The SQLite database (`database/results.db`) is created automatically the
   first time you run the app.

4. **Login with the default admin account**
   ```
   Username: admin
   Password: admin123
   ```

5. **(Optional) Load sample student data**
   To see the app with realistic data already in the table (useful for demos
   or screenshots), run:
   ```bash
   python seed_data.py
   ```
   This adds ~75 randomly generated student records covering a realistic
   mix of grades and a small number of pass/fail cases.

---

## 🖥️ Usage

1. Log in with the admin credentials.
2. Fill in the student's roll number, name, class, and marks for each subject, then click **Add Student**.
3. Click any row in the table to load it into the form — edit the values and click **Update Student**, or click **Delete Student** to remove it.
4. Use the **Search** box to quickly find a student by roll number.
5. Click **Export to CSV** to save all records as a spreadsheet-friendly file.

---

## 📸 Screenshots

> _Add screenshots of the running application here once available._

| Login Screen | Dashboard |
|--------------|-----------|
| ![Login Screen](assets/screenshots/login.png) | ![Dashboard](assets/screenshots/dashboard.png) |

---

## 🔮 Future Improvements

- [ ] Multiple admin accounts with a "Register Admin" screen
- [ ] Editable/configurable subject list instead of a fixed set of 5 subjects
- [ ] Generate individual student report cards as PDF
- [ ] Search/filter by name or class, not just roll number
- [ ] Data visualization (charts for class-wise average, pass/fail ratio, etc.)
- [ ] Dark mode toggle
- [ ] Package the app into a standalone `.exe` using PyInstaller

---

## 🎯 What This Project Demonstrates

- Structuring a multi-file Python application (separation of concerns)
- Building a functional GUI with Tkinter (forms, tables, dialogs)
- Working with SQLite for persistent data storage (CRUD operations)
- Writing input validation and handling errors gracefully
- Basic security practice: hashing passwords instead of storing them as plain text

---

## 👤 Author

**Divyanshi Pandey**

## 👤 Connect

| GitHub | LinkedIn |
|--------|----------|
| [![GitHub](https://img.shields.io/badge/GitHub-Visit%20Profile-181717?style=for-the-badge&logo=github)](https://github.com/codingdivyanshi) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-View%20Profile-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/divyanshi-pandey-a36075423) |

---

## 📄 License

This project is open-source and available for learning purposes. Feel free to
fork it, build on it, and use it in your own portfolio.
