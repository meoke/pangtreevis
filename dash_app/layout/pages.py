import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from pangtreebuild.output.PangenomeJSON import PangenomeJSON

from .layout_ids import *
from .pangtreebuild import pangtreebuild_tab
import dash_cytoscape as cyto
import dash_table
from ..components import mafgraph as mafgraph_component
from ..components import poagraph as poagraph_component


def contact():
    return dbc.Container([
        dbc.Card([
            dbc.CardBody([
                html.H5("Norbert Dojer, PhD.", className="card-title text-info"),
                html.P(html.P("dojer@mimuw.edu.pl"), className='card-text'),
            ]),
        ], outline=True, color="info"),
        dbc.Card([
            dbc.CardBody([
                html.H5("Paulina Dziadkiewicz, B.Sc.", className="card-title text-info"),
                html.P("pedziadkiewicz@gmail.com", className='card-text'),
            ])
        ], outline=True, color="info"),
        dbc.Card([
            dbc.CardBody([
                html.H5("Paulina Knut, B.Sc.", className="card-title text-info"),
                html.P("paulina.knut@gmail.com", className='card-text'),
            ])
        ], outline=True, color="info")
    ])


def index():
    return dbc.Container(
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.A(href="/pangtreebuild",
                           children=html.Img(className="tools-logo circle-img",
                                             src="https://s3.amazonaws.com/media-p.slid.es/uploads/1047434/images/6497196/pasted-from-clipboard.png")),
                    html.Div([
                        html.H4('PangTreeBuild'),
                        html.P("tool for multiple sequence alignment analysis.")
                    ], style={"line-height": "40px"}),
                ], className='tools-logo'),
                dbc.Col([
                    html.A(href="/pangtreevis",
                           children=html.Img(className="tools-logo circle-img",
                                             src="https://s3.amazonaws.com/media-p.slid.es/uploads/1047434/images/6497198/pasted-from-clipboard.png")),
                    html.Div([
                        html.H4('PangTreeVis'),
                        html.P("visualises the results in browser.")
                    ], style={"line-height": "40px"}),
                ], className='tools-logo')
            ]),
            dbc.Row(dbc.CardDeck([
                dbc.Card([
                    dbc.CardHeader(dbc.Row([
                        dbc.Col(html.I(className="fas fa-bezier-curve fa-2x"), className="col-md-3 my-auto"),
                        html.P("Build graph representation of multiple sequence alignment", className="col-md-9 my-auto")
                    ])),
                    dbc.CardBody([
                        html.P(html.Ul([
                            html.Li([
                                "Input formats: ",
                                html.A("MAF",
                                       href="http://www1.bioinf.uni-leipzig.de/UCSC/FAQ/FAQformat.html#format5",
                                       target="_blank"),
                                ", ",
                                html.A("PO",
                                       href="https://github.com/meoke/pang/blob/master/README.md#po-file-format-specification",
                                       target="_blank")
                            ]),
                            html.Li([
                                "Internal representation: ",
                                html.A("Partial Order graph",
                                       href="https://doi.org/10.1093/bioinformatics/18.3.452",
                                       target="_blank")
                            ]),
                            html.Li([
                                "Cycles in graph removed with ",
                                html.A("Mafgraph",
                                       href="https://github.com/anialisiecka/Mafgraph",
                                       target="_blank")
                            ]),
                            html.Li("Complement missing parts from NCBI or fasta")]), className='card-text')
                    ]),
                ]),
                dbc.Card([
                    dbc.CardHeader(dbc.Row([
                        dbc.Col(html.I(className="fas fa-grip-lines fa-2x"), className="col-md-3 my-auto"),
                        html.P("Find sequences consensus", className="col-md-9 my-auto")
                    ])),
                    dbc.CardBody([
                        html.P([
                            "This tool extends Partial Order Alignment (POA) algorithm introduced by ",
                            html.A("Lee et al.",
                                   href="https://doi.org/10.1093/bioinformatics/18.3.452",
                                   target="_blank"),
                            ". It provides:",
                            html.Ul([
                                html.Li([
                                    html.Strong("Consensuses"),
                                    " - agreed representations of input subsets"]),
                                html.Li([
                                    html.Strong("Consensus Tree"),
                                    " - a structure similar to phylogenetic tree but it has a consensus assigned to every node"]),
                                html.Li([
                                    html.Strong("Compatibility"),
                                    " - a measure of similarity between sequence and consensus"])])
                        ], className='card-text'),
                    ]),
                ]),
                dbc.Card([
                    dbc.CardHeader(dbc.Row([
                        dbc.Col(html.I(className="fas fa-eye fa-2x"), className="col-md-3 my-auto"),
                        html.P("Visualise results", className="col-md-9 my-auto")
                    ])),
                    dbc.CardBody([
                        html.P([html.Ul([
                            html.Li("MAF blocks graph"),
                            html.Li("Multiple sequence alignment as Partial Order Graph"),
                            html.Li("Consensus tree"),
                            html.Li("Compatibilities relations")]
                        )], className='card-text')
                    ]),
                ]),
            ]))
        ])
    )


def package():
    return dbc.Container([dbc.Row(html.Span(["The underlying software is available at ",
                                             html.A("GitHub", href="https://github.com/meoke/pangtree", target="_blank"),
                                             # " and ",
                                             # html.A("PyPI", href="", target="_blank"),
                                             ". It can be incorporated into your Python application in this simple way:"])),
                          dbc.Card(dbc.CardBody(dcc.Markdown('''

                          
                          from pangtreebuild import Poagraph, input_types, fasta_provider, consensus

                          poagraph = Poagraph.build_from_dagmaf(input_types.Maf("example.maf"), 
                                                                fasta_provider.FromNCBI())
                          affinity_tree = consensus.tree_generator.get_affinity_tree(poagraph,
                                                                                     Blosum("BLOSUM80.mat"),
                                                                                     output_dir,
                                                                                     stop=1,
                                                                                     p=1)
                          pangenomejson = to_PangenomeJSON(poagraph, affinity_tree)
                          
                          ''')), style={"margin": '30px 0px', 'padding': '10px'}),
                          dbc.Row("or used as a CLI tool:"),
                          dbc.Card(dbc.CardBody(dcc.Markdown(
                              '''pangtreebuild --multialignment "example.maf" --consensus tree --p 1 --stop 1''')),
                              style={"margin": '30px 0px', 'padding': '10px'}),
                          dbc.Row("Check out full documentation at the above link.")
                          ]
                         )


def pangtreebuild():
    return pangtreebuild_tab


def pangtreevis():
    return _pangtreeviz_tab


_load_pangenome_row = dbc.Row(id=id_pangviz_load_row,
                              children=[
                                  dbc.Col(dcc.Upload(id=id_pangenome_upload,
                                                     multiple=False,
                                                     children=[
                                                         dbc.Row([dbc.Col(html.I(className="fas fa-seedling fa-2x"),
                                                                          className="col-md-2"),
                                                                  html.P(
                                                                      "Drag & drop pangenome.json file or select file..",
                                                                      className="col-md-10")])

                                                     ], className="file_upload"), width={"size": 4, "offset": 4}),
                              ])

_task_parameters_row = dbc.Row(id=id_task_parameters_row,
                               children=html.Div([html.Div(html.H3("Task parameters"), className="panel-heading"),
                                                  dcc.Loading(html.Div(id=id_task_parameters_vis, className="panel-body"), type="circle")],
                                                 ),
                               className="vis_row")

_input_data_row = dbc.Row(style={'display':'none'},children=[dbc.Col(html.Div(id=id_input_info_vis)),
                                    dbc.Col(html.Div(id=id_input_dagmaf_vis,
                                                     children=[html.H3("MAF graph"),
                                                               dcc.Loading(cyto.Cytoscape(id=id_mafgraph_graph,
                                                                              elements=[]
                                                                              ,
                                                                              layout={'name': 'cose'},
                                                                              autoRefreshLayout=True,
                                                                              style={'width': 'auto',
                                                                                     'height': '350px'},
                                                                              zoom=1,
                                                                              # style={'width': 'auto',
                                                                              #        'height': '300px'},
                                                                              stylesheet=mafgraph_component.get_mafgraph_stylesheet(),
                                                                              # autolock=True,
                                                                              boxSelectionEnabled=False,
                                                                              # autoungrabify=True,
                                                                              autounselectify=True), type="circle")]
                                                     ))])

_pangenome_row = dbc.Row(children=[dbc.Col(html.H4("Pangenome - Cut Width statistic"), width=12),
                                   dbc.Col([html.P("Representation of full poagraph as Cut Width statistics."),
                                            html.P("Cut Width - edges count between two consecutive columns."),
                                            html.I(id="arrow_icon",
                                                   className="fas fa-level-down-alt fa-flip-horizontal fa-5x")],
                                           width=2),
                                   dbc.Col(html.Div(id=id_full_pangenome_container,
                                                    style={'visibility': 'hidden'},
                                                    children=[dcc.Loading(dcc.Graph(
                                                        id=id_full_pangenome_graph,
                                                        # style={'width': 'auto'},
                                                        style={'height': '200px', 'width': 'auto'},
                                                        figure={},
                                                        config={
                                                            'displayModeBar': False,
                                                        }
                                                    ), type="circle")]), width=10)], className="vis_row")

_poagraph_row = dbc.Row(children=[dbc.Col(html.H4("Pangenome - a closer view on graph details"), width=12),
                                  dbc.Col([html.P(
                                      "This is a visualisation of pangenome internal representation as a PoaGraph"),
                                           html.Div(id=id_poagraph_node_info)], width=2),
                                  dbc.Col(html.Div(id=id_poagraph_container,
                                                   children=dcc.Loading(cyto.Cytoscape(id=id_poagraph,
                                                                           layout={
                                                                               'name': 'preset'},
                                                                           stylesheet=poagraph_component.get_poagraph_stylesheet(),
                                                                           elements=[
                                                                           ],
                                                                           style={'width': 'auto',
                                                                                  'height': '500px',
                                                                                  'background-color': 'white'},
                                                                           zoom=20,
                                                                           minZoom=0.9,
                                                                           maxZoom=1.1,
                                                                           # panningEnabled=False,
                                                                           # userPanningEnabled=False,
                                                                           boxSelectionEnabled=False,
                                                                           # autoungrabify=True,
                                                                           autolock=True,
                                                                           autounselectify=True
                                                                           ), type="circle")), width=10)], className="vis_row")

_consensus_tree_row = dbc.Row(children=[dbc.Col([html.H4("Consensus Tree")], width=12),
                                        dbc.Col([html.P(
                                            "This is consensus tree generated using this software. IOt is similar to a phylogenetic tree but every node has a consensus sequence assigned.")],
                                                width=2),
                                        dbc.Col([dcc.Graph(
                                            id=id_consensus_tree_graph,
                                            style={'height': '600px', 'width': 'auto'},
                                            config={
                                                    'displayModeBar': True
                                                },

                                            # style={'width': 'auto'}
                                        ),
                                            html.Div(dcc.Slider(
                                                id=id_consensus_tree_slider,
                                                min=0,
                                                max=1,
                                                marks={
                                                    int(i) if i % 1 == 0 else i: '{}'.format(i)
                                                    for i
                                                    in
                                                    [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
                                                     0.9,
                                                     1]},
                                                step=0.01,
                                                value=0.5,
                                                dots=True
                                            ), style={"margin": '-1% 20% 0% 3%'})], width=7, id="consensus_tree_col"),
                                        dbc.Col(children=[html.H5("Metadata in consensuses tree leaves:"),
                                                          dcc.Dropdown(
                                                              id=id_leaf_info_dropdown,
                                                              style={'margin-bottom': '20px'},
                                                              options=[
                                                              ],
                                                              value='SEQID'
                                                          ),
                                                          html.H5(["Consensus tree node details:",html.P(
                                                              id=id_consensus_node_details_header
                                                          ),]),

                                                          html.Img(
                                                              id=id_consensus_node_details_distribution,
                                                              style={'max-width': '100%', 'margin-bottom':'2%'}
                                                          ),
                                                          dcc.Loading(dash_table.DataTable(
                                                              id=id_consensus_node_details_table,
                                                              style_table={
                                                                  'maxHeight': '800',
                                                                  'overflowY': 'scroll'
                                                              },
                                                              style_cell={'textAlign': 'left'},
                                                              sorting=True
                                                          ), type="circle")], width=3)], className="vis_row")


_consensus_table_row = dbc.Row(children=[dbc.Col(html.H4("Consensuses on current Consensus Tree cut level"), width=12),
                                  dbc.Col(html.Div(id=id_consensus_table_container,
                                                   children=dcc.Loading(dash_table.DataTable(id=id_consensuses_table,
                                                                       sorting=True,
                                                                       sorting_type="multi"), type="circle")), width=12, style={'overflow-x': 'scroll'})], className="vis_row")

loading_style="circle"
_pangtreeviz_tab = dbc.Container([
    dcc.Store(id=id_visualisation_session_info, data=""),
    dcc.Store(id=id_elements_cache_info, data=""),
    dbc.Row(style={'display': 'none'}, children=[html.Div(id=id_pangenome_hidden),
                                                 html.Div(id=id_poagraph_hidden),
                                                 html.Div(id=id_full_consensustree_hidden),
                                                 html.Div(id=id_partial_consensustable_hidden),
                                                 html.Div(id=id_current_consensustree_hidden),
                                                 html.Div(id=id_full_consensustable_hidden),
                                                 html.Div(id=id_consensus_node_details_table_hidden)]),
    _load_pangenome_row,
    dbc.Collapse(
        id=id_pangviz_result_collapse,
        children=[_task_parameters_row,
                  _input_data_row,
                  _pangenome_row,
                  _poagraph_row,
                  _consensus_tree_row,
                  _consensus_table_row])
], fluid=True)


def get_task_description_layout(jsonpangenome: PangenomeJSON) -> dbc.CardDeck():
    fasta_provider_paragraph = html.P()
    if jsonpangenome.task_parameters.multialignment_format == "Maf":
        opt = jsonpangenome.task_parameters.fasta_complementation_option
        if opt == "ConstSymbolProvider":
            o = f"Const symbol {jsonpangenome.task_parameters.missing_base_symbol}"
        elif opt == "FromFile":
            o = f"Fasta file {jsonpangenome.task_parameters.fasta_source_file}"
        else:
            o = "NCBI"
        fasta_provider_paragraph = html.P(f"Fasta provider: {o}")

    if jsonpangenome.task_parameters.consensus_type == "poa":
        cons_type_paragraph = [html.P(f"Hbmin: {jsonpangenome.task_parameters.hbmin}")]
    else:
        cons_type_paragraph = [html.P(f"P: {jsonpangenome.task_parameters.p}"),
                               html.P(f"Stop: {jsonpangenome.task_parameters.stop}")]

    return dbc.CardDeck(
        [
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.P([
                                html.P(f"Multialignment: {jsonpangenome.task_parameters.multialignment_file_path}"),
                                html.P(f"Metadata : {jsonpangenome.task_parameters.metadata_file_path}"),
                                fasta_provider_paragraph
                            ], className='card-text'
                            ),
                        ]
                    ),
                    dbc.CardFooter("PoaGraph Configuration", className="text-center"),
                ],
                outline=True,
                color="dark",
            ),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.P([
                                             html.P(f"Algorithm: {jsonpangenome.task_parameters.consensus_type}"),
                                             html.P(f"Blosum file: {jsonpangenome.task_parameters.blosum_file_path}")]
                                         + cons_type_paragraph, className='card-text'

                                         ),
                        ]
                    ),
                    dbc.CardFooter("Consensus Configuration", className="text-center"),
                ],
                outline=True,
                color="dark",
            ),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.P([
                                html.P(f"Time: {jsonpangenome.task_parameters.running_time}"),
                                html.P(f"Poagraph nodes count: {len(jsonpangenome.nodes)}"),
                                html.P(f"Sequences count: {len(jsonpangenome.sequences)}"),
                                html.P(f"Consensuses count: {len(jsonpangenome.consensuses)}"),
                            ], className='card-text'
                            ),
                        ]
                    ),
                    dbc.CardFooter("Processing info", className="text-center"),
                ],
                outline=True,
                color="dark",
            ),
        ]
    )
