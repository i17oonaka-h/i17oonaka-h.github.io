---
page_id: teaching
layout: page
permalink: /teaching/
title: Education/Experience
description: 
nav: true
nav_order: 6
---

<div class="timeline">

<h2>🎓 Education</h2>

<div class="education-section">
  
  <div class="education-item current">
    <div class="year-range">2024.04 — Present</div>
    <div class="institution">
      <h3>NAIST (Nara Institute of Science and Technology)</h3>
      <div class="degree">Graduate School of Science and Technology, Information Science (Master's Course)</div>
      <div class="details">
        <span class="lab">🔬 Laboratory: Intelligent Robot Dialogue lab. (RIKEN)</span>
        <span class="supervisor">👨‍🏫 Supervisor: Prof. Koichiro Yoshino</span>
      </div>
    </div>
  </div>

  <div class="education-item">
    <div class="year-range">2022.04 — 2024.03</div>
    <div class="institution">
      <h3>NITTC (National Institute of Technology, Tokuyama College)</h3>
      <div class="degree">Advanced Course, Computer Science and Electronic Engineering</div>
      <div class="details">
        <span class="lab">🔬 Laboratory: Miyazaki-lab</span>
        <span class="supervisor">👨‍🏫 Supervisor: Prof. Ryoichi Miyazaki</span>
      </div>
    </div>
  </div>

  <div class="education-item">
    <div class="year-range">2017.04 — 2022.03</div>
    <div class="institution">
      <h3>NITTC (National Institute of Technology, Tokuyama College)</h3>
      <div class="degree">Regular Course, Computer Science and Electronic Engineering</div>
      <div class="details">
        <span class="lab">🔬 Laboratory: Miyazaki-lab</span>
        <span class="supervisor">👨‍🏫 Supervisor: Prof. Ryoichi Miyazaki</span>
      </div>
    </div>
  </div>

</div>

<h2>💼 Professional Experience</h2>

<div class="experience-section">

  <div class="experience-item current">
    <div class="period">
      <span class="dates">2024.12 — Present</span>
      <span class="type">Part-time</span>
    </div>
    <div class="company">
      <h3>🏢 LY Corporation R&D</h3>
      <div class="mentors">👥 Mentors: Yuma Shirahata, Masaya Kawamura</div>
    </div>
    <div class="projects">
      <div class="project">
        <h4>📝 Theme 1:</h4>
        <p>Improving phonemic and prosodic annotation model for text-to-speech and its sub-task</p>
        <span class="status accepted">✅ Accepted to Interspeech 2025</span>
      </div>
      <div class="project">
        <h4>📝 Theme 2:</h4>
        <p>Neural Vocoder towards High-Quality Speech Generation from SSL features</p>
        <span class="status accepted">✅ Accepted to ICASSP 2026</span>
      </div>
      <div class="project">
        <h4>📝 Theme 3:</h4>
        <p>Work in progress...</p>
        <span class="status ongoing">🚧 In Progress</span>
      </div>
    </div>
  </div>

  <div class="experience-item upcoming">
    <div class="period">
      <span class="dates">2025.02 — 2025.03</span>
      <span class="type">Internship (3 weeks)</span>
    </div>
    <div class="company">
      <h3>🏢 NTT Communication Science Laboratories</h3>
      <div class="mentors">👥 Mentor: Takatomo Kano</div>
    </div>
    <div class="projects">
      <div class="project">
        <h4>📝 Research Theme:</h4>
        <p>Post-refinement of ASR hypotheses for joint multi-channel distant speech recognition</p>
      </div>
    </div>
  </div>

  <div class="experience-item">
    <div class="period">
      <span class="dates">2024.08 — 2024.10</span>
      <span class="type">Internship (8 weeks)</span>
    </div>
    <div class="company">
      <h3>🏢 LY Corporation R&D</h3>
      <div class="mentors">👥 Mentors: Yuma Shirahata, Ryuichi Yamamoto</div>
    </div>
    <div class="projects">
      <div class="project">
        <h4>📝 Research Theme:</h4>
        <p>Improving phonemic and prosodic annotation model for text-to-speech and its sub-task</p>
        <span class="status accepted">✅ Accepted to Interspeech 2025</span>
      </div>
    </div>
  </div>

  <div class="experience-item">
    <div class="period">
      <span class="dates">2022.06 — 2022.07</span>
      <span class="type">Internship (8 weeks)</span>
    </div>
    <div class="company">
      <h3>🏢 The University of Tokyo</h3>
      <div class="department">Saruwatari & Koyama Laboratory</div>
      <div class="mentors">👥 Mentors: Shinnosuke Takamichi, Keisuke Imoto</div>
    </div>
    <div class="projects">
      <div class="project">
        <h4>📝 Research Theme:</h4>
        <p>Environmental Sound Synthesis from Visual Onomatopoeia</p>
        <span class="status accepted">✅ Accepted to ICASSP 2023</span>
      </div>
    </div>
  </div>

</div>

</div>

<style>
.timeline {
  max-width: 1000px;
  margin: 0 auto;
}

.education-section, .experience-section {
  margin: 2rem 0;
}

.education-item, .experience-item {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-left: 4px solid #007bff;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.education-item:hover, .experience-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
}

.education-item.current, .experience-item.current {
  border-left-color: #28a745;
  background: linear-gradient(135deg, #e8f5e8 0%, #ffffff 100%);
}

.experience-item.upcoming {
  border-left-color: #ffc107;
  background: linear-gradient(135deg, #fff3cd 0%, #ffffff 100%);
}

.year-range, .period .dates {
  font-weight: 600;
  color: #007bff;
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
  display: inline-block;
}

.period {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.8rem;
}

.type {
  background: #e9ecef;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 500;
  color: #495057;
}

.institution h3, .company h3 {
  color: #2c3e50;
  margin: 0.5rem 0;
  font-size: 1.3rem;
  font-weight: 700;
}

.degree, .department {
  color: #6c757d;
  font-style: italic;
  margin-bottom: 0.8rem;
  font-size: 1rem;
}

.details, .mentors {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  margin-top: 0.8rem;
}

.lab, .supervisor, .mentors {
  color: #495057;
  font-size: 0.9rem;
}

.projects {
  margin-top: 1rem;
}

.project {
  background: rgba(255, 255, 255, 0.7);
  border-radius: 6px;
  padding: 1rem;
  margin: 0.8rem 0;
  border: 1px solid #e9ecef;
}

.project h4 {
  color: #495057;
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
  font-weight: 600;
}

.project p {
  margin: 0.5rem 0;
  color: #6c757d;
  line-height: 1.5;
}

.status {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 500;
  margin-top: 0.5rem;
}

.status.accepted {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.status.ongoing {
  background: #fff3cd;
  color: #856404;
  border: 1px solid #ffeaa7;
}

@media (max-width: 768px) {
  .education-item, .experience-item {
    padding: 1rem;
    margin: 1rem 0;
  }
  
  .period {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .details, .mentors {
    flex-direction: column;
  }
}
</style>

