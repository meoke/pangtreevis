import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from .server import app
from .layout import layout_ids, pages

app.title = 'PoaPangenome'
app.config.suppress_callback_exceptions = True
draw_poagraph = True

external_css = [
    'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    dbc.themes.FLATLY
]
for css in external_css:
    app.css.append_css({"external_url": css})

app.layout = html.Div([
    dcc.Location(id=layout_ids.id_url, refresh=False),
    html.Div([], className="area"),
    dbc.Navbar([
        html.Ul([
            html.Li(html.A([html.I(className="fas fa-info-circle"), html.Span("Index", className="nav-text")], href="/#")),
            html.Li(html.A([html.I(className="fas fa-tools"), html.Span("Tools", className="nav-text")], href="/tools"), className="has-subnav"),
            html.Li(html.A([html.I(className="fas fa-archive"), html.Span("Package", className="nav-text")], href="/package"), className="has-subnav"),
            html.Li(html.A([html.I(className="fas fa-address-book"), html.Span("Contact", className="nav-text")], href="/contact"), className="has-subnav"),
        ])
    ], className="main-menu", sticky="left"),
    html.Div(id=layout_ids.id_page_content)
])


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output(layout_ids.id_page_content, 'children'),
              [Input(layout_ids.id_url, 'pathname')])
def display_page(pathname):
    if pathname == '/tools':
        return pages.tools()
    elif pathname == '/package':
        return pages.package()
    elif pathname == '/contact':
        return pages.contact()
    else:
        return pages.index()
