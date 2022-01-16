# Review-Sorting
Sorting Amazon reviews by using the wilson lower bound score method 

What is Wilson Lower Bound Score? 
Wilson lower bound method provides an accurate way to sort a product based on positive and negative ratings. It can estimate, with 95% confidence, a product’s popularity across the whole community based on its historical positive and negative votes.

Business Problem: Calculate product ratings and product reviews more accurately on Amazon. The dataset named Amazon product data includes a product with the most reviews in the electronics category. The product has user ratings and reviews.

Variables:
amazon_review.csv
1. reviewerID — ID of the reviewer, e.g. A2SUAM1J3GNN3B
2. asin — ID of the product, e.g. 0000013714
3. reviewerName — Name of the reviewer
4. helpful — Helpfulness rating of the review, e.g. 2/3
5. reviewText — Text of the review
6. overall — Rating of the product
7. summary — Summary of the review
8. unixReviewTime — Time of the review (unix time)
9. reviewTime — Time of the review (raw)
10. day_diff — Number of days since the evaluation
11. helpful_yes — Number of times the review was found helpful
12. total_vote — Number of votes given to the review
