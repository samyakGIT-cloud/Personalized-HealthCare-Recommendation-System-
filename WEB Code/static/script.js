/* ============================================================
   MediCare AI — Frontend Script
   ============================================================ */

'use strict';

/* ── Navbar scroll effect ── */
(function () {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 20);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

/* ── Mobile menu ── */
(function () {
  const btn  = document.querySelector('.nav-hamburger');
  const menu = document.querySelector('.nav-mobile-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  menu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      menu.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
})();

/* ── Toggle pills (symptom checkboxes) ── */
(function () {
  document.querySelectorAll('.toggle-pill').forEach(pill => {
    const input = pill.querySelector('input[type=checkbox]');
    if (!input) return;
    const refresh = () => pill.classList.toggle('active', input.checked);
    input.addEventListener('change', refresh);
    refresh();
  });
})();

/* ── Age range slider ── */
(function () {
  const slider = document.getElementById('ageSlider');
  const display = document.getElementById('ageDisplay');
  if (!slider || !display) return;
  const update = () => {
    display.textContent = slider.value;
    const pct = (slider.value - slider.min) / (slider.max - slider.min);
    slider.style.background = `linear-gradient(to right, var(--accent) ${pct*100}%, var(--bg-3) ${pct*100}%)`;
  };
  slider.addEventListener('input', update);
  update();
})();

/* ── SVG Arc gradient def (inject once) ── */
(function () {
  const ns = 'http://www.w3.org/2000/svg';
  const defs = document.createElementNS(ns, 'defs');
  defs.innerHTML = `
    <linearGradient id="arcGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>`;
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('width', '0'); svg.setAttribute('height', '0');
  svg.style.position = 'absolute';
  svg.appendChild(defs);
  document.body.appendChild(svg);
})();

/* ── Notification toast ── */
function showNotification(msg, duration = 3500) {
  let el = document.getElementById('globalNotification');
  if (!el) {
    el = document.createElement('div');
    el.id = 'globalNotification';
    el.className = 'notification';
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.classList.add('show');
  clearTimeout(el._timer);
  el._timer = setTimeout(() => el.classList.remove('show'), duration);
}

/* ── Animate confidence arc ── */
function animateArc(svgEl, pct) {
  const fill = svgEl.querySelector('.arc-fill');
  const label = svgEl.querySelector('.arc-pct');
  const circumference = 220;
  const offset = circumference - (pct / 100) * circumference;
  requestAnimationFrame(() => {
    fill.style.strokeDashoffset = offset;
    if (label) {
      let current = 0;
      const target = Math.round(pct);
      const step = () => {
        current = Math.min(current + Math.ceil(target / 40), target);
        label.textContent = current + '%';
        if (current < target) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }
  });
}

/* ── Animate bar widths ── */
function animateBar(el, pct) {
  requestAnimationFrame(() => { el.style.width = pct + '%'; });
}

/* ── Risk badge HTML ── */
function riskBadge(risk) {
  const map = {
    low:    { cls: 'risk-low',    label: 'Low Risk' },
    medium: { cls: 'risk-medium', label: 'Medium Risk' },
    high:   { cls: 'risk-high',   label: 'High Risk' },
  };
  const r = map[risk] || map.medium;
  return `<span class="risk-badge ${r.cls}">${r.label}</span>`;
}

/* ── Build medicines HTML ── */
function buildMedicineList(items) {
  if (!items || !items.length) return '<p style="color:var(--text-3);font-size:13px;">No medicines data available.</p>';
  return items.map((m, i) => {
    const emoji = m.match(/^([\u{1F300}-\u{1FFFF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]|\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDE4F]|\uD83D[\uDE80-\uDEFF]|[💊💉💧🍬🆘🧂])/u)?.[0] || '💊';
    const text = m.replace(/^[^\w]+/, '').trim();
    return `<div class="pill-item" style="animation-delay:${i*0.06}s">
      <span class="pill-emoji">${emoji}</span>
      <span>${text}</span>
    </div>`;
  }).join('');
}

/* ── Build advice HTML ── */
function buildAdviceList(items) {
  if (!items || !items.length) return '';
  return items.map((a, i) => {
    const emoji = a.match(/^([\u{1F300}-\u{1FFFF}]|🛏️|💧|🏠|🤧|🌡️|📞|🚭|💨|🏃|📊|🆘|💊|🍽️|👣|💉|🚨|🧂|😌|⚖️|🚫|🔄|☕|🍯|⏱️|🔬|🧠|🩺|🥗|❤️|🌊)/u)?.[0] || '✅';
    const text = a.replace(/^[^\w]+/, '').trim();
    return `<div class="pill-item" style="animation-delay:${i*0.06}s">
      <span class="pill-emoji">${emoji}</span>
      <span>${text}</span>
    </div>`;
  }).join('');
}

/* ── Build top-5 predictions HTML ── */
function buildTopPredictions(top5) {
  if (!top5 || !top5.length) return '';
  return top5.map((p, i) => `
    <div class="pred-row" style="animation-delay:${i*0.08}s">
      <span class="pred-rank">#${i+1}</span>
      <span class="pred-name">${p.disease}</span>
      <div class="pred-bar-track">
        <div class="pred-bar-fill" data-pct="${p.confidence}" style="width:0"></div>
      </div>
      <span class="pred-pct">${p.confidence.toFixed(1)}%</span>
    </div>
  `).join('');
}

/* ── Render full results ── */
function renderResults(data) {
  const panel = document.getElementById('resultsPanel');
  if (!panel) return;

  panel.innerHTML = `
    <!-- Disease Header -->
    <div class="card result-disease">
      <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--text-3);margin-bottom:8px;">Predicted Condition</div>
          <div class="disease-name">${data.disease}</div>
          <div class="disease-confidence">Confidence: <span>${data.confidence.toFixed(1)}%</span></div>
          ${riskBadge(data.risk)}
        </div>
        <svg class="arc-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle class="arc-track" cx="50" cy="50" r="35" stroke-dashoffset="0"
            transform="rotate(-220 50 50)"
            style="stroke-dasharray:220;stroke-dashoffset:${220*(1-0.7)};opacity:1"/>
          <circle class="arc-fill" cx="50" cy="50" r="35"
            transform="rotate(-220 50 50)" stroke="url(#arcGrad)"/>
          <text x="50" y="46" text-anchor="middle" class="arc-text" fill="var(--text-1)">
            <tspan class="arc-pct">0%</tspan>
          </text>
          <text x="50" y="58" text-anchor="middle" class="arc-sub" fill="var(--text-3)">confidence</text>
        </svg>
      </div>
      <div class="divider" style="margin-top:20px;"></div>
      <div class="conf-bar-group">
        <div class="conf-label">Prediction Strength</div>
        <div class="conf-bar-track">
          <div class="conf-bar-fill" id="mainConfBar"></div>
        </div>
      </div>
    </div>

    <!-- Top Predictions -->
    <div class="card">
      <div class="card-header">
        <div class="card-icon blue">📊</div>
        <div>
          <div class="card-title">Top Predictions</div>
          <div class="card-sub">Ranked by model confidence</div>
        </div>
      </div>
      <div class="top-predictions stagger" id="topPredList">
        ${buildTopPredictions(data.top5)}
      </div>
    </div>

    <!-- Medicines -->
    <div class="card">
      <div class="card-header">
        <div class="card-icon cyan">💊</div>
        <div>
          <div class="card-title">Recommended Medicines</div>
          <div class="card-sub">Always consult a physician before use</div>
        </div>
      </div>
      <div class="pill-list stagger">
        ${buildMedicineList(data.medicines)}
      </div>
    </div>

    <!-- Medical Advice -->
    <div class="card">
      <div class="card-header">
        <div class="card-icon green">🩺</div>
        <div>
          <div class="card-title">Medical Advice & Lifestyle</div>
          <div class="card-sub">Actionable recovery steps</div>
        </div>
      </div>
      <div class="pill-list stagger">
        ${buildAdviceList(data.advice)}
      </div>
    </div>

    <!-- Emergency -->
    <div class="emergency-card">
      <div class="card-header" style="margin-bottom:4px;">
        <div class="card-icon red">🚨</div>
        <div>
          <div class="card-title" style="color:var(--red);">Emergency Contacts</div>
          <div class="card-sub">Call immediately if condition worsens</div>
        </div>
      </div>
      <div class="emergency-numbers">
        <div class="emg-num" onclick="showNotification('Calling Emergency Services…')">
          <div class="num">112</div>
          <div class="num-label">National Emergency</div>
        </div>
        <div class="emg-num" onclick="showNotification('Calling Ambulance…')">
          <div class="num">108</div>
          <div class="num-label">Ambulance</div>
        </div>
        <div class="emg-num" onclick="showNotification('Calling Police…')">
          <div class="num">100</div>
          <div class="num-label">Police</div>
        </div>
      </div>
    </div>

    <!-- Disclaimer -->
    <div style="padding:14px 16px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);font-size:12px;color:var(--text-3);line-height:1.6;">
      ⚠️ <strong style="color:var(--text-2)">Medical Disclaimer:</strong>
      This AI-powered tool is for informational purposes only and does not constitute medical advice.
      Always consult a qualified healthcare professional for diagnosis and treatment.
    </div>
  `;

  /* Animate arc + bars after DOM insert */
  requestAnimationFrame(() => {
    const arcSvg = panel.querySelector('.arc-svg');
    if (arcSvg) animateArc(arcSvg, data.confidence);

    const mainBar = document.getElementById('mainConfBar');
    if (mainBar) animateBar(mainBar, data.confidence);

    panel.querySelectorAll('.pred-bar-fill').forEach(bar => {
      animateBar(bar, parseFloat(bar.dataset.pct));
    });
  });
}

/* ── Error display ── */
function renderError(msg) {
  const panel = document.getElementById('resultsPanel');
  if (!panel) return;
  panel.innerHTML = `
    <div class="card" style="border-color:rgba(239,68,68,0.2);background:rgba(239,68,68,0.05);text-align:center;padding:48px 32px;">
      <div style="font-size:36px;margin-bottom:16px;">⚠️</div>
      <div style="font-size:16px;font-weight:600;margin-bottom:8px;color:var(--red);">Prediction Failed</div>
      <div style="font-size:13px;color:var(--text-3);max-width:300px;margin:0 auto;line-height:1.6;">${msg}</div>
      <div style="margin-top:20px;font-size:12px;color:var(--text-3);">Check that Flask is running and .pkl files are present.</div>
    </div>`;
}

/* ── Main predict handler ── */
(function () {
  const form = document.getElementById('predictForm');
  const btn  = document.getElementById('predictBtn');
  if (!form || !btn) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    /* Gather inputs */
    const payload = {
      fever:         form.querySelector('#chkFever')?.checked         ? 1 : 0,
      cough:         form.querySelector('#chkCough')?.checked         ? 1 : 0,
      fatigue:       form.querySelector('#chkFatigue')?.checked       ? 1 : 0,
      breathing:     form.querySelector('#chkBreathing')?.checked     ? 1 : 0,
      age:           parseInt(form.querySelector('#ageSlider')?.value  ?? 30),
      gender:        parseInt(form.querySelector('#genderSelect')?.value ?? 0),
      bloodPressure: parseInt(form.querySelector('#bpSelect')?.value   ?? 1),
      cholesterol:   parseInt(form.querySelector('#cholSelect')?.value  ?? 1),
      model:         form.querySelector('#modelSelect')?.value ?? 'rf',
    };

    /* Require at least one symptom */
    if (payload.fever + payload.cough + payload.fatigue + payload.breathing === 0) {
      showNotification('⚠️ Please select at least one symptom.');
      return;
    }

    /* Loading state */
    btn.disabled = true;
    btn.classList.add('loading');

    /* Show skeleton while loading */
    const panel = document.getElementById('resultsPanel');
    if (panel) {
      panel.innerHTML = `
        <div class="card" style="min-height:160px;">
          <div class="skeleton" style="height:20px;width:60%;margin-bottom:12px;"></div>
          <div class="skeleton" style="height:40px;width:40%;margin-bottom:20px;"></div>
          <div class="skeleton" style="height:8px;width:100%;"></div>
        </div>
        <div class="card">
          <div class="skeleton" style="height:16px;width:50%;margin-bottom:12px;"></div>
          <div class="skeleton" style="height:12px;width:100%;margin-bottom:8px;"></div>
          <div class="skeleton" style="height:12px;width:85%;margin-bottom:8px;"></div>
          <div class="skeleton" style="height:12px;width:70%;"></div>
        </div>`;
    }

    try {
      const res = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await res.json();

      if (data.success) {
        renderResults(data);
        /* Scroll to results on mobile */
        if (window.innerWidth < 900) {
          setTimeout(() => panel?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
        }
      } else {
        renderError(data.message || data.error || 'Unknown error from server.');
      }

    } catch (err) {
      renderError('Could not reach the server. Make sure Flask is running on localhost:5000.');
    } finally {
      btn.disabled = false;
      btn.classList.remove('loading');
    }
  });
})();

/* ── Contact form ── */
(function () {
  const form  = document.getElementById('contactForm');
  const toast = document.getElementById('successToast');
  if (!form || !toast) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    toast.classList.add('show');
    form.reset();
    setTimeout(() => toast.classList.remove('show'), 5000);
  });
})();

/* ── Intersection Observer: fade-in on scroll ── */
(function () {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.08 }
  );

  document.querySelectorAll('.card, .about-feature').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s var(--ease-out), transform 0.5s var(--ease-out)';
    observer.observe(el);
  });
})();
