---
title: "Personalization in the Era of Large Foundation Models\nWorkshop @ AAAI 2026"
layout: page
permalink: /events/perfm-aaai26/
---

<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/assets/aaai2026.css">

<div style="text-align: right; margin-top: -3.5em; margin-bottom: 2em;">
<h2 style="color: #0366d6; font-size: 1.5em; font-weight: 600; margin: 0;"><img src="/icon.png" alt="icon" class="subtitle-icon">  — Shaping the Next Generation of AI Systems</h2>
</div>

<div style="color: #0366d6; margin-bottom: 5ex;">


<div class="sidebar-container">
  <div class="sidebar" id="sidebar">
    <button class="sidebar-toggle" id="sidebar-toggle" onclick="toggleSidebar()">◀</button>
    <div class="sidebar-content">
      <ul>
        <li><a href="#news">📢 News</a></li>
        <li><a href="#1-workshop-introduction">🎯 Workshop Introduction</a></li>
        <li><a href="#2-call-for-contributions-topics-and-scope">📝 Call for Contributions</a></li>
        <li><a href="#3-submissions-and-timeline">📅 Submissions and Timeline</a></li>
        <li><a href="#invited-speakers">🎤 Invited Speakers</a></li>
        <li><a href="#awards">🏆 Awards</a></li>
        <li><a href="#4-tentative-schedule-tba">🗓️ Schedule</a></li>
        <li><a href="#5-organizers">👥 Organizers</a></li>
        <li><a href="#7-faq">❓ FAQ</a></li>
        <li><a href="#program-chairs">👥 Area Chairs and Program Chairs</a></li>
        <li><a href="#contact">📧 Contact</a></li>
      </ul>
    </div>
  </div>
</div>

</div>

<style>
body { background-color: #ffffff; }
h1 { color: #333; text-align: center; margin-top: 0.5em; margin-bottom: 1.5em; }
h2, h3, h4, h5, h6 { color: #333; }
a { color: #0366d6 !important; font-weight: bold; }
a:hover { color: #2222B2 !important; }
/* Fix header font consistency */
.site-nav .page-link { font-size: 26px !important; font-weight: 600 !important; line-height: 54px !important; }
/* Sidebar Navigation */
.sidebar-container {
  position: fixed;
  top: 100px;
  left: 20px;
  z-index: 1000;
}

.sidebar {
  width: 220px;
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  max-height: 80vh;
  overflow-y: auto;
}

.sidebar.collapsed {
  width: 0px;
  padding: 0;
  border: none;
  overflow: hidden;
}

.sidebar-toggle {
  position: absolute;
  top: 8px;
  right: 8px;
  background: #f6f8fa;
  border: 1px solid #d1d5da;
  border-radius: 4px;
  padding: 4px 8px;
  cursor: pointer;
  font-size: 12px;
  transition: all 0.2s ease;
  z-index: 1002;
}

.sidebar-toggle:hover {
  background: #e1e4e8;
}

.sidebar.collapsed .sidebar-toggle {
  position: fixed;
  top: 108px;
  left: 20px;
  right: auto;
}

.sidebar li { margin-bottom: 1px; text-align: left; }
.sidebar > div > ul > li > a { font-weight: 600; font-size: 0.9rem; padding: 1px 0; text-align: left; }
.sidebar a { color: #0366d6; text-decoration: none; transition: color 0.2s; display: block; padding: 1px 0; text-align: left; font-weight: bold; }
.sidebar a:hover { color: #2222B2; text-decoration: underline; text-align: left; }
/* Enhanced icon styles */
.highlight-icon { color: #0366d6; font-weight: bold; margin-right: 8px; font-size: 1.1em; }
.subtitle-icon { display: inline-block; width: 30px; height: 30px; vertical-align: middle; margin-right: 6px; background: none; border: 0; box-shadow: none; border-radius: 0; }
.important-dates { 
  background: linear-gradient(135deg, #f8f9ff 0%, #e8f2ff 100%); 
  padding: 20px; 
  border-radius: 12px; 
  border-left: 5px solid #0366d6; 
  margin: 20px 0; 
  box-shadow: 0 4px 12px rgba(3, 102, 214, 0.1);
}
.callout-box { 
  background: linear-gradient(135deg, #fff8e1 0%, #fff3cd 100%); 
  border: 2px solid #ffc107; 
  border-radius: 10px; 
  padding: 16px; 
  margin: 15px 0; 
  box-shadow: 0 3px 10px rgba(255, 193, 7, 0.2);
}
.topic-card {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 12px 16px;
  margin: 8px 0;
  border-left: 4px solid #0366d6;
  transition: all 0.3s ease;
}
.topic-card:hover {
  background: #e3f2fd;
  transform: translateX(5px);
}
.section-header {
  display: flex;
  align-items: center;
  margin-top: 40px;
  margin-bottom: 20px;
}.section-header h2 {
  margin: 0;
  margin-left: 10px;
}
</style>

<script>
// Simple toggle function
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('sidebar-toggle');
  
  console.log('Toggle clicked');
  
  if (sidebar.classList.contains('collapsed')) {
    sidebar.classList.remove('collapsed');
    toggleBtn.innerHTML = '◀';
    console.log('Sidebar expanded');
  } else {
    sidebar.classList.add('collapsed');
    toggleBtn.innerHTML = '▶';
    console.log('Sidebar collapsed');
  }
}

document.addEventListener("DOMContentLoaded", function() {
  console.log("DOM loaded");
  
  // Smooth scroll functionality
  const anchorLinks = document.querySelectorAll('.sidebar a[href^="#"]');
  anchorLinks.forEach(link => {
    link.addEventListener("click", function(e) {
      e.preventDefault(); // 阻止默认行为
      
      const targetId = this.getAttribute("href").substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        // 平滑滚动到目标元素
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
        
        // 更新URL（可选）
        history.pushState(null, null, "#" + targetId);
      }
    });
  });
});
</script>
<div class="banner-container">
 <div class="banner-overlay"></div>
 <div class="banner-text">
PerFM Workshop @ AAAI 2026 
Personalization for Foundation Models  
January 27, 2026
 </div>
</div>

<br>

<div class="section-header" id="news">
  <span class="highlight-icon">📢</span>
  <h2>News</h2>
</div>

- 📅 **2025-10-15**: **Deadline Extended!** Abstract submission: October 26, 2025; Paper submission: October 28, 2025
- 🎉  **2025-09-11**: Website launched and call for contributions open!
- **Submit your paper:** 🔥🔥🔥 [<span style="color: #8B0000; font-weight: bold;">OpenReview</span>](https://openreview.net/group?id=AAAI.org/2026/Workshop/PerFM){: target="_blank"}
- Welcome to join our <img src="/images/slack.png" alt="Slack" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 5px;"> [Slack workspace](https://join.slack.com/t/personalized-llm/shared_invite/zt-3de9e5pjl-iq_e9jb1cu_pYBAh1ickOA){: target="_blank"}

<div class="important-dates" style="margin-top: 1em;">
<strong>Venue & Time</strong>: January 27, 2026, 9:00–17:00 | <strong>Venue</strong>: EXPO Singapore, Level 2, <strong>Room</strong>: Peridot 201 | <strong>Poster area</strong>: WS31–WS40
</div>

<div class="section-header" id="1-workshop-introduction">
  <span class="highlight-icon">🎯</span><a id="1-workshop-introduction"></a>
  <h2>Workshop Introduction</h2>
</div>

While foundation models excel across NLP, computer vision, and multimodal tasks, they cannot capture individual user characteristics—preferences, behavioral patterns, and contextual needs—creating a disconnect between general intelligence and personalized user experience. This workshop "**Personalization in the Era of Large Foundation Models (PerFM 2026)**" will unite researchers and practitioners to explore theoretical foundations, scalable architectures, evaluation methods, lifelong learning, and ethical considerations, **shaping the next generation of AI systems that adapt to and grow with individual users.** We welcome original work, recently published work, and work-in-progress.

<div style="text-align: center; margin: 30px 0;"><a href="https://openreview.net/group?id=AAAI.org/2026/Workshop/PerFM" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: #1e3a8a !important; color: #ffffff !important; padding: 20px 45px; border-radius: 10px; text-decoration: none !important; font-weight: 700; font-size: 22px; border: none; box-shadow: 0 6px 20px rgba(30, 58, 138, 0.4); transition: all 0.3s ease; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);" onmouseover="this.style.background='#ff6b35'; this.style.color='#ffffff'; this.style.textDecoration='none';" onmouseout="this.style.background='#1e3a8a'; this.style.color='#ffffff'; this.style.textDecoration='none'; this.style.setProperty('color', '#ffffff', 'important');"><img src="/images/icon/fire.png" alt="icon" style="width: 50px; height: 50px; vertical-align: middle; margin-right: 8px; display: inline-block;">Submit Your Paper to PerFM 2026</a></div>

<div class="section-header" id="2-call-for-contributions-topics-and-scope">
  <span class="highlight-icon">📝</span>
  <h2>Call for Contributions (Topics and Scope)</h2>
</div>

We welcome submissions on topics **including but not limited to**:

<div class="topic-card">
<strong>🔬 Theoretical Foundations</strong>: Generalization and stability under personalization, user heterogeneity, multi-task and meta-learning theory, privacy–utility trade-offs.
</div>

<div class="topic-card">
<strong>🛠️ Benchmarks and Tooling</strong>: Datasets, metrics, simulators, open-source libraries, evaluation frameworks across tasks, modalities, data sources, and demographic groups.
</div>

<div class="topic-card">
<strong>🏗️ Architectures and Algorithms</strong>: Parameter-efficient tuning, preference alignment, retrieval-augmented personalization, federated and decentralized personalization, on-device adaptation, agentic personalization frameworks.
</div>

<div class="topic-card">
<strong>🧠 Memory and Lifelong Learning</strong>: Continuous user adaptation, balancing short-term contextual awareness with long-term
memory persistence, catastrophic forgetting prevention, evolving user preference modeling.
</div>

<div class="topic-card">
<strong>⚡️ Efficiency and Scalability</strong>: Computational optimization for millions of users, model compression, distributed serving, cold start strategies for new users, lightweight deployment, parameter sharing across users, cloud-edge collaborative efficiency.
</div>

<div class="topic-card">
<strong>🚀 Applications</strong>: Dialogue systems, recommendation, healthcare, education, finance, scientific discovery, time-series forecasting.
</div>

<div class="topic-card">
<strong>🛡️ Trustworthiness</strong>: Safety, robustness, fairness, algorithmic bias across demographics, transparency in personalized decisions, privacy-preserving policies for personal data collection and storage, societal implications of widespread personalized AI deployment.
</div>


<div class="section-header" id="3-submissions-and-timeline">
  <span class="highlight-icon">📅</span>
  <h2>Submissions and Timeline</h2>
</div>


<div class="important-dates" style="padding-top: 15px;">
<h3 style="margin-top: 0; margin-bottom: 15px;">⏰ Important Dates <span style="font-size: 0.8em; color: #666;">(AoE Time)</span></h3>

<ul>
<li><strong>Abstract submission deadline</strong>: <del>October 17, 2025</del> <strong style="color: #d73a49;">October 26, 2025</strong></li>
<li><strong>Paper submission deadline</strong>: <del>October 22, 2025</del> <strong style="color: #d73a49;">October 28, 2025</strong></li>
<li><strong>Author notification</strong>: <del>November 5, 2025</del> <strong style="color: #d73a49;">November 12, 2025</strong></li>
<li><strong>Camera-ready submission</strong>: TBA</li>
<li><strong>Workshop date</strong>: January 27, 2026 (at AAAI 2026)</li>
</ul>
</div>

<div class="callout-box">
<h3 style="margin-top: 0; margin-bottom: 15px;">🔥 Submission Guidelines</h3>

<ul>
<li>Use the <a href="https://aaai.org/authorkit26-1/" target="_blank">AAAI 2026 style file</a> for formatting. </li>
<li>Submissions should be PDFs of <strong>6-8 pages for full papers</strong> or <strong>2-4 pages for short/position papers</strong> (excluding references and appendices). </li>
<li><strong>Double-blind</strong> review.</li>
<li>By default, submissions are <strong>non-archival</strong>.</li>
<li>Outstanding papers will be selected for lightning talks and a best paper award will be announced at the workshop.</li>
</ul>
</div>

<div class="section-header" id="invited-speakers">
  <span class="highlight-icon">🎤</span>
  <h2>Invited Speakers (Keynotes)</h2>
</div>

<div class="speaker-card">
  <div class="speaker-photo"><img src="/images/people/Jay%20Katukuri.jpeg" alt="Jay Katukuri" width="120" height="120"></div>
  <div class="speaker-info">
    <h3><a href="https://www.linkedin.com/in/jaykatukuri" target="_blank" rel="noopener">Dr. Jay Katukuri</a></h3>
    <p><strong>Affiliation:</strong> JPMorgan Chase, Managing Director of Engineering, Head of Technology AI/ML</p>
    <p><strong>Title:</strong> Driving Personalization in Banking and Finance from Large to Small Language Models</p>
    <p><strong>Abstract:</strong> This talk explores the evolving landscape of personalization in banking and finance, driven by advancements in both large and small language models. The first part delves into how Large Language Models (LLMs) can curate rich, consumer-centric merchant knowledge graphs from diverse metadata, enabling financial institutions to deliver more relevant and insightful experiences to their customers. The second part highlights the role of Small Language Models (SLMs), demonstrating how fine-tuning with low-rank adapters can efficiently mimic individual user behaviors and preferences, paving the way for scalable, targeted personalization. By bridging the capabilities of LLMs and SLMs, this session provides a comprehensive view of how financial organizations can harness the full spectrum of language model technologies to enhance customer engagement in personalization domain.</p>
    <p><strong>Bio:</strong> Dr. Jay Katukuri is Managing Director of Engineering and Head of Technology AI/ML at JPMorgan Chase. His organization is responsible for building best-in-class omni-channel personalization experiences for Chase customers. Prior to joining JPMorgan Chase, Dr. Katukuri was Head of Personalization at Apple, where he built large-scale recommender systems for the App Store, Apple Music, Video, Books, and Podcasts, enhancing personalized discovery experiences for millions of users worldwide.</p>
  </div>
</div>

<div class="speaker-card">
  <div class="speaker-photo"><img src="/images/people/Hamed%20Zamani.jpeg" alt="Hamed Zamani" width="120" height="120"></div>
  <div class="speaker-info">
    <h3><a href="https://groups.cs.umass.edu/zamani/" target="_blank" rel="noopener">Prof. Hamed Zamani</a></h3>
    <p><strong>Affiliation:</strong> UMass Amherst, Associate Professor</p>
    <p><strong>Title:</strong> Personalizing Large Language Models</p>
    <p><strong>Abstract:</strong> Many users these days rely on Large Language Models (LLMs) to learn about topics and find the answer to their questions. In this talk, I will discuss models and evaluation methodologies for generating personalized outputs, depending on the user's preferences, history, or background knowledge. In more detail, I will first introduce three large-scale benchmarks for various LLM personalization tasks. I will later draw connections between LLM personalization and retrieval-enhanced machine learning (REML) and introduce retrieval-augmented and reasoning approaches for personalizing large language models.</p>
    <p><strong>Bio:</strong> Hamed Zamani is an Associate Professor in the Manning College of Information and Computer Sciences at the University of Massachusetts Amherst (UMass), where he serves as the Associate Director of the Center for Intelligent Information Retrieval (CIIR), one of the top academic research labs in Information Retrieval worldwide. Prior to UMass, he was a Researcher at Microsoft. His research focuses on designing and evaluating statistical and machine learning models with applications to (interactive) information access systems and retrieval-enhanced AI systems. His work has led to over 120 refereed publications in the field, in addition to a number of widely-used open-source research artifacts. His research has been recognized by a CAREER Award from NSF, Early Career Excellence in Research and Excellence in Community Engagement awards from ACM SIGIR, multiple research awards from Adobe, Amazon, Cisco, Google, and Microsoft, and multiple paper awards from SIGIR 2024, SIGIR 2023, SIGIR 2022, and CIKM 2020.</p>
  </div>
</div>

<div class="speaker-card">
  <div class="speaker-photo"><img src="/images/people/Aleks%20Farseev.webp" alt="Aleks Farseev" width="120" height="120"></div>
  <div class="speaker-info">
    <h3><a href="https://www.somin.ai" target="_blank" rel="noopener">Dr. Aleks Farseev</a></h3>
    <p><strong>Affiliation:</strong> SOMIN, Singapore, CEO</p>
    <p><strong>Title:</strong> Dynamic RAG Personalisation For the Marketing Content Ideation</p>
    <p><strong>Abstract:</strong> As generative artificial intelligence catalyzes a radical paradigm shift within the advertising industry, the research and practitioner communities are moving beyond general-purpose automation toward a sophisticated model of personalized orchestration. While dominant industry frameworks range from Meta's "black-box" automated pipelines to Google's collaborative co-creation paradigms, the true frontier of competitive advantage lies in the personalization of Large Language Models (LLMs) through dynamic Retrieval-Augmented Generation (RAG). In this keynote, Prof. Aleks Farseev examines how the evolution of advertising hinges on the ability to anchor generative outputs in high-fidelity "Content Perspectives" mined directly from brand ecosystems and competitor landscapes. By transitioning from static prompting to a dynamic RAG architecture that incorporates deep-mined Personas and latent Tensions, platforms like SOMIN demonstrate how AI can move from generic content generation to strategic "context engineering." This shift redefines the role of the marketing agency from a traditional producer of creative assets to a critical architect of AI systems - orchestrating complex workflows, curating personalized outputs, and safeguarding brand integrity through data-driven insights. Ultimately, this session argues that in an era of ubiquitous automation, the synthesis of emotional intelligence and brand-specific grounding via personalized RAG will become the definitive currency of value, transforming brand and agency marketing teams into indispensable strategic consultants and AI facilitators.</p>
    <p><strong>Bio:</strong> Prof. Aleks Farseev is a distinguished luminary in both entrepreneurship and academia. Renowned as a top-tier researcher and international keynote speaker, he stands as the driving force behind SoMonitor.ai – a cloud platform leveraging AI and Large Language Models for Competitor Analytics and Ad Optimization. His expertise shines not only as CEO but also as a Research Professor, where he adeptly imparts wisdom on Digital Marketing, Large Language Models, and AI Technology. Through courses offered in esteemed universities across the Globe and over 30 publications in top-tier conferences, Prof. Farseev ensures that the path to mastery is both accessible and enlightening.</p>
  </div>
</div>

<div class="speaker-card">
  <div class="speaker-photo"><img src="/images/people/xiangnan%20he.png" alt="Xiangnan He" width="120" height="120"></div>
  <div class="speaker-info">
    <h3><a href="https://hexiangnan.github.io/" target="_blank" rel="noopener">Prof. Xiangnan He</a></h3>
    <p><strong>Affiliation:</strong> University of Science and Technology of China, Professor</p>
    <p><strong>Title:</strong> From General to Personal: Towards LLM-based Personal Intelligence</p>
    <p><strong>Abstract:</strong> Large Language Models are increasingly becoming the central interface between people and the digital world, yet most existing systems remain fundamentally generic—optimized for the average user rather than individuals. This keynote argues for a necessary shift from general-purpose intelligence toward LLM-based personal intelligence, and articulates a unified vision built on three core pillars: user memory, personalized alignment, and continual self-evolving. I contend that this transition is essential for enabling AI systems that can understand users, adapt over time, and ultimately realize personal intelligence for everyone.</p>
    <p><strong>Bio:</strong> Xiangnan He is a Professor at the School of Artificial Intelligence, University of Science and Technology of China (USTC). His research focuses on recommendation systems, information retrieval and mining, large language models and general artificial intelligence. He has published over 100 papers in leading conferences and journals, including SIGIR, ICLR, NeurIPS, WWW, KDD, IEEE TKDE, and ACM TOIS, and his work has received more than 70,000 citations on Google Scholar. He is an Elsevier China Highly Cited Researcher and a recipient of multiple international and national research awards, including the ACM SIGIR Best Paper Award, the ICLR Best Paper Award, and the Wu Wenjun Artificial Intelligence Natural Science First Prize. He serves as an Associate Editor for several top journals, including IEEE TKDE, IEEE TBD, ACM TOIS, etc., and senior PC member for conferences including SIGIR, WWW, KDD, MM, etc.</p>
  </div>
</div>

<div class="speaker-card">
  <div class="speaker-photo"><img src="/images/people/quanyu%20dai.jpeg" alt="Quanyu Dai" width="120" height="120"></div>
  <div class="speaker-info">
    <h3><a href="https://scholar.google.com/citations?user=Q1GGOPoAAAAJ&hl=en" target="_blank" rel="noopener">Dr. Quanyu Dai</a></h3>
    <p><strong>Affiliation:</strong> Huawei Foundation Model Department, Senior Researcher</p>
    <p><strong>Title:</strong> Empowering Personal AI Assistants with Socially Intelligent LLMs: Exploration and Future Directions</p>
    <p><strong>Abstract:</strong> Social intelligence in Large Language Models (LLMs) is a core foundational capability for personal AI assistants. It enables assistants to understand user intentions and emotions within complex social contexts, make rational decisions accordingly, and provide personalized and empathetic services, thereby significantly enhancing the human-computer interaction experience. The realization of effective social intelligence primarily relies on two key technologies: first, long-term memory, which encompasses efficient storage, precise retrieval, and dynamic updating of information; and second, social reasoning, which involves a deep understanding of users and scenarios as well as rational decision-making in multi-turn interactions. This report first analyzes the current state of social intelligence in LLMs, revealing the limitations of existing models as the backbone for personal assistants. Subsequently, it shares our explorations in enhancing these capabilities from the perspectives of long-term memory and social reasoning. Finally, the report concludes by proposing several open questions worthy of further exploration based on industrial practices.</p>
    <p><strong>Bio:</strong> Quanyu Dai is a Senior Researcher at the Huawei Foundation Model Department. He received his Bachelor's degree from Shanghai Jiao Tong University and his Ph.D. from The Hong Kong Polytechnic University. His primary research interests include Large Foundation Models, LFM-based agents, and recommender systems. His research achievements have been successfully deployed across multiple scenarios of Huawei terminal business, serving hundreds of millions of users. He has published over 60 academic papers in top-tier AI conferences and journals, such as NeurIPS, KDD, WWW, ACL, TKDE, and TOIS, and serves as a long-standing reviewer for these prestigious venues.</p>
  </div>
</div>

<div class="speaker-card">
  <div class="speaker-photo speaker-photo-contained"><img src="/images/people/yulan%20he.jpeg" alt="Yulan He" width="120" height="120"></div>
  <div class="speaker-info">
    <h3><a href="https://sites.google.com/view/yulanhe/home" target="_blank" rel="noopener">Prof. Yulan He</a></h3>
    <p><strong>Affiliation:</strong> King's College London, UK, Professor</p>
    <p><strong>Title:</strong> Many Minds: Rethinking LLM Personalisation</p>
    <p><strong>Abstract:</strong> Large language models (LLMs) are trained on the collective knowledge of the internet, but they are used to serve billions of individual users. Recent years witness increasing interests in adapting population-level LLMs to accommodate the diverse goals, preferences, and contexts of individual users. To build personalised LLMs, we need models that can maintain memory over time, learn from sparse and heterogeneous personal data, and align with what each user values. In this talk, I will compare three strategies for doing this, retrieval-based prompting, model adaptation, and preference-based alignment, and illustrate each through examples from our group's recent work. I will conclude by discussing open challenges and potential directions for the future of personalised LLM research.</p>
    <p><strong>Bio:</strong> Yulan He is a Professor in Natural Language Processing at King's College London and a Turing AI Fellow. Her research focuses on addressing the limitations of Large Language Models (LLMs), aiming to improve their reasoning capabilities, robustness, and explainability. She has published over 300 papers on topics such as self-evolution of LLMs, mechanistic interpretability, and LLMs for educational assessment and health. She received several prizes and awards for her research, including an SWSA Ten-Year Award, a CIKM Test-of-Time Award, and was recognised as an inaugural Highly Ranked Scholar by ScholarGPS. She served as the General Chair for AACL-IJCNLP 2022 and a Program Co-Chair for various conferences such as ECIR 2024, CCL 2024, and EMNLP 2020.</p>
  </div>
</div>

<style>
.speaker-card {
  display: flex;
  gap: 24px;
  align-items: flex-start;
  background: #f8f9fa;
  border-radius: 10px;
  border-left: 4px solid #0366d6;
  padding: 20px 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.speaker-photo {
  flex-shrink: 0;
  width: 120px;
  height: 120px;
  overflow: hidden;
  border-radius: 50%;
}
.speaker-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 50%;
}
.speaker-photo-contained {
  background: #e8e8e8;
}
.speaker-photo-contained img {
  object-fit: contain;
}
.speaker-info { flex: 1; min-width: 0; }
.speaker-card h3 { margin-top: 0; margin-bottom: 12px; color: #333; }
.speaker-card p { margin: 8px 0; line-height: 1.6; }
</style>

<div class="section-header" id="awards">
  <span class="highlight-icon">🏆</span>
  <h2>Awards</h2>
</div>

<p><strong>Best Paper</strong></p>
<ul class="award-list">
  <li><strong>Title:</strong> Not All Clients Are Equal: Collaborative Model Personalization on Heterogeneous Multi-Modal Clients<br><strong>Author:</strong> Minhyuk Seo, Taeheon Kim, Hankook Lee, Jonghyun Choi, Tinne Tuytelaars</li>
</ul>

<p><strong>Outstanding Papers</strong></p>
<ul class="award-list">
  <li><strong>Title:</strong> Taxonomy-Adaptive Moderation Model with Robust Guardrails for Large Language Models<br><strong>Author:</strong> Mahesh Kumar Nandwana, Youngwan Lim, Joseph Liu, Alex Yang, Varun Notibala, Nishchaie Khanna</li>
  <li><strong>Title:</strong> Federated Agent Reinforcement Learning<br><strong>Author:</strong> Canyu Chen, Kangyu Zhu, Zhaorun Chen, Zhanhui Zhou, Shizhe Diao, Yiping Lu, Tian Li, Manling Li, Dawn Song</li>
  <li><strong>Title:</strong> Drift No More? Context Equilibria in Multi-Turn LLM Interactions<br><strong>Author:</strong> Vardhan Dongre, Ryan A. Rossi, Viet Dac Lai, David Seunghyun Yoon, Dilek Hakkani-Tür, Trung Bui</li>
  <li><strong>Title:</strong> Dynamic Orthogonal Continual Fine-tuning for Mitigating Catastrophic Forgetting of LLMs<br><strong>Author:</strong> Zhixin Zhang, Zeming Wei, Meng Sun</li>
  <li><strong>Title:</strong> Generative Archetype-Grounded Item Representations for Sequential Recommendation<br><strong>Author:</strong> Yifan Li, Jiahong Liu, Xinni Zhang, Yankai Chen, Hao Chen, Wenhao Yu, Jianting Chen, Irwin King</li>
</ul>

<style>
.award-list { list-style: none; padding-left: 0; margin: 0.5em 0 1.5em 0; }
.award-list li {
  background: linear-gradient(135deg, #f8f9ff 0%, #f0f4ff 100%);
  border-left: 4px solid #0366d6;
  padding: 10px 14px;
  margin-bottom: 8px;
  border-radius: 0 8px 8px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
</style>

<div class="section-header" id="4-tentative-schedule-tba">
  <span class="highlight-icon">🗓️</span>
  <h2>Schedule</h2>
</div>

<h3>Workshop Timetable</h3>

| Time | Session |
|------|--------|
| **MORNING SESSION** | |
| 09:00–09:10 | Opening Remarks & Welcome |
| 09:10–09:50 | Keynote: Dr. Jay Katukuri (JPMorgan Chase, CTO – AI/ML) |
| 09:50–10:30 | Keynote: Prof. Hamed Zamani (UMass, Associate Professor) |
| 10:30–11:00 | Coffee Break & Morning Poster Session |
| 11:00–12:00 | Oral Presentations Session 1 |
| 12:00–12:30 | Keynote: Dr. Aleks Farseev (SOMIN, CEO) |
| 12:30–14:00 | Lunch Break |
| **AFTERNOON SESSION** | |
| 14:00–14:30 | Keynote: Prof. Xiangnan He (USTC, Professor) |
| 14:30–15:00 | Keynote: Dr. Quanyu Dai (Huawei, Senior Researcher) |
| 15:00–15:30 | Oral Presentations Session 2 |
| 15:30–16:00 | Coffee Break & Afternoon Poster Session |
| 16:00–16:40 | Keynote: Prof. Yulan He (KCL) |
| 16:40–17:00 | Award Ceremony & Closing Remarks |

<h3>Oral Presentations</h3>

**Session 1 (11:00–12:00)**

| Time | Title | Authors |
|------|-------|--------|
| 11:00–11:15 | Not All Clients Are Equal: Collaborative Model Personalization on Heterogeneous Multi-Modal Clients | Minhyuk Seo, Taeheon Kim, Hankook Lee, Jonghyun Choi, Tinne Tuytelaars |
| 11:15–11:30 | Taxonomy-Adaptive Moderation Model with Robust Guardrails for Large Language Models | Mahesh Kumar Nandwana, Youngwan Lim, Joseph Liu, Alex Yang, Varun Notibala, Nishchaie Khanna |
| 11:30–11:45 | Federated Agent Reinforcement Learning | Canyu Chen, Kangyu Zhu, Zhaorun Chen, Zhanhui Zhou, Shizhe Diao, Yiping Lu, Tian Li, Manling Li, Dawn Song |
| 11:45–12:00 | Drift No More? Context Equilibria in Multi-Turn LLM Interactions | Vardhan Dongre, Ryan A. Rossi, Viet Dac Lai, David Seunghyun Yoon, Dilek Hakkani-Tür, Trung Bui |

**Session 2 (15:00–15:30)**

| Time | Title | Authors |
|------|-------|--------|
| 15:00–15:15 | Dynamic Orthogonal Continual Fine-tuning for Mitigating Catastrophic Forgetting of LLMs | Zhixin Zhang, Zeming Wei, Meng Sun |
| 15:15–15:30 | Generative Archetype-Grounded Item Representations for Sequential Recommendation | Yifan Li, Jiahong Liu, Xinni Zhang, Yankai Chen, Hao Chen, Wenhao Yu, Jianting Chen, Irwin King |

<h3>Poster Sessions</h3>

**Morning Poster Session (10:30–11:00)**

| Title | Authors |
|-------|--------|
| Preference Descriptions for Dynamic Personalization of Large Language Models | Naofumi Osawa |
| A Unified Framework for Prompt Privacy is Elusive and Misleading | Prakhar Ganesh, Yash More, Marco Romanelli, Ferdinando Fioretto, Golnoosh Farnadi |
| PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM | Siqi Liang, Yudi Zhang, Yue Guo |
| Enhancing Serendipity Recommendation System by Constructing Dynamic User Knowledge Graphs with Large Language Models | Qian Yong, Yanhui Li, Jialiang Shi, Yaguang Dou, Tian Qi |
| Domain-Specific LLM Adaptation: Bridging Personalization and Efficiency Through Synthetic Data and Optimization | Iman Abbasnejad, Brett Tully, Wei Zhou, Tomal Deb, Sheldon Liu, Xuefeng Liu, Warren Wei |
| Structured Personalization: Modeling Constraints as Matroids for Data-Minimal LLM Agents | Daniel Platnick, Marjan Alirezaie, Hossein Rahnama |
| LOOM: Personalized Learning Informed by Daily LLM Conversations Toward Long-Term Mastery via a Dynamic Learner Memory Graph | Justin Cui, Kevin Pu, Tovi Grossman |
| ShapLoRA: Allocation of Low-rank Adaption on Large Language Models via Shapley Value Inspired Importance Estimation | Yi Zhao, Wei Zhu |
| Personalization of Large Foundation Models for Health Interventions | Stefan Konigorski, Johannes E. Vedder, Babajide Alamu Owoyele, İbrahim Özkan |
| ATLAS: User-Side Personalization and Privacy Protection Against Geolocation Risks in Large Vision–Language Models | Kelvin Yuxiang Huang, Qingyun Wang, Yi R. Fung, Yue Xiao |
| Controlled Text Generation of DLLMs with Efficient Classifier Guidance | Zhuo Cao, Xuanyi Xie, Qingyan Wei, Jiawang Zhao |

**Afternoon Poster Session (15:30–16:00)**

| Title | Authors |
|-------|--------|
| LENS: Learning Architecture Navigator for LLM Agentic Systems | Guancheng Wan, Jiayi Yang, Mengting Li, Eric Hanchen Jiang, Haixin Wang, Hui Yi Leong, Yizhou Sun, Wei Wang |
| Lightweight Inference-Time Personalization for Frozen Knowledge Graph Embeddings | Cerag Oguztuzun, Ozan Oguztuzun |
| FinPerF: Dynamic User Profiling for Personalized Financial News Recommendation | Kristina Lewandowska |
| T-REX: Transformer-based Category Sequence Generation for Grocery Basket Recommendation | Soroush Mokhtari, Muhammad Tayyab Asif, Sergiy Zubatiy |
| Mitigating Conversational Amnesia in Tutoring Agents via Hybrid Memory and Offline Consolidation | Luoxiao Yang |
| Hybrid Detection of Machine-Generated Texts in Academic Contexts | Viacheslav Shalamov, Korniliev Artemiy, Ilya Astafjev, Valeria Efimova |
| PolyLingua: Margin-based Inter-class Transformer for Robust Cross-domain Language Detection | Ali Lotfi Rezaabad, Bikram Khanal, Shashwat Chaurasia, Lu Zeng, Dezhi Hong, Hossein Bashashati, Thomas Butler, Megan Ganji |
| BiasJailbreak: Analyzing Ethical Biases and Jailbreak Vulnerabilities in Large Language Models | Isack Lee, Haebin Seong |
| SCALE: Upscaled Continual Learning of Large Language Models | Jin-woo Lee, Junhwa Choi, Bongkyu Hwang, Jinho Choo, Bogun Kim, JeongSeon Yi, Joonseok Lee, DongYoung Jung, Jaeseon Park, Kyoungwon Park, Suk-hoon Jung |
| Enhancing Human-Like Responses in Large Language Models | Ethem Yağız Çalık, Talha Rüzgar Akkuş |
| Tiny Personal Critic: A Lightweight Critic for Low-Compute Personalization | Aditya Singh, M Ganesh Kumar |
| Learning Without Forgetting: Preserving Reasoning Capabilities in LLMs via Structural Orthogonality | Mustafa Hayri Bilgin, Mariam Barry, Albert Bifet, Azzedine Ait Said, Soumya Banerjee |

<div class="section-header" id="5-organizers">
  <span class="highlight-icon">👥</span>
  <h2>Organizers</h2>
</div>

<table>
 <tr>
  <td> 
 <img src="/images/people/jiahong.jpg" alt="1" width=200px height=200px><br/>
 <a href="https://misc-lab.cse.cuhk.edu.hk/sciencex_teams/jiahong-liu/" target="_blank" rel="noopener noreferrer">Jiahong Liu</a><br/>
 CUHK
 </td>
   <td> 
 <img src="/images/people/zhangyang.jpg" alt="1" width=200px height=200px><br/>
 <a href="http://home.ustc.edu.cn/~zy2015/" target="_blank" rel="noopener noreferrer">Yang Zhang</a><br/>
 NUS
 </td>
    <td> 
 <img src="/images/people/weizhi.jpg" alt="1" width=200px height=200px><br/>
 <a href="https://davidzwz.github.io/" target="_blank" rel="noopener noreferrer">Weizhi Zhang</a><br/>
 UIC
 </td>
    <td> 
 <img src="/images/people/runcong.png" alt="1" width=200px height=200px><br/>
 <a href="https://sites.google.com/view/runcongzhao/home" target="_blank" rel="noopener noreferrer">Runcong Zhao</a><br/>
 KCL
 </td>
    <td> 
 <img src="/images/people/lucas.png" alt="1" width=200px height=200px><br/>
 <a href="https://www.lucasvinhtran.com/" target="_blank" rel="noopener noreferrer">Lucas Vinh Tran</a><br/>
 JPMorganChase
 </td>
 </tr> 
</table>

<div class="section-header" id="6-invited-speakers-and-panelists">
  <span class="highlight-icon">👥</span>
  <h2>Advisory Committee</h2>
</div>

<table>
 <tr>
  <td> 
 <img src="/images/people/irwin.jpg" alt="1" width=200px height=200px><br/>
 <a href="https://www.cse.cuhk.edu.hk/irwin.king/" target="_blank" rel="noopener noreferrer">Irwin King</a><br/>
 CUHK
 </td>
   <td> 
 <img src="/images/people/chuats.jpg" alt="1" width=200px height=200px><br/>
 <a href="https://www.chuatatseng.com/" target="_blank" rel="noopener noreferrer">Tat-Seng Chua</a><br/>
 NUS
 </td>
    <td> 
 <img src="/images/people/philip.png" alt="1" width=200px height=200px><br/>
 <a href="https://cs.uic.edu/profiles/philip-yu/" target="_blank" rel="noopener noreferrer">Philip S. Yu</a><br/>
 UIC
 </td>
 </tr> 
</table>

<div class="section-header" id="program-chairs">
  <span class="highlight-icon">👥</span>
  <h2>Area Chairs and Program Chairs</h2>
</div>

<ul class="ack-list">
  <li>Yali Fu (JLU, China)</li>
  <li>Zhihao Wu (KCL, UK)</li>
  <li>Tianyi Yao (Microsoft, US)</li>
  <li>Yaozu Wu (UTokyo, Japan)</li>
  <li>Raghav Sharma (Workday, US)</li>
  <li>Hins Hu (Cornell, US)</li>
  <li>Ramasubramanian Balasubramanian (LinkedIn, US)</li>
  <li>Yuyao Yang (UIC, US)</li>
  <li>Zeyu Zhang (RUC, China)</li>
  <li>Bodhisatta Maiti (Home Depot, US)</li>
  <li>Rajendra Ugrani (Meta, US)</li>
  <li>Wei-Chieh Huang (UIC, US)</li>
  <li>Dipanwita Guhathakurta (IBM, US)</li>
  <li>Deep Shah (Google, US)</li>
  <li>Twinkle Joshi (IQGeo, Canada)</li>
  <li>Ketan Thakkar (LinkedIn, US)</li>
  <li>Jeyadev Needhidevan (NYU, US)</li>
  <li>Yilun Qiu (NUS, Singapore)</li>
  <li>Chengyu Cao (HIT, China)</li>
  <li>Huanhuan Ma (UIC, US)</li>
  <li>Yifan Li (CUHK, Hong Kong SAR)</li>
  <li>Jieyong Kim (Yonsei, South Korea)</li>
  <li>Menglin Yang (HKUST(GZ), China)</li>
  <li>Xiaoyan Zhao (CUHK, Hong Kong SAR)</li>
  <li>Wenhao Yu (CUHK, Hong Kong SAR)</li>
  <li>Italo Luis da Silva (KCL, UK)</li>
  <li>Liangwei Yang (UIC, US)</li>
  <li>Qinglin Zhu (KCL, UK)</li>
  <li>Dongha Lee (Yonsei, South Korea)</li>
</ul>

<div class="section-header" id="7-faq">
  <span class="highlight-icon">❓</span>
  <h2>FAQ</h2>
</div>

**🤔 Can I attend virtually?**  
TBA.

**📚 What does non-archival mean?**  
Non-archival means the submissions are not formally published in proceedings.

<div class="section-header" id="contact">
  <span class="highlight-icon">📧</span>
  <h2>Contact</h2>
</div>

Feel free to contact us: 📧 **personalizationllm@outlook.com** or <img src="/images/slack.png" alt="Slack" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 5px;"> [Slack workspace](https://join.slack.com/t/personalized-llm/shared_invite/zt-3de9e5pjl-iq_e9jb1cu_pYBAh1ickOA){: target="_blank"}

