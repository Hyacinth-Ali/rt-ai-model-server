# Problem 4: Model Serving

The objective of this problem is to build an API service that serves the trained predictive models. I have implemented an API service using Python and FastAPI [FastAPI](https://fastapi.tiangolo.com) to achieve this goal. The API service provides an /predict endpoint that accepts input values for vol_moving_avg, adj_close_rolling_med, and optional security (etfs or stock) and responds with the predicted trading volume. When no security is entered or selected from the User Interface, the predicted volume is based on the combined datasets from ETFs and Stock. 

To interact with the API service, you can make HTTP GET requests to the http://34.201.65.4/predict endpoint with the appropriate parameters. Here's an example:

```
curl -X 'GET' \
  'http://34.201.65.4/predict?vol_moving_avg=12345&adj_close_rolling_med=6' \
  -H 'accept: application/json'
```

Alternatively, you can provide a security as a path of the query parameters. Here is an example of GET request for just Stock security.
```
curl -X 'GET' \
  'http://34.201.65.4/predict?vol_moving_avg=10000&adj_close_rolling_med=5&security=stock' \
  -H 'accept: application/json'
 ```
 
The API server will process the request and return a float value representing the predicted trading volume based on the trained model.

## Deployment
The API service, along with the trained model, has been deployed using virtual linux machine (EC2) ON [AWS](https://aws.amazon.com). You can access the deployed API service through thIS [link](http://34.201.65.4/docs)


## Additional Documentation
For further information, including detailed documentation and source code, please refer to the this repository. The directory contains the necessary code, documentation, and any additional resources related to the model serving problem.

Feel free to explore the provided code and documentation to gain a deeper understanding of the model serving solution.

If you have any questions or need further assistance, please don't hesitate to reach out.
