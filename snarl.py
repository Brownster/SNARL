import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from prettytable import PrettyTable
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import DateEntry


def Heat_count_alerts_per_node_hour(file_path, start_date=None, end_date=None):
    # Read in the alert data from a CSV file
    df = pd.read_csv(file_path)

    # Convert the 'Initial event generation time' column to datetime
    df['Initial event generation time'] = pd.to_datetime(df['Initial event generation time'])

    # Filter the data by date range, if provided
    if start_date and end_date:
        mask = (df['Initial event generation time'] >= start_date) & (df['Initial event generation time'] <= end_date)
        df = df.loc[mask]

    # Extract the hour of the day from the 'Initial event generation time' column
    df['Hour of Day'] = df['Initial event generation time'].dt.hour

    # Group the data by node and hour of the day, then count the number of alerts
    count_per_node_hour = df.groupby(['Node', 'Hour of Day'])['Number'].count().unstack()

    # Fill NaN values with 0
    count_per_node_hour = count_per_node_hour.fillna(0).astype(int)

    # Plot a heatmap of the results
    plt.figure(figsize=(10, 8))
    sns.heatmap(count_per_node_hour, annot=True, fmt='d')
    plt.xlabel("Hour of Day")
    plt.ylabel("Node")
    plt.title("Number of Alerts per Node per Hour of Day")
    plt.show()




def count_top_additional_information(file_path, start_date=None, end_date=None):
    # Read in the alert data from a CSV file
    df = pd.read_csv(file_path)

    # Convert the 'Initial event generation time' column to datetime
    df['Initial event generation time'] = pd.to_datetime(df['Initial event generation time'])

    # Filter the data by date range, if provided
    if start_date and end_date:
        mask = (df['Initial event generation time'] >= start_date) & (df['Initial event generation time'] <= end_date)
        df = df.loc[mask]

    # Group the data by 'Additional information' and count the number of alerts
    count_per_additional_info = df.groupby('Additional information')['Number'].count()

    # Sort the counts in descending order and get the top 10
    top_10_additional_info = count_per_additional_info.sort_values(ascending=False).head(10)

    # Display the results in a table using PrettyTable
    table = PrettyTable()
    table.field_names = ["Additional Information", "Number of Alerts"]
    for info, count in top_10_additional_info.items():
        table.add_row([info, count])
    print(table)



def plot_alerts_per_node_day(file_path, start_date=None, end_date=None):
    # Read in the alert data from a CSV file
    df = pd.read_csv(file_path)

    # Convert the 'Initial event generation time' column to datetime
    df['Initial event generation time'] = pd.to_datetime(df['Initial event generation time'])

    # Filter the data by date range, if provided
    if start_date and end_date:
        mask = (df['Initial event generation time'] >= start_date) & (df['Initial event generation time'] <= end_date)
        df = df.loc[mask]

    # Extract the day of the week from the 'Initial event generation time' column
    df['Day of Week'] = df['Initial event generation time'].dt.day_name()

    # Group the data by node and day of the week, then count the number of alerts
    count_per_node_day = df.groupby(['Node', 'Day of Week'])['Number'].count().unstack()

    # Fill NaN values with 0
    count_per_node_day = count_per_node_day.fillna(0).astype(int)

    # Create a bar plot using matplotlib
    ax = count_per_node_day.plot(kind='bar', stacked=True, figsize=(10, 5))
    ax.set_ylabel('Number of Alerts')
    ax.set_title('Alerts per Node by Day of Week')

    # Display the plot
    plt.show()



def count_alerts_per_node_day(file_path, start_date=None, end_date=None):
    # Read in the alert data from a CSV file
    df = pd.read_csv(file_path)

    # Convert the 'Initial event generation time' column to datetime
    df['Initial event generation time'] = pd.to_datetime(df['Initial event generation time'])

    # Filter the data by date range, if provided
    if start_date and end_date:
        mask = (df['Initial event generation time'] >= start_date) & (df['Initial event generation time'] <= end_date)
        df = df.loc[mask]

    # Extract the day of the week from the 'Initial event generation time' column
    df['Day of Week'] = df['Initial event generation time'].dt.day_name()

    # Group the data by node and day of the week, then count the number of alerts
    count_per_node_day = df.groupby(['Node', 'Day of Week'])['Number'].count().unstack()

    # Fill NaN values with 0
    count_per_node_day = count_per_node_day.fillna(0).astype(int)

    # Display the results in a table using PrettyTable
    table = PrettyTable()
    table.field_names = ["Node"] + list(count_per_node_day.columns)
    for node, row in count_per_node_day.iterrows():
        table.add_row([node] + row.tolist())
    print(table)

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
        if query == 'Number of Alerts by Node':
            count_alerts_per_node(file_path, start_date, end_date)
        elif query == 'Alerts by Node and Day':
            count_alerts_per_node_day(file_path, start_date, end_date)
        elif query == 'Plot Alerts by Node and Day':
            plot_alerts_per_node_day(file_path, start_date, end_date)
        elif query == 'Top 10 Additional Information':
            count_top_additional_information(file_path, start_date, end_date)
        elif query == 'Heat Map of Alerts By Customer By Hour':
            Heat_count_alerts_per_node_hour((file_path, start_date, end_date)
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

start_date_variable = tk.StringVar(root)
end_date_variable = tk.StringVar(root)

# Define the query options
QUERY_OPTIONS = ["Number of Alerts by Node", "Alerts by Node and Day", "Plot Alerts by Node and Day", "Top 10 Additional Information", "Heat Map of Alerts By Customer By Hour"]

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
start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, textvariable=start_date_variable)
start_date_entry.grid(column=1, row=2)

end_date_label = tk.Label(root, text="End date:")
end_date_label.grid(column=0, row=3, sticky=tk.W)
end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, textvariable=end_date_variable)
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
