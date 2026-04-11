---
title: "A Survey of Personalized Large Language Models"
layout: clean
permalink: /papers/survey/
---

<link rel="stylesheet" href="/assets/perfit.css">
<link rel="stylesheet" href="/assets/survey.css">

<div class="perfit-page survey-page">
  <header class="perfit-hero survey-hero">
    <div class="perfit-topbar">
      <a class="perfit-back" href="/">Personalized LLM</a>
      <span class="perfit-status">arXiv 2025</span>
    </div>

    <div class="perfit-title-row">
      <img class="survey-title-mark" src="/icon.png" alt="Personalized LLM icon">
      <h1>A Survey of Personalized Large Language Models: Progress and Future Directions</h1>
    </div>
    <p class="perfit-subtitle">A systematic taxonomy of personalized LLMs across prompting, adaptation, alignment, evaluation, and future directions.</p>

    <div class="perfit-meta">
      <p class="perfit-authors">
        <span class="perfit-meta-label">Authors</span>
        Jiahong Liu<sup>1</sup>, Zexuan Qiu<sup>1</sup>, Zhongyang Li<sup>2</sup>, Quanyu Dai<sup>2</sup>, Wenhao Yu<sup>1</sup>,
        Jieming Zhu<sup>2</sup>, Minda Hu<sup>1</sup>, Menglin Yang<sup>3</sup>, Tat-Seng Chua<sup>4</sup>, Irwin King<sup>1</sup>
      </p>
      <p class="perfit-affiliations">
        <span class="perfit-meta-label">affiliations</span>
        <sup>1</sup>CUHK &nbsp; <sup>2</sup>Huawei &nbsp; <sup>3</sup>HKUST(GZ) &nbsp; <sup>4</sup>NUS
      </p>
      <p class="perfit-affiliations">
        <span class="perfit-meta-label">Paper</span>
        arXiv:2502.11528, latest version updated on September 20, 2025
      </p>
    </div>

    <div class="perfit-links">
      <a class="pf-btn pf-btn-primary" href="https://arxiv.org/pdf/2502.11528" target="_blank" rel="noopener noreferrer">
        <svg class="pf-btn-icon" viewBox="0 0 16 16" aria-hidden="true">
          <path d="M4 1.5h5l3 3v10H4z"></path>
          <path d="M9 1.5v3h3"></path>
          <path d="M5.5 7h5M5.5 9h5M5.5 11h3.5"></path>
        </svg>
        Paper (arXiv PDF)
      </a>
      <a class="pf-btn pf-btn-ghost" href="https://arxiv.org/abs/2502.11528" target="_blank" rel="noopener noreferrer">
        <svg class="pf-btn-icon" viewBox="0 0 16 16" aria-hidden="true">
          <path d="M3 8h10"></path>
          <path d="m9 4 4 4-4 4"></path>
        </svg>
        arXiv Page
      </a>
      <a class="pf-btn pf-btn-ghost" href="https://github.com/JiahongLiu21/Awesome-Personalized-Large-Language-Models" target="_blank" rel="noopener noreferrer">
        <svg class="pf-btn-icon" viewBox="0 0 16 16" aria-hidden="true">
          <path d="M6 4 2.5 8 6 12"></path>
          <path d="m10 4 3.5 4-3.5 4"></path>
          <path d="m9 3.5-2 9"></path>
        </svg>
        Resources
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

  <div class="survey-shell">
    <nav class="survey-toc" aria-label="Survey page contents">
      <p>Contents</p>
      <a href="#blog-intro">Why Personalization</a>
      <a href="#highlights">Overview</a>
      <a href="#framework">Taxonomy</a>
      <a href="#query-types">Query Types</a>
      <a href="#prompting">Prompting</a>
      <a href="#adaptation">Adaptation</a>
      <a href="#alignment">Alignment</a>
      <a href="#benchmarks">Benchmarks</a>
      <a href="#future">Future</a>
      <a href="#takeaways">Takeaways</a>
      <a href="#citation">Citation</a>
    </nav>

    <main class="survey-content">
  <section id="blog-intro" class="survey-blog-section">
    <p class="survey-kicker">Why personalization?</p>
    <h2>General LLMs know a lot, but they do not know <em>you</em>.</h2>
    <p>
      A general-purpose LLM is usually optimized for population-level usefulness. That is powerful, but it also creates a
      <strong>one-size-fits-all</strong> behavior: the same query tends to receive a generic answer even when users differ in taste, history,
      language style, goals, and constraints. Personalized Large Language Models (PLLMs) aim to move from this
      one-size-fits-all setting toward <em>one-size-fits-one</em> systems.
    </p>
    <figure class="survey-figure">
      <img src="/images/papers/survey/general-vs-personalized.png" alt="Comparison between general LLMs and personalized LLMs">
      <figcaption>Personalized LLMs adapt to different users instead of forcing diverse preferences into one shared response pattern.</figcaption>
    </figure>
  </section>

  <section id="highlights" class="perfit-highlights-wrap">
    <h2>What This Survey Organizes</h2>
    <div class="perfit-grid">
      <article class="perfit-stat">
        <h3>Personalized Data</h3>
        <p>Profiles, relationships, historical dialogues, historical content, interactions, and preference signals.</p>
      </article>
      <article class="perfit-stat">
        <h3>Technical Levels</h3>
        <p>Input-level prompting, model-level adaptation, and objective-level alignment.</p>
      </article>
      <article class="perfit-stat">
        <h3>Evaluation Landscape</h3>
        <p>Benchmarks across extraction, abstraction, generalization, classification, generation, and recommendation.</p>
      </article>
    </div>
  </section>

  <section id="framework" class="survey-blog-section">
    <p class="survey-kicker">The taxonomy</p>
    <h2>Three places to inject personalization</h2>
    <p>
      The paper frames PLLM methods around the personalization operation: how user-specific data is turned into behavior
      that changes a model's response. The key organizing idea is simple and useful. Personalization can happen before the
      model sees the input, inside the model through adapted parameters or modules, or in the <strong>learning objective</strong> that defines
      which responses are preferred.
    </p>
    <figure class="survey-figure survey-wide-figure">
      <img src="/images/papers/survey/framework.png" alt="Taxonomy framework for personalized large language models">
      <figcaption>
        The survey groups PLLM techniques into Personalized Prompting, Personalized Adaptation, and Personalized Alignment,
        while also tracking personalized data types, query types, and task families.
      </figcaption>
    </figure>
    <div class="survey-comparison-grid">
      <article class="survey-note-card">
        <h3>Input Level: Prompting</h3>
        <p>Keep the base LLM fixed. Build prompts, retrieved memories, soft prompts, or contrastive steering signals from user data.</p>
      </article>
      <article class="survey-note-card">
        <h3>Model Level: Adaptation</h3>
        <p>Change model behavior through PEFT modules, user embeddings, LoRA variants, MoE-style routing, or per-user adapters.</p>
      </article>
      <article class="survey-note-card">
        <h3>Objective Level: Alignment</h3>
        <p>Optimize or decode with user-specific preferences, reward models, model merging, ensembles, or test-time feedback.</p>
      </article>
    </div>
  </section>

  <section id="query-types" class="survey-blog-section">
    <p class="survey-kicker">What does a personalized query ask?</p>
    <h2>Extraction, abstraction, and generalization require different memory behavior</h2>
    <p>
      Not every personalized query is equally hard. Some questions ask the system to extract an explicit fact from a user's
      history. Others require <strong>abstraction</strong>, where the model must summarize or infer higher-level preferences. The hardest
      cases often require <strong>generalization</strong>: the model must use personal evidence plus external knowledge to produce a response
      that fits the user but is not directly stated in the history.
    </p>
    <figure class="survey-figure survey-tall-figure">
      <img src="/images/papers/survey/query-types.png" alt="Examples of personalized data and query types">
      <figcaption>
        The survey distinguishes query types by how directly the answer can be grounded in user data and whether external
        knowledge is needed.
      </figcaption>
    </figure>
  </section>

  <section id="prompting" class="survey-blog-section">
    <p class="survey-kicker">Path 1</p>
    <h2>Personalized Prompting: efficient, flexible, but bounded by context</h2>
    <p>
      Prompting-based methods put personalization around the <strong>frozen LLM</strong>. They are attractive because they are cheap to deploy,
      work well with black-box models, and can update memories without retraining the generator. The survey separates this
      family into four subtypes: profile-augmented prompting, retrieval-augmented prompting, soft-fused prompting, and
      contrastive prompting.
    </p>
    <figure class="survey-figure">
      <img src="/images/papers/survey/prompting.png" alt="Personalized prompting methods">
      <figcaption>
        Prompting methods differ in how they transform user history into context: summaries, retrieved records, soft
        embeddings, or contrastive steering signals.
      </figcaption>
    </figure>
    <div class="survey-table-wrap">
      <table class="survey-table">
        <thead>
          <tr>
            <th>Method Family</th>
            <th>How It Works</th>
            <th>Strength</th>
            <th>Main Risk</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Profile-Augmented</td>
            <td>Summarize user history into profile tokens.</td>
            <td>Efficient and easy to cache.</td>
            <td>Compression may lose useful details.</td>
          </tr>
          <tr>
            <td>Retrieval-Augmented</td>
            <td>Retrieve relevant memories and concatenate them with the query.</td>
            <td>Good fit for long-term memory and explicit facts.</td>
            <td>Retrieval can be noisy or expensive.</td>
          </tr>
          <tr>
            <td>Soft-Fused</td>
            <td>Encode user data into embeddings, prefixes, attention signals, or logits.</td>
            <td>Captures semantic nuance beyond text summaries.</td>
            <td>Less interpretable and often harder for black-box deployment.</td>
          </tr>
          <tr>
            <td>Contrastive</td>
            <td>Compare model states with and without personal context.</td>
            <td>More controllable and interpretable.</td>
            <td>Sensitive to steering scale and hyperparameters.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section id="adaptation" class="survey-blog-section">
    <p class="survey-kicker">Path 2</p>
    <h2>Personalized Adaptation: deeper personalization with parameter trade-offs</h2>
    <p>
      Adaptation-based methods modify a <strong>small set of parameters or modules</strong>, often through PEFT. This makes them more capable
      than pure prompting when the target behavior is implicit, stylistic, or hard to express as retrieved text. The core
      design choice is whether all users share one personalized module or each user owns a separate module.
    </p>
    <figure class="survey-figure">
      <img src="/images/papers/survey/adaptation.png" alt="Personalized adaptation methods">
      <figcaption>
        Shared adapters improve scalability; per-user adapters improve isolation and personalization depth but introduce
        storage and training overhead.
      </figcaption>
    </figure>
    <div class="survey-table-wrap">
      <table class="survey-table">
        <thead>
          <tr>
            <th>Adaptation Strategy</th>
            <th>Best For</th>
            <th>Pros</th>
            <th>Cons</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>One PEFT for All Users</td>
            <td>Large-scale services with many users and limited adapter budget.</td>
            <td>Parameter-efficient, scalable, easier to maintain.</td>
            <td>May blur individual differences and depend heavily on user data encoding.</td>
          </tr>
          <tr>
            <td>One PEFT Per User</td>
            <td>High-stakes or private settings where user isolation matters.</td>
            <td>Stronger personalization, better separation between users.</td>
            <td>Higher storage, training, synchronization, and cold-start cost.</td>
          </tr>
          <tr>
            <td>Collaborative or Federated PEFT</td>
            <td>Settings that need both personalization and cross-user transfer.</td>
            <td>Can share useful population-level signals without raw data sharing.</td>
            <td>Must balance privacy leakage, communication cost, and robustness.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section id="alignment" class="survey-blog-section">
    <p class="survey-kicker">Path 3</p>
    <h2>Personalized Alignment: preferences are not universal</h2>
    <p>
      Generic alignment optimizes for broad human preferences. <strong>Personalized alignment</strong> asks a different question: what if
      users disagree about style, values, depth, risk tolerance, or decision behavior? The survey treats this as a preference
      modeling problem, often connected to multi-objective reward learning, decoding-time model combination, and test-time
      feedback.
    </p>
    <figure class="survey-figure">
      <img src="/images/papers/survey/alignment.png" alt="Personalized alignment methods">
      <figcaption>
        Personalized alignment can happen through multi-objective RLHF, user-weighted model merging, or ensembles of
        specialized policies.
      </figcaption>
    </figure>
    <div class="survey-table-wrap">
      <table class="survey-table">
        <thead>
          <tr>
            <th>Alignment Route</th>
            <th>Personalization Mechanism</th>
            <th>Strength</th>
            <th>Limitation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Training-Time Personalization</td>
            <td>Use user-specific reward mixtures during policy optimization.</td>
            <td>Strong personalization and efficient inference.</td>
            <td>High training cost and less flexibility after training.</td>
          </tr>
          <tr>
            <td>Decoding-Time Personalization</td>
            <td>Merge or ensemble policies using user-specific weights at inference.</td>
            <td>Flexible and can adapt without retraining the base model.</td>
            <td>Extra storage and inference overhead.</td>
          </tr>
          <tr>
            <td>Test-Time Feedback</td>
            <td>Update prompts, personas, or reward signals from live interactions.</td>
            <td>Promising for evolving user preferences.</td>
            <td>Benchmarks and stability guarantees remain underdeveloped.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section id="benchmarks" class="survey-blog-section">
    <p class="survey-kicker">Evaluation</p>
    <h2>Personalization should be evaluated by data type, query type, and task</h2>
    <p>
      The benchmark landscape is broad because personalization itself is broad. Dialogue-based benchmarks often test memory
      extraction from conversation histories. Content-based benchmarks such as <strong>LaMP</strong> and <strong>LongLaMP</strong> test whether the model can
      incorporate a user's historical text. Preference-based benchmarks emphasize <em>subjective alignment</em>. Interaction-based
      benchmarks connect personalization to recommendation and user behavior modeling.
    </p>
    <div class="survey-table-wrap">
      <table class="survey-table">
        <thead>
          <tr>
            <th>Benchmark Group</th>
            <th>Personalized Data</th>
            <th>Typical Query</th>
            <th>Common Metrics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>MemoryBank, PerLTQA, LoCoMo, LongMemEval, MMRC, IMPLEXCONV, MemBench</td>
            <td>User profiles and dialogues</td>
            <td>Mostly extraction, with some abstraction and generalization</td>
            <td>LLM-E, F1, Recall, Human-E, Acc</td>
          </tr>
          <tr>
            <td>LaMP, LongLaMP, PEFT-U, pGraphRAG, LaMP-QA, DPL, PERSONABench</td>
            <td>Historical content</td>
            <td>Abstraction and generalization</td>
            <td>Acc, F1, MAE, RMSE, ROUGE, BLEU, METEOR, LLM-E</td>
          </tr>
          <tr>
            <td>PRISM, PersonalLLM, ALOE, HiCUPID</td>
            <td>Human preferences and personas</td>
            <td>Preference-aware generation</td>
            <td>BLEU, ROUGE-L, LLM-E, human evaluation</td>
          </tr>
          <tr>
            <td>REGEN, PersonalWAB, RecBench+</td>
            <td>User interactions and profiles</td>
            <td>Recommendation or behavior-grounded generation</td>
            <td>Acc, Precision, Recall, ROUGE-L, BLEU, SBERT</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section id="future" class="survey-blog-section">
    <p class="survey-kicker">Future directions</p>
    <h2>The next frontier is memory that can remember, adapt, and evolve</h2>
    <p>
      The survey's forward-looking view is that PLLMs should not only retrieve user-specific facts, but also abstract from
      long-term evidence and evolve as users change. This creates a difficult <strong>trilemma</strong>: stronger personalization tends to
      need more computation or more private data; stronger privacy often limits cross-user transfer; and scalable deployment
      on edge devices makes both constraints sharper.
    </p>
    <figure class="survey-figure">
      <img src="/images/papers/survey/future-directions.png" alt="Future directions for personalized large language models">
      <figcaption>
        Future PLLMs should improve efficacy, efficiency, and trustworthiness across extraction, abstraction, generalization,
        and lifelong evolution.
      </figcaption>
    </figure>
    <div class="survey-comparison-grid survey-five-grid">
      <article class="survey-note-card">
        <h3>Complex User Data</h3>
        <p>Move beyond text-only histories toward multi-source, graph-like, and multimodal user signals.</p>
      </article>
      <article class="survey-note-card">
        <h3>Edge Computing</h3>
        <p>Support lightweight personalization on phones and local devices through small models, quantization, and distillation.</p>
      </article>
      <article class="survey-note-card">
        <h3>Edge-Cloud Collaboration</h3>
        <p>Balance local privacy with cloud-scale capability while reducing synchronization cost.</p>
      </article>
      <article class="survey-note-card">
        <h3>Model Updates</h3>
        <p>Update user-specific modules when base LLMs change without retraining everything from scratch.</p>
      </article>
      <article class="survey-note-card">
        <h3>Lifelong Updating</h3>
        <p>Let personal memories change over time without catastrophic forgetting or stale preferences.</p>
      </article>
    </div>
  </section>

  <section id="takeaways" class="survey-blog-section">
    <p class="survey-kicker">Takeaways</p>
    <h2>A practical reading map</h2>
    <div class="survey-takeaways">
      <p><strong>Use prompting</strong> when personalization mainly means retrieving explicit facts or adding lightweight context.</p>
      <p><strong>Use adaptation</strong> when the model must internalize implicit style, preferences, and behavior patterns.</p>
      <p><strong>Use alignment</strong> when the key problem is subjective preference, value trade-offs, or dynamic feedback.</p>
      <p><strong>Evaluate carefully</strong> because success depends on data type, query type, task type, and whether the metric actually measures personalization rather than generic generation quality.</p>
    </div>
  </section>

  <section id="citation">
    <h2>Citation</h2>
    <div class="perfit-cite-wrap">
      <div class="perfit-cite-head">
        <strong>BibTeX</strong>
        <button class="perfit-copy" type="button" onclick="copySurveyBibtex()">Copy</button>
      </div>
      <pre id="survey-bibtex">@article{liu2025survey,
  title={A Survey of Personalized Large Language Models: Progress and Future Directions},
  author={Liu, Jiahong and Qiu, Zexuan and Li, Zhongyang and Dai, Quanyu and Yu, Wenhao and Zhu, Jieming and Hu, Minda and Yang, Menglin and Chua, Tat-Seng and King, Irwin},
  journal={arXiv preprint arXiv:2502.11528},
  year={2025}
}</pre>
    </div>
  </section>
    </main>
  </div>

  <p class="perfit-footer">Contact: jiahong.liu21@gmail.com</p>
</div>

<script>
function copySurveyBibtex() {
  var text = document.getElementById("survey-bibtex").innerText;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text);
  }
}
</script>
