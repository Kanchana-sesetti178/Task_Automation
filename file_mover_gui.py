import os
import shutil
import tkinter as tk
from tkinter import messagebox

SOURCE = "Source_Folder"
DESTINATION = "Destination_Folder"

def move_files():
    moved_count = 0

    if not os.path.exists(SOURCE):
        messagebox.showerror("Error", "Source_Folder not found!")
        return

    if not os.path.exists(DESTINATION):
        os.makedirs(DESTINATION)

    output_box.delete("1.0", tk.END)

    for file_name in os.listdir(SOURCE):

        if file_name.lower().endswith(".jpg"):

            source_path = os.path.join(SOURCE, file_name)
            destination_path = os.path.join(DESTINATION, file_name)

            shutil.move(source_path, destination_path)

            output_box.insert(
                tk.END,
                f"Moved: {file_name}\n"
            )

            moved_count += 1

    output_box.insert(
        tk.END,
        f"\nTask Completed!\nTotal JPG Files Moved: {moved_count}"
    )

# Window
root = tk.Tk()
root.title("JPG File Mover")
root.geometry("700x500")
root.configure(bg="#111111")

# Title
title = tk.Label(
    root,
    text="📁 JPG File Mover",
    font=("Segoe UI", 22, "bold"),
    bg="#111111",
    fg="#FFD700"
)
title.pack(pady=20)

# Source Label
source_label = tk.Label(
    root,
    text="Source Folder : Source_Folder",
    bg="#111111",
    fg="white",
    font=("Segoe UI", 11)
)
source_label.pack()

# Destination Label
destination_label = tk.Label(
    root,
    text="Destination Folder : Destination_Folder",
    bg="#111111",
    fg="white",
    font=("Segoe UI", 11)
)
destination_label.pack(pady=5)

# Button
move_button = tk.Button(
    root,
    text="🚀 Move JPG Files",
    command=move_files,
    bg="#FFD700",
    fg="black",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=20,
    pady=10
)
move_button.pack(pady=20)

# Output Box
output_box = tk.Text(
    root,
    height=15,
    width=70,
    bg="#1E1E1E",
    fg="white",
    font=("Consolas", 10)
)
output_box.pack(pady=10)

root.mainloop()