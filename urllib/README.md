## Examples
- Download files using `urllib`: Note that, to write the response into a file, one needs to **write the bytes**, i.e. `"wb"`, instead of `"w"`.
    - Some GitHub file
      ```python
      url = "https://github.com/taborlab/FlowCal/raw/master/examples/FCFiles/sample001.fcs"
      with urllib.request.urlopen(url) as response:
          saved_path = Path.cwd()/url.split("/")[-1]
          with open(saved_path, "wb") as f:
              f.write(response.read())
          print(f'Finish downloading {saved_path}')
      ```
    - MNIST test set
      ```python
      mnist_url = "http://yann.lecun.com/exdb/mnist/"
      test_set_gzip = "t10k-images-idx3-ubyte.gz"
      mnist_test_set_url = mnist_url + test_set_gzip
      with urllib.request.urlopen(mnist_test_set_url) as response:
          mnist_path = Path.cwd()/mnist_test_set_url.split("/")[-1]
          with open(mnist_path, "wb") as f:
              f.write(response.read())
          print(f'The gzip file is downloaded at {mnist_path.absolute()}')"
      ```
