# MedCabinet # 
This project is our contribution to a "build week" at Lambda School. We are part of team of student data scientists and software engineers at Lambda School who have collaborated to create an online application. This application permits users to input their desired qualities in marijuana products, and the application returns a set of recommended strains of marijuana. In our roles as data and machine learning engineers, we have constructed an online API which returns a set of recommened strains of marijuana, given user preferences.

The online Med-Cabinet app can be accessed [here](https://med-cabinet8.netlify.app/).
- - - -

## Installation ## 
git clone https://github.com/buildweek-medcabinet-8/data.git

- - - -

## Setup ## 
pipenv install

- - - -

## Process ## 
The API performs the following four functions in order.
1. The API receives a string from an external server. The string contains a list of words and sentences describing the effects, flavors, and general description of what type of marijuana a customer is looking for.
2. The string is received in the format of form-data sent with a key named Flavors/Effects, to the endpoint https://medcabinet-ds.herokuapp.com/recommend
3. The string is passed into a natural language processing algorithm (NLP). This algorithm was previously fitted onto a dataset of several thousand strains; it includes each strain's type, rating, flavor, effects, and general description.
4. The NLP algorithm returns the top five strains most compatible with the inputted string. Finally, the API returns this information as a JSON file.

## Usage ##
1. The API can be accessed by sending a Post request https://medcabinet-ds.herokuapp.com/recommend. 
2. The request should use the key "Flavors/Effects" with a string of words and /or sentences describing what kind of marijuana strain the user is looking for. 
3. The API will return a JSON file with the top five strains that match the description. Each strain in the JSON file will be represented by a dictionary with the following keys; Description, Effects, Flavor Rating, Strain, and Type.

## Example ##
Alternatively, the API can be accessed using a software called [Postman](https://www.postman.com/), which is a "collaboration platform for API development."
1. Download Postman onto your local computer and open it
2. Select "Post"
3. Enter URL https://medcabinet-ds.herokuapp.com/recommend
4. Select  "Body" label
5. Select "form-data"
6. Add Key titled "Flavors/Effects"
7. Enter a string in the Value field in the form of a series of words and sentecnes, for example: "happy sweet anxiety I want something to help me sleep."
8. Click Send
9. The software will send a Post request with the entered Flavors/Effects to the API, which returns a JSON with top five matching strains.
The following screenshot of [Postman](https://www.postman.com/) highlights the main elements of the software which you will need to use.
![Postman Screenshot](/postman_example.png)
10. Enjoy!

- - - -

## Authors ## 
**Ruby Laguna** - Machine Learning Engineer   
**Makoa Noble** - Data Engineer  
**Ilya Novak** - Data Engineer
