import csv

results = []

# Reading data from the CSV file
with open('Topics.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
    data_reader = csv.DictReader(csvfile, delimiter=',')

    # Displaying the available column names
    print("Available Columns:", data_reader.fieldnames)

    # Finding the index of the 'Topic name' column
    topic_index = next((i for i, col in enumerate(data_reader.fieldnames) if col.strip().lower() == 'topic name'), None)

    if topic_index is not None:
        # Iterating through each row in the CSV file
        for row in data_reader:

            topics = row[data_reader.fieldnames[topic_index]].split('; ')

            for topic in topics:
                results.append({
                    'DOI': row['DOI'],
                    'Topic': topic
                })

        # Saving the results to a new CSV file
        output_file = 'output.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['DOI', 'Topic']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for result in results:
                writer.writerow(result)

        print(f"Output saved to {output_file}")
    else:
        print("Error: 'Topic' column not found in the CSV file.")
