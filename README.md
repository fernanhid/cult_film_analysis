# predicting_cult_films

 My project aims to built build a regression model to predict which movies will become cult hits. For this project, the definition of a cult movie is: <b> a movie that is loved by critics but has very low attendance </b>. My method was to identify a critic that regularly rates cult movies highly and predict his Metacritic rating.
 
Here are my steps:

1. Scrape/Clean data from widely-released films
2. Find the movies that fit into the cult categories and those that do not
3. Find the critic that rates cult movies high and anti-cult low
4. Scrape/Clean his reviews from Metacritic
5. Explore/ Build Regression Model

The best model I found was the Regression Model with Lasso Regularization which improved ~8% over the baseline. The most predictive features were:<br>

a. When it was released in January<br>
b. When it was released in October<br>
c. When the genre was Drama<br>
d. When the genre was Mystery<br>
e. When the Genre was Biography<br>

I look forward for any feedback and if there is any other creative methods to approach this problem!