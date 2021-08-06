## How to Get Rid of Ligature?
- Either execute in a cell the following
  ```python
  from IPython.core.display import HTML
  HTML("""
      <style>
      body { font-feature-settings: "liga" 0; }
      </style>
  """)
  ```
- Or add the following to the file `~/.jupyter/custom/custom.css`
  ```css
  .CodeMirror pre {
      font-feature-settings: "liga" 0;
  }
  ```
