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

* **Technique / Model Family Covered This Week: Linear regression **
* **Key Assumptions of This Technique: 
- Linear regression requires an actual relationship between the datapoints/features.** (1–2 bullets)

**Fit Assessment (required): **

> I expect this technique to be a **good** fit for my project because: I have been planning on using the logic of linear regression. The only way we can predict something like home runs is by looking at related factors, which is perfect for linear regression. 

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

* **Representation or Proxy Chosen: (preprocessed) Tabular data**

* **Why this representation was reasonable for this week: Linear regression needs numeric points, which seems perfect for a table of data.**

---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Linear regression baseline, training on those preprocesssed features, and also tracked what it popped out. Mainly tried to keep it as simple as possible.
* What you intentionally did *not* attempt and why: Nothing outside of that, like optimization. At this stage, just trying to get the baseline set. 
* Any constraints encountered (data, labels, compute, time): Limited data, but that has and will continue to be a factor. 
---

## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

The loss is a little high, and also based on the stats it popped out, I think there's some overfitting. I need to determine how to prevent that especiallyw ith the small dataset. 
---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

The implementation of linear regression worked mostly as expected, but the loss was high. I think the nature of the data may lead so some noise, and the model right now is trying it still, and that's why it's overfitting. I also think it may be due to there being multiple data points, none of which directly correlate, but rather all together can give the picture of potential home runs. 


---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
    - I want to tweak the notebook so the loss and overfitting is minimized. I think I'll go through the data split sets to make sure it makes sense, to see if there are any issues. 
* What would you try next if data or resources were not constrained?

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable)

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: It isn't quite there, but close I think. After trying to implement, I realize the data isn't exactly linear.
* Evidence supporting that conclusion: loss is high
* What value this attempt still provided: shows I might need to get some more or different features/data points.




---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

