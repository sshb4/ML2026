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

* **Technique / Model Family Covered This Week: Practical Deep Learning and Frameworks**
* **Key Assumptions of This Technique: 
- These techniques are useful to my case.** (1–2 bullets)

**Fit Assessment (required): Practical Deep Learning Systems**

> I expect this technique to be a **partial** fit for my project because: Several points would be useful or probably useful, like checkpointing. Others, like dataloader would not hurt, but my model is so small it might not actually make much difference. Overall, I will try applying what seems potentially useful.
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

* **Why this representation was reasonable for this week: I'm simply adding a few extra bits to the MLP set from 11, so it should stay the same. w**


---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Added random seeds before running MLP. Added checkpointing after you run the MLP. 
* What you intentionally did *not* attempt and why: Skipped dataloading and of course CNN, as this is tabular data and only a few thousand rows.  
* Any constraints encountered (data, labels, compute, time): None.  


## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

Checkpoint worked as expected/hoped and confirmed to be successful.

---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

Some of these additions that could have been implemented show that this is a unique case, in that it's so small and honestly a weird type of data, so it is a bit different from many models would be. Also of course, something like a visual analysis would be much different and probbaly far more complex than a tabular data analysis, utilizing things like CNN. 
Additionally, the checkpoint shows the MLP should be good, since it gave the same output. 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
    - I did not get to adding a secondary threshhold yet. 
* What would you try next if data or resources were not constrained?

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable) - 

If this week’s technique was a poor fit, explain:

* Why it does not align with your project: not a poor fit, only partial.
* Evidence supporting that conclusion: CNN was not applicable, but the others were at least potentially useful.
* What value this attempt still provided: Showed variance between different projects and models, especially the difference that having a small model can cause.



---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

