Assignment 5 – Part A: Classification and Metrics
Overview
In this assignment, you will train an end-to-end classification model on a shared toy dataset and evaluate it using multiple metrics.

The goal is to build the workflow correctly and to learn when different metrics tell different stories. You will compare metrics, interpret confusion matrices, and reason about thresholds and class imbalance.

Learning Objectives
By completing this assignment, you will be able to:

Build a safe train/validation/test workflow for a classification task
Train a baseline classifier using a pipeline-based preprocessing workflow
Compute and interpret classification metrics from model outputs
Compare metrics under class imbalance and explain tradeoffs
Select a decision threshold and justify it in context
Dataset
You will use an instructor-provided shared toy dataset appropriate for binary (or multiclass) classification.

The dataset may include: - Numeric and categorical features - Missing values - A discrete target label

Assume the dataset is suitable for supervised learning. If the dataset is imbalanced, treat that as part of the intended learning.

Required Tasks
1. Train / Validation / Test Split
Split the dataset into: - Training set - Validation set - Test set

You must: - State the split proportions - Justify the splitting strategy (random, stratified, temporal, etc.) - Keep the test set fully isolated until the end

2. Pipeline-Based Data Preparation
Use scikit-learn pipelines to perform data preparation.

Requirements: - Use Pipeline - Use ColumnTransformer if you have mixed numeric and categorical features - Include steps for: - imputation - scaling of numeric features - encoding of categorical features - Ensure the pipeline is fit only on training data (by fitting the full pipeline on the training split)

3. Baseline Classification Model
Train at least one baseline classifier.

Requirements: - Use an appropriate classifier for the dataset (e.g., logistic regression, linear model, or another baseline recommended by the instructor) - Train using the preprocessing + model pipeline - Report the validation performance for your primary metric

4. Confusion Matrix and Derived Metrics
Compute a confusion matrix on the validation set and use it to report metrics.

Required metrics: - Accuracy - Precision - Recall - F1-score

You must: - Interpret the confusion matrix in words - Explain at least one reason why accuracy can be misleading

5. ROC Curve (or PR Curve) and Thresholding
Using predicted probabilities or decision scores: - Plot an ROC curve and compute ROC AUC

If the dataset is meaningfully imbalanced, also include: - a Precision-Recall curve and PR AUC

Then: - Choose a decision threshold other than 0.5 (even if you keep 0.5 later) - Explain what changed (precision vs recall) and why that tradeoff might matter

6. Final Test Evaluation
After you have finalized your pipeline and threshold choices: - Evaluate once on the test set - Report the same metrics you used on the validation set

Include a short comparison: - Did test behavior match validation behavior? - If not, what might explain the mismatch?

Constraints
For Assignment 5 – Part A:

You must use pipeline-based preprocessing (including imputation, scaling, and encoding as needed)
You must report multiple metrics (not just accuracy)
You must keep the test set isolated until the end
Extensive hyperparameter tuning is not required (that is the focus of Assignment 6)
Focus on correct workflow, correct metric computation, and clear interpretation.

Deliverables
Submit:

A short writeup (PDF) addressing each required task
Code or a notebook showing:
your split strategy
your preprocessing + model pipeline
confusion matrix and metric computation
ROC (and PR if applicable) curve(s)
your threshold choice and justification
final test evaluation
Clarity of reasoning and correctness of evaluation matter more than maximizing performance.