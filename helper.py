import pandas as pd
import plotly.express as px
import streamlit as st

atr_clubdf = pd.read_csv('Ranking_clubs.csv', index_col='Unnamed: 0')
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
    global atr_clubdf, atr_countrydf

    topcountrygrp = atr_clubdf.groupby("Country")["Club"].count().sort_values(ascending=False)

    atr_clubdf
    atr_countrydf

    atr_countrydf = atr_countrydf.sort_index()
    st.dataframe(atr_countrydf)
    clubfig = px.bar(topcountrygrp, title = 'Countries With Most Number Of Clubs')
    clubfig.layout.yaxis.title.text = 'Number of Clubs'
    clubfig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    st.plotly_chart(clubfig)

    countryfig = px.line(atr_countrydf[:15], x='Country', y='Titles', markers=True, title = 'Countries With Most Number Of Champions League Titles')
    countryfig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    st.plotly_chart(countryfig)

    # country_dict = {"ESP": "Spain", "ENG": "England", "ITA": "Italy", "GER": "Germany", "POR": "Portugal",
    #                 "FRA": "France", "NED": "Netherlands", "POL": "Poland", "ROU": "Romania", "RUS": "Russia",
    #                 "AUT": "Austria", "SCO": "Scotland", "SRB": "Serbia", "SUI": "Switzerland", "SVK": "Slovakia",
    #                 "SVN": "SLovenia", "TUR": "Turkey", "NOR": "Norway", "ISR": "Israel", "KAZ": "Kazakhstan",
    #                 "AZE": "Azerbaijan", "HUN": "Hungary", "GRE": "Greece", "FIN": "Finland", "DEN": "Denmark",
    #                 "SWE": "Swedend", "CZE": "Czech Republic", "CYP": "Cyprus", "CRO": "Croatia", "BUL": "Bulgaria",
    #                 "BLR": "Belarus", "BEL": "Belguim", "UKR": "Ukraine", "MDV": "Moldova"}
    # atr_clubdf['Country'] = atr_clubdf['Country'].map(country_dict)
    #atr_clubdf.at[104, 'Country'] = 'Moldova'

    st.dataframe(atr_clubdf)

    clubdf = atr_clubdf[['Club', 'Titles', 'Goal Diff', 'Played', 'Win', 'Draw']]
    clubdf = clubdf.sort_values(by='Titles', ascending=False)
    clubdf = clubdf.head(15)
    clubdf.head()

    clubdf['Win Percentage'] = (((clubdf['Win'] + (0.5 * clubdf['Draw'])) / clubdf['Played']) * 100) \
                                   .round(decimals=2).astype(str) + '%'
    clubanalysisfig = px.bar(clubdf, y='Club', x='Titles', color='Goal Diff', text='Win Percentage', \
                             title = 'Clubs With Most Number Of Titles With Win Percentage')
    clubanalysisfig.update_yaxes(categoryorder='max ascending')
    clubanalysisfig.update_layout(margin=dict(t=75, b=75, l=75, r=75))
    st.plotly_chart(clubanalysisfig)



    # atr_countrydf = atr_countrydf[['Country', 'Titles']]
    # atr_countrydf.sort_values(by='Titles', ascending=False)
    # atr_countrydf = atr_countrydf.head(10)
    # atr_countrydf.head()


def Coach_Analysis():
    global coach_detailsdf

    st.dataframe(coach_detailsdf)
    club_coach_df = pd.DataFrame(coach_detailsdf['Coach'].value_counts())
    coachfig1 = px.line(club_coach_df, markers=True, title = 'Most Number Teams Coached')
    coachfig1.update_layout(margin=dict(t=50, b=50, l=50, r=50), xaxis_title="Coach", yaxis_title="Number Of Teams")
    st.plotly_chart(coachfig1)

    coachfig2 = px.scatter(coach_detailsdf, x='Club', y='Appearance', color='Coach',\
                           title = 'Coaches With Most Number Of Appearances With Clubs')
    coachfig2.update_layout(margin=dict(t=50, b=50, l=50, r=50), xaxis_title="Clubs")
    st.plotly_chart(coachfig2)

def Player_Analysis():
    global player_detailsdf, player_goal_detailsdf,player_goal_totalssdf

    player_goal_detailsdf['Appearances'] = player_detailsdf['Appearances']
    st.dataframe(player_goal_detailsdf)

    player_detailsdf.sort_values(by='Appearances', ascending=False).head()

    PlayerAppearancesfig = px.bar(player_detailsdf[:75], x='Player', y='Appearances', color='Club', title = 'Players With Most Appearances')
    PlayerAppearancesfig.update_traces(width=0.5)
    PlayerAppearancesfig.update_xaxes(categoryorder='total descending')
    PlayerAppearancesfig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    st.plotly_chart(PlayerAppearancesfig)

    player_goal_totalssdf.at[173, 'Goals'] = '10'
    player_goal_totalssdf['Goals'] = player_goal_totalssdf['Goals'].astype(int)
    p = px.bar(player_goal_totalssdf[:50], y='Goals', x='Player', title = 'Players With Most Number Of Goals')
    p.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    st.plotly_chart(p)

    TOPplayer_goal_detailsdf = player_goal_detailsdf.head(100)
    TOPplayer_goal_detailsdf['Goals'] = TOPplayer_goal_detailsdf['Goals'].astype(int)

    topGoals = px.bar(TOPplayer_goal_detailsdf, x='Player', y='Goals', color='Club',\
                      title = 'Players With Most Number Of Goals For Clubs')
    topGoals.update_xaxes(categoryorder='total descending')
    topGoals.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    st.plotly_chart(topGoals)

def Overall_Analysis():
    st.title = 'Overall Analysis'
    global Top_GoalScorerdf, player_totaldf, Top_GoalScorerdf, coach_totaldf

    Top_GoalScorerdf.at[26, ['Club', 'Goals', 'Appearances']] = ['FC Barcelona', '10 Goals', '12 Appearances']
    Top_GoalScorerdf['Goals Scored'] = Top_GoalScorerdf['Goals'].map(lambda x: str(x)[:-6])
    Top_GoalScorerdf['Appearance'] = Top_GoalScorerdf['Appearances'].map(lambda x: str(x)[:-12])
    Top_GoalScorerdf.at[33, 'Appearance'] = '8'
    Top_GoalScorerdf[['Goals Scored', 'Appearance']] = Top_GoalScorerdf[['Goals Scored', 'Appearance']].apply(
        lambda x: x.astype(int))

    Top_GoalScorerfig = px.bar(Top_GoalScorerdf, y='Year', x='Goals Scored', color='Player', title = 'Top Goal Scorers Each Season')
    Top_GoalScorerfig.update_traces(width=0.8)
    Top_GoalScorerfig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    st.plotly_chart(Top_GoalScorerfig)

    col1, col2 = st.columns(2)
    with col1:

        donutPlayerapp = px.pie(player_totaldf[:5], labels='Player', values='Appearances', hole=.5,
                                color_discrete_sequence=px.colors.sequential.Turbo, title='Top 5 Appearances')
        donutPlayerapp.update_traces(textposition='inside', text=(player_totaldf['Player']), textinfo='text + value')
        donutPlayerapp.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.plotly_chart(donutPlayerapp, use_container_width=True)

    with col2:
        donut = px.pie(player_goal_totalssdf[:5], labels='Player', values='Goals', hole=.5,
                       color_discrete_sequence=px.colors.sequential.RdBu, title='Top 5 Goal Scorers')
        donut.update_traces(textposition='inside', text=(player_goal_totalssdf['Player']), textinfo='text + value')
        donut.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.plotly_chart(donut, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        top5club = px.pie(atr_clubdf[:5], labels='Club', values='Titles', hole=.5,
                          color_discrete_sequence=px.colors.sequential.YlGn,\
                          title = 'Top 5 Clubs with most Titles')
        top5club.update_traces(textposition='inside', text=(atr_clubdf['Club']), textinfo='text + value')
        top5club.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.plotly_chart(top5club, use_container_width=True)

    with col4:
        top5country = px.pie(atr_countrydf[:5], labels='Country', values='Titles', hole=.5,
                             color_discrete_sequence=px.colors.sequential.YlOrRd,\
                             title = 'Top 5 Countries with most Titles')
        top5country.update_traces(textposition='inside', text=(atr_countrydf['Country']), textinfo='text + value')
        top5country.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.plotly_chart(top5country, use_container_width=True)

    Top5coach = px.line(coach_totaldf[:10], y='Appearance', x='Coach', markers = True,\
                        title = 'Top 10 Coaches with most Appearances')

    st.plotly_chart(Top5coach)

