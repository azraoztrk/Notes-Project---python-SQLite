# Notes App

A simple Python Notes Application to add, list, delete, and search notes.  
Each note is automatically tagged with the date it was created.  

## Features

- ➕ **Add Note:** Add a new note with the current date automatically included.
- 🗒️ **List Notes:** View all notes with their creation dates.
- 🗑️ **Delete Note:** Remove any note by choosing its number.
- 🔍 **Search Notes:** Search notes by keyword (case-insensitive) using regex.
- ✅ **Persistent Storage:** All notes are saved to `notesList.json` automatically.

## How to Use

1. Run the program: `python notesApp.py`
2. Follow the menu options:
   - 1: Add Note
   - 2: List Notes
   - 3: Delete Note
   - 4: Search Notes
   - 5: Exit

All changes are saved automatically to `notesList.json`.

## Requirements

- Python 3.x
