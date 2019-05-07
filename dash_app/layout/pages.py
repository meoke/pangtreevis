import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from .layout_ids import *
import dash_cytoscape as cyto
import dash_table
from ..components import mafgraph as mafgraph_component
from ..components import poagraph as poagraph_component


def contact():
    return dbc.Container(
        [
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardTitle("Norbert Dojer, PhD.", className="text-info"),
                            dbc.CardText(html.P("dojer@mimuw.edu.pl")),
                        ]
                    ),
                ],
                outline=True,
                color="info"
            ),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardTitle("Paulina Dziadkiewicz, B.Sc.", className="text-info"),
                            dbc.CardText("pedziadkiewicz@gmail.com"),
                        ]
                    )
                ],
                outline=True,
                color="info",
            )
        ]
    )


def index():
    return dbc.Container(
        html.Div([
            dbc.Jumbotron(children=[dbc.Row(
                [dbc.Col([html.H2("PoaPangenome"),
                          html.P("is a tool for multiple sequence alignment analysis."),
                          html.H2("PangViz"),
                          html.P("visualises the results in browser.")
                          ],
                         className="col-md-8"),
                 dbc.Col(html.I(className="fas fa-seedling fa-10x logo"), className="col-md-4")])]),
            dbc.Row(
                dbc.CardDeck(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(dbc.Row([dbc.Col(html.I(className="fas fa-bezier-curve fa-2x"),
                                                                className="col-md-3 my-auto"),
                                                        html.P(
                                                            "Build graph representation of multiple sequence alignment",
                                                            className="col-md-9 my-auto")])),
                                dbc.CardBody(
                                    [
                                        dbc.CardText(
                                            html.Ul([html.Li(
                                                ["Input formats: ",
                                                 html.A("MAF",
                                                        href="http://www1.bioinf.uni-leipzig.de/UCSC/FAQ/FAQformat.html#format5",
                                                        target="_blank"), ", ",
                                                 html.A("PO",
                                                        href="https://github.com/meoke/pang/blob/master/README.md#po-file-format-specification",
                                                        target="_blank")]),
                                                html.Li(["Internal representation: ", html.A("Partial Order graph",
                                                                                             href="https://doi.org/10.1093/bioinformatics/18.3.452",
                                                                                             target="_blank")]),
                                                html.Li(["Cycles in graph removed with ", html.A("Mafgraph",
                                                                                                 href="https://github.com/anialisiecka/Mafgraph",
                                                                                                 target="_blank")]),
                                                html.Li("Complement missing parts from NCBI or fasta")]))
                                    ]
                                ),
                            ]
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader(dbc.Row([dbc.Col(html.I(className="fas fa-grip-lines fa-2x"),
                                                                className="col-md-3 my-auto"),
                                                        html.P("Find sequences consensus",
                                                               className="col-md-9 my-auto")])),
                                dbc.CardBody(
                                    [
                                        dbc.CardText(
                                            ["This tool extends Partial Order Alignment (POA) algorithm introduced by ",
                                             html.A("Lee et al.",
                                                    href="https://doi.org/10.1093/bioinformatics/18.3.452",
                                                    target="_blank"), ". It provides:",
                                             html.Ul([html.Li([html.Strong("Consensuses"),
                                                               " - agreed representations of input subsets"]),
                                                      html.Li([html.Strong("Consensus Tree"),
                                                               " - a structure similar to phylogenetic tree but it has a consensus assigned to every node"]),
                                                      html.Li([html.Strong("Compatibility"),
                                                               " - a measure of similarity between sequence and consensus"])])
                                             ]),
                                    ]
                                ),
                            ]
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader(dbc.Row([dbc.Col(html.I(className="fas fa-eye fa-2x"),
                                                                className="col-md-3 my-auto"),
                                                        html.P("Visualise results",
                                                               className="col-md-9 my-auto")])),
                                dbc.CardBody(
                                    [
                                        dbc.CardText(
                                            [
                                                html.Ul([html.Li(
                                                    "MAF blocks graph"),
                                                    html.Li("Multiple sequence alignment as Partial Order Graph"),
                                                    html.Li("Consensus tree"),
                                                    html.Li("Compatibilities relations")]
                                                )])
                                    ]
                                ),
                            ]
                        ),
                    ]
                )
            )

        ])
    )


def package():
    return dbc.Container([dbc.Row(html.Span(["The underlying software is available at ",
                                             html.A("GitHub", href="https://github.com/meoke/pang", target="_blank"),
                                             " and ",
                                             html.A("PyPI", href="", target="_blank"),
                                             ". It can be incorporated into your Python application in this simple way:"])),
                          dbc.Card(dbc.CardBody(dcc.Markdown('''

                          
                          from poapangenome import Poagraph, input_types, fasta_provider, consensus

                          poagraph = Poagraph.build_from_dagmaf(input_types.Maf("example.maf"), 
                                                                fasta_provider.FromNCBI())
                          consensus_tree = consensus.tree_generator.get_consensus_tree(poagraph,
                                                                                       Blosum("BLOSUM80.mat"),
                                                                                       output_dir,
                                                                                       stop=1,
                                                                                       p=1)
                          pangenomejson = to_PangenomeJSON(poagraph, consensus_tree)
                          
                          ''')), style={"margin": '30px 0px', 'padding': '10px'}),
                          dbc.Row("or used as a CLI tool:"),
                          dbc.Card(dbc.CardBody(dcc.Markdown(
                              '''poapangenome --multialignment "example.maf" --consensus tree --p 1 --stop 1''')),
                              style={"margin": '30px 0px', 'padding': '10px'}),
                          dbc.Row("Check out full documentation at the above links.")
                          ]
                         )


def tools():
    return html.Div([
        dbc.Jumbotron(children=[dbc.Row(
            [dbc.Col(dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardText(
                                html.Ul([html.Li(
                                    [html.Span(html.I(className="fas fa-file"), className="fa-li"), "multialignment ",
                                     html.A("MAF",
                                            href="http://www1.bioinf.uni-leipzig.de/UCSC/FAQ/FAQformat.html#format5",
                                            target="_blank"), " or ",
                                     html.A("PO",
                                            href="https://github.com/meoke/pang/blob/master/README.md#po-file-format-specification",
                                            target="_blank")]),
                                    html.Li([html.Span(html.I(className="fas fa-file"), className="fa-li"),
                                             "metadata CSV"]),
                                    html.Li([html.Span(html.I(className="fas fa-sliders-h"), className="fa-li"),
                                             "additional parameters"])], className="fa-ul")
                            )
                        ]
                    ),
                ], outline=True
            ), className="col-md-2 offset-md-1"),
                dbc.Col(html.I(className="fas fa-long-arrow-alt-right fa-3x"),
                        className="col-md-1 my-auto text-center"),
                dbc.Col(html.H2(dbc.Badge("PoaPangenome", className="badge-success badge-pill")),
                        className="col-md-2 my-auto"),
                dbc.Col(html.I(className="fas fa-long-arrow-alt-right fa-3x"),
                        className="col-md-1 my-auto text-center"),
                dbc.Col(dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dbc.CardText(dbc.Row(
                                    [
                                        dbc.Col(html.I(className="fas fa-file"), className="col-md-3"),
                                        dbc.Col("pangenome.json"),
                                    ],
                                    align="center",
                                    no_gutters=True,
                                ))
                            ]
                        ),
                    ]
                ), className="col-md-2 my-auto"),
                dbc.Col(html.I(className="fas fa-long-arrow-alt-right fa-3x"),
                        className="col-md-1 my-auto text-center"),
                dbc.Col(html.H2(dbc.Badge("PangViz", className="badge-success badge-pill badge-block")),
                        className="col-md-2 my-auto"),
            ]
        )]),
        dbc.Tabs(
            [
                dbc.Tab(_poapangenome_tab_content, id=id_poapangenome_tab, label="PoaPangenome",
                        tab_style={"margin-left": "auto"}),
                dbc.Tab(_pangviz_tab_content, id=id_pangviz_tab, label="PangViz", label_style={"color": "#00AEF9"}),
            ], className="nav-justified",
            id=id_tools_tabs,
        )
    ])


_data_type_form = dbc.FormGroup(
    [
        dbc.Label("Data Type", html_for=id_data_type, width=3, className="poapangenome_label"),
        dbc.Col([dbc.RadioItems(value="Nucleotides", options=[{"label": "Nucleotides", "value": "Nucleotides"},
                                                              {"label": "Proteins", "value": "Proteins"}],
                                id=id_data_type),
                 dbc.FormText(
                     "Type of aligned sequences provided in the uploaded multialignment file.",
                     color="secondary",
                 )], width=6)
    ],
    row=True
)

_metadata_upload_form = dbc.FormGroup(
    [
        dbc.Label("Sequences metadata", html_for=id_metadata_upload, width=3, className="poapangenome_label"),
        dbc.Col([dcc.Upload(id=id_metadata_upload,
                            multiple=False,
                            children=[
                                dbc.Row([dbc.Col(html.I(className="fas fa-file-csv fa-2x"),
                                                 className="col-md-2"),
                                         html.P(
                                             "Drag & drop CSV metadata file or select file...",
                                             className="col-md-10")])

                            ], className="file_upload"),
                 dcc.Store(id=id_metadata_upload_state),
                 dbc.FormText(
                     [
                         "CSV with metadata about the sequences. It can enhance"
                         " the visualisation. 'seqid' column is obligatory and must match"
                         " sequences ids present in MULTIALIGNMENT file. "
                         "Other columns are optional. Example file: ",
                         html.A("metadata.csv",
                                href="https://github.com/meoke/pang/blob/master/data/Fabricated/f_metadata.csv",
                                target="_blank")],
                     color="secondary",
                 )
                 ], width=6),
        dbc.Label(id=id_metadata_upload_state_info, width=3, className="poapangenome_label")
    ],
    row=True
)

_multialignment_upload_form = dbc.FormGroup(
    [
        dbc.Label("Mulitialignment", html_for=id_multialignment_upload, width=3, className="poapangenome_label"),
        dbc.Col([dcc.Upload(id=id_multialignment_upload,
                            multiple=False,
                            children=[
                                dbc.Row([dbc.Col(html.I(className="fas fa-align-justify fa-2x"),
                                                 className="col-md-2"),
                                         html.P(
                                             "Drag & drop multialignment file or select file...",
                                             className="col-md-10")])

                            ], className="file_upload"),
                 dcc.Store(id=id_multialignment_upload_state),
                 dbc.FormText(
                     [
                         "Multialignment file. Accepted formats: ",
                         html.A(
                             href="http://www1.bioinf.uni-leipzig.de/UCSC/FAQ/FAQformat.html#format5",
                             target="_blank", children="maf"), ", ",
                         html.A(
                             href="https://github.com/meoke/pang/blob/master/README.md#po-file-format-specification",
                             target="_blank", children="po"),
                         ". See example file: ",
                         html.A(
                             href="https://github.com/meoke/pang/blob/master/data/Fabricated/f.maf",
                             target="_blank",
                             children="example.maf")],
                     color="secondary",
                 )
                 ], width=6),
        dbc.Label(id=id_multialignment_upload_state_info, width=3, className="poapangenome_label")
    ],
    row=True
)

_missing_data_form = dbc.Collapse([dbc.FormGroup(
    [
        dbc.Label("Missing nucleotides source", html_for=id_fasta_provider_choice, width=3,
                  className="poapangenome_label"),
        dbc.Col([dbc.RadioItems(value="NCBI", options=[{'label': "NCBI", 'value': 'NCBI'},
                                                       {'label': 'Fasta File',
                                                        'value': 'File'},
                                                       {'label': 'Custom symbol',
                                                        'value': 'Symbol'}],
                                id=id_fasta_provider_choice),
                 dbc.FormText(
                     "MAF file may not inlcude full sequences. Specify source of missing nucleotides/proteins.",
                     color="secondary",
                 )], width=6)
    ],
    row=True
), dbc.Collapse(id=id_missing_symbol_param, children=[dbc.FormGroup(
    children=[
        dbc.Label("Missing symbol for unknown nucleotides/proteins", html_for=id_fasta_provider_choice,
                  width=3, className="poapangenome_label"),
        dbc.Col([dbc.Input(value="?",
                           id=id_missing_symbol_input, type='text', maxlength=1, minlength=1),
                 dbc.FormText(
                     "Any single character is accepted but it must be present in BLOSUM file. Default BLOSUM file uses '?'.",
                     color="secondary",
                 )], width=6)], row=True
)]),
    dbc.Collapse(id=id_fasta_upload_param, children=[dbc.FormGroup(
        children=[
            dbc.Label("Missing symbols file source", html_for=id_fasta_provider_choice,
                      width=3, className="poapangenome_label"),
            dbc.Col([dcc.Upload(id=id_fasta_upload,
                                multiple=False,
                                children=[
                                    dbc.Row([dbc.Col(html.I(className="fas fa-align-left fa-2x"),
                                                     className="col-md-2"),
                                             html.P(
                                                 "Drag & drop FASTA/ZIP file or select file..",
                                                 className="col-md-10")])

                                ], className="file_upload"),
                     dcc.Store(id=id_fasta_upload_state),
                     dbc.FormText(
                         [
                             "Provide zip with fasta files or single fasta file. It must contain full sequeneces which are not fully represented in provided MAF file."],
                         color="secondary",
                     )
                     ], width=6),
            dbc.Label(id=id_fasta_upload_state_info, width=3, className="poapangenome_label")], row=True
    )])
], id=id_maf_specific_params)

_consensus_algorithm_form = dbc.FormGroup(
    [
        dbc.Label("Consensus algorithm", html_for=id_data_type, width=3, className="poapangenome_label"),
        dbc.Col([dbc.RadioItems(value="tree", options=[
            {'label': "Poa", 'value': 'poa'},
            {'label': 'Tree', 'value': 'tree'},
        ],
                                id=id_consensus_algorithm_choice),
                 dbc.FormText(
                     [
                         "There are two available algorithms for consensus tree generation. 'Poa' by ",
                         html.A(
                             "Lee et al.",
                             href="https://doi.org/10.1093/bioinformatics/18.3.452"),
                         " and 'Tree' algorithm described ",
                         html.A("here",
                                href="https://github.com/meoke/pang#idea-and-algorithm-description")],
                     color="secondary",
                 )], width=6)
    ],
    row=True
)

_blosum_upload_form = dbc.FormGroup(
    [
        dbc.Label("BLOSUM file", html_for=id_blosum_upload, width=3, className="poapangenome_label"),
        dbc.Col([dcc.Upload(id=id_blosum_upload,
                            multiple=False,
                            children=[
                                dbc.Row([dbc.Col(html.I(className="fas fa-table fa-2x"),
                                                 className="col-md-2"),
                                         html.P(
                                             "Drag & drop BLOSUM file or select file...",
                                             className="col-md-10")])

                            ], className="file_upload"),
                 dcc.Store(id=id_blosum_upload_state),
                 dbc.FormText(
                     [
                         "BLOSUM file. This parameter is optional as default BLOSUM file is ", html.A(
                         href="https://github.com/meoke/pang/blob/master/bin/blosum80.mat",
                         target="_blank", children="BLOSUM80"),
                         ". The BLOSUM file must contain '?' or custom symbol for missing nucleotides/proteins if specified."],
                     color="secondary",
                 )
                 ], width=6),
        dbc.Label(id=id_blosum_upload_state_info, width=3, className="poapangenome_label")
    ],
    row=True
)

_poa_hbmin_form = dbc.Collapse([dbc.FormGroup(
    [
        dbc.Label("HBMIN", html_for=id_hbmin_input, width=3,
                  className="poapangenome_label"),
        dbc.Col([dbc.Input(value=0.9, type='number', min=0, max=1,
                           id=id_hbmin_input),
                 dbc.FormText(
                     "HBMIN is required minimum value of similarity between sequence and assigned consensus. It must be a value  from range [0,1].",
                     color="secondary",
                 )], width=6)
    ],
    row=True
)
], id=id_poa_specific_params)

_tree_params_form = dbc.Collapse([dbc.FormGroup([
    dbc.Label("P", html_for=id_hbmin_input, width=3,
              className="poapangenome_label"),
    dbc.Col([dbc.Input(value=1, type='number', min=0,
                       id=id_p_input),
             dbc.FormText(
                 "P is used during cutoff search. P < 1 decreases distances between small compatibilities and increases distances between the bigger ones while P > 1 works in the opposite way. This value must be > 0.",
                 color="secondary",
             )], width=6)
],
    row=True), dbc.FormGroup([
    dbc.Label("Stop", html_for=id_hbmin_input, width=3,
              className="poapangenome_label"),
    dbc.Col([dbc.Input(value=1, type='number', min=0, max=1,
                       id=id_stop_input),
             dbc.FormText(
                 "Minimum value of compatibility in tree leaves. It must be a value  from range [0,1].",
                 color="secondary",
             )], width=6)
],
    row=True)], id=id_tree_specific_params)

_output_form = dbc.FormGroup(
    [
        dbc.Label("Additional output generation", html_for=id_output_configuration, width=3,
                  className="poapangenome_label"),
        dbc.Col([dbc.Checklist(id=id_output_configuration,
                               options=[
                                   {
                                       'label': 'FASTA (all sequences and consensuses in fasta format)',
                                       'value': 'fasta'},
                                   {'label': 'PO (poagraph in PO format)', 'value': 'po'},
                               ],
                               values=['fasta', 'po'])], width=6)
        ,
    ], row=True
)

_poapangenome_form = dbc.Form([_data_type_form,
                               _metadata_upload_form,
                               _multialignment_upload_form,
                               _missing_data_form,
                               _blosum_upload_form,
                               _consensus_algorithm_form,
                               _poa_hbmin_form,
                               _tree_params_form,
                               _output_form
                               ])

_poapangenome_tab_content = html.Div([
    dcc.Store(id=id_session_state),
    dcc.Store(id=id_session_dir),
    dbc.Row([
        dbc.Col(
            [
                html.H3("Task Parameters"),
                _poapangenome_form,
                dbc.Row(
                    dbc.Col(dbc.Button("Run", id=id_pang_button, color="primary", className="offset-md-5 col-md-4 ")),
                    dbc.Col(dcc.Loading(id="l2", children=html.Div(id=id_running_indicator), type="default")))
            ], className="col-md-6 offset-md-1"),
        dbc.Col([
            html.H3("Example Input Data"),
            dbc.Card(
                [
                    dbc.CardHeader(
                        dbc.Button("Fabricated", id="collapse_fabricated_button",
                                   className="mb-3 btn-block my-auto opac-button")),
                    dbc.Collapse(
                        id="fabricated_collapse",
                        children=
                        dbc.CardBody(
                            [
                                dbc.CardText(["This dataset is very small and consists of fabricated sequences."
                                              "Its aim is to demonstrate how the processing and visualisation works",
                                              html.Button("a", className="btn btn-primary btn-block dataset")]),
                            ]
                        )),
                ]
            ),
            dbc.Card(
                [
                    dbc.CardHeader(
                        dbc.Button("Ebola", id="collapse-ebola-button",
                                   className="mb-3 btn-block my-auto opac-button")),
                    dbc.Collapse(
                        id="ebola_collapse",
                        children=dbc.CardBody(
                            [
                                dbc.CardText(["This dataset orginates from ", html.A("UCSC Ebola Portal",
                                                                                     href="https://genome.ucsc.edu/ebolaPortal/",
                                                                                     target="_blank")]),
                            ]
                        ))
                ],
            ),
            dbc.Card(
                [
                    dbc.CardHeader(
                        dbc.Button("Balibase", id="collapse-balibase-button",
                                   className="mb-3 btn-block my-auto opac-button")),
                    dbc.Collapse(
                        id="balibase_collapse",
                        children=dbc.CardBody(
                            [
                                dbc.CardText(["This is a multiplwe protein sequence alignment. It is based on ",
                                              html.A("BAliBASE 4", href="http://www.lbgi.fr/balibase/",
                                                     target="_align")]),
                            ]
                        )),
                ],
            ),

        ], className="col-md-3 offset-md-1")
    ], className="poapangenome_content"),
    dbc.Collapse(id=id_poapangenome_result, children=dbc.Row(
        children=[dbc.Col([html.Div(id=id_poapangenome_result_description)], className="col-md-6 offset-md-1"),
                  dbc.Col([
                      html.A(dbc.Button("Download result files", block=True, className="result_btn", color="info"),
                             id=id_download_processing_result),
                      dbc.Button("Go to visualisation", id=id_go_to_vis_tab,
                                 n_clicks_timestamp=0, block=True, className="result_btn", color="success")],
                      className="col-md-3 offset-md-1")]

    ))
])

_load_pangenome_row = dbc.Row(id=id_pangviz_load_row,
                              children=[
                                  dbc.Col(dcc.Upload(id=id_pangenome_upload,
                                                     multiple=False,
                                                     children=[
                                                         dbc.Row([dbc.Col(html.I(className="fas fa-align-left fa-2x"),
                                                                          className="col-md-2"),
                                                                  html.P(
                                                                      "Drag & drop pangenome.json file or select file..",
                                                                      className="col-md-10")])

                                                     ], className="file_upload"), className="col-md-4 offset-md-1"),
                                  dbc.Col("or", className="col-md-2"),
                                  dbc.Col(dbc.DropdownMenu(
                                      label="load example data",
                                      children=[
                                          dbc.DropdownMenuItem("Fabricated", id=id_pangviz_example_fabricated),
                                          dbc.DropdownMenuItem("Ebola", id_pangviz_example_ebola),
                                          dbc.DropdownMenuItem("Ballibase", id=id_pangviz_example_ballibase),
                                      ]
                                  ), className="col-md-4")

                              ])

_task_parameters_row = dbc.Row(id=id_task_parameters_row, children=[html.Div(id=id_task_parameters_vis)])

_input_data_row = dbc.Row(children=[dbc.Col(html.Div(id=id_input_info_vis)),
                                    dbc.Col(html.Div(id=id_input_dagmaf_vis,
                                                     children=[html.H3("MAF graph"),
                                                               cyto.Cytoscape(id=id_mafgraph_graph,
                                                                              elements=[],
                                                                              layout={'name': 'cose'},
                                                                              style={'width': 'auto',
                                                                                     'height': '300px'},
                                                                              stylesheet=mafgraph_component.get_mafgraph_stylesheet(),
                                                                              # autolock=True,
                                                                              boxSelectionEnabled=False,
                                                                              # autoungrabify=True,
                                                                              autounselectify=True)]
                                                     ))])

_pangenome_row = dbc.Row(children=[dbc.Col(html.H3("Pangenome info"),
                                           html.Div(id=id_poagraph_node_info), className="col-md-1"),
                                   dbc.Col([html.H3("Pangenome graphs"),
                                            html.Div(id=id_full_pangenome_container,
                                                     children=[dcc.Graph(
                                                         id=id_full_pangenome_graph,
                                                         style={'width': 'auto'},
                                                         # style={'height': '400px', 'width': 'auto'},
                                                         figure={},
                                                         config={
                                                             'displayModeBar': False,
                                                         }
                                                     )]),
                                            html.Div(id=id_poagraph_container,
                                                     children=cyto.Cytoscape(id=id_poagraph,
                                                                             layout={
                                                                                 'name': 'preset'},
                                                                             stylesheet=poagraph_component.get_poagraph_stylesheet(),
                                                                             elements=[
                                                                             ],
                                                                             style={'width': 'auto', 'height': '500px'},
                                                                             zoom=1,
                                                                             # minZoom=0.9,
                                                                             # maxZoom=1.1,
                                                                             # panningEnabled=False,
                                                                             # userPanningEnabled=False,
                                                                             boxSelectionEnabled=False,
                                                                             autoungrabify=True,
                                                                             autolock=True,
                                                                             autounselectify=True
                                                                             ))
                                            ], className="col-md-11")])

_consensus_tree_row = dbc.Row(children=[
    dbc.Col(children=[dcc.Graph(
        id=id_consensus_tree_graph,
        style={'height': '1000px', 'width': 'auto'}
    ),
        dcc.Slider(
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
        )
    ], className="col-md-8"),
    dbc.Col(children=[ html.H5("Metadata in consensuses tree leaves:"),
                                               dcc.Dropdown(
                                                   id=id_leaf_info_dropdown,
                                                   style={'margin-bottom': '20px'},
                                                   options=[
                                                   ],
                                                   value='SEQID'
                                               ),
                                               html.H5("Consensus tree node details:"),
                                               html.H5(
                                                   id=id_consensus_node_details_header
                                               ),
                                               html.Img(
                                                   id=id_consensus_node_details_distribution,
                                               ),
                                               dash_table.DataTable(
                                                   id=id_consensus_node_details_table,
                                                   style_table={
                                                       'maxHeight': '800',
                                                       'overflowY': 'scroll'
                                                   },
                                                   style_cell={'textAlign': 'left'},
                                                   sorting=True
                                               )], className="col-md-4")
])

_consensus_table_row = dbc.Row(html.Div(id=id_consensus_table_container,
                                         children=[dash_table.DataTable(id=id_consensuses_table,
                                                          sorting=True,
                                                          sorting_type="multi")

], style={'width': 'auto'}))

_pangviz_tab_content = html.Div([
    html.Div(style={'display': 'none'}, children=[html.Div(id=id_pangenome_hidden),
                                                  html.Div(id=id_poagraph_hidden),
                                                  html.Div(id=id_full_consensustree_hidden),
                                                  html.Div(id=id_partial_consensustable_hidden),
                                                  html.Div(id=id_current_consensustree_hidden),
                                                  html.Div(id=id_full_consensustable_hidden),
                                                  html.Div(id=id_consensus_node_details_table_hidden)]),
    _load_pangenome_row,
    _task_parameters_row,
    _input_data_row,
    _pangenome_row,
    _consensus_tree_row,
    _consensus_table_row
])
