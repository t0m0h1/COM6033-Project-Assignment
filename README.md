# COM6033-Project-Assignment

*Links to other labs:*

- https://github.com/t0m0h1/Week-1-Artificial-Intelligence.git
- https://github.com/t0m0h1/Week-2-AI-Tasks.git
- https://github.com/t0m0h1/Week-3-AI-Tasks.git
- https://github.com/t0m0h1/Week-4-AI-Tasks.git
- https://github.com/t0m0h1/AI-Week-5.git
- https://github.com/t0m0h1/Week-6-AI.git


# Sentiment Analysis Flask App

The system will predict whether the sentiment of the text is positive, negative, or neutral.

### Installation

git clone https://github.com/t0m0h1/COM6033-Project-Assignment.git

(bash)
   
cd sentiment-analysis-flask

python3 -m venv venv

source venv/bin/activate

command prompt commands may be different - see flask docs.


### Running the App:

Run main.py within the virtual environment

run index.html on the live server extension.

Type in or paste a tweet



### Model

I decided to use Logistic Regression as it is a simple model to implement and understand and is computationally efficient and works well with smaller datasets, which may be the case for this problem.

In future work, it may be beneficial to experiment with some alternatives, particularly if the dataset grows or the task becomes more complex, such as:

- Deep Learning Models (LSTM, CNN)
- Support Vector Machines
- Naive Bayes
- Random Forest




### Evaluation

The model's performance is evaluated using a testing dataset that was not seen during training. Evaluation metrics we will be using:

Precision, which is the amount of correct positive predictions out of all positive predictions made.  
Recall, the amount of correct positive predictions out of all actual positives.  
F1 score, The mean of precision and recall, balancing the two metrics.
