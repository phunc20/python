- `uv add` can also add wheels
    - e.g. [玉山證券 SDK](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/download/download-sdk/): Just download the wheel file and `uv add path/to/the/downloaded/filename.whl`
    - cf. <https://docs.astral.sh/uv/concepts/projects/dependencies/#path>
- [dev Python packages](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies)
    - e.g.
      ```bash
      uv add --dev pytest
      ```
