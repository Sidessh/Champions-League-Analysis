import streamlit as st
import pandas as pd
import helper

st.sidebar.title('Champions League Analysis')
st.sidebar.image('https://e7.pngegg.com/pngimages/105/775/png-clipart-2017-18-uefa-champions-league-uefa-europa-league-2018-uefa-champions-league-final-2015-16-uefa-champions-league-2014-15-uefa-champions-league-football-white-text.png')
User_Menu = st.sidebar.radio('Select An Option', ('Countries & Clubs Analysis', 'Player Analysis', 'Coach Analysis', 'Overall Analysis'))

if User_Menu == 'Countries & Clubs Analysis':
    st.write("# Countries & Clubs Analysis")
    club_analysis = helper.Club_Analysis()

if User_Menu == 'Coach Analysis':
    st.write("# Coach Analysis")
    Coach_Analysis = helper.Coach_Analysis()

if User_Menu == 'Player Analysis':
    st.write("# Player Analysis")
    Player_Analysis = helper.Player_Analysis()

if User_Menu == 'Overall Analysis':
    st.write("# Overall Analysis")
    Overall_Analysis = helper.Overall_Analysis()




