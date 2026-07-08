// ── CORS PROTOCOL CHECK ──
if (window.location.protocol === 'file:') {
  console.warn("Rank Overflow is running under the 'file://' protocol. SPA page loading will fail due to browser security settings.");
  document.addEventListener('DOMContentLoaded', () => {
    const banner = document.createElement('div');
    banner.style.cssText = `
      position: fixed; top: 0; left: 0; right: 0; z-index: 10000;
      background: #ff4d1c; color: #fff; padding: 12px 5%;
      font-family: 'DM Sans', sans-serif; font-size: 14px; text-align: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15); font-weight: bold;
    `;
    banner.innerHTML = `
      ⚠️ Local Browser Block: Rank Overflow's AJAX router is running on the file:// protocol. 
      Please open this workspace using a local web server (e.g., Live Server extension or running 'npx serve') to make pages work.
    `;
    document.body.appendChild(banner);
    
    // Adjust Nav position to sit below the banner
    const nav = document.getElementById('mainNav');
    if (nav) {
      nav.style.top = '44px';
    }
  });
}

// ── SPA HASH ROUTER ──
const routes = {
  home: 'pages/home.html',
  services: 'pages/services.html',
  casestudies: 'pages/casestudies.html',
  about: 'pages/about.html',
  contact: 'pages/contact.html',
  score: 'pages/score.html'
};

async function router() {
  let pageId = window.location.hash.slice(1) || 'home';
  if (!routes[pageId]) {
    pageId = 'home';
  }

  // Update active state in nav links (both desktop and mobile)
  document.querySelectorAll('.nav-links a[data-page], .mobile-menu a[data-page]').forEach(a => {
    a.classList.toggle('active', a.getAttribute('data-page') === pageId);
  });

  try {
    const response = await fetch(routes[pageId]);
    if (!response.ok) throw new Error('Page fragment load failed');
    const html = await response.text();
    document.getElementById('content').innerHTML = html;

    // Scroll back to top smoothly
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Initialize the fade up transitions for new elements
    initFadeUps();
  } catch (error) {
    console.error('Error routing pages:', error);
    document.getElementById('content').innerHTML = `
      <div class="container section text-center">
        <h2>Page Loading Error</h2>
        <p style="color:var(--muted); margin-top:1rem;">Failed to load the page fragment for: <strong>${pageId}</strong>.</p>
        <p style="font-size:0.85rem; color:var(--accent); margin-top:0.5rem;">If you are viewing files locally via double-clicking index.html, run a web server (like VS Code Live Server) to bypass browser CORS security.</p>
      </div>
    `;
  }
}

// Page trigger function
function showPage(pageId) {
  window.location.hash = '#' + pageId;
}

// Listen for routing events
window.addEventListener('hashchange', router);
window.addEventListener('DOMContentLoaded', router);

// ── HAMBURGER MENU ──
function toggleMenu() {
  document.getElementById('mobileMenu').classList.toggle('open');
}

// Close mobile menu when hash changes
window.addEventListener('hashchange', () => {
  const menu = document.getElementById('mobileMenu');
  if (menu && menu.classList.contains('open')) {
    menu.classList.remove('open');
  }
});

// ── NAV SCROLL ACTIVE STYLE ──
window.addEventListener('scroll', () => {
  const nav = document.getElementById('mainNav');
  if (nav) {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  }
});

// ── FADE UPS INTERSECTION OBSERVER ──
function initFadeUps() {
  setTimeout(() => {
    const els = document.querySelectorAll('#content .fade-up');
    if (els.length === 0) return;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((e, i) => {
        if (e.isIntersecting) {
          setTimeout(() => e.target.classList.add('visible'), i * 80);
        }
      });
    }, { threshold: 0.1 });
    els.forEach(el => observer.observe(el));
  }, 100);
}

// ── CONTACT FORM SUBMISSION ──
function submitContact() {
  const wrapper = document.getElementById('contactFormWrapper');
  const success = document.getElementById('contactSuccess');
  if (wrapper) wrapper.style.display = 'none';
  if (success) success.classList.add('visible');
}

// ── SCORE AUDIT FORM STEPS ──
function updateScoreStep() {
  const url = document.getElementById('scoreUrl').value;
  const step2 = document.getElementById('step-bar-2');
  const step3 = document.getElementById('step-bar-3');
  
  if (url.length > 5) {
    if (step2) {
      step2.classList.add('done');
      step2.classList.remove('active');
    }
    if (step3) {
      step3.classList.add('active');
    }
  }
}

function submitScoreForm() {
  const formContent = document.getElementById('scoreFormContent');
  const successBox = document.getElementById('scoreSuccess');
  const step3 = document.getElementById('step-bar-3');

  if (formContent) formContent.style.display = 'none';
  if (successBox) successBox.classList.add('visible');
  if (step3) {
    step3.classList.add('done');
    step3.classList.remove('active');
  }
}
