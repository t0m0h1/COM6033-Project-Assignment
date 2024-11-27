# COM6033-Project-Assignment

# Sentiment Analysis Flask App

the system will predict whether the sentiment of the text is positive, negative, or neutral.

## Installation

git clone https://github.com/t0m0h1/COM6033-Project-Assignment.git

(bash)
   
cd sentiment-analysis-flask

python3 -m venv venv

source venv/bin/activate

command prompt commands may be different - see flask docs.



Model

I decided to use Logistic Regression as it is a simple model to implement and understand and is computationally efficient and works well with smaller datasets, which may be the case for this problem.

In future work, it may be beneficial to experiment with some alternatives, particularly if the dataset grows or the task becomes more complex, such as:

- Deep Learning Models (LSTM, CNN)
- Support Vector Machines
- Naive Bayes
- Random Forest




Evaluation

The model's performance is evaluated using a testing dataset that was not seen during training. Common evaluation metrics for sentiment analysis include:

Accuracy: The percentage of correctly predicted sentiments.
Precision: The ability of the model to avoid false positives.
