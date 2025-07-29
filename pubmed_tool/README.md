# PubMed Tool

A CLI tool to fetch and filter PubMed research papers for non-academic authors.

## Features
- Search PubMed with a user-specified query
- Fetch research paper metadata
- Detect non-academic (industry) authors from affiliations
- Output results to a structured CSV

## Installation

```sh
# From the project root
cd pubmed_tool
poetry install
```

## Usage

```sh
poetry run pubmed-tool --query "cancer immunotherapy" --output results.csv
```

## Project Structure
- `src/pubmed_tool/cli.py`: CLI entrypoint
- `src/pubmed_tool/pubmed_api.py`: PubMed fetching logic
- `src/pubmed_tool/filtering.py`: Affiliation heuristics
- `src/pubmed_tool/utils.py`: Helper functions

## Requirements
- Python 3.8+
- Poetry

---

This README will be expanded as the project develops.

---

## ✅ Features Implemented

- **CLI Tool**: Search PubMed with a user-specified query, output results to CSV.
- **PubMed Fetching**: Uses Biopython’s Entrez to fetch articles and parse metadata.
- **Filtering**: Detects non-academic (industry) authors using simple, extensible heuristics.
- **CSV Output**: Outputs key metadata and a flag for non-academic authors.
- **Professional Structure**: Modular code, type hints, docstrings, error handling, and ready for packaging.
- **Documentation**: README with install and usage instructions.

---

## 🚀 How to Use

1. **Set your email in `pubmed_api.py`**  
   Edit the line:
   ```python
   Entrez.email = "supriyawakchaure0@gmail.com"
   ```
   Replace with your real email (required by NCBI).

2. **Install dependencies**
   ```sh
   cd pubmed_tool
   poetry install
   ```

3. **Run the CLI tool**
   ```sh
   poetry run pubmed-tool --query "cancer immunotherapy" --output results.csv --max-results 20
   ```

4. **Check your CSV output**  
   The file will contain columns: PMID, Title, Authors, Journal, Year, Has_NonAcademic_Author, Affiliations.

---

## 📝 Next Steps (Optional)

- Add more industry/academic keywords to `filtering.py` for better accuracy.
- Write unit tests in the `tests/` directory.
- Expand the README with examples and limitations.
- (Bonus) Publish to Test PyPI.

---

Would you like to:
- Test the tool now?
- Add more features (e.g., more advanced heuristics, config file, etc.)?
- Get a summary of the code for your report/interview?

Let me know how you’d like to proceed!

---

## 1. **Check for Errors in the Terminal**
- Did you see any error messages after running the command?
- If yes, please copy and paste the error here.

---

## 2. **Confirm the Command Used**
- Please make sure you ran:
  ```sh
  poetry run python -m pubmed_tool.cli --query "cancer immunotherapy" --output results.csv --max-results 20
  ```
- If you ran a different command, let me know which one.

---

## 3. **Check the Current Directory**
- The `results.csv` file will be created in the directory where you ran the command.
- Run this to list files in your current directory:
  ```sh
  dir
  ```
  or
  ```sh
  ls
  ```
- See if `results.csv` is present.

---

## 4. **Check for Silent Failures**
- If there was no error and no file, it’s possible the script exited early (e.g., no articles found, or a bug).
- Try running with a different query, e.g.:
  ```sh
  poetry run python -m pubmed_tool.cli --query "diabetes" --output results.csv --max-results 10
  ```

---

## 5. **Add Debug Output**
- If you still don’t get a file, let’s add a debug print in `cli.py` after fetching articles:
  ```python
  typer.echo(f"Articles: {articles}")
  ```
  This will show if any articles are being fetched.

---

## 6. **Check for Output in a Different Directory**
- Sometimes, the file is created in a parent directory. Search for `results.csv` in your project folder.

---

### Please:
- Tell me if you saw any error messages.
- Confirm the command you used.
- Check if the file is in your current directory.
- Try a different query if needed.

Once you provide this info, I’ll help you fix the issue quickly!
