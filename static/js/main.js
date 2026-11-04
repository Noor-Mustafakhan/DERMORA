/**
 * DERMORA — Luxury Editorial Skincare & Aesthetic Dermatology
 * JavaScript Controller — Vanilla JS & GSAP ScrollTrigger
 * Signature Feature: Rotating Treatment Selector Wheel
 */

document.addEventListener('DOMContentLoaded', () => {
    'use strict';

    /* ==========================================================================
       1. STICKY HEADER SCROLL STATE
       ========================================================================== */
    const siteHeader = document.getElementById('site-header');
    const updateHeaderOnScroll = () => {
        if (!siteHeader) return;
        if (window.scrollY > 25) {
            siteHeader.classList.add('is-scrolled');
        } else {
            siteHeader.classList.remove('is-scrolled');
        }
    };
    window.addEventListener('scroll', updateHeaderOnScroll, { passive: true });
    updateHeaderOnScroll();

    /* ==========================================================================
       2. MOBILE NAVIGATION DRAWER & TREATMENTS DROPDOWN
       ========================================================================== */
    const mobileToggle = document.querySelector('.js-mobile-toggle');
    const mobileNav = document.getElementById('mobile-nav');
    const mobileCloseButtons = document.querySelectorAll('.js-mobile-close, .js-nav-close');

    const toggleMobileMenu = (open) => {
        if (!mobileNav || !mobileToggle) return;
        const isOpen = typeof open === 'boolean' ? open : !mobileNav.classList.contains('is-open');

        if (isOpen) {
            mobileNav.classList.add('is-open');
            mobileNav.setAttribute('aria-hidden', 'false');
            mobileToggle.setAttribute('aria-expanded', 'true');
            document.body.style.overflow = 'hidden';
        } else {
            mobileNav.classList.remove('is-open');
            mobileNav.setAttribute('aria-hidden', 'true');
            mobileToggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        }
    };

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => toggleMobileMenu());
    }

    mobileCloseButtons.forEach(btn => {
        btn.addEventListener('click', () => toggleMobileMenu(false));
    });

    // Desktop Treatments Dropdown
    const navDropdown = document.querySelector('.js-nav-dropdown');
    const dropdownTrigger = document.querySelector('.js-dropdown-trigger');
    const dropdownMenu = document.querySelector('.js-dropdown-menu');
    const dropdownLinks = document.querySelectorAll('.nav-dropdown__link, .nav-dropdown__footer-link');
    let dropdownCloseTimer = null;

    if (dropdownTrigger && navDropdown) {
        const openDropdown = () => {
            if (dropdownCloseTimer) {
                clearTimeout(dropdownCloseTimer);
                dropdownCloseTimer = null;
            }
            navDropdown.classList.add('is-open');
            dropdownTrigger.setAttribute('aria-expanded', 'true');
            if (dropdownMenu) dropdownMenu.style.display = 'block';
        };

        const closeDropdown = () => {
            if (dropdownCloseTimer) {
                clearTimeout(dropdownCloseTimer);
                dropdownCloseTimer = null;
            }
            navDropdown.classList.remove('is-open');
            dropdownTrigger.setAttribute('aria-expanded', 'false');
            if (dropdownMenu) dropdownMenu.style.display = 'none';
        };

        const toggleDropdown = () => {
            if (navDropdown.classList.contains('is-open')) {
                closeDropdown();
            } else {
                openDropdown();
            }
        };

        // Explicit button click toggle
        dropdownTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleDropdown();
        });

        // Intentional hover: open on mouseenter, clean close on mouseleave with 250ms buffer
        navDropdown.addEventListener('mouseenter', () => {
            openDropdown();
        });

        navDropdown.addEventListener('mouseleave', () => {
            dropdownCloseTimer = setTimeout(() => {
                closeDropdown();
            }, 250);
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!navDropdown.contains(e.target)) {
                closeDropdown();
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navDropdown.classList.contains('is-open')) {
                closeDropdown();
                dropdownTrigger.focus();
            }
        });

        // Close on clicking any link inside
        dropdownLinks.forEach(link => {
            link.addEventListener('click', () => {
                closeDropdown();
            });
        });
    }

    // Mobile Treatments Accordion
    const mobileAccordionBtn = document.querySelector('.js-mobile-accordion');
    const mobileAccordionPanel = document.querySelector('.js-mobile-accordion-panel');
    if (mobileAccordionBtn && mobileAccordionPanel) {
        mobileAccordionBtn.addEventListener('click', () => {
            const isOpen = mobileAccordionBtn.getAttribute('aria-expanded') === 'true';
            mobileAccordionBtn.setAttribute('aria-expanded', !isOpen);
            mobileAccordionPanel.hidden = isOpen;
            const parentAccordion = mobileAccordionBtn.closest('.mobile-nav__accordion');
            if (parentAccordion) parentAccordion.classList.toggle('is-open', !isOpen);
        });
    }

    // Hub Dome Click: Scroll smoothly to Treatments
    const hubDome = document.querySelector('.hero-arc__hub-dome');
    if (hubDome) {
        hubDome.addEventListener('click', () => {
            const treatmentsSec = document.getElementById('treatments');
            if (treatmentsSec) {
                treatmentsSec.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }

    /* ==========================================================================
       3. SIGNATURE ROTATING TREATMENT ORBIT (FLAWLESS & STABLE)
       ========================================================================== */
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const orbitRing = document.getElementById('hero-orbit-ring');
    const orbitStage = document.getElementById('hero-orbit-stage');
    const orbitSpokes = orbitRing ? orbitRing.querySelectorAll('.js-spoke') : [];

    if (!prefersReducedMotion && typeof window.gsap !== 'undefined' && orbitRing && orbitSpokes.length > 0) {
        const gsap = window.gsap;
        // Spoke base angles: spoke 0 is top apex (270°), spoke 1 is 315°, etc.
        const spokeAngles = [270, 315, 0, 45, 90, 135, 180, 225];
        let isOrbitPaused = false;

        const updateSpokePositions = (currentRingAngle) => {
            orbitSpokes.forEach((spoke, idx) => {
                const capsule = spoke.querySelector('.spoke__capsule');
                if (!capsule) return;

                const baseAngle = spokeAngles[idx];
                const worldAngle = ((baseAngle + currentRingAngle) % 360 + 360) % 360;

                // Mathematical counter-rotation: capsule is always 0° horizontal in world space
                capsule.style.transform = `translate(-50%, -50%) rotate(${-currentRingAngle - baseAngle}deg)`;

                // Smooth horizon fade: fully opaque in upper arc, dissolves smoothly at the horizon
                let opacity = 0;
                if (worldAngle >= 180 && worldAngle <= 360) {
                    const rad = ((worldAngle - 180) / 180) * Math.PI;
                    const sinVal = Math.sin(rad);
                    if (sinVal > 0) {
                        opacity = Math.min(1, sinVal * 1.6);
                    }
                }

                capsule.style.opacity = opacity.toFixed(3);
                capsule.style.pointerEvents = (opacity > 0.35) ? 'auto' : 'none';
            });
        };

        // Initialize positions
        updateSpokePositions(0);

        // Continuous smooth rotation around the Explore Treatments button (70s calming luxury pace)
        const orbitTween = gsap.to(orbitRing, {
            rotation: 360,
            duration: 70,
            repeat: -1,
            ease: 'none',
            onUpdate: () => {
                const currentAngle = gsap.getProperty(orbitRing, 'rotation') % 360;
                updateSpokePositions(currentAngle);
            }
        });

        // Pause on hover or touch, resume smoothly on leave
        if (orbitStage) {
            orbitStage.addEventListener('mouseenter', () => {
                if (!isOrbitPaused) orbitTween.pause();
            });
            orbitStage.addEventListener('mouseleave', () => {
                if (!isOrbitPaused) orbitTween.resume();
            });
            orbitStage.addEventListener('touchstart', () => {
                if (!isOrbitPaused) orbitTween.pause();
            }, { passive: true });
            orbitStage.addEventListener('touchend', () => {
                if (!isOrbitPaused) orbitTween.resume();
            }, { passive: true });
        }
    }

    /* ==========================================================================
       4. RESULTS JOURNAL BEFORE & AFTER DRAGGABLE SLIDER
       ========================================================================== */
    const resultsSliders = document.querySelectorAll('.js-results-slider');
    resultsSliders.forEach(slider => {
        const range = slider.querySelector('.js-slider-range');
        const beforeEl = slider.querySelector('.js-slider-before, .results-slider__before');
        const handleEl = slider.querySelector('.js-slider-handle, .results-slider__handle');

        const updatePosition = (percent) => {
            const clamped = Math.max(0, Math.min(100, percent));
            slider.style.setProperty('--slider-pos', `${clamped}%`);
            if (beforeEl) beforeEl.style.width = `${clamped}%`;
            if (handleEl) handleEl.style.left = `${clamped}%`;
            if (range && Math.abs(parseFloat(range.value) - clamped) > 0.5) {
                range.value = clamped;
            }
        };

        if (range) {
            range.addEventListener('input', (e) => updatePosition(parseFloat(e.target.value)));
            range.addEventListener('change', (e) => updatePosition(parseFloat(e.target.value)));
        }

        // Pointer drag support directly on the slider container
        let isDragging = false;
        const calculateDragPercent = (clientX) => {
            const rect = slider.getBoundingClientRect();
            const offsetX = clientX - rect.left;
            return (offsetX / rect.width) * 100;
        };

        const onPointerMove = (e) => {
            if (!isDragging) return;
            const clientX = e.clientX || (e.touches && e.touches[0] ? e.touches[0].clientX : 0);
            updatePosition(calculateDragPercent(clientX));
        };

        const stopDragging = () => {
            if (isDragging) {
                isDragging = false;
                slider.classList.remove('is-dragging');
                window.removeEventListener('pointermove', onPointerMove);
                window.removeEventListener('pointerup', stopDragging);
                window.removeEventListener('pointercancel', stopDragging);
            }
        };

        slider.addEventListener('pointerdown', (e) => {
            isDragging = true;
            slider.classList.add('is-dragging');
            const clientX = e.clientX || (e.touches && e.touches[0] ? e.touches[0].clientX : 0);
            updatePosition(calculateDragPercent(clientX));
            window.addEventListener('pointermove', onPointerMove, { passive: true });
            window.addEventListener('pointerup', stopDragging);
            window.addEventListener('pointercancel', stopDragging);
        });

        // Initialize at 50%
        updatePosition(50);
    });

    /* ==========================================================================
       5. CONSULTATION RESERVATION FORM PROTOTYPE
       ========================================================================== */
    const consultForm = document.querySelector('.js-consult-form');
    const consultFeedback = document.querySelector('.js-consult-feedback');

    if (consultForm) {
        consultForm.addEventListener('submit', (e) => {
            e.preventDefault();
            if (consultFeedback) {
                consultFeedback.hidden = false;
                consultForm.reset();
            }
        });
    }

    /* ==========================================================================
       6. AI SKIN ASSISTANT DRAWER & CLINICAL CHAT INTERACTION
       ========================================================================== */
    const aiDrawer = document.getElementById('ai-drawer');
    const aiOpenButtons = document.querySelectorAll('.js-open-ai');
    const aiCloseButtons = document.querySelectorAll('.js-close-ai');
    const aiChatStream = document.getElementById('ai-chat-stream') || document.querySelector('.js-ai-chat-stream');
    const aiForm = document.querySelector('.js-ai-form');
    const aiInput = document.querySelector('.js-ai-input');
    const aiChips = document.querySelectorAll('.js-ai-chip');
    const aiTyping = document.querySelector('.js-ai-typing');
    let lastActiveElement = null;

    const openAiDrawer = () => {
        if (!aiDrawer) return;
        lastActiveElement = document.activeElement;
        aiDrawer.classList.add('is-open');
        aiDrawer.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';

        const inputField = aiDrawer.querySelector('.js-ai-input');
        if (inputField) {
            setTimeout(() => inputField.focus(), 250);
        }
    };

    const closeAiDrawer = () => {
        if (!aiDrawer) return;
        aiDrawer.classList.remove('is-open');
        aiDrawer.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';

        if (lastActiveElement && typeof lastActiveElement.focus === 'function') {
            lastActiveElement.focus();
        }
    };

    aiOpenButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            toggleMobileMenu(false);
            openAiDrawer();
        });
    });

    aiCloseButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            closeAiDrawer();
        });
    });

    // Helper: append message bubble
    const appendChatMessage = (role, htmlContent) => {
        if (!aiChatStream) return;
        const msgWrapper = document.createElement('div');
        msgWrapper.className = `ai-msg ai-msg--${role}`;
        
        const bubble = document.createElement('div');
        bubble.className = 'ai-msg__bubble';
        bubble.innerHTML = htmlContent;

        msgWrapper.appendChild(bubble);

        // Insert before typing indicator if present, else append
        if (aiTyping && aiTyping.parentNode === aiChatStream) {
            aiChatStream.insertBefore(msgWrapper, aiTyping);
        } else {
            aiChatStream.appendChild(msgWrapper);
        }

        aiChatStream.scrollTop = aiChatStream.scrollHeight;
    };

    // Clinical response knowledge base tailored for South Asian skin (Fitzpatrick III-VI)
    const clinicalResponses = {
        'laser-safety': `
            <p class="font-medium text-forest mb-1"><strong>Clinical Safety &bull; Fitzpatrick III&ndash;VI Calibrated</strong></p>
            <p class="mb-2">Melanin-rich skin requires precise wavelength calibration to preserve epidermal integrity. At DERMORA, we deploy <strong>Long-Pulsed Nd:YAG (1064nm)</strong> and triple-diode systems with sapphire contact cooling.</p>
            <p class="text-xs text-charcoal-muted">Bypasses epidermal melanin to reach deep follicle bulbs without triggering post-inflammatory hyperpigmentation (PIH). A complimentary physician patch test in Gulberg III precedes every treatment package.</p>
        `,
        'dark-areas': `
            <p class="font-medium text-forest mb-1"><strong>Targeted Dark Areas Protocol</strong></p>
            <p class="mb-2">Darkening on underarms, elbows, knuckles, and ankles in South Asian phototypes is typically driven by mechanical friction and epidermal thickening (acanthosis)&mdash;never poor hygiene.</p>
            <p class="text-xs text-charcoal-muted">Our protocol combines non-ablative Q-switched laser toning with mandelic/lactic micro-infusions to safely disperse dermal melanin clumps without rebound hyperpigmentation.</p>
        `,
        'hydrafacial': `
            <p class="font-medium text-forest mb-1"><strong>HydraFacial MD Elite vs. Chemical Peels</strong></p>
            <p class="mb-2"><strong>HydraFacial MD Elite:</strong> Patented 4-step vortex suction cleansing, painless extractions, and antioxidant infusion with zero downtime. Ideal 48-72 hours before weddings or public events.</p>
            <p class="text-xs text-charcoal-muted"><strong>Physician Peels:</strong> Mandelic and salicylic formulations tailored for active acne or deeper melasma. Our physicians often combine both into a curated treatment pathway.</p>
        `,
        'acne-scars': `
            <p class="font-medium text-forest mb-1"><strong>Acne Scars &amp; Barrier Health</strong></p>
            <p class="mb-2">Aggressive ablative resurfacing carries significant PIH risks in Fitzpatrick III&ndash;VI. We utilize non-ablative fractional laser passes, subcision, and peptide nano-infusions.</p>
            <p class="text-xs text-charcoal-muted">Promotes deep collagen remodeling while preserving superficial barrier integrity. Strict broad-spectrum mineral SPF 50+ is mandatory throughout care.</p>
        `
    };

    const getAssistantReply = (query) => {
        const q = query.toLowerCase();
        if (q.includes('laser') || q.includes('hair') || q.includes('diode') || q.includes('yag')) {
            return `
                <p class="font-medium text-forest mb-1"><strong>Laser Treatments at DERMORA</strong></p>
                <p class="mb-2">We utilize medical-grade Long-Pulsed Nd:YAG (1064nm) and triple-wavelength diode lasers with sapphire cooling tips. Designed specifically for safe, permanent hair reduction and vascular clearing on South Asian skin (Fitzpatrick III&ndash;VI) with zero burn risk.</p>
                <p class="text-xs text-charcoal-muted">Typical courses require 6&ndash;8 sessions spaced 4&ndash;6 weeks apart. Schedule an in-person test patch in Gulberg III to confirm parameters.</p>
            `;
        }
        if (q.includes('underarm') || q.includes('elbow') || q.includes('knuckle') || q.includes('ankle') || q.includes('hand') || q.includes('dark') || q.includes('pigment') || q.includes('melasma')) {
            return `
                <p class="font-medium text-forest mb-1"><strong>Targeted Hyperpigmentation Protocols</strong></p>
                <p class="mb-2">For dark underarms, elbows, knuckles, and seated ankle pressure zones, we combine gentle Q-switched laser toning with biocompatible mandelic and lactic exfoliants. This breaks down dermal melanin deposits without damaging the barrier.</p>
                <p class="text-xs text-charcoal-muted">We strictly avoid harsh bleaching agents or aggressive physical scrubs that exacerbate melanin darkening.</p>
            `;
        }
        if (q.includes('hydra') || q.includes('facial') || q.includes('glow') || q.includes('cleanse') || q.includes('blackhead') || q.includes('bb glow')) {
            return `
                <p class="font-medium text-forest mb-1"><strong>HydraFacial MD &amp; Radiance Infusions</strong></p>
                <p class="mb-2">Our HydraFacial MD Elite combines spiral vortex extraction, gentle salicylic/glycolic resurfacing, and multi-peptide hydration. Leaves your skin visibly decongested, plumper, and lit from within with zero peeling or recovery downtime.</p>
                <p class="text-xs text-charcoal-muted">Popular before weddings and events. Can be augmented with our BB Glow nano-peptide infusion.</p>
            `;
        }
        if (q.includes('acne') || q.includes('scar') || q.includes('texture') || q.includes('pore') || q.includes('pimple')) {
            return `
                <p class="font-medium text-forest mb-1"><strong>Acne Scars &amp; Textural Refinement</strong></p>
                <p class="mb-2">We address rolling scars, boxcar scars, and textural irregularities through multi-modality therapies: non-ablative fractional laser passes, subcision, and barrier-restoring ceramide infusions.</p>
                <p class="text-xs text-charcoal-muted">Calibrated to avoid post-inflammatory hyperpigmentation while inducing natural dermal neocollagenesis.</p>
            `;
        }
        if (q.includes('price') || q.includes('cost') || q.includes('fee') || q.includes('charge') || q.includes('pkr') || q.includes('package') || q.includes('rate')) {
            return `
                <p class="font-medium text-forest mb-1"><strong>Transparent Package Curation</strong></p>
                <p class="mb-2">DERMORA offers structured clinical programs&mdash;including our <em>Bridal Radiance Curation</em>, <em>Complete Laser Hair Reduction</em>, and <em>Targeted Body Radiance</em> bundles.</p>
                <p class="text-xs text-charcoal-muted">Visit our <a href="/packages" class="text-champagne underline">Offers &amp; Packages</a> page for detailed inclusions, or book an in-person assessment for a customized prescription.</p>
            `;
        }
        if (q.includes('book') || q.includes('appointment') || q.includes('consult') || q.includes('schedule') || q.includes('doctor') || q.includes('timing') || q.includes('hour') || q.includes('address') || q.includes('lahore') || q.includes('gulberg')) {
            return `
                <p class="font-medium text-forest mb-1"><strong>Consultation at Gulberg III, Lahore</strong></p>
                <p class="mb-2">Our clinic is located in Gulberg III, Lahore, Pakistan. We welcome patients Monday through Saturday, 10:00 AM to 08:00 PM.</p>
                <p class="text-xs text-charcoal-muted">You can reserve your physician consultation directly through our <a href="/contact#consultation" class="text-champagne underline">booking calendar</a> or call our concierge desk at +92 (42) 3578-XXXX.</p>
            `;
        }
        return `
            <p class="font-medium text-forest mb-1"><strong>Doctor Assessment Recommended</strong></p>
            <p class="mb-2">Thank you for your inquiry. Because melanin behavior and barrier resilience vary across individual skin profiles, our physicians in Gulberg III conduct comprehensive visual and dermatoscopic examinations before prescribing any active clinical course.</p>
            <p class="text-xs text-charcoal-muted">Would you like to reserve a personalized doctor consultation or explore our clinical treatment catalog?</p>
        `;
    };

    const handleUserQuery = (userText, queryKey = null) => {
        if (!userText || !userText.trim()) return;
        const cleanText = userText.trim();

        // 1. Render User Message
        appendChatMessage('user', `<p>${cleanText.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</p>`);

        // 2. Display Typing Indicator
        if (aiTyping) {
            aiTyping.style.display = 'inline-flex';
            if (aiChatStream) aiChatStream.scrollTop = aiChatStream.scrollHeight;
        }

        // 3. Simulated Clinical Response Timing (550ms)
        setTimeout(() => {
            if (aiTyping) {
                aiTyping.style.display = 'none';
            }
            const replyHtml = queryKey && clinicalResponses[queryKey] 
                ? clinicalResponses[queryKey] 
                : getAssistantReply(cleanText);

            appendChatMessage('assistant', replyHtml);
        }, 550);
    };

    // Chip Click Handlers
    aiChips.forEach(chip => {
        chip.addEventListener('click', (e) => {
            e.preventDefault();
            const queryKey = chip.getAttribute('data-query');
            const chipLabel = chip.textContent.trim().replace(/^[✦•\s]+/, '');
            handleUserQuery(chipLabel, queryKey);
        });
    });

    // Form Submit Handler
    if (aiForm && aiInput) {
        aiForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const text = aiInput.value;
            if (!text || !text.trim()) return;
            aiInput.value = '';
            handleUserQuery(text);
        });
    }

    /* ==========================================================================
       7. LEGAL MODAL (PRIVACY & TERMS)
       ========================================================================== */
    const legalModal = document.getElementById('legal-modal');
    const legalOpenButtons = document.querySelectorAll('.js-legal-open');
    const legalCloseButtons = document.querySelectorAll('.js-legal-close');
    const legalTitle = document.querySelector('.js-legal-title');
    const legalContent = document.querySelector('.js-legal-content');

    const openLegalModal = (type) => {
        if (!legalModal) return;
        if (type === 'privacy') {
            if (legalTitle) legalTitle.textContent = 'Privacy Policy';
            if (legalContent) {
                legalContent.innerHTML = `
                    <p>At DERMORA, patient confidentiality and medical ethics are foundational. In this Phase 1 portfolio presentation, no patient data is persistently stored.</p>
                    <p>Upon commercial onboarding, all medical records, photography consent forms, and diagnostic notes are safeguarded under strict international healthcare confidentiality standards.</p>
                `;
            }
        } else {
            if (legalTitle) legalTitle.textContent = 'Terms of Service';
            if (legalContent) {
                legalContent.innerHTML = `
                    <p>Welcome to the DERMORA aesthetic dermatology digital portal.</p>
                    <p>All aesthetic treatments, laser sessions, and clinical peels require an in-person consultation, contraindication screening, and physician supervision prior to administration.</p>
                `;
            }
        }
        legalModal.classList.add('is-open');
        legalModal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    };

    const closeLegalModal = () => {
        if (!legalModal) return;
        legalModal.classList.remove('is-open');
        legalModal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    };

    legalOpenButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const docType = btn.getAttribute('data-type') || 'privacy';
            openLegalModal(docType);
        });
    });

    legalCloseButtons.forEach(btn => {
        btn.addEventListener('click', closeLegalModal);
    });

    /* ==========================================================================
       8. GLOBAL KEYBOARD ESCAPE HANDLING
       ========================================================================== */
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' || e.keyCode === 27) {
            if (aiDrawer && aiDrawer.classList.contains('is-open')) closeAiDrawer();
            if (mobileNav && mobileNav.classList.contains('is-open')) toggleMobileMenu(false);
            if (legalModal && legalModal.classList.contains('is-open')) closeLegalModal();
        }
    });

    /* ==========================================================================
       9. SMOOTH SCROLL FOR IN-PAGE ANCHORS
       ========================================================================== */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#' || targetId.startsWith('#privacy') || targetId.startsWith('#terms')) {
                return;
            }
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    /* ==========================================================================
       10. GSAP SCROLLTRIGGER EDITORIAL ENTRANCES
       ========================================================================== */
    if (!prefersReducedMotion && typeof window.gsap !== 'undefined') {
        const gsap = window.gsap;
        if (typeof window.ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(window.ScrollTrigger);
        }

        // Hero Typography Staggered Reveal (Subtle, calm entrance)
        const heroTexts = document.querySelectorAll('.js-hero-text');
        if (heroTexts.length > 0) {
            gsap.from(heroTexts, {
                opacity: 0,
                y: 18,
                duration: 0.85,
                stagger: 0.12,
                ease: 'power2.out'
            });
        }

        // Hero Background Subtle Parallax Movement (Restrained, smooth)
        const allHeroBgs = document.querySelectorAll('.js-hero-bg, .page-hero__bg');
        if (allHeroBgs.length > 0 && typeof window.ScrollTrigger !== 'undefined') {
            allHeroBgs.forEach(bg => {
                const parentSection = bg.closest('.hero-cinematic, .page-hero') || bg.parentElement;
                gsap.to(bg, {
                    scrollTrigger: {
                        trigger: parentSection,
                        start: 'top top',
                        end: 'bottom top',
                        scrub: true
                    },
                    yPercent: 4,
                    ease: 'none'
                });
            });
        }

        // ScrollTrigger Section & Card Reveals
        if (typeof window.ScrollTrigger !== 'undefined') {
            const reveals = document.querySelectorAll('.js-reveal, .treatment-catalog-card, .concern-catalog-card, .package-card, .journal-card, .environment-card, .benefit-card, .factor-card');
            reveals.forEach(el => {
                gsap.from(el, {
                    scrollTrigger: {
                        trigger: el,
                        start: 'top 95%',
                        toggleActions: 'play none none none'
                    },
                    opacity: 0,
                    y: 18,
                    duration: 0.65,
                    ease: 'power2.out'
                });
            });
        }
    }

    /* ==========================================================================
       11. PHASE 2: INTERACTIVE FILTERS & FORMS
       ========================================================================== */

    // Treatments Catalog Filter
    const treatmentFilterBtns = document.querySelectorAll('.js-filter-btn');
    const treatmentCards = document.querySelectorAll('.js-treatment-card');
    if (treatmentFilterBtns.length > 0 && treatmentCards.length > 0) {
        treatmentFilterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const filter = btn.getAttribute('data-filter');
                treatmentFilterBtns.forEach(b => b.classList.remove('is-active'));
                btn.classList.add('is-active');

                treatmentCards.forEach(card => {
                    const cat = card.getAttribute('data-category');
                    if (filter === 'all' || cat === filter) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // Skin Concerns Catalog Filter
    const concernFilterBtns = document.querySelectorAll('.js-concern-filter');
    const concernCards = document.querySelectorAll('.js-concern-card');
    if (concernFilterBtns.length > 0 && concernCards.length > 0) {
        concernFilterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const filter = btn.getAttribute('data-filter');
                concernFilterBtns.forEach(b => b.classList.remove('is-active'));
                btn.classList.add('is-active');

                concernCards.forEach(card => {
                    const cat = card.getAttribute('data-category');
                    const type = card.getAttribute('data-filter-type');
                    if (filter === 'all' || cat === filter || type === filter) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // Accessible FAQ Accordion Handler
    const faqTriggers = document.querySelectorAll('.js-faq-trigger');
    faqTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const item = trigger.closest('.js-faq-item');
            if (!item) return;
            const panel = item.querySelector('.js-faq-panel');
            const isOpen = item.classList.contains('is-open');

            if (isOpen) {
                item.classList.remove('is-open');
                trigger.setAttribute('aria-expanded', 'false');
                if (panel) panel.setAttribute('hidden', '');
            } else {
                item.classList.add('is-open');
                trigger.setAttribute('aria-expanded', 'true');
                if (panel) panel.removeAttribute('hidden');
            }
        });
    });

    // Interactive Contact Form (Client-side validation & preview)
    const contactForm = document.querySelector('.js-contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            let isValid = true;

            const nameInput = document.getElementById('f-fullname');
            const phoneInput = document.getElementById('f-phone');
            const emailInput = document.getElementById('f-email');
            const subjectSelect = document.getElementById('f-subject');

            const errName = document.querySelector('.js-error-fullname');
            const errPhone = document.querySelector('.js-error-phone');
            const errEmail = document.querySelector('.js-error-email');
            const errSubject = document.querySelector('.js-error-subject');
            const feedbackCard = document.querySelector('.js-form-feedback');

            // Name check
            if (nameInput && nameInput.value.trim().length < 2) {
                isValid = false;
                nameInput.classList.add('is-invalid');
                if (errName) errName.removeAttribute('hidden');
            } else if (nameInput) {
                nameInput.classList.remove('is-invalid');
                if (errName) errName.setAttribute('hidden', '');
            }

            // Phone check
            const phoneVal = phoneInput ? phoneInput.value.trim() : '';
            if (phoneVal.length < 7) {
                isValid = false;
                if (phoneInput) phoneInput.classList.add('is-invalid');
                if (errPhone) errPhone.removeAttribute('hidden');
            } else if (phoneInput) {
                phoneInput.classList.remove('is-invalid');
                if (errPhone) errPhone.setAttribute('hidden', '');
            }

            // Email check
            const emailVal = emailInput ? emailInput.value.trim() : '';
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailVal)) {
                isValid = false;
                if (emailInput) emailInput.classList.add('is-invalid');
                if (errEmail) errEmail.removeAttribute('hidden');
            } else if (emailInput) {
                emailInput.classList.remove('is-invalid');
                if (errEmail) errEmail.setAttribute('hidden', '');
            }

            // Subject check
            if (subjectSelect && (!subjectSelect.value || subjectSelect.value === '')) {
                isValid = false;
                subjectSelect.classList.add('is-invalid');
                if (errSubject) errSubject.removeAttribute('hidden');
            } else if (subjectSelect) {
                subjectSelect.classList.remove('is-invalid');
                if (errSubject) errSubject.setAttribute('hidden', '');
            }

            if (isValid && feedbackCard) {
                const nameDisplay = document.querySelector('.js-feedback-name');
                const subjectDisplay = document.querySelector('.js-feedback-subject');
                if (nameDisplay && nameInput) nameDisplay.textContent = nameInput.value.trim();
                if (subjectDisplay && subjectSelect) subjectDisplay.textContent = subjectSelect.value;

                feedbackCard.removeAttribute('hidden');
                feedbackCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        });
    }
});
