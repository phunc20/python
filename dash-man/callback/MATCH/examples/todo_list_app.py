from dash import (
    Dash, dcc, html, Input, Output, State,
    MATCH, ALL, Patch, callback, no_update,
    callback_context,
)
from dash.exceptions import PreventUpdate

# TODO:
# 1. Checklist label instead of output-str
# 2. More the alignment prettier

app = Dash()

app.layout = html.Div(
    [
        dcc.Checklist(
            options=[{"label": "anything", "value": "done"}],
            #id={"index": button_clicked, "type": "done"},
            #style={"display": "inline", "text-align": "left"},
            #labelStyle={"display": "inline"},
            style={"text-decoration": "line-through"}
        ),
        html.Div(
            "Dash To-Do list",
            style={
                "text-align": "center",
            },
        ),
        html.Div(
            id="todo-list-div",
            children=[
                html.Div(
                    id="list-controller-div",
                    children=[
                        dcc.Input(id="new-item-input", n_submit=0),
                        html.Button("Add", id="add-btn"),
                        html.Button(
                            "Clear Done",
                            id="clear-done-btn",
                        ),
                    ],
                    style={
                        #"display": "inline",
                        "display": "block",
                        #"text-align": "center",
                    },
                ),
                html.Div(
                    id="list-container-div",
                    style={
                        #"display": "flex",
                        #"justify-content": "center",
                        #"align-items": "center",
                        #"display": "grid",
                        #"place-items": "center",

                        #"display": "inline-block",
                        #"display": "inline",
                        "display": "block",
                        "text-align": "left",
                        #"display": "flex",
                        #"justify-content": "center",
                        #"width": "100%",
                    },
                ),
                html.Div(
                    id="totals-div",
                    style={
                        #"display": "inline-block",
                        "display": "block",
                        #"display": "inline",
                        #"text-align": "left",
                        #"text-align": "center",
                    },
                ),
            ],
            style={
                #"align-items": "center",

                #"display": "flex",
                #"justify-content": "center",
                #"width": "100%",
                #"text-align": "center",
            },
        ),
        #dcc.Input(id="new-item-input", n_submit=0),
        #html.Button("Add", id="add-btn"),
        #html.Button("Clear Done", id="clear-done-btn"),
        #html.Div(id="list-container-div"),
        #html.Div(id="totals-div"),
    ]
)


@callback(
    Output("add-btn", "n_clicks"),
    Input("new-item-input", "n_submit"),
    State("add-btn", "n_clicks"),
    prevent_initial_call=True,
)
def enable_enter_keypress(n_submit, n_clicks):
    """
    When the user type an item in the input text box and press Enter,
    this should have the same effet as clicking the add button.
    """
    if n_clicks is None:
        return 1
    else:
        return n_clicks + 1


@callback(
    Output("list-container-div", "children", allow_duplicate=True),
    Output("new-item-input", "value"),
    Input("add-btn", "n_clicks"),
    State("new-item-input", "value"),
    prevent_initial_call=True,
)
def add_item(button_clicked, value):
    """
    Output("new-item-input", "value")
    The reason we put this output in the callback is because
    we want to clean up the input text once the user confirms
    one todo item, i.e. we return an empty string `""`.
    """
    def new_checklist_item():
        return html.Div(
            [
                dcc.Checklist(
                    options=[{"label": "", "value": "done"}],
                    id={"index": button_clicked, "type": "done"},
                    style={"display": "inline-block", "vertical-align": "middle"},
                    inputStyle={"margin": "0"}
                ),
                html.Div(
                    value,
                    id={"index": button_clicked, "type": "output-str"},
                    style={"display": "inline-block", "vertical-align": "middle", "margin-left": "8px"},
                ),
            ],
            style={
                "display": "flex",
                "align-items": "center",
                "padding": "2px 0" # Vertical tightness
            }
        )

    # Cf. <https://dash.plotly.com/partial-properties#allowing-duplicate-callback-outputs>
    # in case one wonders how Patch() works with multiple-output callbacks.
    patched_list = Patch()
    patched_list.append(new_checklist_item())
    return patched_list, ""


#    #def new_checklist_item():
#    #    return html.Div(
#    #        [
#    #            dcc.Checklist(
#    #                options=[{"label": "", "value": "done"}],
#    #                id={"index": button_clicked, "type": "done"},
#    #                style={"display": "inline", "text-align": "left"},
#    #                labelStyle={"display": "inline"},
#    #            ),
#    #            html.Div(
#    #                [value],
#    #                id={"index": button_clicked, "type": "output-str"},
#    #                style={"display": "inline", "margin": "10px"},
#    #            ),
#    #        ]
#    #    )
#
#    def new_checklist_item():
#        #return html.Div(
#        #    [
#        #        dcc.Checklist(
#        #            options=[{"label": "", "value": "done"}],
#        #            id={"index": button_clicked, "type": "done"},
#        #            style={"margin-right": "10px"},
#        #        ),
#        #        html.Div(
#        #            [value],
#        #            id={"index": button_clicked, "type": "output-str"},
#        #            style={"flex": "1"}, # Allows text to take up remaining space
#        #        ),
#        #    ],
#        #    style={
#        #        "display": "flex",          # Turn on Flexbox
#        #        "align-items": "center",    # Vertically aligns checkbox with text
#        #        "justify-content": "center",# Centers the whole row horizontally
#        #        "max-width": "500px",       # Prevents the list from getting too wide
#        #        "margin": "0 auto",         # Centers the container itself on the page
#        #        "padding": "10px"
#        #    }
#        #)
#
#        #return html.Div(
#        #    [
#        #        dcc.Checklist(
#        #            options=[{"label": "", "value": "done"}],
#        #            id={"index": button_clicked, "type": "done"},
#        #            # inline-block keeps it from forcing a new line
#        #            style={"display": "inline-block", "vertical-align": "middle"},
#        #            inputStyle={"margin": "0"} # Removes default checkbox margin
#        #        ),
#        #        html.Div(
#        #            [value],
#        #            id={"index": button_clicked, "type": "output-str"},
#        #            style={"display": "inline-block", "vertical-align": "middle"}
#        #        ),
#        #    ],
#        #    style={
#        #        "display": "flex",
#        #        "align-items": "center",
#        #        "justify-content": "center", # Centers the whole group
#        #        "gap": "8px",                # Controlled pixel-perfect horizontal gap
#        #        "padding": "2px 0",          # Tight vertical spacing between rows
#        #        "line-height": "1",          # Collapses vertical text height
#        #    }
#        #)
#        return html.Div(
#            [
#                dcc.Checklist(
#                    options=[{"label": "", "value": "done"}],
#                    id={"index": button_clicked, "type": "done"},
#                    style={"display": "inline-block", "vertical-align": "middle"},
#                    inputStyle={"margin": "0"}
#                ),
#                html.Div(
#                    value,
#                    id={"index": button_clicked, "type": "output-str"},
#                    style={"display": "inline-block", "vertical-align": "middle", "margin-left": "8px"},
#                ),
#            ],
#            style={
#                "display": "flex",
#                "align-items": "center",
#                "padding": "2px 0" # Vertical tightness
#            }
#        )


@callback(
    Output({"index": MATCH, "type": "done"}, "value"),
    Input({"index": MATCH, "type": "output-str"}, "n_clicks"),
    State({"index": MATCH, "type": "done"}, "value"),
    prevent_initial_call=True,
)
def equiv_output_str_and_checkbox_clicks(
        n_clicks,
        current_value,
):
    if n_clicks:
        if current_value is None or current_value == []:
            return ["done"]
        else:
            return []
    else:
        raise PreventUpdate


@callback(
    Output({"index": MATCH, "type": "output-str"}, "style"),
    Input({"index": MATCH, "type": "done"}, "value"),
    prevent_initial_call=True,
)
def checkbox_toggle(
        value,
):
    """
    The only `value` I have seen are
    - `[]`
    - `["done"]`
    """
    print(f'(checkbox_check_and_decheck) {value = }')
    #if isinstance(value, list):
    style = Patch()
    if len(value) == 0:
        # Note that we cannot write style.pop() because style is not a dict
        style["textDecoration"] = None
        style["color"] = None
    elif value[0] == "done":
        #style = {
        #    "display": "inline",
        #    #"margin": "10px",
        #    "textDecoration": "line-through",
        #    "color": "#888",
        #}
        style["textDecoration"] = "line-through"
        style["color"] = "gray"
    return style


# Callback to delete items marked as done
@callback(
    Output("list-container-div", "children", allow_duplicate=True),
    Input("clear-done-btn", "n_clicks"),
    State({"index": ALL, "type": "done"}, "value"),
    prevent_initial_call=True,
)
def delete_items(n_clicks, state):
    patched_list = Patch()
    values_to_remove = []
    for i, val in enumerate(state):
        if val:
            values_to_remove.insert(0, i)
    for v in values_to_remove:
        del patched_list[v]
    return patched_list


# Callback to update totals
@callback(
    Output("totals-div", "children"),
    Input({"index": ALL, "type": "done"}, "value"),
)
def show_totals(done):
    count_all = len(done)
    count_done = len([d for d in done if d])
    result = f"{count_done} of {count_all} items completed"
    if count_all:
        result += f" - {int(100 * count_done / count_all)}%"
    return result


if __name__ == "__main__":
    app.run(
        debug=True,
        # Change port if the default 8050 is in use by another app
        port=8055,
    )
