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

* **Technique / Model Family Covered This Week: Splitting/Preparing data **
* **Key Assumptions of This Technique: 
- There is a way to split the data that will result in a meaningful/good outcome** (1–2 bullets)

**Fit Assessment (required): Good/NA, as splitting data is a key aspect of ML**

> I expect this technique to be a **good** fit for my project because: it will assist in training and validating my model. This will help determine how best to split the model, which will help the rest of the project be successful.  

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

* **Representation or Proxy Chosen: Tabular data**

* **Why this representation was reasonable for this week: Tables of data are typically easy for both humans and machines to understand.**

---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week: Implemented the todos in the py file, mainly one-hot encoding. Also implemented sorting for the data, really mainly preparing the data. Also implemented a lot of prints to easily get information on the data. 
* What you intentionally did *not* attempt and why: Not applicable at this stage
* Any constraints encountered (data, labels, compute, time): I decided to keep it fairly simple, there are a lot of data points that my dataset included, and it was a bit overwhelming so I pared it down to only Season, Age, AB, HR. 

---

## 5. Results or Observations

You may include metrics **if applicable**, but qualitative observations are also valid.

Examples:

* Evaluation metrics
* Training behavior or convergence issues
* Error patterns
* Unexpected behaviors

This week's processing was as expected, nothing weird or strange as we haven't delved into actual training yet. However it did bring up some characteristics of the dataset or concept of the project overall that I need to consider, that I want to discuss in the interpretation. 

---

## 6. Interpretation and Judgment

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

These preparation steps worked as expected. Mainly cleaning things up, getting my actual dataset for use ready, and splitting it into the sets. It did bring up an issue, which is that the data I am using is quite finite, especially compared to other projects. My project can't just take in some more data from another set as there is only so many players and years, and I'm trying to predict for individuals rather than the whole/random players. 

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
* What would you try next if data or resources were not constrained?
- I need to adjust the split, as I need to ensure it is by player, rather than random. It needs to train on a certain set of players, then try itself on a new player and see what it gives. 

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable)

If this week’s technique was a poor fit, explain:

* Why it does not align with your project
* Evidence supporting that conclusion
* What value this attempt still provided

Not applicable at this stage

---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

