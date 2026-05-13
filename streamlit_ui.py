from pathlib import Path
import os
import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CRUD File Manager",
    page_icon="📁",
    layout="centered"
)

st.title("📁 CRUD File Manager")

# ---------------- SHOW FILES & FOLDERS ---------------- #

st.subheader("Current Files & Folders")

p = Path('.')

items = list(p.rglob('*'))

if items:
    for item in items:
        st.write(item)
else:
    st.info("No files or folders found.")


# ---------------- SIDEBAR MENU ---------------- #

option = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder",
        "Create File in Folder"
    ]
)


# ---------------- 1. CREATE FILE ---------------- #

if option == "Create File":

    st.header("Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("File already exists!")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("File created successfully!")


# ---------------- 2. READ FILE ---------------- #

elif option == "Read File":

    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, 'r') as file:
                st.text(file.read())

        else:
            st.error("File not found!")


# ---------------- 3. UPDATE FILE ---------------- #

elif option == "Update File":

    st.header("Update File")

    file_name = st.text_input("Enter file name")

    update_option = st.radio(
        "Choose Update Option",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if update_option == "Overwrite":

                with open(file_name, 'w') as file:
                    file.write(content)

                st.success("File overwritten successfully!")

            elif update_option == "Append":

                with open(file_name, 'a') as file:
                    file.write(content)

                st.success("Content appended successfully!")

        else:
            st.error("File not found!")


# ---------------- 4. DELETE FILE ---------------- #

elif option == "Delete File":

    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(file_name)

            st.success("File deleted successfully!")

        else:
            st.error("File not found!")


# ---------------- 5. RENAME FILE ---------------- #

elif option == "Rename File":

    st.header("Rename File")

    old_name = st.text_input("Enter current file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("File renamed successfully!")

        else:
            st.error("File not found!")


# ---------------- 6. CREATE FOLDER ---------------- #

elif option == "Create Folder":

    st.header("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():

            st.error("Folder already exists!")

        else:

            p.mkdir()

            st.success("Folder created successfully!")


# ---------------- 7. DELETE FOLDER ---------------- #

elif option == "Delete Folder":

    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            try:
                p.rmdir()
                st.success("Folder deleted successfully!")

            except:
                st.error("Folder is not empty!")

        else:
            st.error("Folder not found!")


# ---------------- 8. CREATE FILE IN FOLDER ---------------- #

elif option == "Create File in Folder":

    st.header("Create File in Folder")

    folder_name = st.text_input("Enter folder name")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        folder_path = Path(folder_name)

        if folder_path.exists():

            file_path = folder_path / file_name

            with open(file_path, 'w') as file:
                file.write(content)

            st.success("File created inside folder!")

        else:
            st.error("Folder does not exist!")