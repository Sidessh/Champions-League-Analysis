import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('AllTimeRankingByClub.csv', encoding='utf-16')
def preprocess():
    global df
    country_dict = {"ESP": "Spain", "ENG": "England", "ITA": "Italy", "GER": "Germany", "POR": "Portugal",
                    "FRA": "France", "NED": "Netherlands", "POL": "Poland", "ROU": "Romania", "RUS": "Russia",
                    "AUT": "Austria", "SCO": "Scotland", "SRB": "Serbia", "SUI": "Switzerland", "SVK": "Slovakia",
                    "SVN": "SLovenia", "TUR": "Turkey", "NOR": "Norway", "ISR": "Israel", "KAZ": "Kazakhstan",
                    "AZE": "Azerbaijan", "HUN": "Hungary", "GRE": "Greece", "FIN": "Finland", "DEN": "Denmark",
                    "SWE": "Swedend", "CZE": "Czech Republic", "CYP": "Cyprus", "CRO": "Croatia", "BUL": "Bulgaria",
                    "BLR": "Belarus", "BEL": "Belguim", "UKR": "Ukraine", "MDV": "Moldova"}
    df['Country'] = df['Country'].map(country_dict)
    df.at[104, 'Country'] = 'Moldova'

    df['Win Percentage'] = (((df['Win'] + (0.5 * df['Draw'])) / df['Played']) * 100) \
                                   .round(decimals=2).astype(str) + '%'
    topcountrygrp = df.groupby("Country")["Club"].count().sort_values(ascending=False)

    return df

