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

**Fit Assessment (required): SVMs**

> I expect this technique to be a **partial** fit for my project because: I am sticking with binary classification as the basis, and SVMs is potentially useful for this. However, it won't be very useful in this case because the data from the two sides of the binary are all jumbled rather than able to draw a line down the middle.  
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

* **Why this representation was reasonable for this week: Good for our binary classification model. 20 is a threshold far less than half should reach, but it is a good mark. Picking these points ensured there was multiple points including AB/time played, which is a huge factor in determining HRs.  **


---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Implemented SVMs into our binary classification model. Also, adjusted the way it view the dataset so the model can actually take into account the previous HRs. 
* What you intentionally did *not* attempt and why: Did not try anything crazy to tune it, only added in the previous HRs.
* Any constraints encountered (data, labels, compute, time): Only the fact that SVMs doesn't work great for this dataset. 


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

Before fixing it by adding in previous HRs, the F1 was pretty much the same for SVMs (and the rest): .64 

After adding in HRs, it had a whopping gain up to: 0.67. It's not much, but its at least an improvement from the last several assignements.
---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

SVMs wasn't different or any better as it wasn't super applicable to the case. Adding the HRs made it more accurate, better than changing the model ever has. I think the best thing in the future (or theoretical future) would be to add more data points if possible, and see if it also improves the F1. 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
* What would you try next if data or resources were not constrained?
    - Add more data points and rerun everything just the same with the model. 

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable)

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: The data is all mixed up, mainly due to having multiple points, so SVMs doesn't improve anything.
* Evidence supporting that conclusion: The F1 was almost identical to everything else we've tried.
* What value this attempt still provided: Showed more evidence the best thing to do right now is add more data rather than adjust the model.



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

