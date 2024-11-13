import clean_Data as DataClean
import seaborn as sns
import matplotlib.pyplot as plt

# funcion to make line plot
def linePlot(hourly_counts):
    # Set the seaborn theme for better aesthetics
    sns.set_theme(style="whitegrid")

    # Create a plot with seaborn to show the quantity of items written by hour
    sns.relplot(kind='line', data=hourly_counts, x='hour', y='counts', palette='viridis')

    # Add points for each value
    sns.scatterplot(data=hourly_counts, x='hour', y='counts', color='red')

    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Items Written')
    plt.title('Number of Items Written by Hour of the Day')
    # Ensure the x-axis shows all hours of the day
    plt.xticks(range(24))
    plt.show()

# Define a function to format the labels with the total count
def format_autopct(pct, allvals):
    absolute = int(pct/100.*sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

# funcion to make pie plot
def pieplot(date_counts):
    # Create a pie chart with matplotlib to show the quantity of items written by day
    plt.figure(figsize=(8, 8))

    explode = [0.1] + [0] * (len(date_counts) - 1)  # only "explode" the first slice

    # Create the pie chart
    plt.pie(date_counts['counts'], labels=date_counts['date'], autopct=lambda pct: format_autopct(pct, date_counts['counts']), startangle=140, explode=explode, shadow=True)

    plt.title('Number of Items Written by Day')
    plt.show()

# Function to analyze the data
def analysisEdaAPi():
    data = DataClean.cleanData()
    if data is None or data.empty:
        return None

    test = data.groupby('author')['publishedAt'].value_counts()
    print('test', test)
    print("data['description']", data['description'])

    # Extract the hour from the 'publishedAt' column
    data['hour'] = data['publishedAt'].dt.hour

    # Extract the hour from the 'publishedAt' column
    data['date'] = data['publishedAt'].dt.date

    # Group by the hour and count the number of items for each hour
    hourly_counts = data.groupby('hour').size().reset_index(name='counts')
    # linePlot(hourly_counts)



    # Group by the day and count the number of items for each day
    date_counts = data.groupby('date').size().reset_index(name='counts')
    # pieplot(date_counts)
    
    data = data.drop(columns=['urlToImage','content', 'url', 'source', 'title'])

    return data


def analysisEdaCSV():
    data = DataClean.cleanDataCSV()
    if data is None or data.empty:
        return None

    test = data.groupby('author')['publishedAt'].value_counts()
    # Extract the hour from the 'publishedAt' column
    data['hour'] = data['publishedAt'].dt.hour

    # Extract the hour from the 'publishedAt' column
    data['date'] = data['publishedAt'].dt.date

    # # Group by the hour and count the number of items for each hour
    # hourly_counts = data.groupby('hour').size().reset_index(name='counts')
    # linePlot(hourly_counts)

    # # Group by the day and count the number of items for each day
    # date_counts = data.groupby('date').size().reset_index(name='counts')
    # pieplot(date_counts)

    return data
