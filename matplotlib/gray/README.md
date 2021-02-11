### There are more than one way to specify `gray`
By default, `matplotlib` does not `plt.imshow()` images with a single channel in black and white. Instead, it displays them
in some sort of blue and yellow. To display in black and white, there exists multiple ways:
- `plt.imshow(array2d, cmap=plt.cm.gray)`
- `plt.imshow(array2d, cmap="gray")`

**Rmk.** `plt.cm` provides many other options (which you can inspect via `dir(plt.cm)`), e.g.
- `plt.cm.bone` for displaying medical images with bones
- `plt.cm.coolwarm` for displaying thermal images
  - `plt.cm.coolwarm_r`, there are many options named `sth_r`, which means **the same as** `sth` **but with the colors reversed**.

