import pandas as pd
import tkinter as tk
from prettytable import PrettyTable
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import DateEntry

###### counts per cust
def count_alerts_per_node(file_path, start_date=None, end_date=None):
    # Read in the alert data from a CSV file
    df = pd.read_csv(file_path)

    # Filter the data by date range, if provided
    if start_date and end_date:
        mask = (df['Initial event generation time'] >= start_date) & (df['Initial event generation time'] <= end_date)
        df = df.loc[mask]

    # Group the data by node and count the number of alerts for each node
    count_per_node = df.groupby('Node')['Number'].count()

    # Display the results in a table using PrettyTable
    table = PrettyTable()
    table.field_names = ["Node", "Number of Alerts"]
    for node, count in count_per_node.items():
        table.add_row([node, count])
    print(table)

def run_query():
    query = query_variable.get()

    # Get the file path selected by the user
    file_path = file_path_variable.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file path")
        return

    # Get the selected date range
    start_date = start_date_entry.get() if start_date_entry.get() else None
    end_date = end_date_entry.get() if end_date_entry.get() else None

    try:
        if query == 'Number of Alerts by Node' or query == 'Number of Alerts by Customer':
            count_alerts_per_node(file_path, start_date, end_date)
        else:
            messagebox.showerror("Error", "Invalid query selected")
            return

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the GUI window
root = tk.Tk()
root.title("Alert Query Tool")

# Define the query options
QUERY_OPTIONS = ["Number of Alerts by Node", "Number of Alerts by Customer"]

# create a variable to store the selected query
query_variable = tk.StringVar(root)
query_variable.set(QUERY_OPTIONS[0])  # default value

# create a variable to store the file path
file_path_variable = tk.StringVar(root)

# create drop-down menu for selecting the query
query_label = tk.Label(root, text="Select query:")
query_label.grid(column=0, row=0, sticky=tk.W)
query_dropdown = tk.OptionMenu(root, query_variable, *QUERY_OPTIONS)
query_dropdown.grid(column=1, row=0)

# create browse button to select file path
file_path_label = tk.Label(root, text="Select CSV file:")
file_path_label.grid(column=0, row=1, sticky=tk.W)
file_path_entry = tk.Entry(root, width=50, textvariable=file_path_variable)
file_path_entry.grid(column=1, row=1)
def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_variable.set(file_path)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(column=2, row=1)

# create entry widgets for start and end date using DateEntry
start_date_label = tk.Label(root, text="Start date:")
start_date_label.grid(column=0, row=2, sticky=tk.W)
start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date_entry.grid(column=1, row=2)

end_date_label = tk.Label(root, text="End date:")
end_date_label.grid(column=0, row=3, sticky=tk.W)
end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date_entry.grid(column=1, row=3)

# Create the input fields
n_label = tk.Label(root, text="N:")
n_label.grid(column=0, row=4, sticky=tk.W)
n_entry = tk.Entry(root)
n_entry.grid(column=1, row=4)

# Create the "Run" button
run_button = tk.Button(root, text="Run", command=run_query)
run_button.grid(column=0, row=5, columnspan=2)

# Start the main loop
root.mainloop()
