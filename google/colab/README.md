




- Stop and delete runtime
  ```python
  from google.colab import runtime
  runtime.unassign()
  ```
- Load Google Drive
  ```python
  from google.colab import drive
  drive.mount("/content/drive")
  ```
