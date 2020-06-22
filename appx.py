# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

with open('./onesixeight.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        df.append(dict(
            Task=row[1][:25] + '..') if len(row[1]) > 25 else row[1],
                  Start='2020





fig = ff.create_gantt(df)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.H2(children='''
        BD's gonna get there!
    '''),

    dcc.Graph(
        id='bd--ganttChart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
