from tkinter import *
from tkinter import messagebox, simpledialog
from pathlib import Path
import os

# ---------------- MAIN WINDOW ---------------- #

root = Tk()
root.title("CRUD File Manager")
root.geometry("500x500")
root.config(bg="lightblue")

# ---------------- FUNCTIONS ---------------- #

def show_items():
    listbox.delete(0, END)

    p = Path('.')

    for item in p.rglob('*'):
        listbox.insert(END, item)


# 1. Create File
def create_file():
    file_name = simpledialog.askstring("Create File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "File already exists!")

    else:
        content = simpledialog.askstring("Content", "Enter file content:")

        with open(file_name, 'w') as file:
            file.write(content if content else "")

        messagebox.showinfo("Success", "File created successfully!")

    show_items()


# 2. Read File
def read_file():
    file_name = simpledialog.askstring("Read File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'r') as file:
            content = file.read()

        messagebox.showinfo("File Content", content)

    else:
        messagebox.showerror("Error", "File not found!")


# 3. Update File
def update_file():
    file_name = simpledialog.askstring("Update File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        choice = simpledialog.askinteger(
            "Update Option",
            "Press 1 to Overwrite\nPress 2 to Append"
        )

        content = simpledialog.askstring("Content", "Enter new content:")

        if choice == 1:

            with open(file_name, 'w') as file:
                file.write(content)

            messagebox.showinfo("Success", "Content overwritten!")

        elif choice == 2:

            with open(file_name, 'a') as file:
                file.write(content)

            messagebox.showinfo("Success", "Content appended!")

        else:
            messagebox.showerror("Error", "Invalid choice!")

    else:
        messagebox.showerror("Error", "File not found!")

    show_items()


# 4. Delete File
def delete_file():
    file_name = simpledialog.askstring("Delete File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        os.remove(file_name)

        messagebox.showinfo("Success", "File deleted!")

    else:
        messagebox.showerror("Error", "File not found!")

    show_items()


# 5. Rename File
def rename_file():
    file_name = simpledialog.askstring("Rename File", "Enter current file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        new_name = simpledialog.askstring("Rename", "Enter new file name:")

        p.rename(new_name)

        messagebox.showinfo("Success", "File renamed!")

    else:
        messagebox.showerror("Error", "File not found!")

    show_items()


# 6. Create Folder
def create_folder():
    folder_name = simpledialog.askstring("Create Folder", "Enter folder name:")

    if not folder_name:
        return

    p = Path(folder_name)

    if p.exists():

        messagebox.showerror("Error", "Folder already exists!")

    else:

        p.mkdir()

        messagebox.showinfo("Success", "Folder created!")

    show_items()


# 7. Delete Folder
def delete_folder():
    folder_name = simpledialog.askstring("Delete Folder", "Enter folder name:")

    if not folder_name:
        return

    p = Path(folder_name)

    if p.exists():

        try:
            p.rmdir()
            messagebox.showinfo("Success", "Folder deleted!")

        except:
            messagebox.showerror(
                "Error",
                "Folder is not empty!"
            )

    else:
        messagebox.showerror("Error", "Folder not found!")

    show_items()


# 8. Create File Inside Folder
def create_file_in_folder():

    folder_name = simpledialog.askstring(
        "Folder",
        "Enter folder name:"
    )

    file_name = simpledialog.askstring(
        "File",
        "Enter file name:"
    )

    if not folder_name or not file_name:
        return

    folder_path = Path(folder_name)

    if folder_path.exists():

        file_path = folder_path / file_name

        with open(file_path, 'w') as file:
            content = simpledialog.askstring(
                "Content",
                "Enter file content:"
            )

            file.write(content if content else "")

        messagebox.showinfo(
            "Success",
            "File created inside folder!"
        )

    else:
        messagebox.showerror(
            "Error",
            "Folder does not exist!"
        )

    show_items()


# ---------------- BUTTONS ---------------- #

Button(root, text="Create File", width=25, command=create_file).pack(pady=5)

Button(root, text="Read File", width=25, command=read_file).pack(pady=5)

Button(root, text="Update File", width=25, command=update_file).pack(pady=5)

Button(root, text="Delete File", width=25, command=delete_file).pack(pady=5)

Button(root, text="Rename File", width=25, command=rename_file).pack(pady=5)

Button(root, text="Create Folder", width=25, command=create_folder).pack(pady=5)

Button(root, text="Delete Folder", width=25, command=delete_folder).pack(pady=5)

Button(root, text="Create File in Folder", width=25, command=create_file_in_folder).pack(pady=5)

# ---------------- LISTBOX ---------------- #

listbox = Listbox(root, width=60, height=10)
listbox.pack(pady=20)

show_items()

# ---------------- RUN WINDOW ---------------- #

root.mainloop()