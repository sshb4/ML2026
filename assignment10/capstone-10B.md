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

* **Technique / Model Family Covered This Week: Unsupervised Learning**
* **Key Assumptions of This Technique: 
- Groups exist within the data that are visible on graphed.** (1–2 bullets)

**Fit Assessment (required): **

> I expect this technique to be a **partial** fit for my project because: I already have a general idea of the structure of the data, rather than needing to find unknown structures in the data. It's a project that naturally lends to supervised more. 
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

* **Representation or Proxy Chosen: Maintain at Hand-engineered features, adding in SLG.**

* **Why this representation was reasonable for this week: Same as previous, but now added the new column of slugging. **


---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Added in SLG, and tried PCA.
* What you intentionally did *not* attempt and why: Did not attempt any other data, although it was tempting. I also almost was going to see the difference running it with SLG or OPS would do, but I wanted to keep it simple.
* Any constraints encountered (data, labels, compute, time): I wanted to maybe add ISO, but my data didn't include that as a column.


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

The main difference this time was from adding the SLG data in, which gave us a jump on F1 from 0.7 to 0.75 which is a new high. 

The graph I got was not particularly interesting for a binary classification, just very split down the middle for "power" vs not hitters. 

---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

The results of the clustering aligned in a way that makes sense with the data and threshhold I had picked for supervised. However it found that mark naturally, so 20 seems like a good point to have picked. I think that was due to the addition of SLG possibly, that a distinction emerged once that data was added. 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
    - Now that I've figured out how to pull more data, I probably will add another feature to see if we can get even more improvement from 0.75.
* What would you try next if data or resources were not constrained?

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable) - 
Not applicable for this project at this stage. I think it was a good fit. 

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: 
* Evidence supporting that conclusion: 
* What value this attempt still provided: 



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

