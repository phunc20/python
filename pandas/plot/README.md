## Histograms
```python
ax = df.plot.hist(bins=range(2,20),
                  alpha=0.5,
		  grid=True,
)
ax.set_xlabel("Time (sec)")
ax.set_ylabel("Temporature (Celsius)")
fig = ax.get_figure()
fig.savefig("temp_vs_time.png")
```
