
# TMDb Movie ID Extractor

This Python script extracts TMDb movie IDs from a list of movies based on their **name**, **director(s)**, and **country** using the [TMDb API](https://developers.themoviedb.org/3).

## Features

- Reads a structured list of movies (name, director(s), country) from a tab-separated file (`movies_list.txt`).
- Searches the TMDb database for each movie.
- Saves the results (movie name, director(s), country, and TMDb ID) to a CSV file (`movies_with_ids.csv`).

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tmdb-movie-id-extractor.git
cd tmdb-movie-id-extractor
```

### 2. Install Dependencies

Install the required Python library:

```bash
pip install requests
```

### 3. Get a TMDb API Key

1. Visit [TMDb API Settings](https://www.themoviedb.org/settings/api) to create a free account and get an API key.
2. Replace the placeholder `your_api_key` in the script with your actual API key:

   ```python
   API_KEY = "your_api_key"  # Replace this with your TMDb API key
   ```

### 4. Prepare Your `movies_list.txt` File

Create a file named `movies_list.txt` in the same folder as the script.  
Format it as **tab-separated values** with each line containing:

```
Movie Name    Director(s)    Country
```

#### Example:

```
Crimson Harbor    Victor Bonafonte    Spain
Dolores    Cecilia Andalón    Mexico
```

## Usage

Run the script in the terminal:

```bash
python tmdb_script.py
```

The script will:
1. Parse the data from `movies_list.txt`.
2. Search for each movie on TMDb.
3. Save the results in a file named `movies_with_ids.csv`.

## Output

The output will be saved in `movies_with_ids.csv` with the following columns:
- `movie_name`: Name of the movie.
- `director`: Director(s) of the movie.
- `country`: Country of origin.
- `movie_id`: TMDb ID (or `None` if not found).

### Example Output (Terminal):

```
Crimson Harbor (Spain) by Victor Bonafonte: 1367441
Dolores (Mexico) by Cecilia Andalón: 420283
```

### Example Output (CSV):

```csv
movie_name,director,country,movie_id
Crimson Harbor,Victor Bonafonte,Spain,1367441
Dolores,Cecilia Andalón,Mexico,420283
```

## File Descriptions

| File Name            | Description                                                      |
|----------------------|------------------------------------------------------------------|
| `tmdb_script.py`     | The main Python script that extracts TMDb IDs.                  |
| `movies_list.txt`    | Input file containing tab-separated movie data.                 |
| `movies_with_ids.csv`| Output file with movie names, directors, countries, and TMDb IDs.|

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Troubleshooting

1. **Missing API Key**:
   - Ensure your TMDb API key is correctly added in the script:
     ```python
     API_KEY = "your_api_key"
     ```

2. **Invalid Input Format**:
   - Check that `movies_list.txt` is formatted correctly (tab-separated).
   - Each line should include **movie name**, **director(s)**, and **country**.

3. **No Results Found**:
   - Some movie names may not have a match in TMDb, especially if they are very specific or uncommon.

## Contributing

If you’d like to contribute, feel free to submit issues or pull requests. Suggestions for improvements are always welcome!

## Acknowledgments

- Thanks to [TMDb](https://www.themoviedb.org/) and everyone contributing to their database.

