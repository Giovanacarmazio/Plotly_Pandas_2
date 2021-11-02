#1
df1 = albums_df.groupby(['year_of_pub'])      .agg({'rolling_stone_critic':'mean', 'mtv_critic':'mean', 'music_maniac_critic':'mean', 'id':'count'})

fig1 = px.line(df1, x=df1.index, y='mtv_critic',color_discrete_sequence = px.colors.qualitative.Pastel1,template='plotly_white',
labels={'mtv_critic': 'Critica MTV','year_of_pub': 'Ano de publicação'})
fig1.update_layout(title={'text' : 'Anos de maior e pior sucesso dos albuns Black Bear Records na MTV','y': 0.9,'x': 0.5},
annotations=[{"x":2019,"y":2.704,"text":"Pior Ano","arrowhead": 3, "showarrow":True, "font": {"size": 12}},{"x":2005,"y":2.800,"text":"Melhor Ano","arrowhead": 3, "showarrow":True, "font": {"size": 12}}])
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)
fig1.update_layout(annotations=[{"x":2019,"y":2.704,"text":"Pior Ano","arrowhead": 3, "showarrow":True, "font": {"size": 17}},
                                   {"x":2005,"y":2.800,"text":"Melhor Ano","arrowhead": 3, "showarrow":True, "font": {"size": 17}}])
fig1.show()     

#2
df2 = artists_df.groupby(['role'], as_index=False).agg({'id':'count'})
fig2 = px.bar(df2.sort_values(by='id', ascending=False), x='role', y='id',text='id',color="role",color_discrete_sequence = px.colors.qualitative.T10,template='plotly_white',
labels={'role':'Estilo','id': 'Contagem de artistas'})
fig2.update_layout(title={'text' : 'Artistas por catálogo','y': 0.9,'x': 0.5})
fig2.update_traces(texttemplate='%{y:.0f}',textposition='outside')
fig2.show()

#3
df3 = artists_df.copy()
fig3_v1 = px.histogram(df3, x='released_albums',histnorm='percent',color_discrete_sequence=px.colors.qualitative.Pastel2,template='plotly_white')
fig3_v1.update_layout(title={'text' : 'Distribuição de álbuns por artista','y': 0.9,'x': 0.5},
xaxis_title='Álbuns lançados',yaxis_title='Total de artistas',yaxis_ticksuffix='%')
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)
fig3_v1.show()

#4
#4
df4 = albums_df.groupby(['genre', 'year_of_pub'], as_index=False).agg({'num_of_sales':'sum', 'id':'count'})
df_sales_per_genre = albums_df.groupby(['genre']).agg({'num_of_sales':'sum'})
df_top_8_sales = df_sales_per_genre.sort_values(by='num_of_sales', ascending=False).iloc[:8]
main_genres = df_top_8_sales.index.tolist()
df4.loc[:, 'top_genero'] = 'Outros'
df4.loc[df4['genre'].isin(main_genres), 'top_genero'] = df4['genre']
df4_v2 = df4.groupby(['year_of_pub', 'top_genero'], as_index=False).agg({'num_of_sales':'sum', 'id':'sum'})
df4_v3 = df4.loc[df4['genre'].isin(main_genres)].groupby(['year_of_pub', 'genre'], as_index=False).agg({'num_of_sales':'sum', 'id':'sum'})
fig4_v3 = px.line(df4_v3, x='year_of_pub', y='num_of_sales', color='genre',color_discrete_sequence=px.colors.qualitative.T10_r,template='plotly_white')
fig4_v3.update_layout(title={'text': 'Desempenho comercial dos Top 8 Gêneros Musicais 2000 - 2019','y': 0.9,'x': 0.5},
    yaxis_title='Vendas (R$)',
    yaxis_tickprefix='R$',
    xaxis_title='Ano',
    legend_title='Gênero Musical'
)
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)
fig4_v3.show()



