When we deal with images in python, we often use <code>numpy</code>, <code>cv2</code>, <code>matplotlib</code>, etc.

In <code>cv2</code>, there is a function called <code><b>cv2.resize()</b></code>. What I want to explain here is the word <b><code>size</code></b> and its difference to <code><b>shape</b></code>.

- <code><b>shape</b></code> means <code><b>(n_rows, n_cols, n_channels)</b></code>
- <code><b>size</b></code> means <code><b>(width, height)</b></code>, or equiv. <code><b>(n_cols, n_rows)</b></code>

**N.B.** However, this only holds true in Python, and is <b>not</b> a unified term in all programming languages.
For example, in <b>Julia</b>, <code><b>size()</b></code> returns <code><b>(n_rows, n_cols) = (height, width)</b></code> instead.







