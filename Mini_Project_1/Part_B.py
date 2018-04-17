import matplotlib.pyplot as plt
import movie_data_helper
import numpy as np
import scipy
import scipy.misc
from sys import exit

def infer_true_movie_ratings(num_observations=-1):
    """
    For every movie, computes the posterior distribution and MAP estimate of
    the movie's true/inherent rating given the movie's observed ratings.

    Input
    -----
    - num_observations: integer that specifies how many available ratings to
        use per movie (the default value of -1 indicates that all available
        ratings will be used).

    Output
    ------
    - posteriors: a 2D array consisting of the posterior distributions where
        the number of rows is the number of movies, and the number of columns
        is M, i.e., the number of possible ratings (remember ratings are
        0, 1, ..., M-1); posteriors[i] gives a length M vector that is the
        posterior distribution of the true/inherent rating of the i-th movie
        given ratings for the i-th movie (where for each movie, the number of
        observations used is precisely what is specified by the input variable
        `num_observations`)
    - MAP_ratings: a 1D array with length given by the number of movies;
        MAP_ratings[i] gives the true/inherent rating with the highest
        posterior probability in the distribution `posteriors[i]`
    """

    M = 11  # all of our ratings are between 0 and 10
    prior = np.array([1.0 / M] * M)  # uniform distribution
    likelihood = compute_movie_rating_likelihood(M)

    # get the list of all movie IDs to process
    movie_id_list = movie_data_helper.get_movie_id_list()
    num_movies = len(movie_id_list)

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE FOR PART (d)
    #
    # Your code should iterate through the movies. For each movie, your code
    # should:
    #   1. Get all the observed ratings for the movie. You can artificially
    #      limit the number of available ratings used by truncating the ratings
    #      vector according to num_observations.
    #   2. Use the ratings you retrieved and the function compute_posterior to
    #      obtain the posterior of the true/inherent rating of the movie
    #      given the observed ratings
    #   3. Find the rating for each movie that maximizes the posterior

    # These are the output variables - it's your job to fill them.
    posteriors = np.zeros((num_movies, M))
    MAP_ratings = np.zeros(num_movies)
    
    for i in range(num_movies):
        movie_id = movie_id_list[i]
        y = movie_data_helper.get_ratings(movie_id)[:num_observations]
        posteriors[i] = compute_posterior(prior,likelihood,y)
        MAP_ratings[i] = np.argmax(posteriors[i])
    #
    # END OF YOUR CODE FOR PART (d)
    # -------------------------------------------------------------------------

    return posteriors, MAP_ratings
    
print(infer_true_movie_ratings)