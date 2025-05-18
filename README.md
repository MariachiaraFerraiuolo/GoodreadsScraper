# Web Scraping and Topic Evolution Analysis

## Overview
This project focuses on scraping web data related to the most loved books on Goodreads in the last 20 years analyzing narrative structures to detect the evolution of topics per genre over time.

The project is structured in three main phases:

1. Web Scraping: Extract raw data from online sources.

2. Data Analysis: Perform exploratory analysis and clean the dataset (e.g., handling missing values).

3. Topic Evolution Analysis: Study how different topics change and develop over the data timeline.


## Installation
1. Clone the repository: 
```bash
git clone https://github.com/MariachiaraFerraiuolo/GoodreadsScraper.git
cd GoodreadsScraper
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   
venv\Scripts\activate 
```
3. Install dependencies
```bash
pip install -r requirements.txt 
```
## How to run
1. Scrape 
```bash
python src/scraping.py
```
or run the full pipeline:
```bash
python main.py
```

2. Analyze data opening the Jupyter Notebook:
```bash
jupyter src\data_analysis\data_analysis.ipynb
```
3. Run topic modelling
```bash
python src\topic_evolution\bertopic.py
```

4. Analyze the topic evolution for each genre via Jupyter Notebook topic_analysis.ipynb
```bash
jupyter src\data_analysis\topic_analysis.ipynb
```