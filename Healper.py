import pandas as pd
atr_clubdf = pd.read_csv('AllTimeRankingByClub.csv', encoding='utf-16')
atr_countrydf = pd.read_csv('AllTimeRankingByCountry.csv', index_col='Unnamed: 0')
coach_detailsdf = pd.read_csv('CoachesAppearDetails.csv', index_col='Unnamed: 0')
coach_totaldf = pd.read_csv('CoachesAppearTotals.csv', index_col='Unnamed: 0')
goal_statsdf = pd.read_csv('GoalStatsPerGroupRound.csv', index_col='Unnamed: 0')
player_detailsdf = pd.read_csv('PlayerAppearDetails.csv', index_col='Unnamed: 0')
player_totaldf = pd.read_csv('PlayerAppearTotals.csv', index_col='Unnamed: 0')
player_goal_detailsdf = pd.read_csv('PlayerGoalDetails.csv', index_col='Unnamed: 0')
player_goal_totalssdf = pd.read_csv('PlayerGoalTotals.csv', index_col='Unnamed: 0')
Top_GoalScorerdf = pd.read_csv('TopGoalScorer.csv', index_col='Unnamed: 0')

def Club_Analysis():
