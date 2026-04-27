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

**Fit Assessment (required): Ensemble learning**

> I expect this technique to be a **partial** fit for my project because: it may be useful to add some stability. However, with only three features at this point, it may not be diverse enough for this strategy. 
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

* **Representation or Proxy Chosen: Maintain at Hand-engineered features, setting threshhold at 20.**

* **Why this representation was reasonable for this week: Same as previous, but now added the new column of preious HRs. **


---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Added ensemble models and reran all models with improved dataset. 
* What you intentionally did *not* attempt and why: Did not add any additionial features yet past rerunning everything on the new previous HR data. 
* Any constraints encountered (data, labels, compute, time): Number of features/data. One note with this project is that while you can go farther back and get more rows of data, but in sports things do slowly change over time including average stats. 


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

Overall, rerunning all the types of models on the improved dataset of course improved pretty much every outcome. However, none improved past the wall we're hitting around the mid .60s on F1, except now Logistic Regression has hit .70, which is our best so far. 


---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

Random forest underperformed comparatively because in this set, there's only a few features. The others were similar to what was results have already happened, but the decision tree results showed more overfitting. 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
* What would you try next if data or resources were not constrained?
    - More data/features. 

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable)

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: Ensembles need a little more diversity than is present in my set.
* Evidence supporting that conclusion: Random forest did badly.
* What value this attempt still provided: Showing something that doesn't work better at least can help guide in the opposite direction. It also showed that adding in a validation set didn't necessarily improve results on my set (at least at this point).



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

