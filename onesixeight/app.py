import datetime

from flask import Flask

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.figure_factory as ff

from onesixeight.extensions import db, migrate


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class ProjectItem(db.Model):
    __tablename__ = 'projectitem'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    start_date = db.Column(db.Date, unique=False, nullable=True)
    finish_date = db.Column(db.Date, unique=False, nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('projectitem.id'), index=True, nullable=True)
    hours_to_complete = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<ProjectItem %r>' % self.title


def create_app(testing=False, cli=False):
    """Application factory, used to create application """
    app = Flask("onesixeight")
    app.config.from_object("onesixeight.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
#    configure_apispec(app)
#    register_blueprints(app)
#    init_celery(app)

    return app


def configure_extensions(app, cli):
    """configure flask extensions"""

    db.init_app(app)
#    jwt.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


# db = SQLAlchemy(server)

#############################
#       init server         #
#############################
server = create_app()
# server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onesixeight.db'
# server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# migrate = Migrate(server, db)

#############################
#       other routes        #
#############################
@server.route('/')
def index():
    return 'Hello Flask app'


#############################
#       dash routes         #
#############################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets=external_stylesheets
)

df = [dict(Task="Job A", Start='2020-05-01', Finish='2020-05-28'),
      dict(Task="Job B", Start='2020-06-05', Finish='2020-06-15'),
      dict(Task="Job C", Start='2020-06-20', Finish='2020-06-30')]

for i in ProjectItem.query.all():
    finish = None
    start = None
    if i.start_date:
        finish = i.start_date + datetime.timedelta(hours=i.hours_to_complete)
        finish = finish.strftime('%Y-%m-%d')
        start = i.start_date.strftime('%Y-%m-%d'),

    df.append(dict(
        Task=i.title,
        Start=start,
        Finish=finish
    ))

fig = ff.create_gantt(df)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    html.H1(children='''BD's Gantt Chart'''),

    dcc.Graph(
        id='bd--gantt',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
