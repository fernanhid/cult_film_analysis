# cult_film_analysis

 My project aims to built build a regression model to predict which movies will become cult hits. For this project, the definition of a movie that is: <b> one that is loved by critics but has very low attendance </b>. My method was to identify a critic that regularly rates cult movies highly and predict his Metacritic rating.
 
Here are my steps:

1. Scrape/Clean data from widely-released films
2. Find the movies that fit into the cult categories and those that do not
3. Find the critic that rates cult movies high and anti-cult low
4. Scrape/Clean his reviews from Metacritic
5. Explore/ Build Regression Model

The best model I found was the Regression Model with Lasso Regularization which improved ~8% over the baseline. The most predictive features were:

1. When it was released in January
2. When it was released in October
3. When the genre was Drama
4. When the genre was Mystery
5. When the Genre was Biography

I look forward for any feedback and if there is any other creative methods to approach this problem!