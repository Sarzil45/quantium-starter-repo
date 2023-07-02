# Import necessary libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback

# Load dataset into DataFrame
df = pd.read_csv("data/pink_morsel.csv")
df['date'] = pd.to_datetime(df['date'])

# Instantiate the app
app = Dash(__name__)

# Define the HTML layout
app.layout = html.Div(className="main-body", children=[
    html.Div(id="heading", children=[
        html.H1(id="header", children="Pink Morsel Sales"),
        html.P(children="Sale of pink morsel over time"),
    ]),
    html.Div(className="filters", children=[
        html.Div(className="filter", children=[
            html.Label("Select a Date Range: "),
            dcc.DatePickerRange(
                id="date-slider",
                min_date_allowed=df['date'].min(),
                max_date_allowed=df['date'].max(),
                start_date_placeholder_text="From",
                end_date_placeholder_text="To",
                clearable=True,
            ),
        ]),
        html.Div(className="filter", children=[
            html.Label("Region"),
            dcc.RadioItems(
                id="region",
                options=[
                    {"label": "North", "value": "north"},
                    {"label": "South", "value": "south"},
                    {"label": "East", "value": "east"},
                    {"label": "West", "value": "west"},
                    {"label": "All", "value": "all"}
                ],
                value="all",
                inline=True,
            ),
        ]),
    ]),
    dcc.Graph(
        id="line-chart",
        config={
            'displayModeBar': False,
        }
    ),
])


# Create the line chart based on the filters selected
@callback(
    Output("line-chart", "figure"),
    Input("date-slider", "start_date"),
    Input("date-slider", "end_date"),
    Input("region", "value")
)
def make_line_chart(st_date, e_date, region):
    # A bit of validation action
    if st_date is None:
        st_date = df['date'].min()
    if e_date is None:
        e_date = df['date'].max()
    # Filter as needed
    if region == "all":
        mask = (df['date'] >= st_date) & (df['date'] <= e_date)
    else:
        mask = (df['date'] >= st_date) & (df['date'] <= e_date) & (df['region'] == region)
    filtered_df = df[mask]
    # Make the graph
    fig = px.line(data_frame=filtered_df, x="date", y="sales")
    fig.update_layout(
        xaxis_title=None,
        yaxis_title="Sales",
        yaxis_tickprefix='$',
        yaxis_tickformat=',',
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FC9B7A",
    )
    fig.update_traces(line_color="red")
    fig.update_xaxes(rangeslider_visible=True)
    return fig


# Start the app
if __name__ == '__main__':
    app.run(debug=True)
