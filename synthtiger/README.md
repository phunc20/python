## Troubleshoot
- `AttributeError: 'FreeTypeFont' object has no attribute 'getsize'` with `synthtiger==1.2.1`
   when generating synthetic images
    - This is because `pip` installed `Pillow==10.0.1` as dependency of `synthtiger==1.2.1`
      and Pillow 10 changed code (from `getsize(string)` to `getlength(string)`)
    - One can either downgrade to, say, `Pillow==9.5.0` or update all mentions of `getsize` in one's code
    - Cf. <https://github.com/tensorflow/models/issues/11040>
