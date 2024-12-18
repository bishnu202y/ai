from owlready2 import get_ontology
from tkinter import Tk, Label, Button, Listbox, Scrollbar, VERTICAL, RIGHT, Y, Frame, TOP, X, LEFT, BOTH
from tkinter import ttk

# Load the ontology
ontology_file = "AI-Ontology.owx"  # RDF/XML format (change to your AI ontology file)
ontology = get_ontology(ontology_file).load()

# Function to fetch classes
def fetch_classes():
    listbox.delete(0, "end")  # Clear the listbox
    for cls in ontology.classes():
        listbox.insert("end", f"Class: {cls.name}")

# Function to fetch individuals
def fetch_individuals():
    listbox.delete(0, "end")  # Clear the listbox
    for individual in ontology.individuals():
        listbox.insert("end", f"Individual: {individual.name}")

# Function to fetch object properties
def fetch_object_properties():
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.object_properties():
        listbox.insert("end", f"Object Property: {prop.name}")

# Function to fetch data properties
def fetch_data_properties():
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.data_properties():
        listbox.insert("end", f"Data Property: {prop.name}")

# Build the enhanced UI
root = Tk()
root.title("AI Ontology Viewer")
root.geometry("650x550")
root.configure(bg="#f0f8ff")  # Set the background color to AliceBlue

# Header Label
header = Label(
    root,
    text="AI Ontology Viewer",
    font=("Helvetica", 20, "bold"),
    fg="white",
    bg="#2e8b57",  # SeaGreen
    pady=10
)
header.pack(fill=X)

# Frame for buttons
button_frame = Frame(root, bg="#f0f8ff", pady=10)
button_frame.pack(fill=X)

# Styled Buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)

class_button = ttk.Button(
    button_frame, text="Show Classes", style="TButton", command=fetch_classes
)
class_button.pack(side=LEFT, padx=10)

individual_button = ttk.Button(
    button_frame, text="Show Individuals", style="TButton", command=fetch_individuals
)
individual_button.pack(side=LEFT, padx=10)

object_prop_button = ttk.Button(
    button_frame, text="Show Object Properties", style="TButton", command=fetch_object_properties
)
object_prop_button.pack(side=LEFT, padx=10)

data_prop_button = ttk.Button(
    button_frame, text="Show Data Properties", style="TButton", command=fetch_data_properties
)
data_prop_button.pack(side=LEFT, padx=10)

# Frame for listbox
listbox_frame = Frame(root, bg="#f0f8ff")
listbox_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Scrollbar and Listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    listbox_frame,
    yscrollcommand=scrollbar.set,
    font=("Courier", 12),
    bg="#e6e6fa",  # Lavender
    fg="black",
    height=15,
    selectbackground="#2e8b57",  # SeaGreen
    selectforeground="white"
)
listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Footer Label
footer = Label(
    root,
    text="AI Ontology Viewer - Developed in Python",
    font=("Arial", 10),
    bg="#2e8b57",  # SeaGreen
    fg="white",
    pady=5
)
footer.pack(fill=X)

# Run the application
root.mainloop()
