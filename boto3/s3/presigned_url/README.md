

## Ref.
https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/s3/s3_basics/presigned_url.py
https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples
https://github.com/awsdocs/aws-doc-sdk-examples
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html?highlight=presigned
https://docs.aws.amazon.com/code-library/latest/ug/python_3_s3_code_examples.html
https://docs.aws.amazon.com/code-library/latest/ug/python_3_code_examples_cross_service.html
https://docs.aws.amazon.com/code-library/latest/ug/s3_code_examples.html


```bash
$ openssl rand -out fake.pdf -base64 $((2**24 * 3/4))
$ du -hsx fake.pdf
17M     fake.pdf
$ python presigned_url.py ge10mb fake.pdf put
```
