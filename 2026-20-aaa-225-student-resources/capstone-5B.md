# Part B – Weekly Capstone Assignment Template

This template is used for **each of the 14 Part B capstone submissions** throughout the semester. The structure remains the same every week so that you can focus on *thinking and judgment*, not guessing expectations.

Your goal is not to achieve the best performance, but to **reason carefully about how this week’s machine learning technique applies (or does not apply) to your project**.

---

## 1. Project Context (Brief)

Provide the same short context each week so graders can orient quickly.

* **Project Title: MLB Home Runs**
* **Data Modality: Tabular ** (tabular, image, audio, text, other)
* **Task Type: Regression** (regression, classification, clustering, sequence modeling, etc.)
* **One-Sentence Goal: Predict how many home runs MLB players will hit next season.** What are you trying to predict, detect, or understand?

---

## 2. This Week’s Technique and Its Assumptions

* **Technique / Model Family Covered This Week: Binary Classification **
* **Key Assumptions of This Technique: 
- There is a possible/useful binary classification in this situation.** (1–2 bullets)

**Fit Assessment (required): **

> I expect this technique to be a **partial** fit for my project because: my goal for the project is a regression analysis to be more specific, but the idea of a binary classification is still potentially useful  and I would like to try it. 

(2–4 sentences)

---

## 3. Representation or Proxy Used

Describe how your data was represented so that this week’s technique could be applied.

Examples include:

* Hand-engineered features

* Summary statistics

* Frozen embeddings

* Dimensionality reduction

* A proxy task

* **Representation or Proxy Chosen: Hand-engineered features, with target at 20 HR **

* **Why this representation was reasonable for this week: 20 is a threshold far less than half should reach, but it is a good mark. Picking these points ensured there was multiple points including AB/time played, which is a huge factor in determining HRs. **

---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Changed the split to be old (<2022) vs new, rather than random, which makes much more sense. Also implemented the actual binary classification to predict whether based on the previous data, if X Y or Z player will hit at least 20 HR next season. 
* What you intentionally did *not* attempt and why: I did not (yet) attempt to add in more data/features, though I think it could help the model be a little more accurate. I also only did the one threshold, rather than something like a <20 (power hitter) vs <40 (all-star) hitter.
* Any constraints encountered (data, labels, compute, time): Main constraint is conceptual, reframing the problem from regression to a binary classification. It was interesting to look at from another angle though. 


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

Found some interesting data, the way I split, this was the ratio: 
Power hitters in train: 560 / 3869 = 14.47%
Power hitters in test:  357 / 2646 = 13.49%

The split is fairly consistent, though it is interesting that the recent power hitter ratio is lower. 

For the processing itself, I got:
- Precision (power hitter): 0.60
- Recall (power hitter): 0.68
- F1 (power hitter): 0.64
- Overall accuracy: 0.90

90% is pretty good on paper but actually, looking closer, the F1 shows less than 2/3 performance. 


---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

It is not truly all that accurate. One thing I ran into was figuring out how to properly use previous home runs as a feature, which may seem like a large omission here. The problem is I think the only way to make it trainable might be to adjust the way the data is actually set up, so the rows are offset by one only on the HR column. That way the training isn't getting obvious leakage (I originally did not even notice the obvious issue and got 100% accuracy, which was a silly error). 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
    - I will 100% want to adjust the dataset so the training can be better and actually use the closest related data point (previous HRs correlated to future HRs). 
* What would you try next if data or resources were not constrained?

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable)

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: My ultimate goal (at least for now) is to guess a number, not whether a player will meet a threshhold. Binary classification is a different question.
* Evidence supporting that conclusion: For example, someone could hit 19 and miss the mark, but maybe they are still a good power hitter. Actual number prediction is more useful than a threshhold in this case.
* What value this attempt still provided:  Took a look at accuracy metrics, and had to think mroe about the setup of the dataset. It also made me realize an obvious mistake in logic/double-checking, when I tried to run it and got 100%. 



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

