# DERMORA — Brand Experience & Cinematic Landing Page

> **Phase 1: Cinematic Skincare Campaign & Rotating Treatment Wheel**  
> Visual Direction: Modern Clinical Luxury + Cinematic Editorial Beauty  
> Signature Interaction: Animated Rotating Radial Treatment Selector  
> Specialized for South Asian Skin Phototypes (Fitzpatrick III–VI)

---

## 1. Project Overview & Brand Identity

**DERMORA** is a premium skin and laser clinic based in Gulberg III, Lahore, Pakistan. The digital brand experience bridges advanced dermatological science with high-fashion beauty editorial aesthetics.

### Visual Foundations
- **Wordmark Identity**: Custom serif typographic wordmark (`DERMORA`) typeset in Cormorant Garamond with optical kerning and uppercase tracking. Free of generic medical crosses, leaves, or separate monogram symbols.
- **Cinematic Photography**: Warm, dewy, realistic South Asian skin photography with natural lighting, pores, depth, and shadow play.
- **Signature Interaction**: Continuous GSAP-powered rotating circular treatment wheel with counter-rotating label capsules (HydraFacial, Laser Treatments, BB Glow, Dark Underarms, Dark Elbows, Dark Knuckles, Dark Hands, Dark Ankles).
- **Clinical Integrity**: Physician-supervised clinical protocols calibrated for melanin-rich skin safety (PIH prevention). No fake reviews, no fabricated clinical before-and-after claims.

### Color Palette

| Color Name | Hex Code | Visual Role |
|:---|:---|:---|
| **Deep Forest Green** | `#183D35` | Grounding luxury shade for primary contrast, text, and immersive philosophy section |
| **Warm Ivory** | `#F5F3ED` | Editorial canvas background with tactile paper warmth |
| **Champagne** | `#C5A77D` | Warm metallic accent for highlights, buttons, and numbering |
| **Charcoal** | `#292D2B` | Typographic body text providing crisp, comfortable reading |
| **Soft Sage** | `#D8E0D8` | Calming botanical tone for secondary text and borders |
| **White** | `#FFFFFF` | Crisp clinical gallery backdrop for featured treatments |

---

## 2. Technology Stack

- **Backend**: Python 3 (Flask 3.1.x)
- **Templating**: Jinja2 (`templates/base.html`, `templates/index.html`)
- **CSS Architecture**: Dual-layer system:
  1. Tailwind CSS via brand configuration for responsive utility support
  2. Modular custom design system in `static/css/style.css` (19 organized sections)
- **Animation & Motion**:
  - GSAP 3.12.5 + ScrollTrigger
  - Continuous counter-rotating circular orbit engine
  - Subtle hero background parallax
  - Staggered typography reveals and scroll triggers
- **Assets**: Curated local photography and vector SVGs in `static/images/`

---

## 3. Connected Homepage Sections

1. **Section 01 — Cinematic Hero with Rotating Treatment Selector**:
   - Full-screen cinematic background with warm lighting and subtle parallax (`hero-cinematic-bg.jpg`).
   - Headline: *"Healthy, confident skin starts here."*
   - Supporting text: *"Advanced skincare and aesthetic treatments designed around your skin."*
   - Dual actions: *Explore Treatments* & *Book Consultation*.
   - **Signature Circular Selector**: Central bottom dome (*Explore our treatments*) surrounded by 8 radiating spoke capsules (HydraFacial, Laser Treatments, BB Glow, Dark Underarms, Dark Elbows, Dark Knuckles, Dark Hands, Dark Ankles).
   - Pauses on hover, updates active spotlight card, and seamlessly adapts into a touch carousel on mobile.
2. **Section 02 — Skin Storytelling**:
   - Headline: *"Your skin deserves more than a routine."*
   - Pull-quote manifesto honoring melanin depth and natural skin texture.
   - Asymmetrical diptych visual layout.
3. **Section 03 — Explore Treatments**:
   - Large editorial image spreads for HydraFacial MD Elite, Laser Hair Reduction, BB Glow Meso-Revitalisation, and Targeted Pigment Harmonisation.
   - Numbered indices (`01`, `02`, `03`, `04`) with duration, downtime, and protocol focus.
4. **Section 04 — Explore Skin Concerns**:
   - 10-item comprehensive South Asian skin concerns grid (Acne marks, Melasma, Dark circles, Uneven tone, Pores, Dehydration, Dark underarms, Dark elbows, Dark knuckles, Dark hands & ankles).
   - Medical disclaimer clarifying preliminary assessment requirements.
5. **Section 05 — Results Journal Preview**:
   - Interactive draggable Before & After comparison slider with clear labels.
   - Smooth mouse/touch drag and keyboard accessible range control.
   - Ethical clinical disclosure.
6. **Section 06 — Why DERMORA**:
   - 4 clinical pillars: *Personalised Consultations*, *Professional Assessment*, *Melanin-Safe Protocols*, and *Patient Comfort & Technology*.
7. **Section 07 — Offers & Packages**:
   - 4 curated care programs: *The Hydration Ritual*, *Clear Skin Journey*, *Radiance & Glow Package*, and *Laser Care Package*.
8. **Section 08 — About DERMORA**:
   - Clinic suite in Gulberg III, Lahore, with physician oversight and sterile standards.
9. **Section 09 — Final Consultation CTA**:
   - Headline: *"Your skin journey starts with the right consultation."*
   - Reservation inquiry form with instant submission feedback.
10. **Fixed Floating AI Skin Assistant**:
    - Bottom-right launcher button opening the Phase 5 diagnostic preview drawer.

---

## 4. How to Run the Project

1. Open PowerShell and navigate to the project directory:
   ```powershell
   cd c:\Users\noor\Desktop\DERMORA
   ```

2. Run the application using the project virtual environment:
   ```powershell
   .venv\Scripts\python.exe app.py
   ```

3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
