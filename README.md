# MedCabinet # 
This project is our contribution to a "build week" at Lambda School. We are part of team of student data scientists and software engineers at Lambda School who have collaborated to create an online application. This application permits users to input their desired qualities in marijuana products, and the application returns a set of recommended strains of marijuana. In our roles as data and machine learning engineers, we have constructed an online API which returns a set of recommened strains of marijuana, given user preferences

- - - -

## Installation ## 
git clone https://github.com/buildweek-medcabinet-8/data.git

- - - -

## Setup ## 
pipenv install

- - - -

## Usage ## 
The API performs the following three functions in order. The url to handle 
1. The API receives a string from an external server. The string contains a list of words and sentences describing the effects, flavors, and general description of what type of marijuana a customer is looking for.
2. The string is received in the format of form-data sent with a key named Flavors/Effects, to the endpoint https://medcabinet-ds.herokuapp.com/recommend
3. The string is passed into a natural language processing algorithm (NLP). This algorithm was previously fitted onto a dataset of several thousand strains; it includes each strain's type, rating, flavor, effects, and general description.
4. The NLP algorithm returns the top five strains most compatible with the inputted string. Finally, the API returns this information as a JSON file.

- - - -

## Authors ## 
**Ruby Laguna** - Machine Learning Engineer   
**Makoa Noble** - Data Engineer  
**Ilya Novak** - Data Engineer