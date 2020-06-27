class Book():
    def __init__(self,id,isbn,isbn13,ratingsCount = 0,reviewsCount = 0,textReviewsCount = 0,workRatingsCount = 0,workReviewsCount = 0,workTextReviewsCount = 0,averageRating = 0):
        self.id = id
        self.isbn = isbn
        self.ratingsCount = ratingsCount
        self.reviewsCount = reviewsCount
        self.textReviewsCount = textReviewsCount
        self.workRatingsCount = workRatingsCount
        self.workReviewsCount = workReviewsCount
        self.workTextReviewsCount = workTextReviewsCount
        self.averageRating = averageRating

