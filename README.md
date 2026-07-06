# Python File Organizer & Gmail Extractor

## 📌 Overview

**Python File Organizer & Gmail Extractor** is a simple automation project built using Python. The program organizes files into separate folders based on their file extensions and extracts unique Gmail addresses from text files.

This project demonstrates the use of Python's file handling, directory management, and built-in modules such as `os` and `shutil`.

## ✨ Features

- 📄 Organizes all `.txt` files into a **Text Files** folder
- 🖼️ Organizes image files (`.jpg`, `.jpeg`, `.png`) into an **Images** folder
- 📧 Extracts Gmail addresses from all text files
- ✅ Removes duplicate email addresses using Python `set`
- 💾 Saves all unique email addresses into `Email.txt`
- ⚠️ Uses exception handling to prevent unexpected crashes

## 📁 Project Structure

```
Python-File-Organizer/
│
├── file_organizer.py
├── README.md
├── .gitignore
│
├── Source/
│   ├── sample.txt
│   ├── image1.jpg
│   ├── image2.png
│   └── notes.txt
│
└── Output/
    ├── Text Files/
    │   ├── sample.txt
    │   └── notes.txt
    ├── Images/
    │   ├── image1.jpg
    │   └── image2.png
    └── Email.txt
```

## 🛠️ Technologies Used

- **Python 3.6+**
- `os` module (directory operations)
- `shutil` module (file operations)
- `re` module (regex for email extraction)
- File Handling & I/O
- Exception Handling
- Set Data Structure

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.6 or higher installed
- Basic understanding of Python
- Read/Write permissions in the source and destination folders

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Python-File-Organizer.git
cd Python-File-Organizer
```

### 2. Update File Paths

Open `file_organizer.py` and modify these variables:

```python
source = r"C:\Users\YourName\Downloads\Source"  # Windows
# OR
source = "/Users/YourName/Downloads/Source"      # macOS/Linux

destination = r"C:\Users\YourName\Downloads\Output"  # Windows
# OR
destination = "/Users/YourName/Downloads/Output"     # macOS/Linux
```

**Note:** Use raw strings (`r""`) for Windows paths to avoid escape character issues.

### 3. Run the Program

```bash
python file_organizer.py
```

## 📖 Usage Example

### Input Structure

```
Source/
├── Contacts.txt
├── Notes.txt
├── photo.jpg
├── logo.png
└── holiday.jpeg
```

### Output Structure

```
Output/
├── Text Files/
│   ├── Contacts.txt
│   └── Notes.txt
├── Images/
│   ├── photo.jpg
│   ├── logo.png
│   └── holiday.jpeg
└── Email.txt
```

### Sample Email.txt Output

```
john.doe@gmail.com
jane.smith@gmail.com
contact.info@gmail.com
```

## 📚 Concepts Demonstrated

This project covers fundamental Python concepts:

- **File Handling** - Reading and writing files
- **Directory Management** - Creating folders and moving files
- **Path Manipulation** - Using `os.path` for cross-platform compatibility
- **Exception Handling** - Try-except blocks for error prevention
- **Regular Expressions** - Email pattern matching with `re` module
- **Data Structures** - Sets for duplicate removal
- **Loops & Conditionals** - Iterating through files and filtering
- **String Operations** - Text processing and manipulation

## ⚙️ How It Works

1. **Read Source Folder** - Scans all files in the source directory
2. **Organize Files** - Creates folders (Text Files, Images) and moves files based on extensions
3. **Extract Emails** - Opens `.txt` files and finds all Gmail addresses using regex
4. **Remove Duplicates** - Uses Python `set` to eliminate duplicate emails
5. **Save Results** - Writes unique emails to `Email.txt` in the output folder

## 🔍 Supported File Types

### Text Files
- `.txt`

### Images
- `.jpg`
- `.jpeg`
- `.png`

**Want to add more?** Modify the file extension lists in the code!

## ⚠️ Error Handling

The program handles common errors gracefully:

- **Permission Denied** - If you don't have read/write access
- **File Not Found** - If the source folder doesn't exist
- **Corrupted Files** - Skips files that can't be read
- **Invalid Paths** - Validates folder paths before processing

## 🔮 Future Improvements

- [ ] Support additional file types (`.pdf`, `.docx`, `.mp4`, `.zip`, etc.)
- [ ] Auto-create folders for every file extension
- [ ] Extract emails from all providers (not just Gmail)
- [ ] Add GUI using Tkinter or PyQt
- [ ] Allow runtime path input via command-line arguments
- [ ] Add logging functionality
- [ ] Create configuration file for settings
- [ ] Add progress bar for large file operations

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Module not found** | Ensure Python 3.6+ is installed: `python --version` |
| **Permission Denied** | Check folder permissions and run as administrator if needed |
| **No Email.txt created** | Verify `.txt` files contain valid Gmail addresses |
| **Files not moving** | Check that source and destination paths are correct |


## 📄 License

This project is open source and available under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**SARAN**
- Python Developer
- Cybersecurity Enthusiast
- [GitHub](https://github.com/saran-2101)
- [Email](mailto:saran2101selvam@gmail.com)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork this repository
- Create a new branch for your feature
- Submit a pull request

## 📞 Support

If you encounter any issues or have questions, feel free to:
- Open an issue on GitHub
- Contact the author
- Check the troubleshooting section above

---

**Made with ❤️ by SARAN**
