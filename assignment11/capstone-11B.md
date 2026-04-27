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

* **Technique / Model Family Covered This Week: **
* **Key Assumptions of This Technique: 
- Groups exist within the data that are visible on graphed.** (1–2 bullets)

**Fit Assessment (required): Neural Networks**

> I expect this technique to be a **partial** fit for my project because: neural networks would be better on a larger model. My set is pretty small comparatively. 
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

* **Representation or Proxy Chosen: Maintain at Hand-engineered features applied to MLP.**

* **Why this representation was reasonable for this week: I want to reasonably compare each weeks model. **


---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Trained for MLP, and adjusted the threshhold. 
* What you intentionally did *not* attempt and why: Did not try to adjusting my data so it would apply better, as I wanted it to be a fair compatison.
* Any constraints encountered (data, labels, compute, time):  The small dataset limited the results of MLP in this case.


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

Previous to this, our best score for F1 has been 0.75. On MLP, we got 0.74 which is very comparable. The accuracy between both was also very similar but it was interesting that going to MLP made precision go down but recall go up, so more false positives but catching a higher percent of the true positives too. 


---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

At first it kept predicting basically no one is a power hitter, which means an easy mostly accurate model, but obviously very flawed. Adding in some weight for the minority side of the binary classification by upping the threshold helped. Overall, I think it would be useful to implement a more-than-binary classification, so it isn't so black and white. 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
    - Add in another sector of hitters (probably 40+)
* What would you try next if data or resources were not constrained?

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable) - 

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: not exactly a poor fit, but not really any better, just neutral.
* Evidence supporting that conclusion: Scores did not improve, and the dataset is small. However this is only unless I am ok with swapping from false negatives to false positives, but I believe it would be better to ensure the list of power hitters is accurate, even if it misses a few. 
* What value this attempt still provided: Learned how to analyse the set depending on the goal and what I'm willing to sacrifice. 



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

