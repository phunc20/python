## Q&A
1. How to print in `$ pytest`
    - Write prints in the code
    - Run `pytest` with option `-s`, i.e. `$ pytest -s`
1. Combinations with `pytest.mark.parametrize`
    - Just write them separately, e.g.
      ```python
      @pytest.mark.parametrize("input1", [x1, x2, x3])
      @pytest.mark.parametrize("input2", [y1, y2])
      def test_sth(input1, input2):
          test_body
      ```
