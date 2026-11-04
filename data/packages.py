"""DERMORA Offers & Packages Registry.

Curated clinical treatment journeys designed around comprehensive skin restoration.
Transparent presentation following medical ethics — no artificial discounts, fake countdown timers,
or misleading guarantees. All clinical packages require an initial in-person assessment.
"""

PACKAGES = [
    {
        "id": "hydration-ritual",
        "name": "The Hydration Ritual",
        "tagline": "Deep Vortex Purification & Intensive Barrier Replenishment",
        "category": "Facial Restoration",
        "description": (
            "A restorative multi-session sequence designed for environmentally stressed, dehydrated, or dulled skin. "
            "Combines patented HydraFacial MD Elite hydra-dermabrasion with tailored peptide boosters and physiological "
            "ceramide infusion to restore cellular bounce and luminous barrier vitality."
        ),
        "included_treatments": [
            "Comprehensive Digital Skin Moisture & Barrier Analysis",
            "HydraFacial MD Elite with Customized Hyaluronic Peptide Booster",
            "Targeted Perk Eye or Lip Barrier Nourishment",
            "Soothing Bio-Cellulose Mask with Calming LED Light Therapy",
            "Personalized Take-Home Barrier Repair Product Guide"
        ],
        "ideal_for": "Dry, dehydrated, or fatigued skin; pre-event radiance; seasonal transitions.",
        "indicative_pricing": "Price on Consultation",
        "pricing_detail": "Course bundles calibrated during consultation based on skin phototype and barrier requirements.",
        "sessions": "Recommended as a 3-Session Ritual spaced 3–4 weeks apart",
        "badge": "Signature Ritual"
    },
    {
        "id": "clear-skin-journey",
        "name": "The Clear Skin Journey",
        "tagline": "Targeted Blemish Clarification & Follicular Decongestion",
        "category": "Clarifying & Acne Care",
        "description": (
            "An integrated dermatological pathway crafted for congested, oily, and breakout-prone complexions. "
            "Focuses on painlessly clearing follicular impactions, reducing superficial inflammation, and preventing "
            "stubborn post-inflammatory hyperpigmentation (PIH) through controlled acid exfoliation and blue-light therapy."
        ),
        "included_treatments": [
            "In-Depth Sebum, Pores & Cutaneous Flora Assessment",
            "Clarifying HydraFacial with Salicylic Vortex Extraction",
            "Calibrated Superficial Mandelic or Lactic Acid Resurfacing",
            "Antibacterial Blue-Light Phototherapy Session",
            "Post-Clarification Anti-Inflammatory Soothing Barrier Infusion"
        ],
        "ideal_for": "Persistent blackheads, enlarged pores, superficial inflammatory blemishes, and excess sebum.",
        "indicative_pricing": "Price on Consultation",
        "pricing_detail": "Tailored based on active lesion severity. Systemic medical therapies coordinated separately if needed.",
        "sessions": "4-Session Progressive Pathway spaced 2–3 weeks apart",
        "badge": "Clinical Protocol"
    },
    {
        "id": "radiance-package",
        "name": "The Radiance Package",
        "tagline": "Antioxidant Revitalisation & Complexion Harmony",
        "category": "Tone & Pigmentation",
        "description": (
            "Designed to address dullness, uneven sun tanning, and superficial tone irregularities. "
            "Unites gentle enzymatic resurfacing, BB Glow meso-revitalisation ampoules, and non-ablative laser toning "
            "to safely disperse clustered pigment and restore uniform natural light reflection."
        ),
        "included_treatments": [
            "Fitzpatrick Phototype & Melanin Distribution Diagnostic",
            "Enzymatic Pre-Cleansing & Micro-Exfoliation",
            "BB Glow Meso-Infusion with Biocompatible Radiance Peptides",
            "Low-Fluence Q-Switched Laser Toning (Pigment Dispersion)",
            "Intensive Antioxidant Glutathione & Vitamin C Barrier Seal"
        ],
        "ideal_for": "Uneven skin tone, sun tanning, post-acne flat marks, and photo-fatigued complexions.",
        "indicative_pricing": "Price on Consultation",
        "pricing_detail": "Customized to individual pigment density and targeted facial or neck areas.",
        "sessions": "3 to 4 Sessions spaced 2–3 weeks apart",
        "badge": "Editorial Beauty"
    },
    {
        "id": "laser-care-package",
        "name": "The Melanin-Calibrated Laser Package",
        "tagline": "Precision Follicular Reduction Engineered for South Asian Phototypes",
        "category": "Laser Dermatology",
        "description": (
            "A structured course of medical-grade laser hair reduction using long-pulsed Nd:YAG (1064nm) and diode wavelengths. "
            "Specifically programmed for Pakistani and South Asian skin tones to ensure profound follicular reduction while "
            "completely safeguarding epidermal melanocytes with continuous sub-zero sapphire cooling."
        ),
        "included_treatments": [
            "Fitzpatrick Phototype Evaluation & Mandatory Localized Patch Test",
            "Targeted Treatment Area Preparation & Continuous Contact Cooling",
            "Long-Pulsed Nd:YAG or Diode Laser Session Calibrated to Melanin Density",
            "Immediate Post-Laser Thermal Soothing & Barrier Calming Application",
            "Post-Care Anti-Inflammatory Cream Support"
        ],
        "ideal_for": "Unwanted facial or body hair, chronic ingrown hairs, folliculitis, and sensitive skin irritated by shaving.",
        "indicative_pricing": "Price on Consultation",
        "pricing_detail": "Varies by anatomical treatment area (Full Face, Underarms, Full Arms, Full Legs, Full Body).",
        "sessions": "6 to 8 Sessions spaced 4–6 weeks apart for optimal hair cycle synchronization",
        "badge": "Precision Laser"
    }
]

PACKAGE_FAQS = [
    {
        "q": "Why are prices listed as 'Price on Consultation' rather than a flat fixed rate?",
        "a": (
            "At DERMORA, we practice ethical dermatology. Skin biology, surface area, melanin density, and medical history vary "
            "significantly from person to person. Rather than imposing rigid, generic packages, our clinical practitioners evaluate "
            "your skin in person to recommend the exact number of sessions and boosters required, ensuring you only pay for what your skin genuinely needs."
        )
    },
    {
        "q": "Are consultation fees deductible from treatment packages?",
        "a": (
            "Yes. When you proceed with any multi-session treatment journey or clinical package on the day of your assessment, "
            "your initial clinical consultation fee is credited directly toward your selected package."
        )
    },
    {
        "q": "Can packages be customized between different treatments?",
        "a": (
            "Absolutely. Many patients benefit from synergistic combinations — such as pairing HydraFacial with laser hair reduction "
            "or targeted joint smoothing. Your clinician will formulate a personalized treatment plan during your initial visit."
        )
    },
    {
        "q": "Do you offer installment or payment plan options?",
        "a": (
            "Yes. Multi-session packages can be settled in structured session installments to ensure treatments remain accessible "
            "and comfortable for our patients."
        )
    }
]

