import requests
import csv

def get_author_info(author_id, api_key):
    base_url = "https://api.elsevier.com/content/search/author"
    
    params = {
        "query": f"au-id({author_id})",
        "apiKey": api_key
    }

    headers = {
        "Accept": "application/json"
    }

    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        author_data = response.json()
        return author_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def save_to_csv(author_id, affiliation_current):
    filename = "author_info.csv"

    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Author_ID', 'Affiliation_URL', 'Affiliation_ID', 'Affiliation_Name', 'Affiliation_City', 'Affiliation_Country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty and write header only if needed
        
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'Author_ID': author_id,
            'Affiliation_URL': affiliation_current.get('affiliation-url', ''),
            'Affiliation_ID': affiliation_current.get('affiliation-id', ''),
            'Affiliation_Name': affiliation_current.get('affiliation-name', ''),
            'Affiliation_City': affiliation_current.get('affiliation-city', ''),
            'Affiliation_Country': affiliation_current.get('affiliation-country', '')
        })


if __name__ == "__main__":
    # author_ids_array is a comma-delimited values array
    author_ids_array = [6507283659,56281907000,...{add more ids as needed}]
    api_key = "{API_KEY}"

    for author_id in author_ids_array:
        author_info = get_author_info(author_id, api_key)

        if author_info and 'search-results' in author_info:
            entry = author_info['search-results']['entry'][0]
            affiliation_current = entry.get('affiliation-current', None)

            if affiliation_current:
                print(f"Affiliation Current Information for Author ID {author_id}:")
                print(affiliation_current)

                save_to_csv(author_id, affiliation_current)
                print(f"Data for Author ID {author_id} saved to author_info.csv")
            else:
                print(f"Affiliation Current information not found for Author ID {author_id}.")
        else:
            print(f"Invalid or incomplete response from the API for Author ID {author_id}.")
