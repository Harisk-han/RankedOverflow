import os
import re

# Source paths
ROOT_DIR = r"c:\Users\Hp\OneDrive\Desktop\Rankedflow"
PAGES_DIR = os.path.join(ROOT_DIR, "pages")
CSS_DIR = os.path.join(ROOT_DIR, "css")

# CSS Files
MAIN_CSS_PATH = os.path.join(CSS_DIR, "main.css")
RESPONSIVE_CSS_PATH = os.path.join(CSS_DIR, "responsive.css")
PAGES_CSS_PATH = os.path.join(CSS_DIR, "pages.css")

# Read CSS contents
with open(MAIN_CSS_PATH, 'r', encoding='utf-8') as f:
    main_css = f.read()

with open(RESPONSIVE_CSS_PATH, 'r', encoding='utf-8') as f:
    responsive_css = f.read()

with open(PAGES_CSS_PATH, 'r', encoding='utf-8') as f:
    pages_css = f.read()

# Define CSS segments for each page from pages.css lines
# Note: lines are 1-indexed in the original file, python lists are 0-indexed.
pages_css_lines = pages_css.splitlines()

def get_css_segment(start_line, end_line):
    return "\n".join(pages_css_lines[start_line - 1 : end_line])

css_segments = {
    "home": get_css_segment(1, 637),
    "services": get_css_segment(638, 782),
    "about": get_css_segment(783, 904),
    "casestudies": get_css_segment(905, 1021),
    "contact": get_css_segment(1022, 1128),
    "score": get_css_segment(1129, 1223)
}

# JS common & page-specific code
common_js = """
// Hamburger menu toggle
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) {
    menu.classList.toggle('open');
  }
}

// Nav scroll effect
window.addEventListener('scroll', () => {
  const nav = document.getElementById('mainNav');
  if (nav) {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  }
});

// Fade ups on scroll
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

document.addEventListener('DOMContentLoaded', () => {
  initFadeUps();
});
"""

page_scripts = {
    "home": """
function triggerHeroAudit() {
  const urlInput = document.getElementById('heroAuditUrl');
  if (urlInput && urlInput.value) {
    window.location.href = 'score.html?url=' + encodeURIComponent(urlInput.value);
  } else {
    window.location.href = 'score.html';
  }
}
""",
    "services": "",
    "about": "",
    "casestudies": "",
    "contact": """
function submitContact() {
  const wrapper = document.getElementById('contactFormWrapper');
  const success = document.getElementById('contactSuccess');
  if (wrapper) wrapper.style.display = 'none';
  if (success) success.classList.add('visible');
}
""",
    "score": """
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

document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const urlParam = params.get('url');
  if (urlParam) {
    const scoreUrlInput = document.getElementById('scoreUrl');
    if (scoreUrlInput) {
      scoreUrlInput.value = urlParam;
      updateScoreStep();
    }
  }
});
"""
}

# SPA template index.html
TEMPLATE_PATH = os.path.join(ROOT_DIR, "index.html")
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_html = f.read()

# Replace CSS files with a placeholder in template
# We look for the stylesheet link tags and replace them with a single <style> placeholder
style_regex = r'<link rel="stylesheet" href="css/main.css">\s*<link rel="stylesheet" href="css/pages.css">\s*<link rel="stylesheet" href="css/responsive.css">'
template_html = re.sub(style_regex, '<!-- STYLE_PLACEHOLDER -->', template_html)

# Replace JS file link with placeholder
js_regex = r'<script src="js/app.js"></script>'
template_html = re.sub(js_regex, '<!-- SCRIPT_PLACEHOLDER -->', template_html)

# We also need to clean the navbar and footer routing in the template
# Navbar links mapping:
# <a href="#home" data-page="home">Home</a> -> <a href="index.html" data-page="home">Home</a>
# <a href="#services" data-page="services">Services</a> -> <a href="services.html" data-page="services">Services</a>
# etc.
navbar_replacements = {
    'href="#home"': 'href="index.html"',
    'href="#services"': 'href="services.html"',
    'href="#casestudies"': 'href="casestudies.html"',
    'href="#about"': 'href="about.html"',
    'href="#contact"': 'href="contact.html"',
    'href="#score"': 'href="score.html"',
}

for src, dest in navbar_replacements.items():
    template_html = template_html.replace(src, dest)

# Footer showPage onclick replacements
# onclick="showPage('services')" etc
footer_onclick_regex = r'onclick="showPage\(\'([^\']+)\'\)"'
template_html = re.sub(footer_onclick_regex, '', template_html)

# Also fix the # href in the footer links to point directly to pages
footer_href_replacements = {
    'href="#services"': 'href="services.html"',
    'href="#about"': 'href="about.html"',
    'href="#casestudies"': 'href="casestudies.html"',
    'href="#contact"': 'href="contact.html"',
    'href="#score"': 'href="score.html"',
}
for src, dest in footer_href_replacements.items():
    template_html = template_html.replace(src, dest)

pages_info = [
    {"id": "home", "file": "home.html", "output": "index.html", "title": "Rank Overflow — Rank Higher. Grow Faster."},
    {"id": "services", "file": "services.html", "output": "services.html", "title": "Services — Rank Overflow"},
    {"id": "about", "file": "about.html", "output": "about.html", "title": "About Us — Rank Overflow"},
    {"id": "casestudies", "file": "casestudies.html", "output": "casestudies.html", "title": "Case Studies — Rank Overflow"},
    {"id": "contact", "file": "contact.html", "output": "contact.html", "title": "Contact Us — Rank Overflow"},
    {"id": "score", "file": "score.html", "output": "score.html", "title": "Get My Score — Rank Overflow"}
]

for page in pages_info:
    # Read page content fragment
    page_frag_path = os.path.join(PAGES_DIR, page["file"])
    with open(page_frag_path, 'r', encoding='utf-8') as f:
        page_content = f.read()

    # Clean up page fragment's own hash links & onclick showPage
    # Replace href="#pagename" onclick="showPage('pagename')" with pagename.html
    page_content = re.sub(r'href="#home"\s*onclick="showPage\(\'home\'\)"', 'href="index.html"', page_content)
    page_content = re.sub(r'href="#([a-zA-Z0-9]+)"\s*onclick="showPage\(\'[a-zA-Z0-9]+\'\)"', r'href="\1.html"', page_content)
    
    # Simple href target replacements for those without onclick
    for src, dest in footer_href_replacements.items():
        page_content = page_content.replace(src, dest)
    page_content = page_content.replace('href="#home"', 'href="index.html"')

    # Assemble HTML
    html = template_html
    
    # 1. Title replacement
    html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', html)
    
    # 2. Content insertion
    html = html.replace('<main id="content"></main>', f'<main id="content">\n{page_content}\n</main>')
    
    # 3. CSS Inlining
    combined_css = f"{main_css}\n\n{css_segments[page['id']]}\n\n{responsive_css}"
    css_tag = f"<style>\n{combined_css}\n</style>"
    html = html.replace('<!-- STYLE_PLACEHOLDER -->', css_tag)
    
    # 4. JS Inlining
    combined_js = f"{common_js}\n\n{page_scripts[page['id']]}"
    js_tag = f"<script>\n{combined_js}\n</script>"
    html = html.replace('<!-- SCRIPT_PLACEHOLDER -->', js_tag)
    
    # 5. Highlight active tab in navigation
    # Remove active class from any pre-existing links first
    html = html.replace('class="active"', '')
    html = html.replace('class="nav-cta active"', 'class="nav-cta"')
    
    # Add active class to corresponding link (both desktop and mobile)
    # Target desktop link: data-page="pageId"
    # Target mobile link inside mobile-menu
    page_id = page["id"]
    
    # Desktop nav link:
    desktop_pattern = rf'(<a href="[^"]+"\s+data-page="{page_id}")'
    if page_id == 'score':
        html = re.sub(desktop_pattern, r'\1 class="nav-cta active"', html)
    else:
        html = re.sub(desktop_pattern, r'\1 class="active"', html)
        
    # Mobile nav link:
    # Wait, the mobile nav has the same data-page attribute, let's match both using re.sub with search/replace
    # Let's write a custom replace function
    def add_active_class(match):
        element = match.group(0)
        if 'class=' in element:
            # Append active
            if 'nav-cta' in element:
                return element.replace('class="nav-cta"', 'class="nav-cta active"')
            else:
                return element.replace('class="', 'class="active ')
        else:
            if page_id == 'score':
                return element.replace('data-page="score"', 'class="nav-cta active" data-page="score"')
            else:
                return element.replace('data-page="', 'class="active" data-page="')
                
    html = re.sub(rf'<a\s+[^>]*data-page="{page_id}"[^>]*>', add_active_class, html)

    # Write output file
    output_path = os.path.join(ROOT_DIR, page["output"])
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated standalone page: {page['output']}")

print("All pages generated successfully!")
