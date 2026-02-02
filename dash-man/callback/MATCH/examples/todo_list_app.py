from dash import (
    ALL,
    MATCH,
    Dash,
    Input,
    Output,
    Patch,
    State,
    callback,
    #no_update,
    #callback_context,
    dcc,
    html,
)

#from dash.exceptions import PreventUpdate

# TODO:
# 1. [x] Checklist label instead of output-str
# 2. CSS (style)
#    - [ ] Make the alignment prettier
#    - [ ] The item/checkbox label not aligned with checkbox when str is too long. Bad
# 3. [x] Add a toggle-all-btn
# 4. refactorization
#    - [ ] naming of functions, variables
#    - [x] import order
# 5. [ ] When the list is so long that a scrollbar appears, auto-focus to last item

app = Dash()

app.layout = html.Div(
    [
        html.H1(
            "Dash To-Do list",
            style={
                "text-align": "center",
            },
        ),
        html.Div(
            id="control-div",
            children=[
                dcc.Input(id="new-item-input", n_submit=0),
                html.Button("Add", id="add-btn"),
                html.Button(
                     "Clear Done",
                     id="clear-done-btn",
                ),
                html.Button(
                     "Toggle All",
                     id="toggle-all-btn",
                ),
            ],
            style={
                "display": "flex",
                "justify-content": "center",
                "gap": "5px",
                "margin-bottom": "10px"
            },
        ),
        html.Div(
            id="list-container-div",
            style={
                "margin": "0 auto",      # Centers the box horizontally
                "width": "300px",        # FIXED WIDTH prevents shifting when items change
                "display": "flex",
                "max-height": "250px",
                "overflow-y": "auto",
                "flex-direction": "column",
                "align-items": "flex-start", # Keeps checkboxes flush left inside the 300px box
                #"gap": "5px"             # Tight vertical spacing
            },
         ),
        html.Div(
            id="totals-div",
            style={
                "text-align": "center",
                "margin-top": "20px",
                #"display": "inline-block",
                #"display": "block",
                #"display": "inline",
                #"text-align": "left",
            },
        ),
    ],
    style={"width": "100%"},
)


@callback(
    Output("list-container-div", "children", allow_duplicate=True),
    Output("new-item-input", "value"),
    Input("add-btn", "n_clicks"),
    State("new-item-input", "value"),
    prevent_initial_call=True,
)
def add_item(n_clicks: int, item: str):
    """
    Output("new-item-input", "value")
    The reason we put this output in the callback is because
    we want to clean up the input text once the user confirms
    one todo item, i.e. we return an empty string `""`.
    """
    def new_checklist_item():
        return html.Div(
            children=dcc.Checklist(
                options=[{"label": item if item else "", "value": "done"}],
                id={"index": n_clicks, "type": "done"},
                style={"display": "inline-block", "vertical-align": "middle"},
                inputStyle={"margin-right": "10px"},
                #labelStyle={},
            ),
            style={
                #"display": "flex",
                "display": "inline",
                "align-items": "center",
                "padding": "2px 0" # Vertical tightness
            }
        )

    # Cf. <https://dash.plotly.com/partial-properties#allowing-duplicate-callback-outputs>
    # in case one wonders how Patch() works with multiple-output callbacks.
    patched_list = Patch()
    patched_list.append(new_checklist_item())
    return patched_list, ""


@callback(
    Output({"index": MATCH, "type": "done"}, "style"),
    Input({"index": MATCH, "type": "done"}, "value"),
    prevent_initial_call=True,
)
def toggle_checkbox_style_change(value):
    """
    The only `value` I have seen are
    - `[]`
    - `["done"]`
    """
    #if isinstance(value, list):
    style = Patch()
    if len(value) == 0:
        # Note that we cannot write style.pop() because style is not a dict
        style["text-decoration"] = None
        style["color"] = None
    elif value[0] == "done":
        style["text-decoration"] = "line-through"
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


# The following callbacks are COMPLEMENTARY and
# may be disabled without affecting the basic functionality

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
    Output({"index": ALL, "type": "done"}, "value"),
    Input("toggle-all-btn", "n_clicks"),
    State({"index": ALL, "type": "done"}, "value"),
    prevent_initial_call=True,
)
def toggle_all_items(n_clicks, current_values):
    #print(f'{current_values = }')
    # Using any/all provides diff behaviors
    if all(current_values):
        #return [None] * len(current_values) # Wrong, but hard to explain
        return [[]] * len(current_values)
    else:
        return [["done"]] * len(current_values)


if __name__ == "__main__":
    app.run(
        debug=True,
        # Change port if the default 8050 is in use by another app
        port=8055,
    )
