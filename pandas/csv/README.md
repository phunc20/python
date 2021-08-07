## Read and Write `.csv` Files
- write using `to_csv()` method
- read using `read_csv()` method
  - By default, the first line of the CSV file will become the column names of the DataFrame. One way to change this is to provide the parameter `name=` a list of strings (column names).
  - **Caveat.** If you want the first column of your `.csv` file be the index of the DataFrame, then you should specify **`index_col=0`** to `read_csv()`.
    ```python
    In [2]: df = pd.DataFrame([[16, "F"], [35, "M"], [75, "M"]], index=["Alice", "Bob", "Charlie"], columns=["age", "gender"])
    
    In [3]: df
    Out[3]:
             age gender
    Alice     16      F
    Bob       35      M
    Charlie   75      M
    
    In [4]: df.to_csv("age_gender.csv")
    
    In [5]: !cat age_gender.csv
    ,age,gender
    Alice,16,F
    Bob,35,M
    Charlie,75,M
    
    In [6]: df_wrong = pd.read_csv("age_gender.csv"); df_wrong
    Out[6]:
      Unnamed: 0  age gender
    0      Alice   16      F
    1        Bob   35      M
    2    Charlie   75      M
    
    In [7]: df_right = pd.read_csv("age_gender.csv", index_col=0); df_right
    Out[7]:
             age gender
    Alice     16      F
    Bob       35      M
    Charlie   75      M
    ```
