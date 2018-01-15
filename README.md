# EmailSimilarity
Computation of email similarity  with various algorithms, including the Levenshtein algorithms, based on randomly generated names.

## Requierments
Python 3.6:
  - numpy
  - python-levenshtein (https://pypi.python.org/pypi/python-Levenshtein/0.12.0)
  - Matplotlib, sklearn, pandas for the plotting (plot.py)
 
 ## Usage:
 The randoms names are in the names.txt file.
 distance_function.py: Contains the different functions used for the computation.
 name2email.py : Generate the email addresses from the names
 generate_couple.py : Generate the test dataset with similar and nonsimilar sets
 analyse-paper.py: Plot the ROC curve and the distributions.
