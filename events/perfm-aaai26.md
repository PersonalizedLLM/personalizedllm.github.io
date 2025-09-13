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
        <li><a href="#4-tentative-schedule-tba">🗓️ Schedule</a></li>
        <li><a href="#5-organizers">👥 Organizers</a></li>
        <li><a href="#6-invited-speakers-and-panelists">🎤 Invited Speakers</a></li>
        <li><a href="#7-faq">❓ FAQ</a></li>
        <li><a href="#contact">📧 Contact</a></li>
        <li><a href="#8-sponsors-tba">🏢 Sponsors</a></li>
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

- 🎉  **2025-09-11**: Website launched and call for contributions open!
- **Submit your paper:** 🔥🔥🔥 [<span style="color: #8B0000; font-weight: bold;">OpenReview</span>](https://openreview.net/group?id=AAAI.org/2026/Workshop/PerFM){: target="_blank"}
- Welcome to join our <img src="/images/slack.png" alt="Slack" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 5px;"> [Slack workspace](https://join.slack.com/t/personalized-llm/shared_invite/zt-3de9e5pjl-iq_e9jb1cu_pYBAh1ickOA){: target="_blank"}

<div class="section-header" id="1-workshop-introduction">
  <span class="highlight-icon">🎯</span><a id="1-workshop-introduction"></a>
  <h2>Workshop Introduction</h2>
</div>

While foundation models excel across NLP, computer vision, and multimodal tasks, they cannot capture individual user characteristics—preferences, behavioral patterns, and contextual needs—creating a disconnect between general intelligence and personalized user experience. This workshop "**Personalization in the Era of Large Foundation Models (PerFM 2026)**" will unite researchers and practitioners to explore theoretical foundations, scalable architectures, evaluation methods, lifelong learning, and ethical considerations, **shaping the next generation of AI systems that adapt to and grow with individual users.** We welcome original work, recently published work, and work-in-progress.

<div style="text-align: center; margin: 30px 0;"><a href="https://openreview.net/group?id=AAAI.org/2026/Workshop/PerFM" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: #1e3a8a !important; color: #ffffff !important; padding: 20px 45px; border-radius: 10px; text-decoration: none !important; font-weight: 700; font-size: 22px; border: none; box-shadow: 0 6px 20px rgba(30, 58, 138, 0.4); transition: all 0.3s ease; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);" onmouseover="this.style.background='#ff6b35'; this.style.color='#ffffff'; this.style.textDecoration='none';" onmouseout="this.style.background='#1e3a8a'; this.style.color='#ffffff'; this.style.textDecoration='none'; this.style.setProperty('color', '#ffffff', 'important');">🔥 Submit Your Paper to PerFM 2026</a></div>

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
<li><strong>Abstract submission deadline</strong>: October 17, 2025</li>
<li><strong>Paper submission deadline</strong>: October 22, 2025</li>
<li><strong>Author notification</strong>: November 5, 2025</li>
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


  <!-- <span class="highlight-icon"></span> -->
  <h2><span class="highlight-icon">🗓️</span>Tentative Schedule (TBA)</h2>

<!-- Example schedule; uncomment and edit when ready.
- 8:30–8:50 AM: Poster setup
- 8:50–9:00 AM: Opening remarks
- 9:00–9:50 AM: Invited talk 1
- 9:50–10:40 AM: Invited talk 2
- 10:40–11:30 AM: Invited talk 3
- 11:30–11:50 AM: Discussions and coffee break
- 11:50–12:55 PM: Poster session
- 12:55–1:30 PM: Lunch break
- 1:30–2:20 PM: Invited talk 4
- 2:20–3:10 PM: Invited talk 5
- 3:10–4:00 PM: Invited talk 6
- 4:00–4:50 PM: Contributed talks
- 4:50–5:30 PM: Panel discussions
-->

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


<div class="section-header" id="7-faq">
  <span class="highlight-icon">🎤</span>
  <h2>Invited Speakers and Panelists (TBA)</h2>
</div>

| Speaker | Affiliation |
|---|---|
| TBA | TBA |

<div class="section-header" id="contact">
  <span class="highlight-icon">❓</span>
  <h2>FAQ</h2>
</div>

**🤔 Can I attend virtually?**  
TBA.

**📚 What does non-archival mean?**  
Non-archival means the submissions are not formally published in proceedings.

<div class="section-header" id="8-sponsors-tba">
  <span class="highlight-icon">📧</span>
  <h2>Contact</h2>
</div>

Feel free to contact us: **personalizationllm@outlook.com** or <img src="/images/slack.png" alt="Slack" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 5px;"> [Slack workspace](https://join.slack.com/t/personalized-llm/shared_invite/zt-3de9e5pjl-iq_e9jb1cu_pYBAh1ickOA){: target="_blank"}

<div class="section-header" id="news">
  <span class="highlight-icon">🏢</span>
  <h2>Sponsors (TBA)</h2>
</div>

We welcome sponsorship inquiries. Please contact the organizers.
