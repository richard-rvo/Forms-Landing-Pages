import re

with open("index2.html", "r") as f:
    content = f.read()

# 1. Insert fonts
font_links = """  <link rel="icon" type="image/svg+xml" href="images/logo.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Lora:ital,wght@0,400;1,400&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">"""
content = content.replace('  <link rel="icon" type="image/svg+xml" href="images/logo.svg" />', font_links)

# 2. Replace the whole <style>...</style>
new_style = """<style>
:root {
  --orange-50: #fff4e8;
  --orange-100: #fde3c7;
  --orange-300: #f8a23b;
  --orange-500: #f08113;
  --orange-600: #e94d1d;
  --orange-700: #c13a12;
  --brand-grad: linear-gradient(135deg, #f8a23b 0%, #f08113 48%, #e94d1d 100%);
  --brand-grad-soft: linear-gradient(135deg, #fdb976 0%, #f39553 50%, #ee6f3a 100%);
  --paper: #faf7f2;
  --paper-2: #f2eee7;
  --paper-3: #e8e3da;
  --hairline: rgba(26, 22, 20, 0.08);
  --hairline-strong: rgba(26, 22, 20, 0.14);
  --ink: #1a1614;
  --ink-2: #423b36;
  --stone: #87807a;
  --mist: #b8b1ab;
  --font-display: "Plus Jakarta Sans", -apple-system, system-ui, sans-serif;
  --font-text: "Lora", Georgia, serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
  --glass-shadow: 0 30px 60px -20px rgba(170, 90, 40, 0.18), 0 12px 24px -16px rgba(26, 22, 20, 0.16);
  --shadow-brand: 0 40px 80px -20px rgba(233, 77, 29, 0.45), inset 0 2px 0 rgba(255, 255, 255, 0.40);
  --shadow-cta: 0 12px 24px -8px rgba(233, 77, 29, 0.50), inset 0 1px 0 rgba(255, 255, 255, 0.30);
}
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
html {
  scroll-behavior: smooth;
}
body {
  font-family: var(--font-display);
  background: var(--paper);
  color: var(--ink);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
}
.ambient {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}
.ambient::before {
  content: "";
  position: absolute;
  width: 900px;
  height: 900px;
  background: radial-gradient(circle, rgba(240, 129, 19, 0.28), transparent 70%);
  filter: blur(140px);
  border-radius: 50%;
  top: -300px;
  right: -260px;
  animation: driftA 12s ease-in-out infinite alternate;
}
.ambient::after {
  content: "";
  position: absolute;
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(233, 77, 29, 0.18), transparent 70%);
  filter: blur(140px);
  border-radius: 50%;
  top: 60%;
  left: -300px;
  animation: driftB 16s ease-in-out infinite alternate;
}
@keyframes driftA {
  from { transform: translate(0, 0) scale(1); }
  to { transform: translate(-80px, 60px) scale(1.1); }
}
@keyframes driftB {
  from { transform: translate(0, 0) scale(1); }
  to { transform: translate(60px, -80px) scale(1.08); }
}
.navbar {
  position: sticky;
  top: 16px;
  z-index: 100;
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 16px auto 0;
  padding: 12px 22px;
  background: rgba(250, 247, 242, 0.72);
  backdrop-filter: blur(28px) saturate(140%);
  -webkit-backdrop-filter: blur(28px) saturate(140%);
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: 999px;
  box-shadow: var(--glass-shadow);
}
.nav-logo {
  display: flex;
  align-items: center;
  gap: 12px;
}
.nav-logo-img {
  height: 32px;
  width: auto;
  display: block;
}
.nav-logo-sep {
  width: 1px;
  height: 20px;
  background: var(--hairline-strong);
}
.nav-logo-label {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 13px;
  color: var(--ink-2);
}
.nav-tag {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--orange-600);
  padding: 6px 14px;
  border-radius: 999px;
  background: var(--orange-50);
  border: 1px solid var(--orange-100);
}
.page {
  position: relative;
  z-index: 1;
  max-width: 680px;
  margin: 0 auto;
  padding: 60px 24px 100px;
}
.badge {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--orange-600);
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 24px;
}
.badge-dot {
  width: 6px;
  height: 6px;
  background: var(--orange-500);
  border-radius: 50%;
  box-shadow: 0 0 6px var(--orange-300);
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
h1 {
  font-family: var(--font-display);
  font-size: clamp(28px, 5.5vw, 48px);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 0.95;
  margin-bottom: 24px;
}
.gradient-text {
  background: var(--brand-grad);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.subtitle {
  font-family: var(--font-text);
  font-size: 16px;
  line-height: 1.55;
  color: var(--ink-2);
  max-width: 520px;
  margin-bottom: 40px;
  font-style: italic;
  background: rgba(255, 255, 255, 0.4);
  border-left: 3px solid var(--orange-500);
  padding: 14px 18px;
  border-radius: 0 14px 14px 0;
}
.subtitle em {
  font-style: italic;
  color: var(--ink-2);
}
.divider {
  height: 1px;
  background: var(--hairline);
  margin-bottom: 36px;
}
.progress-wrap {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 28px;
}
.progress-step {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  font-weight: 600;
  color: var(--mist);
  transition: color 0.3s;
}
.progress-step.active, .progress-step.done {
  color: var(--orange-600);
}
.step-num {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 1.5px solid currentColor;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  transition: all 0.3s;
}
.progress-step.active .step-num, .progress-step.done .step-num {
  background: var(--orange-600);
  border-color: var(--orange-600);
  color: #fff;
}
.progress-line {
  flex: 1;
  height: 1px;
  background: var(--hairline);
  transition: background 0.5s;
}
.progress-line.filled {
  background: var(--orange-600);
}
.step-card {
  display: none;
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(28px) saturate(140%);
  -webkit-backdrop-filter: blur(28px) saturate(140%);
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: 28px;
  box-shadow: var(--glass-shadow);
  padding: 36px;
  animation: fadeUp 0.4s ease;
}
.step-card.active {
  display: block;
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
.step-label {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--orange-600);
  margin-bottom: 8px;
}
.step-title {
  font-family: var(--font-display);
  font-size: 21px;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 4px;
}
.step-desc {
  font-family: var(--font-text);
  font-size: 15px;
  color: var(--ink-2);
  margin-bottom: 28px;
  line-height: 1.65;
  border-bottom: 1px solid var(--hairline);
  padding-bottom: 22px;
}
.field {
  margin-bottom: 22px;
}
.field label {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--stone);
  margin-bottom: 8px;
  display: block;
}
.field label span {
  color: var(--orange-600);
  margin-left: 2px;
}
input[type="text"], input[type="email"], input[type="tel"], select, textarea {
  width: 100%;
  background: rgba(255, 255, 255, 0.75);
  border: 1px solid var(--hairline-strong);
  border-radius: 14px;
  padding: 12px 16px;
  font-family: var(--font-display);
  font-size: 14px;
  color: var(--ink-2);
  outline: none;
  transition: border-color 200ms, box-shadow 200ms;
  -webkit-appearance: none;
}
input::placeholder, textarea::placeholder {
  color: var(--mist);
}
select {
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%2387807A' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  padding-right: 36px;
}
textarea {
  resize: vertical;
  min-height: 80px;
  line-height: 1.5;
}
input:focus, select:focus, textarea:focus {
  border-color: var(--orange-300);
  box-shadow: 0 0 0 3px rgba(240, 129, 19, 0.12);
}
input.error, select.error, textarea.error {
  border-color: var(--orange-600);
  box-shadow: 0 0 0 3px rgba(233, 77, 29, 0.12);
}
.field-error {
  font-size: 12px;
  color: var(--orange-600);
  margin-top: 5px;
  display: none;
}
.field-error.show {
  display: block;
}
.feeling-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.feeling-chip input {
  display: none;
}
.feeling-chip label {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 18px;
  border-radius: 14px;
  border: 1px solid var(--hairline-strong);
  background: rgba(255, 255, 255, 0.75);
  font-size: 14px;
  font-family: var(--font-display);
  font-weight: 600;
  color: var(--ink-2);
  cursor: pointer;
  transition: all 0.2s;
  line-height: 1.45;
}
.feeling-chip input:checked + label {
  border-color: var(--orange-500);
  background: var(--orange-50);
  color: var(--orange-700);
}
.feeling-chip label:hover {
  background: rgba(255, 255, 255, 0.9);
  border-color: var(--orange-300);
}
.chip-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.chip input {
  display: none;
}
.chip label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid var(--hairline-strong);
  background: rgba(255, 255, 255, 0.75);
  font-size: 13px;
  font-family: var(--font-display);
  font-weight: 600;
  color: var(--ink-2);
  cursor: pointer;
  transition: all 0.2s;
  margin: 0;
}
.chip input:checked + label {
  border-color: var(--orange-500);
  background: var(--orange-50);
  color: var(--orange-700);
}
.chip label:hover {
  background: rgba(255, 255, 255, 0.9);
  border-color: var(--orange-300);
}
.btn-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 28px;
  padding-top: 22px;
  border-top: 1px solid var(--hairline);
  gap: 12px;
}
.btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 16px 28px;
  border-radius: 999px;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 15px;
  letter-spacing: -0.01em;
  cursor: pointer;
  border: 0;
  text-decoration: none;
  transition: transform 200ms, box-shadow 200ms;
}
.btn-primary {
  background: var(--brand-grad);
  color: white;
  box-shadow: var(--shadow-cta);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 18px 36px -10px rgba(233, 77, 29, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.3);
}
.btn-ghost {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px);
  color: var(--ink);
  border: 1px solid rgba(255, 255, 255, 0.85);
}
.btn-ghost:hover {
  background: rgba(255, 255, 255, 0.85);
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none !important;
  box-shadow: none !important;
}
.btn-icon {
  font-size: 16px;
}
.success-screen {
  display: none;
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(28px) saturate(140%);
  -webkit-backdrop-filter: blur(28px) saturate(140%);
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: 28px;
  box-shadow: var(--glass-shadow);
  padding: 56px 36px;
  text-align: center;
  animation: fadeUp 0.45s ease;
}
.success-screen.show {
  display: block;
}
.success-icon {
  width: 76px;
  height: 76px;
  background: var(--orange-50);
  border: 2px solid var(--orange-300);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  margin: 0 auto 24px;
}
.success-screen h2 {
  font-family: var(--font-display);
  font-size: 28px;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 12px;
}
.success-screen p {
  font-family: var(--font-text);
  color: var(--ink-2);
  font-size: 16px;
  line-height: 1.6;
}
.success-screen strong {
  font-family: var(--font-display);
  font-weight: 700;
  color: var(--orange-600);
}
.footer {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mist);
  text-align: center;
  margin-top: 40px;
}
@media (max-width: 540px) {
  .page { padding: 36px 16px 80px; }
  .step-card { padding: 28px 24px; }
  h1 { font-size: 28px; }
  .btn-row { flex-direction: column-reverse; }
  .btn { width: 100%; justify-content: center; }
  .navbar { padding: 12px 16px; }
}
</style>"""

content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

# 3. Replace orbs with ambient
old_orbs = '''  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>'''
content = content.replace(old_orbs, '  <div class="ambient"></div>')

with open("index2.html", "w") as f:
    f.write(content)

