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

* **Technique / Model Family Covered This Week:  **
* **Key Assumptions of This Technique: 
- .** (1–2 bullets)

**Fit Assessment (required): Model Family Comparison**

> I expect this technique to be a **good** fit for my project because: it will allow me to test other model families and potentially find one that is better than what we have tried so far. The two models used in the toy problem theoretically could work on this project, and it will be interesting to see how it works.

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

* **Representation or Proxy Chosen: Same as last week, Hand-engineered features, with target at 20 HR **

* **Why this representation was reasonable for this week: The same, as we are trying to compare these results.
20 is a threshold far less than half should reach, but it is a good mark. Picking these points ensured there was multiple points including AB/time played, which is a huge factor in determining HRs. **


---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: I added two model families, Naive Bayes (Gaussian) and kNN, similar to the tou proble . 
* What you intentionally did *not* attempt and why: I skipped trying to adjust anything (besides the model) compared to last week, so it could be a more accurate comparison. 
* Any constraints encountered (data, labels, compute, time): Attempted a few versions of kNN, but it was fairly easy to try new values so it was not exactly a constraint.


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

The models performed differently in some ways, but overall similarly.
Both had similar accuracy to the binary classification, 0.88 and 0.89, but the f1 was still lowish on both (0.65 and 0.62). 
The Gaussian specifically caught more "power hitters", but also had low precision/false positives. 

---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

I think after seeing all three of these models, its clear that more data would help. The f1 is always low. kNN makes sense why it was a little worse than Gaussian, as the dataset isn're really conducive to neighbor data points. However Gaussian assumes the labels are all independent, where they might not necessarily be. I think neither are really more interesting for this over simple binary classiciation. 


---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
    - Now that the comparison of models is over, I would like to either switch back to linear regression or just adjust the data and try to maximize the usefulness of the binary classification style model. I haven't 100% decided yet.
* What would you try next if data or resources were not constrained?

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable)

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: Neither model was particularly great or standout.
* Evidence supporting that conclusion: The data is very similar to the previous binary classification.
* What value this attempt still provided: Learned to keep things simple, and just try to adjust what I already have. 



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

