import os
import pandas as pd
from bertopic import BERTopic
from typing import Tuple

INPUT_FILE = r'output\lemmatized_data.xlsx'
TOPIC_INFO_FILE = r'output\topic_model_50topics.xlsx'
EVOLUTION_FILE = r'output\topic_evolution_50topics_named.xlsx'
TOPIC_COUNT = 50
MIN_TOPIC_SIZE = 100


#Preprocessing
def load_and_preprocess_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    
    # Create year group
    df['year_group'] = pd.cut(df['year'], bins=[2003, 2010, 2015, 2020, 2025],
                              labels=['2004-10', '2010-15', '2015-20', '2020-25'])

    # Explode genres
    df['genres'] = df['genres'].str.split(',')
    df = df.explode('genres')
    df['genres'] = df['genres'].str.strip()

    # Drop rows without lemmatized plots
    df = df.dropna(subset=['plot_lemmatized'])

    return df


#Topic modelling phase
def generate_topics(df: pd.DataFrame, min_topic_size: int, n_topics: int) -> Tuple[BERTopic, pd.DataFrame]:
    plots = df['plot_lemmatized'].tolist()
    model = BERTopic(min_topic_size=min_topic_size)
    model.fit(plots)

    # Reduce topics and re-transform
    model.reduce_topics(plots, nr_topics=n_topics)
    topics = model.transform(plots)[0]

    df['topic'] = topics
    df = df[df['topic'] != -1]  # Remove outliers
    return model, df


#Topic aggregation phase
def compute_topic_evolution(df: pd.DataFrame, model: BERTopic) -> pd.DataFrame:
    topic_info = model.get_topic_info()
    topic_info.to_excel(TOPIC_INFO_FILE, index=False)

    # Map ID to name
    topic_map = dict(zip(topic_info['Topic'], topic_info['Name']))

    # Group by genre and year group
    evolution = df.groupby(['genres', 'year_group'])['topic'].value_counts().unstack(fill_value=0)
    evolution = evolution.rename(columns=topic_map)
    return evolution.reset_index()



def main():
    df = load_and_preprocess_data(INPUT_FILE)
    topic_model, df_with_topics = generate_topics(df, MIN_TOPIC_SIZE, TOPIC_COUNT)
    topic_evolution = compute_topic_evolution(df_with_topics, topic_model)

    topic_evolution.to_excel(EVOLUTION_FILE, index=False)
    print("Topic evolution saved to:", EVOLUTION_FILE)


if __name__ == "__main__":
    main()
