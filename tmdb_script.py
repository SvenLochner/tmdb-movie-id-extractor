import requests
import csv

# TMDb API key (replace with your actual API key locally)
API_KEY = "your_api_key"
BASE_URL = "https://api.themoviedb.org/3/search/movie"

def get_movie_id(movie_name):
    """Fetch the TMDb movie ID for a given movie name."""
    params = {
        "api_key": API_KEY,
        "query": movie_name
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            # Return the ID of the first search result
            return data['results'][0]['id']
        else:
            return None  # No results found
    else:
        print(f"Error: {response.status_code}")
        return None

# The movies_list.txt file should contain tab-separated data in the format:
# Movie Name    Director(s)    Country
try:
    with open("movies_list.txt", "r", encoding="utf-8") as file:
        movies = file.readlines()
except FileNotFoundError:
    print("Error: movies_list.txt file not found. Please create the file with your movie data.")
    exit()

# Parse and process each line
results = []
for line in movies:
    parts = line.strip().split("\t")  # Split by tab
    if len(parts) >= 3:
        movie_name = parts[0].strip()
        director = parts[1].strip()
        country = parts[2].strip()

        # Search for the movie ID
        movie_id = get_movie_id(movie_name)

        # Append the result to the list
        results.append({
            "movie_name": movie_name,
            "director": director,
            "country": country,
            "movie_id": movie_id
        })
    else:
        print(f"Skipping invalid line: {line}")

# Print the results
for result in results:
    print(f"{result['movie_name']} ({result['country']}) by {result['director']}: {result['movie_id']}")

# Save results to a CSV file
with open("movies_with_ids.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["movie_name", "director", "country", "movie_id"])
    writer.writeheader()
    writer.writerows(results)

print("Results saved to movies_with_ids.csv")
