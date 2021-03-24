### Requirements
- flask 
- requests

### Endpoints
- "/" Endpoint (GET Method) 
    - Returns and display my name with h1 format
- "/whoami" Endpoint (GET Method) 
    - Needs firstname and lastname parameters in url 
    - Returns entered parameters as json 
- "/alert" Endpoint (POST Method) 
    - Requires and only accept Json data
    - Posts received data to webhook.site dummy url 
    - To change the dummy url, change the url variable in the alert function 