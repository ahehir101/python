# Import libraries
import pandas as pd
import pyodbc
from matplotlib import pyplot as plt
import textwrap as tw

# Connect to SQL Server with pyodbc hello hel'o
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=W10-UK-STF-3004;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

# Transform SQL query to dataset
df = pd.read_sql_query('SELECT [GroupName], AVG([SickLeaveHours]) AS av FROM [HumanResources].[Employee] AS he INNER JOIN [HumanResources].[vEmployeeDepartment] AS hve ON he.JobTitle = hve.JobTitle GROUP BY [GroupName] ORDER BY av DESC;', conn)

# Creating a subplot
fig, ax1 = plt.subplots()

# Creating a bar chart 
ax1.bar(df.GroupName, df.av)

# Set font properties for title and labels
font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'black','size':15}

# Associating data accordingly
ax1.set_xlabel('Job Title', fontdict = font2)
ax1.set_ylabel('Sick Leave Hours', fontdict = font2)
ax1.set_title('Amount of Sick Leave Taken by Job Titles', fontdict = font1)

# List format
xticklabel = []
for i in range(0, len(df.GroupName)):
    xticklabel.append(tw.fill(df.GroupName[i], width = 15))

# Matplotlib xlabel multiple lines
ax1.set_xticklabels(xticklabel)
plt.tight_layout()

# Visualise
plt.show()
