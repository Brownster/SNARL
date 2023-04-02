Alert Query Tool

This Alert Query Tool is a Python application that allows users to perform analysis on a given CSV file containing alert data. The tool provides a simple GUI to input the desired query parameters and displays the results in a table format.
Features

    The GUI allows users to select a query type from a drop-down menu (either "Number of Alerts by Node" or "Number of Alerts by Customer").
    Users can browse and select a CSV file to use for the query.
    Users can input start and end dates for the date range using DateEntry widgets.
    The code filters the data by date range (if provided) before grouping the data by the node and counting the number of alerts for each node.
    The results are displayed in a table format using PrettyTable.

Installation

Before running the application, make sure you have the required packages installed. You can install them using the following commands:

pip install pandas
pip install prettytable
pip install tkcalendar

Usage

To run the application, execute the Python script in your Python environment, and the GUI should appear. Users can then select a query, choose a CSV file, specify a date range (if desired), and see the results in a table format. If there are any issues with the file or the selected query, the application will display an error message.


![Screenshot from 2023-04-02 10-25-55](https://user-images.githubusercontent.com/6543166/229344362-2e2b67c7-4e40-4aa2-8157-10df81eba4f3.png)


![Screenshot from 2023-04-02 10-26-38](https://user-images.githubusercontent.com/6543166/229344363-4ba7cd9b-afd2-4159-be22-b2ebfa5ddff4.png)
