import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from .layout_ids import *


def pang_task_form(label, label_id, form, text, extra_label_id=None):
    form_group_children = [
        dbc.Label(label, html_for=label_id, width=3, className="poapangenome_label"),
        dbc.Col(form + [dbc.FormText(text, color="secondary")], width=6)
    ]
    if extra_label_id: form_group_children.append(dbc.Label(id=extra_label_id, width=3, className="poapangenome_label"))

    return dbc.FormGroup(form_group_children, row=True)


_data_type_form = pang_task_form(
    label_id=id_data_type,
    label="Data Type",
    form=[
        dbc.RadioItems(value="Nucleotides",
                       id=id_data_type,
                       options=[{"label": l, "value": v}
                                for l, v in [("Nucleotides", "Nucleotides"), ("Proteins", "Aminoacids")]])
    ],
    text="Type of aligned sequences provided in the uploaded multialignment file."
)  # style={"display": "none"}

_metadata_upload_form = pang_task_form(
    label_id=id_metadata_upload,
    label="Sequences metadata",
    extra_label_id=id_metadata_upload_state_info,
    form=[
        dcc.Upload(id=id_metadata_upload, multiple=False, children=[
            dbc.Row([
                dbc.Col(html.I(className="fas fa-file-csv fa-2x"), className="col-md-2"),
                html.P("Drag & drop or select file...", className="col-md-10")
            ])
        ], className="file_upload"),
        dcc.Store(id=id_metadata_upload_state)
    ],
    text=[
        """CSV with sequences metadata. It will be included in the visualisation. The 'seqid' column is obligatory and 
        must match sequences identifiers from MULTIALIGNMENT file. Other columns are optional. Example file: """,
        html.A("metadata.csv",
               href="https://github.com/meoke/pang/blob/master/data/Fabricated/f_metadata.csv",
               target="_blank")],
)

_multialignment_upload_form = pang_task_form(
    label_id=id_multialignment_upload,
    label="Multialignment",
    extra_label_id=id_multialignment_upload_state_info,
    form=[
        dcc.Upload(id=id_multialignment_upload, multiple=False, children=[
            dbc.Row([
                dbc.Col(html.I(className="fas fa-align-justify fa-2x"), className="col-md-2"),
                html.P("Drag & drop or select file...", className="col-md-10")
            ])
        ], className="file_upload"),
        dcc.Store(id=id_multialignment_upload_state),
    ],
    text=["Accepted formats: ",
          html.A(href="http://www1.bioinf.uni-leipzig.de/UCSC/FAQ/FAQformat.html#format5",
                 target="_blank",
                 children="maf"),
          ", ",
          html.A(href="https://github.com/meoke/pang/blob/master/README.md#po-file-format-specification",
                 target="_blank",
                 children="po"),
          ". See example file: ",
          html.A(href="https://github.com/meoke/pang/blob/master/data/Fabricated/f.maf",
                 target="_blank",
                 children="example.maf")],
)

_missing_data_form = dbc.Collapse([
    pang_task_form(
        label_id=id_fasta_provider_choice,
        label="Missing nucleotides source",
        form=[dbc.RadioItems(value="NCBI",
                             options=[{"label": l, "value": v}
                                      for l, v in [("NCBI", "NCBI"), ("Fasta File", "File"), ("Custom symbol", "Symbol")]],
                             id=id_fasta_provider_choice)],
        text="MAF file may not inlcude full sequences. Specify source of missing nucleotides/proteins."
    ),
    dbc.Collapse(id=id_missing_symbol_param, children=pang_task_form(
        label_id=id_fasta_provider_choice,
        label="Missing symbol for unknown nucleotides/proteins",
        form=[dbc.Input(value="?", id=id_missing_symbol_input, type='text', maxLength=1, minLength=1)],
        text="Any single character is accepted but it must be present in BLOSUM file. Default BLOSUM file uses '?'."
    )),
    dbc.Collapse(id=id_fasta_upload_param, children=pang_task_form(
        label_id=id_fasta_provider_choice,
        label="Missing symbols file source",
        extra_label_id=id_fasta_upload_state_info,
        form=[
            dcc.Upload(id=id_fasta_upload, multiple=False, children=[
                dbc.Row([
                    dbc.Col(html.I(className="fas fa-align-left fa-2x"),className="col-md-2"),
                    html.P("Drag & drop or select file...", className="col-md-10")
                ])
            ], className="file_upload"),
            dcc.Store(id=id_fasta_upload_state)
        ],
        text="""Provide zip with fasta files or single fasta file. It must contain full sequeneces which are not 
        fully represented in provided MAF file."""
    ))
], id=id_maf_specific_params)

_consensus_algorithm_form = pang_task_form(
    label_id=id_data_type,
    label="Consensus algorithm",
    form=[
        dbc.RadioItems(value="tree",
                       options=[{'label': "Poa", 'value': 'poa'}, {'label': 'Tree', 'value': 'tree'}],
                       id=id_consensus_algorithm_choice)
    ],
    text=["There are two available algorithms for consensus tree generation. 'Poa' by ",
          html.A("Lee et al.", href="https://doi.org/10.1093/bioinformatics/btg109"),
          " and 'Tree' algorithm described ",
          html.A("here", href="https://github.com/meoke/pang#idea-and-algorithm-description")]
)

_blosum_upload_form = pang_task_form(
    label_id=id_blosum_upload,
    label="BLOSUM",
    extra_label_id=id_blosum_upload_state_info,
    form=[
        dcc.Upload(id=id_blosum_upload,
                   multiple=False,
                   children=[dbc.Row([
                       dbc.Col(html.I(className="fas fa-table fa-2x"), className="col-md-2"),
                       html.P("Drag & drop or select file...", className="col-md-10")])], className="file_upload"),
        dcc.Store(id=id_blosum_upload_state)
    ],
    text=["This parameter is optional as default BLOSUM file is ",
          html.A(href="https://github.com/meoke/pang/blob/master/bin/blosum80.mat", target="_blank", children="BLOSUM80"),
          ". The BLOSUM matrix must contain '?' or the custom symbol for missing nucleotides, if specified."]
)

_poa_hbmin_form = dbc.Collapse(pang_task_form(
    label_id=id_hbmin_input,
    label="HBMIN",
    form=[dbc.Input(value=0.9, type='number', min=0, max=1, id=id_hbmin_input)],
    text="""HBMIN is required minimum value of similarity between sequence and assigned consensus. It must be a value 
    from range [0,1]."""
), id=id_poa_specific_params)

_tree_params_form = dbc.Collapse([
    pang_task_form(
        label_id=id_hbmin_input,
        label="P",
        form=[dbc.Input(value=1, type='number', min=0, id=id_p_input)],
        text=["""P is used during cutoff search. P < 1 decreases distances between small compatibilities and increases 
        distances between the bigger ones while P > 1 works in the opposite way. This value must be > 0. """,
              html.A("Read more...", href="https://github.com/meoke/pang", target="_blank")]
    ),
    pang_task_form(
        label_id=id_hbmin_input,
        label="Stop",
        form=[dbc.Input(value=1, type='number', min=0, max=1, id=id_stop_input)],
        text="Minimum value of compatibility in tree leaves. It must be a value  from range [0,1]."
    )
], id=id_tree_specific_params)

_output_form = pang_task_form(
    label_id=id_output_configuration,
    label="Additional output generation",
    form=[dbc.Checklist(id=id_output_configuration,
                        options=[{'label': 'FASTA (all sequences and consensuses in fasta format)', 'value': 'fasta'},
                                 {'label': 'PO (poagraph in PO format)', 'value': 'po'}],
                        values=['fasta', 'po'])],
    text=""
)

_pang_form = dbc.Form([
    _data_type_form,
    _metadata_upload_form,
    _multialignment_upload_form,
    _missing_data_form,
    _blosum_upload_form,
    _consensus_algorithm_form,
    _poa_hbmin_form,
    _tree_params_form,
    _output_form
])

pangtreebuild_tab = html.Div([
    dcc.Store(id=id_session_state),
    dcc.Store(id=id_session_dir),
    dbc.Row([
        dbc.Col([
            html.H3("Task Parameters"),
            _pang_form,
            dbc.Row(
                dbc.Col(dbc.Button("Run", id=id_pang_button, color="primary", className="offset-md-5 col-md-4 ")),
                dbc.Col(dcc.Loading(id="l2", children=html.Div(id=id_running_indicator), type="default")))
            ], className="col-md-8 offset-md-1", id='poapangenome_form'),
    ], className="poapangenome_content"),
    dbc.Collapse(id=id_poapangenome_result, children=dbc.Row(children=[
        dbc.Col([
            dbc.Row([
                html.I(id=id_result_icon),
                html.H3("Task completed!", className="next_to_icon")
            ]),
            dbc.Col(html.Div(id=id_poapangenome_result_description), className="col-md-11")
        ], className="col-md-6 offset-md-1"),
        dbc.Col([
            html.A(dbc.Button("Download result files", block=True, className="result_btn", color="info"),
                   id=id_download_processing_result),
            dbc.Button("Go to visualisation",
                       id=id_go_to_vis_tab,
                       n_clicks_timestamp=0,
                       block=True, className="result_btn",
                       color="success",
                       style={"visibility": "hidden"})
        ], className="col-md-3 offset-md-1")]
    ))
])
