# Project Manage Notes

import json
from pathlib import Path

file_name = Path("notes.json")

def load_notes():
    """Load notes from the json file."""
    try:
        with file_name.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_notes(notes):
    """Save notes to JSON file."""
    with file_name.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)


def add_notes(notes):
    """Add notes"""
    title = input("\nEnter note title : ").strip()
    content = input("Enter note content : ").strip()

    if not title or not content:
        print("Title or content can not be empty.")
        return

    notes.append({
        "title" : title,
        "content" : content,
    })

    save_notes(notes)
    print("Notes saved successfully!")


def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"\n{index}, {note["title"]}")
        print(note["content"])


def main():
    notes = load_notes()

    while True:
        print("\n-----Python Notes Manager-----")
        print("1. Add Note...")
        print("2. View Note...")
        print("3. Exit...")

        choice = input("Choice an option : ").strip()

        try:
            if choice == "1":
                add_notes(notes)
            elif choice == "2":
                view_notes(notes)
            elif choice == "3":
                print("Thank you for using Notes Manager")
                break
            else:
                print("Invalid choice. Select between 1-3")

        except OSError as error:
            print(f"\nFile operation failed : {error}")

if __name__== "__main__":
    main()    
                    
              
