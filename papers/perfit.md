---
title: "PerFit"
layout: clean
permalink: /papers/perfit/
---

<link rel="stylesheet" href="/assets/perfit.css">

<div class="perfit-page">
  <header class="perfit-hero">
    <div class="perfit-topbar">
      <a class="perfit-back" href="/">Personalized LLM</a>
      <span class="perfit-status">ICLR 2026</span>
    </div>

    <div class="perfit-title-row">
      <img class="perfit-title-icon" src="/images/papers/perfit/perfit_icon.png" alt="PerFit icon">
      <h1><span class="perfit-title-word">PerFit</span>: Exploring Personalization Shifts in Representation Space of LLMs</h1>
    </div>
    <p class="perfit-subtitle">—— A two-stage representation-space fine-tuning method for efficient LLM personalization.</p>
    <div class="perfit-meta">
      <p class="perfit-authors">
        <span class="perfit-meta-label">Authors</span>
        Jiahong Liu<sup>1</sup>, Wenhao Yu<sup>1</sup>, Quanyu Dai<sup>2</sup>, Zhongyang Li<sup>3</sup>, Jieming Zhu<sup>2</sup>,
        Menglin Yang<sup>4</sup>, Tat-Seng Chua<sup>5</sup>, Irwin King<sup>1</sup>
      </p>
      <p class="perfit-affiliations">
        <span class="perfit-meta-label">Affiliations</span>
        <sup>1</sup>CUHK &nbsp; <sup>2</sup>Huawei &nbsp; <sup>3</sup>Microsoft AI &nbsp; <sup>4</sup>HKUST(GZ) &nbsp; <sup>5</sup>NUS
      </p>
    </div>

    <div class="perfit-links">
      <a class="pf-btn pf-btn-primary" href="/assets/papers/perfit-iclr2026.pdf" target="_blank" rel="noopener noreferrer">
        <svg class="pf-btn-icon" viewBox="0 0 16 16" aria-hidden="true">
          <path d="M4 1.5h5l3 3v10H4z"></path>
          <path d="M9 1.5v3h3"></path>
          <path d="M5.5 7h5M5.5 9h5M5.5 11h3.5"></path>
        </svg>
        Paper (PDF)
      </a>
      <a class="pf-btn pf-btn-ghost" href="https://github.com/JiahongLiu21/PerFit" target="_blank" rel="noopener noreferrer">
        <svg class="pf-btn-icon" viewBox="0 0 16 16" aria-hidden="true">
          <path d="M6 4 2.5 8 6 12"></path>
          <path d="m10 4 3.5 4-3.5 4"></path>
          <path d="m9 3.5-2 9"></path>
        </svg>
        Code
      </a>
      <a class="pf-btn pf-btn-ghost" href="#citation">
        <svg class="pf-btn-icon" viewBox="0 0 16 16" aria-hidden="true">
          <path d="M4.8 6.3h2v2.2h-2z"></path>
          <path d="M9.2 6.3h2v2.2h-2z"></path>
          <path d="M4.8 6.3V5.2a1.2 1.2 0 0 1 1.2-1.2h.8"></path>
          <path d="M9.2 6.3V5.2a1.2 1.2 0 0 1 1.2-1.2h.8"></path>
        </svg>
        BibTeX
      </a>
    </div>
  </header>

  <div class="perfit-teaser">
    <img src="/images/papers/perfit/perfit_figure.png" alt="PerFit framework overview figure">
    <p class="perfit-figure-note">
      Figure 1. PerFit framework overview and performance/parameter trade-off.
    </p>
  </div>

  <section id="highlights" class="perfit-highlights-wrap">
    <h2>Highlights</h2>
    <div class="perfit-grid">
    <article class="perfit-stat">
      <h3>Core Idea</h3>
      <p>Identify personalization shift and fine-tune personalized LLMs directly in representation space.</p>
    </article>
    <article class="perfit-stat">
      <h3>Key Result</h3>
      <p>Strong overall performance across all six LaMP personalization tasks.</p>
    </article>
    <article class="perfit-stat">
      <h3>Efficiency</h3>
      <p>81.25%-98.44% fewer trainable parameters and 17.0%-35.8% less training time.</p>
    </article>
    </div>
  </section>

  <section id="abstract">
    <h2>Abstract</h2>
    <p>
      Personalization has become a pivotal field of study in contemporary intelligent systems. While
      large language models (LLMs) excel at general knowledge tasks, they often struggle with
      personalization, i.e., adapting their outputs to individual user expectations. Existing methods
      (e.g., RAG/PAG and LoRA-based PEFT) face challenges in balancing effectiveness and efficiency.
      PerFit first uncovers key patterns in representation space: personalized information lies in a
      low-rank subspace, and user vectors exhibit both a collective shift and user-specific shifts.
      Based on these findings, PerFit introduces a two-stage representation-space intervention tuning
      strategy that directly steers hidden representations with minimal parameter overhead.
    </p>
  </section>

  <section id="insights">
    <h2>Key Observations</h2>
    <p class="perfit-observation-intro">
      <code>Delta vectors</code> are extracted at each layer by taking the hidden-state difference
      between original queries and personalization-enhanced queries for each user.
      These <code>delta vectors</code> are then analyzed across users.
    </p>
    <div class="perfit-observation-grid">
      <article class="perfit-observation perfit-observation-lowrank">
        <h3>Observation 1: Low-rank Subspace</h3>
        <p>
          The <code>delta vectors</code> can be effectively represented within a low-dimensional orthogonal
          subspace, significantly reducing the original feature space dimensionality.
        </p>
        <div class="perfit-results perfit-observation-table">
          <table>
            <thead>
              <tr>
                <th>Dataset</th>
                <th>r (0.8)</th>
                <th>‰ (0.8)</th>
                <th>r (0.9)</th>
                <th>‰ (0.9)</th>
                <th>r (0.95)</th>
                <th>‰ (0.95)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>LaMP-2M</td>
                <td>1</td>
                <td>1.21</td>
                <td>3</td>
                <td>3.62</td>
                <td>12</td>
                <td>14.48</td>
              </tr>
              <tr>
                <td>LaMP-2N</td>
                <td>1</td>
                <td>3.65</td>
                <td>4</td>
                <td>14.60</td>
                <td>20</td>
                <td>72.90</td>
              </tr>
              <tr>
                <td>LaMP-3</td>
                <td>3</td>
                <td>0.73</td>
                <td>18</td>
                <td>4.39</td>
                <td>93</td>
                <td>22.71</td>
              </tr>
              <tr>
                <td>LaMP-4</td>
                <td>34</td>
                <td>22.03</td>
                <td>167</td>
                <td>108.23</td>
                <td>368</td>
                <td>238.50</td>
              </tr>
              <tr>
                <td>LaMP-5</td>
                <td>4</td>
                <td>0.98</td>
                <td>40</td>
                <td>9.77</td>
                <td>203</td>
                <td>49.56</td>
              </tr>
              <tr>
                <td>LaMP-7</td>
                <td>3</td>
                <td>0.73</td>
                <td>32</td>
                <td>7.81</td>
                <td>177</td>
                <td>43.21</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="perfit-observation-note">
          Table 1 (+ appendix, same Llama backbone). Effective rank is far below full dimensionality,
          indicating strong low-rank structure.
        </p>
      </article>

      <article class="perfit-observation perfit-observation-shift">
        <h3>Observation 2: Collective and Personalized Shifts</h3>
        <p>
          The <code>delta vectors</code> exhibit a collective shift, accompanied by personalized shifts
          reflecting individual variability.
        </p>
        <figure class="perfit-observation-figure">
          <img src="/images/papers/perfit/figure2.png" alt="Observation 2 shift analysis figure">
          <figcaption>
            Figure 2. First row: low-rank vectors projected onto the first two principal components.
            Second row: coordinate distributions across dimensions, showing shared shift and user-level variation.
          </figcaption>
        </figure>
      </article>
    </div>
  </section>

  <section id="method">
    <h2>Method Overview</h2>
    <div class="perfit-cards">
      <article class="perfit-card">
        <h3>Stage-1 Collective Shift</h3>
        <p>Train on all users to learn a shared intervention in low-rank representation subspace.</p>
      </article>
      <article class="perfit-card">
        <h3>Stage-2 Personalized Shift</h3>
        <p>Fine-tune user-specific interventions on top of Stage-1 for individual adaptation.</p>
      </article>
    </div>
    <figure class="perfit-figure-card perfit-method-figure">
      <img src="/images/papers/perfit/perfit2.png" alt="PerFit two-stage method figure">
      <figcaption>Two-stage personalization: learn a collective shift first, then refine with user-specific shift.</figcaption>
    </figure>
  </section>

  <section id="results">
    <h2>Main Results on LaMP</h2>
    <div class="perfit-results">
      <table>
        <thead>
          <tr>
            <th>Classification</th>
            <th>LaMP-2N (Acc / F1)</th>
            <th>LaMP-2M (Acc / F1)</th>
            <th>LaMP-3 (MAE / RMSE)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>OPPU</td>
            <td>0.810 / 0.589</td>
            <td>0.600 / 0.493</td>
            <td>0.179 / 0.443</td>
          </tr>
          <tr>
            <td class="best">PerFit</td>
            <td class="best">0.818 / 0.586</td>
            <td class="best">0.630 / 0.518</td>
            <td class="best">0.179 / 0.443</td>
          </tr>
          <tr>
            <td class="best">Param. reduction vs OPPU</td>
            <td class="best">93.75% / 81.25%</td>
            <td class="best">91.67% / 98.44%</td>
            <td class="best">87.50% / 97.66%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="perfit-results" style="margin-top: 14px;">
      <table>
        <thead>
          <tr>
            <th>Generation</th>
            <th>LaMP-4 (R-1 / R-L)</th>
            <th>LaMP-5 (R-1 / R-L)</th>
            <th>LaMP-7 (R-1 / R-L)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>OPPU</td>
            <td>0.191 / 0.171</td>
            <td>0.519 / 0.442</td>
            <td>0.539 / 0.483</td>
          </tr>
          <tr>
            <td class="best">PerFit</td>
            <td class="best">0.207 / 0.186</td>
            <td class="best">0.521 / 0.451</td>
            <td class="best">0.525 / 0.472</td>
          </tr>
          <tr>
            <td class="best">Param. reduction vs OPPU</td>
            <td class="best">87.50% / 97.66%</td>
            <td class="best">95.83% / 98.44%</td>
            <td class="best">91.67% / 93.75%</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section id="citation">
    <h2>Citation</h2>
    <div class="perfit-cite-wrap">
      <div class="perfit-cite-head">
        <strong>BibTeX</strong>
        <button class="perfit-copy" type="button" onclick="copyPerfitBibtex()">Copy</button>
      </div>
      <pre id="perfit-bibtex">@inproceedings{liu2026perfit,
  title={PerFit: Exploring Personalization Shifts in Representation Space of LLMs},
  author={Liu, Jiahong and Yu, Wenhao and Dai, Quanyu and Li, Zhongyang and Zhu, Jieming and Yang, Menglin and Chua, Tat-Seng and King, Irwin},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2026}
}</pre>
    </div>
  </section>

  <p class="perfit-footer">Contact: jiahong.liu21@gmail.com</p>
</div>

<script>
function copyPerfitBibtex() {
  var text = document.getElementById("perfit-bibtex").innerText;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text);
  }
}
</script>
