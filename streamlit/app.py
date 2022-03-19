# https://docs.pinot.apache.org/users/clients/python
#pinotDB docs referenced above
#https://markhneedham.medium.com/analysing-github-events-with-apache-pinot-and-streamlit-2ed555e9fb78


import streamlit as st
from pinotdb import connect
import pandas as pd
import numpy as np
import altair as alt
import urllib.parse

st.title("Wiki Events Streaming Page")

broker_port = 8099
conn = connect(host='localhost', port=broker_port, path='/query/sql', scheme='http')



query = f"""
select user, count(comment) as counts from wikievents
group by user
order by count(comment) desc
limit 50
"""

st.write (query)
curs = conn.cursor()
curs.execute(query)

st.header(" Orgs that  have the most wiki events")

st.subheader("Generate Table format:")
df = pd.DataFrame(curs, columns=[item[0] for item in curs.description])
st.table(df)
#st.write(df)

st.subheader ("Generate Bar Graph:")

p = alt.Chart(df).mark_bar().encode(
        x='user',
        y='counts'
        )

p = p.properties(
        width = alt.Step(20)
        )
st.write(p)

st.subheader("Generate line chart:")

pl = alt.Chart(df).mark_line(point=True).encode(
        alt.X('user', title ='wiki user name', sort=None),
        alt.Y('counts',title='event counts')
        )
pl = pl.properties(
        width = alt.Step(20)
)
st.write(pl)

