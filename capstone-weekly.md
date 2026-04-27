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

## 2. This Week’s Technique and Its Assumptions - N/A

* **Technique / Model Family Covered This Week:**
* **Key Assumptions of This Technique:** (1–2 bullets)

**Fit Assessment (required):**

> I expect this technique to be a **good / partial / poor** fit for my project because:

(2–4 sentences)

---

## 3. Representation or Proxy Used - N/A

Describe how your data was represented so that this week’s technique could be applied.

Examples include:

* Hand-engineered features

* Summary statistics

* Frozen embeddings

* Dimensionality reduction

* A proxy task

* **Representation or Proxy Chosen:**

* **Why this representation was reasonable for this week:**

---

## 4. What Was Attempted

Be concrete and scoped. Do not list everything you *could* have done.

* What you implemented this week
  - Initialized the working notebook for my personal project, and decided on a tentative data set to focus on.
* What you intentionally did *not* attempt and why
  - Any actual "Machine Learning" or training, as we have not gotten there yet.
* Any constraints encountered (data, labels, compute, time)
  - Could not easily find some of the data I wanted.

---

## 5. Results or Observations

Cell output produced by my local python project:

CSV path: /Users/sashabates/Desktop/4320/df_power.csv
Shape: (4843, 323)

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Season</th>
      <th>Name</th>
      <th>HR</th>
      <th>prev_HR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017</td>
      <td>A.J. Cole</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018</td>
      <td>A.J. Cole</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017</td>
      <td>A.J. Ellis</td>
      <td>6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018</td>
      <td>A.J. Ellis</td>
      <td>1</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017</td>
      <td>A.J. Pollock</td>
      <td>14</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>
---

## 6. Interpretation and Judgment - N/A

This section matters most.

Reflect on:

* Why the method behaved as it did
* Which assumptions held or failed
* What this reveals about your data or problem framing

(1–2 thoughtful paragraphs)

---

## 7. Forward-Looking Adjustment

Answer **one** of the following:

* What will you keep, change, or discard before the next assignment?
* What would you try next if data or resources were not constrained?
  - I would adjust the dataset to include more points I want to train the model on.

---

## 8. Mismatch Acknowledgment (Complete Only If Applicable) - N/A

If this week’s technique was a poor fit, explain:

* Why it does not align with your project
* Evidence supporting that conclusion
* What value this attempt still provided

---

## Submission Notes

* Written submission format: **Markdown or PDF**
* Code or notebooks: **optional unless explicitly requested**
* Performance is **not** graded competitively
* Clear reasoning and honest reflection matter more than results

