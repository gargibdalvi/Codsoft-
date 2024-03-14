import tkinter as tk
from tkinter import messagebox

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Please enter a name.")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"{name} has been added to your contacts.")
    clear_entries()

# Function to view all contacts
def view_contacts():
    if not contacts:
        messagebox.showinfo("Info", "Your contacts list is empty.")
    else:
        contact_list = "\n".join([f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n{'-'*20}" 
                                  for name, details in contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().lower()
    found_contacts = [f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n{'-'*20}" 
                      for name, details in contacts.items() 
                      if search_term in name.lower() or search_term in details["Phone"]]
    if found_contacts:
        messagebox.showinfo("Search Results", "\n".join(found_contacts))
    else:
        messagebox.showinfo("Info", "Contact not found.")

# Function to update a contact
def update_contact():
    name = update_name_entry.get()
    if name in contacts:
        contacts[name]["Phone"] = update_phone_entry.get()
        contacts[name]["Email"] = update_email_entry.get()
        contacts[name]["Address"] = update_address_entry.get()
        messagebox.showinfo("Success", f"{name}'s contact details have been updated.")
        clear_update_entries()
    else:
        messagebox.showerror("Error", "Contact not found.")

# Function to delete a contact
def delete_contact():
    name = delete_name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"{name} has been deleted from your contacts.")
        clear_delete_entry()
    else:
        messagebox.showerror("Error", "Contact not found.")

# Function to clear entry fields after adding a contact
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to clear entry fields after updating a contact
def clear_update_entries():
    update_name_entry.delete(0, tk.END)
    update_phone_entry.delete(0, tk.END)
    update_email_entry.delete(0, tk.END)
    update_address_entry.delete(0, tk.END)

# Function to clear entry fields after deleting a contact
def clear_delete_entry():
    delete_name_entry.delete(0, tk.END)

# Main UI window
root = tk.Tk()
root.title("Contact Management System")

# Contact Management Functions
contacts = {}

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w")

# Entry Fields
name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=1, sticky="ew")

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=1, sticky="ew")

# Search Functionality
tk.Label(root, text="Search:").grid(row=6, column=0, sticky="w")
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=6, column=2)

# Update Functionality
tk.Label(root, text="Update Name:").grid(row=7, column=0, sticky="w")
update_name_entry = tk.Entry(root)
update_name_entry.grid(row=7, column=1)

tk.Label(root, text="New Phone:").grid(row=8, column=0, sticky="w")
update_phone_entry = tk.Entry(root)
update_phone_entry.grid(row=8, column=1)

tk.Label(root, text="New Email:").grid(row=9, column=0, sticky="w")
update_email_entry = tk.Entry(root)
update_email_entry.grid(row=9, column=1)

tk.Label(root, text="New Address:").grid(row=10, column=0, sticky="w")
update_address_entry = tk.Entry(root)
update_address_entry.grid(row=10, column=1)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=11, column=1, sticky="ew")

# Delete Functionality
tk.Label(root, text="Delete Name:").grid(row=12, column=0, sticky="w")
delete_name_entry = tk.Entry(root)
delete_name_entry.grid(row=12, column=1)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=13, column=1, sticky="ew")

root.mainloop()