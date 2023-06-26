## Upload Some Local Dataset onto Kaggle's Datasets
- If you want to upload a single file, say, `harry_potter.txt`, then just select it and upload and it's done
- If you want to upload an entire directory
    - Zip the directory
    - But please don't zip it with itself as the parent directory during uncompression
        - How? Say, if the directory is named `vina-cased_chunked_dataset/`, then `cd` into it and then
          ```sh
          $ zip -r vccd.zip .
          ```
        - Then upload `vccd.zip`
