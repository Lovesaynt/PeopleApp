# PeopleApp — CLI Person Manager

![status](https://badgen.net/badge/status/active/green)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![build](https://img.shields.io/badge/build-PyInstaller-orange)

PeopleApp is a command-line application written in Python for managing a person registry using a `.txt` file. The program supports creating, listing, editing, viewing, and deleting records with automatic file and directory creation.

> **Note:** This is an early project from my Python learning journey. It contains imperfections that I've intentionally preserved as a record of my beginnings.

## 🗂 Storage Structure

The program automatically creates the following structure:

```bash
C:\Users\<User>\Documents\PessoaApp
│
└── pessoas.txt
```

Line format:
```
Name;Age;Weight;Height;Gender;Marital Status;Nationality;
```

## 📁 Project Structure

```bash
PessoaApp/
│
├── pplmanager.py          # Main script
├── arquivos/              # CRUD and file manipulation functions
└── pessoas.txt            # Created automatically
```

## 🛠 Technologies Used

- Python 3
- PyInstaller
- Text file manipulation

## 🔐 Error Handling

The application handles:

- Invalid menu selections
- Non-numeric input where numbers are expected
- Out-of-range record IDs
- Missing files (auto-created)
- Missing directories (auto-created)
- Invalid numeric fields
- Empty values preserve original data

## 📄 License

This project is distributed under the MIT License.

---

**Developed by:** Lovesaynt
