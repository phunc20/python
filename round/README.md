## The Concept of "Round to Even"
When dealing with decimals, we might have all been taught
at elementary school that
- When the number in question is midway btw two numbers whose precision we accept $\implies$ **round up**
- otherwise **round down**

But there exists another (equally famous) proposal to deal with tie:
> One round up 50% of the time and round down also 50% of the time

More precisely, facing tie
- we **round up** when the digit we want to round to is **odd** before rounding
- we **round down** when the digit we want to round to is **even** before rounding

Rounding to even seems to be **fairer** in that
when doing finite-precision arithmetic, errors accumulate
step by step. If we keep rounding up at ties, the errors add up;
if we round up and down both 50% of the time, the errors get hope
to cancel out.

Python seems to implement this rounding to even scheme.  
**Caveat.** Be careful with non machine-representable decimals --
they are not really midway between two numbers.

```python
In [27]: round(4.75, ndigits=1)
Out[27]: 4.8

In [28]: round(4.25, ndigits=1)
Out[28]: 4.2

In [29]: round(4.55, ndigits=1)
Out[29]: 4.5
```
