## How to Remove A File?
In `pathlib`, for the `Path` object's methods, there is no such thing called `remove()`.
At most, there is `rmdir()`. Then how does one delete files using `pathlib`? Or is
`pathlib` incapable of that?

The answer is
> Via the method `unlink()`.

`pathlib` chooses the naming for the method which deletes a file or unlinks a link.


