"""DERMORA Treatment Data Registry.

Clinical & aesthetic treatment protocols calibrated for South Asian skin phototypes.
"""

TREATMENTS = {
    "hydrafacial": {
        "slug": "hydrafacial",
        "name": "HydraFacial MD Elite",
        "category": "facial",
        "category_label": "Facial Treatments",
        "short_desc": "Patented vortex extraction, gentle chemical exfoliation, and targeted peptide hydration with zero social downtime.",
        "tagline": "Deep pore purification and radiant barrier replenishment.",
        "image": "thumb-hydrafacial.jpg",
        "banner_image": "treatment-hydrafacial.jpg",
        "primary_concern": "Congestion, Dullness, Enlarged Pores & Barrier Dehydration",
        "duration": "45–60 Minutes",
        "downtime": "Zero Downtime (Immediate Radiance)",
        "frequency": "Monthly or Bi-monthly Maintenance",
        "pricing_note": "Starting from PKR 18,000 per clinical session (Consultation required for customized booster selection)",
        "overview": (
            "HydraFacial MD Elite is a multi-step medical-grade facial treatment combining deep vacuum cleansing, "
            "gentle chemical resurfacing, painless vortex extraction, and concentrated antioxidant-peptide infusion. "
            "Unlike traditional aggressive microdermabrasion, HydraFacial uses hydra-dermabrasion technology that cleanses "
            "and exfoliates while concurrently saturating the skin with nourishing botanical serums, making it exceptionally "
            "well-tolerated across delicate and melanin-rich skin tones."
        ),
        "concerns_addressed": [
            "Enlarged pores and follicular congestion",
            "Superficial dehydration and compromised moisture barrier",
            "Dullness, environmental pollution buildup, and uneven tone",
            "Early fine expression lines and loss of skin elasticity",
            "Keratin buildup and rough skin texture"
        ],
        "how_it_works": [
            {
                "step": "01. Cleanse & Peel",
                "detail": "Gentle mechanical exfoliation with lactic acid and glucosamine uncovers a fresh, radiant layer of skin while softening sebum."
            },
            {
                "step": "02. Painless Vortex Extraction",
                "detail": "A patented spiral tip creates a gentle fluid vortex that suctions out comedones, sebum plugs, and debris from pores without mechanical pinching or tissue trauma."
            },
            {
                "step": "03. Targeted Booster Infusion",
                "detail": "Customized clinical boosters (brightening peptide complexes, hyaluronic acid, or niacinamide) are delivered directly into the prepared dermal layers."
            },
            {
                "step": "04. Barrier Seal & Protect",
                "detail": "High-potency antioxidants and broad-spectrum mineral UV protection lock in hydration and defend against post-treatment environmental oxidative stress."
            }
        ],
        "benefits": [
            "Visibly clearer, unclogged pores and refined skin texture immediately after treatment.",
            "Deep dermal hydration without the redness or flaking typical of aggressive clinical peels.",
            "Enhanced skin radiance and smoother makeup application.",
            "Stimulates micro-circulation for a naturally luminous, refreshed appearance.",
            "Safe for South Asian skin phototypes with minimal risk of post-inflammatory hyperpigmentation (PIH)."
        ],
        "suitability": (
            "HydraFacial MD Elite is suitable for almost all skin types, including sensitive and acne-prone skin. "
            "It is ideal for individuals seeking regular preventive skincare, pre-event radiance, or deep seasonal purification. "
            "However, individuals with active open wounds, severe inflammatory cystic acne flare-ups, or active sunburn "
            "should undergo a preliminary clinical assessment before proceeding."
        ),
        "precautions": [
            "Contraindicated during active facial eczema flare-ups, active oral herpes simplex outbreaks, or severe sunburn.",
            "Patients currently using oral isotretinoin (Accutane) must consult their dermatologist regarding appropriate waiting periods.",
            "Discontinue topical retinoids, AHA/BHA exfoliants, and benzoyl peroxide 48 hours prior to appointment.",
            "Melanin-rich skin: While HydraFacial has an outstanding safety record, high-strength acid boosters must be calibrated to avoid triggering post-inflammatory erythema."
        ],
        "aftercare": [
            "Avoid strenuous workouts, saunas, hot showers, and steam rooms for 24 hours.",
            "Do not apply active acids, retinoids, or physical scrubs for 48 hours post-treatment.",
            "Apply SPF 50+ mineral broad-spectrum sunscreen daily, reapplying every 2–3 hours during sun exposure.",
            "Maintain optimal skin barrier hydration with gentle, fragrance-free ceramide moisturizers."
        ],
        "faqs": [
            {
                "q": "Is there any pain or discomfort during HydraFacial?",
                "a": "No. The procedure is entirely painless and widely described as a cool, soothing sensation similar to a gentle wet massage."
            },
            {
                "q": "How soon will I see results?",
                "a": "Skin clarity, refined pores, and healthy hydration are visible immediately upon completion. The radiant glow typically peaks over the next 48 to 72 hours."
            },
            {
                "q": "How often should I schedule a session?",
                "a": "For sustained skin health and cellular turnover, we recommend scheduling one session every 4 to 6 weeks."
            }
        ],
        "related_concerns": ["enlarged-pores", "dryness-dehydration", "skin-texture", "uneven-skin-tone"]
    },
    "laser-treatments": {
        "slug": "laser-treatments",
        "name": "Calibrated Laser Protocols (Diode & Nd:YAG)",
        "category": "laser",
        "category_label": "Laser Treatments",
        "short_desc": "Triple-wavelength diode and long-pulsed Nd:YAG lasers engineered specifically for safe, effective hair reduction and pigment toning on South Asian skin phototypes III–VI.",
        "tagline": "Safe, high-precision laser dermatology calibrated for melanin depth.",
        "image": "thumb-laser.jpg",
        "banner_image": "treatment-laser-hair.jpg",
        "primary_concern": "Unwanted Hair, Pseudofolliculitis, Folliculitis & Pigment Toning",
        "duration": "30–90 Minutes (depending on treatment area)",
        "downtime": "Minimal (Mild perifollicular erythema resolving within 2–6 hours)",
        "frequency": "6–8 Sessions spaced 4–6 weeks apart",
        "pricing_note": "Package and single session pricing provided upon clinical evaluation and patch testing",
        "overview": (
            "Laser treatments on South Asian and melanin-rich skin require precise physics and deep dermatological understanding. "
            "Because epidermal melanin competes with hair melanin for optical absorption, incorrect wavelength or pulse duration selection "
            "carries risks of hyperpigmentation or burns. At DERMORA, we exclusively employ medical-grade triple-wavelength Diode (808nm) "
            "and long-pulsed Nd:YAG (1064nm) lasers equipped with real-time sapphire contact chilling. The longer 1064nm wavelength bypasses "
            "the melanin in the upper epidermis to safely target the follicular bulb and vascular feeding network."
        ),
        "concerns_addressed": [
            "Coarse, unwanted facial and body hair",
            "Ingrown hairs, razor bumps, and chronic pseudofolliculitis",
            "Post-epilation hyperpigmentation and skin barrier irritation",
            "Hormonal hirsutism management (in coordination with endocrinological guidance)",
            "Superficial pigment irregularity and uneven dermal texture"
        ],
        "how_it_works": [
            {
                "step": "01. Skin Phototype Analysis & Patch Test",
                "detail": "Every patient undergoes Fitzpatrick phototype assessment and a localized patch test 24–48 hours prior to the first full session to confirm exact energy parameters."
            },
            {
                "step": "02. Surface Cleansing & Pre-Cooling",
                "detail": "Treatment areas are sanitized and pre-cooled with continuous sapphire contact cooling (-5°C to 0°C) to protect the epidermal layer from thermal injury."
            },
            {
                "step": "03. Selective Photothermolysis",
                "detail": "Controlled laser pulses deliver optical energy that converts into heat inside the follicular melanin, destroying the germinative cells responsible for hair regrowth."
            },
            {
                "step": "04. Post-Cooling & Soothing Barrier",
                "detail": "Calming medical balms with zinc oxide, panthenol, and cooling thermal compresses soothe treated follicles immediately."
            }
        ],
        "benefits": [
            "Significant, long-term reduction in hair density and thickness across treated areas.",
            "Resolves chronic painful ingrown hairs and rough follicle bumps.",
            "Integrated continuous sapphire contact cooling ensures maximum patient comfort.",
            "Long-pulsed Nd:YAG wavelength minimizes the risk of post-inflammatory pigmentation on Fitzpatrick phototypes III–VI.",
            "Saves time and prevents recurrent skin barrier irritation caused by shaving, waxing, and depilatory creams."
        ],
        "suitability": (
            "Suitable for adults of all genders seeking permanent hair reduction. Exceptionally beneficial for individuals suffering from "
            "recurrent ingrown hairs, folliculitis, or PCOS-related hirsutism. An in-person consultation and patch test are mandatory "
            "before any laser procedure can commence."
        ),
        "precautions": [
            "Strictly avoid sun tanning, bleaching, waxing, plucking, or threading for at least 3 weeks prior to treatment. Only clean shaving is permitted.",
            "Inform our clinical team if you have a history of keloid scarring, photosensitizing medications (e.g., doxycycline), or oral retinoid use.",
            "Laser energy cannot target white, grey, or very light blonde hair due to lack of chromophore melanin.",
            "Pregnancy and active cutaneous infections are strict contraindications."
        ],
        "aftercare": [
            "Apply pure aloe vera or prescribed soothing post-laser cream twice daily for 48 hours.",
            "Avoid hot baths, saunas, vigorous cardiovascular workouts, and swimming pools for 24–48 hours.",
            "Strict sun avoidance and daily application of broad-spectrum SPF 50+ mineral sunscreen are mandatory.",
            "Do not scratch, pick, or scrub treated follicles; shed hairs will naturally expulse over 10–14 days."
        ],
        "faqs": [
            {
                "q": "Is laser safe for Pakistani and brown skin tones?",
                "a": "Yes, when using the correct wavelength. We utilize long-pulsed Nd:YAG (1064nm) and calibrated diode technologies that bypass epidermal melanin to safely target deep follicles without burning surface skin."
            },
            {
                "q": "How many sessions are typically required?",
                "a": "Hair grows in distinct biological cycles (anagen, catagen, telogen). Most patients require between 6 and 8 sessions spaced 4 to 6 weeks apart for 80–90% reduction."
            },
            {
                "q": "Does laser hair removal hurt?",
                "a": "With our integrated sapphire sub-zero contact cooling, sensation is minimal, typically described as a mild rubber band snap."
            }
        ],
        "related_concerns": ["uneven-skin-tone", "skin-texture", "acne-marks", "dark-underarms"]
    },
    "bb-glow": {
        "slug": "bb-glow",
        "name": "BB Glow Meso-Infusion",
        "category": "facial",
        "category_label": "Facial Treatments",
        "short_desc": "Gentle nano-needling micro-infusion of biocompatible peptide ampoules and mineral pigments to restore luminous, uniform skin tone.",
        "tagline": "Semi-permanent radiance and antioxidant peptide revitalization.",
        "image": "thumb-bbglow.jpg",
        "banner_image": "treatment-bbglow.jpg",
        "primary_concern": "Superficial Discoloration, Dullness, Minor Post-Blemish Marks",
        "duration": "60–75 Minutes",
        "downtime": "12–24 Hours (Mild transient pinkness)",
        "frequency": "Series of 3–4 sessions spaced 2 weeks apart",
        "pricing_note": "Price on consultation (Customized based on targeted area and serum formulation)",
        "overview": (
            "BB Glow Meso-Infusion is an advanced non-invasive mesotherapy procedure that utilizes microscopic nano-needles "
            "to deliver biocompatible, plant-derived peptide serums, niacinamide, and micro-encapsulated mineral pigments into the "
            "superficial epidermal layers. Unlike tattoo cosmetics, BB Glow does not penetrate into the dermis. It works as an intensive "
            "cellular booster that encourages collagen synthesis while evening out dullness and minor discoloration for a radiant, bare-faced glow."
        ),
        "concerns_addressed": [
            "Dull, fatigued, and environmentally stressed complexion",
            "Superficial post-acne pigmentation and minor spot marks",
            "Uneven skin tone and loss of natural radiance",
            "Enlarged superficial pores and mild texture irregularity"
        ],
        "how_it_works": [
            {
                "step": "01. Enzymatic Cleansing & Exfoliation",
                "detail": "An enzymatic cleansing foam gently loosens dead stratum corneum cells to optimize micro-channel penetration."
            },
            {
                "step": "02. Meso-Revitalizing Serum Application",
                "detail": "A targeted peptide ampoule packed with hyaluronic acid, niacinamide, and growth factors is smoothed across the face."
            },
            {
                "step": "03. Gentle Nano-Needling Infusion",
                "detail": "Microscopic silicone or surgical-grade nano-pins create temporary micro-channels in the upper epidermis without pain or bleeding."
            },
            {
                "step": "04. Bio-Cellulose Soothing Mask & LED",
                "detail": "A cooling peptide mask and calming LED light therapy soothe the skin, reduce pinkness, and lock in moisture."
            }
        ],
        "benefits": [
            "Delivers an immediate natural radiant glow and revitalized appearance.",
            "Subtly diminishes the appearance of minor skin discolorations and dark spots.",
            "Stimulates natural cellular renewal and collagen synthesis.",
            "Nourishes the skin barrier with deeply absorbed peptides and antioxidants.",
            "Non-surgical with negligible social downtime."
        ],
        "suitability": (
            "BB Glow is suited for patients with dull, uneven skin seeking temporary tone refinement. "
            "Crucially, at DERMORA, we verify that candidate skin has no active inflammatory acne or open pustules. "
            "BB Glow is not a medical cure for deep dermal melasma or systemic hyperpigmentation; our dermatologists ensure "
            "patients understand realistic cosmetic outcomes during preliminary skin assessment."
        ),
        "precautions": [
            "Not suitable for patients with active cystic acne, open blemishes, psoriasis, or active eczema.",
            "A preliminary patch test is performed behind the ear to confirm absence of sensitivity to serum components.",
            "Do not expect permanent skin bleaching or complete erasure of deep melasma; BB Glow is a superficial tone harmonizer.",
            "Avoid if you have a known history of severe contact allergies to cosmetic mineral pigments."
        ],
        "aftercare": [
            "Do not wash the face or apply any cosmetics for at least 12–24 hours post-session.",
            "Strictly avoid sun exposure for 72 hours; apply broad-spectrum mineral sunscreen religiously.",
            "Avoid strenuous exercise, saunas, and swimming pools for 48 hours.",
            "Avoid retinoids, AHAs, BHAs, and facial scrubs for 7 days."
        ],
        "faqs": [
            {
                "q": "Is BB Glow like a permanent cosmetic tattoo?",
                "a": "No. BB Glow uses microscopic nano-needles that operate exclusively within the upper epidermis. The mineral pigments and peptides fade naturally over several weeks as your skin sheds dead cells."
            },
            {
                "q": "How long do the results last?",
                "a": "A single introductory session lasts 1 to 2 weeks. A recommended series of 3 to 4 sessions can provide subtle radiant results lasting 3 to 4 months with proper sun protection."
            },
            {
                "q": "Is the procedure painful?",
                "a": "Most patients report only a mild vibration sensation. Nano-needles do not puncture deep enough to draw blood or cause significant pain."
            }
        ],
        "related_concerns": ["uneven-skin-tone", "pigmentation", "skin-texture", "acne-marks"]
    },
    "dark-underarms": {
        "slug": "dark-underarms",
        "name": "Dark Underarms Protocol",
        "category": "targeted",
        "category_label": "Targeted Skin Areas",
        "short_desc": "Targeted non-ablative Q-switched laser toning, gentle exfoliating chemical peel solutions, and barrier creams designed to reduce friction-induced axillary hyperpigmentation.",
        "tagline": "Gentle, calibrated dermatological protocol for sensitive axillary skin.",
        "image": "thumb-underarms.jpg",
        "banner_image": "thumb-underarms.jpg",
        "primary_concern": "Axillary Friction Darkening, Post-Shaving Irritation, Keratosis",
        "duration": "30–45 Minutes",
        "downtime": "Zero (Immediate return to routine activities)",
        "frequency": "4–6 Sessions spaced 3–4 weeks apart",
        "pricing_note": "Starting from PKR 12,000 per session / Course packages available upon assessment",
        "overview": (
            "Axillary (underarm) hyperpigmentation is extremely common in South Asian skin due to a combination of genetic melanin density, "
            "continuous mechanical friction from clothing, post-inflammatory hyperpigmentation (PIH) caused by shaving or waxing, and harsh chemical deodorants. "
            "In some cases, underarm darkening can also be a dermatological marker of Acanthosis Nigricans associated with insulin resistance. "
            "At DERMORA, we first evaluate the underlying cause, combining low-fluence Q-switched Nd:YAG laser toning with mandelic or lactic acid peels "
            "specifically safe for intertriginous fold areas."
        ),
        "concerns_addressed": [
            "Friction-induced axillary hyperpigmentation",
            "Post-epilation folliculitis and dark blemish spots",
            "Thickened, velvety skin texture in the underarm vault",
            "Deodorant sensitivity and recurrent contact dermatitis marks"
        ],
        "how_it_works": [
            {
                "step": "01. Dermatological Evaluation",
                "detail": "Examination to distinguish between cosmetic friction hyperpigmentation, post-inflammatory pigmentation, and systemic Acanthosis Nigricans."
            },
            {
                "step": "02. Gentle Degreasing & Pre-Treatment",
                "detail": "The underarm vault is cleansed and degreased with a neutral botanical preparation to ensure even penetration."
            },
            {
                "step": "03. Non-Ablative Laser Toning / Gentle Acid Peel",
                "detail": "Low-fluence 1064nm Q-switched laser pulses or mild lipophilic mandelic acid safely shatter excess pigment granules without damaging surface skin."
            },
            {
                "step": "04. Barrier Soothing & Depigmenting Balm",
                "detail": "Medical-grade barrier cream formulated with licorice extract, alpha-arbutin, and niacinamide is applied to prevent reactive rebound pigmentation."
            }
        ],
        "benefits": [
            "Gradual, safe lightening of dark underarm skin without harsh bleaching agents.",
            "Diminishes roughness and bumps caused by chronic shaving irritation.",
            "Non-ablative protocol designed specifically to prevent post-inflammatory hyperpigmentation (PIH) in skin folds.",
            "Improves confidence when wearing sleeveless clothing and sports attire."
        ],
        "suitability": (
            "Suitable for adults experiencing chronic underarm darkening. A clinical evaluation is essential to confirm that darkening "
            "is not related to active fungal infection (erythrasma/tinea versicolor) or unmanaged metabolic imbalances."
        ),
        "precautions": [
            "Do not shave or wax underarms for 48 hours prior to the procedure.",
            "Avoid alcohol-based, scented deodorants and antiperspirants for 48 hours before and after treatment.",
            "Never use aggressive home bleaching concoctions (lemon juice, baking soda), which aggravate inflammation and worsen pigmentation.",
            "If Acanthosis Nigricans is suspected, metabolic screening (fasting blood glucose, HbA1c) will be advised."
        ],
        "aftercare": [
            "Wear loose, breathable cotton clothing to minimize friction against treated axillae.",
            "Use only fragrance-free, roll-on barrier moisturizers recommended by our clinic.",
            "Avoid heavy sweating, intense cardio, hot tubs, and saunas for 24 hours.",
            "Strictly avoid harsh body scrubs or mechanical loofahs."
        ],
        "faqs": [
            {
                "q": "Why do underarms darken in South Asian skin?",
                "a": "Melanin-rich skin responds to irritation, shaving micro-tears, and clothing friction by producing excess protective melanin (post-inflammatory hyperpigmentation). Deodorant alcohol and genetics also play key roles."
            },
            {
                "q": "Can I use deodorant after the session?",
                "a": "We recommend pausing commercial deodorants containing alcohol or synthetic fragrances for 48 hours. A soothing mineral balm will be provided."
            },
            {
                "q": "How many sessions are needed for noticeable improvement?",
                "a": "Because axillary skin is continually subjected to friction, gradual restoration typically requires 4 to 6 sessions along with proper home barrier care."
            }
        ],
        "related_concerns": ["dark-underarms", "pigmentation", "uneven-skin-tone", "skin-texture"]
    },
    "dark-elbows": {
        "slug": "dark-elbows",
        "name": "Dark Elbows Smoothing",
        "category": "targeted",
        "category_label": "Targeted Skin Areas",
        "short_desc": "Deep enzymatic exfoliation, urea-rich keratolytic micro-infusions, and gentle resurfacing to soften thickened stratum corneum and restore even skin tone.",
        "tagline": "Specialized smoothing and depigmenting care for high-friction joints.",
        "image": "thumb-elbows.jpg",
        "banner_image": "thumb-elbows.jpg",
        "primary_concern": "Hyperkeratosis, Friction Joint Darkening, Rough Thickened Skin",
        "duration": "30–45 Minutes",
        "downtime": "Zero (Mild flaking over days 3–5 as thickened skin sheds)",
        "frequency": "3–5 Sessions spaced 3 weeks apart",
        "pricing_note": "Price on consultation / Joint protocol bundles available",
        "overview": (
            "The skin over the olecranon process (elbow) naturally possesses fewer sebaceous glands and a significantly thicker stratum corneum "
            "designed to withstand mechanical stretching. In South Asian individuals, continuous pressure from resting elbows on desks, seated postures, "
            "and natural melanin concentration frequently lead to hyperkeratosis (thickening) combined with hyperpigmentation. "
            "Our Dark Elbows protocol combines medical-strength keratolytics (high-concentration urea and lactic acid) with non-thermal laser toning "
            "to safely dissolve dead keratin layers and illuminate underlying skin."
        ),
        "concerns_addressed": [
            "Rough, leathery texture and thickened skin over elbows",
            "Deep gray or brown hyperpigmentation on joint creases",
            "Severe localized dryness and ashiness resistant to regular body lotions",
            "Post-friction darkening from desk-leaning and work postures"
        ],
        "how_it_works": [
            {
                "step": "01. Skin Thickness Assessment",
                "detail": "Examination of stratum corneum depth and verification that joint darkening is non-arthritic and non-psoriatic."
            },
            {
                "step": "02. Targeted Keratolytic Peel",
                "detail": "Application of a specialized keratolytic compound containing lactic acid and high-purity urea to weaken the bonds between compacted dead skin cells."
            },
            {
                "step": "03. Gentle Micro-Resurfacing / Laser Toning",
                "detail": "Mild acoustic laser pulses shatter localized deep pigment deposits without heat buildup or epidermal blistering."
            },
            {
                "step": "04. Deep Lipid & Ceramide Infusion",
                "detail": "Occlusive application of pharmaceutical-grade ceramides, shea butter, and dimethicone to restore skin pliability and barrier function."
            }
        ],
        "benefits": [
            "Noticeably softer, smoother joint texture within days of the first session.",
            "Gradual lightening of stubborn gray-brown hyperpigmentation.",
            "Restores long-term barrier resilience and elasticity to heavily stressed joint folds.",
            "Eliminates embarrassing dry, rough ashiness when wearing short-sleeved clothing."
        ],
        "suitability": (
            "Suitable for adults with darkened, thickened elbow skin. Not performed over active psoriasis plaques, eczema flares, "
            "or open scrapes."
        ),
        "precautions": [
            "Avoid leaning elbows directly on hard surfaces (desks, tables) without cushioning during the recovery phase.",
            "Do not vigorously scrub with pumice stones or stiff brushes, which triggers protective hyperkeratosis and makes skin darker.",
            "Keep elbows well-moisturized twice daily with the prescribed barrier formulation."
        ],
        "aftercare": [
            "Apply the provided keratolytic barrier balm morning and night.",
            "Avoid hot water showers directly focused on elbows for 48 hours.",
            "Wear soft, non-abrasive cotton sleeves during desk work.",
            "Apply SPF 50+ to elbows when outdoors in sunlit environments."
        ],
        "faqs": [
            {
                "q": "Why are my elbows so much darker than the rest of my arms?",
                "a": "Elbow joints undergo constant friction and pressure. To protect itself, the skin thickens (hyperkeratosis) and melanocytes produce extra pigment. Because elbows lack oil glands, moisture is quickly lost, deepening the dark appearance."
            },
            {
                "q": "Will pumice stones or scrubbing at home help?",
                "a": "No, aggressive scrubbing causes micro-trauma. The skin responds defensively by producing thicker, darker skin. Chemical exfoliation under clinical supervision is the safe approach."
            },
            {
                "q": "How many treatments will I need?",
                "a": "Most patients achieve satisfying softening and visible brightening across 3 to 5 sessions, depending on how chronic the thickening has been."
            }
        ],
        "related_concerns": ["dark-elbows", "skin-texture", "pigmentation", "dark-knuckles"]
    },
    "dark-knuckles": {
        "slug": "dark-knuckles",
        "name": "Dark Knuckles Clarification",
        "category": "targeted",
        "category_label": "Targeted Skin Areas",
        "short_desc": "Safe, low-fluence Nd:YAG laser pulses and depigmenting micro-infusions formulated specifically for delicate finger joint skin.",
        "tagline": "High-precision brightening for delicate hand and finger joints.",
        "image": "thumb-knuckles.jpg",
        "banner_image": "thumb-knuckles.jpg",
        "primary_concern": "Knuckle Hyperpigmentation, Acanthosis Nigricans, Bleach Rebound",
        "duration": "30–40 Minutes",
        "downtime": "Zero (Mild erythema lasting under 1 hour)",
        "frequency": "4–6 Sessions spaced 3 weeks apart",
        "pricing_note": "Price on clinical evaluation / Patch test required prior to first full session",
        "overview": (
            "Dark knuckles represent one of the most complex concerns in aesthetic dermatology. Because hand joint skin is thin, "
            "lacks subcutaneous fat, and is constantly flexed, aggressive treatments or unauthorized OTC bleaching creams often lead to "
            "severe paradoxical hyperpigmentation and skin thinning. At DERMORA, we employ ultra-gentle, non-ablative laser protocols "
            "combined with transdermal antioxidant infusions (glutathione, tranexamic acid, and vitamin C) that clarify pigment "
            "without inciting inflammatory trauma."
        ),
        "concerns_addressed": [
            "Stubborn, localized darkening over proximal and distal interphalangeal joints",
            "Paradoxical darkening caused by past steroid creams or mercury-laden bleaches",
            "Joint hyperkeratosis caused by friction, manual work, or genetics",
            "Uneven hand tone contrasting with forearm complexion"
        ],
        "how_it_works": [
            {
                "step": "01. Dermatological Analysis & History",
                "detail": "Thorough assessment of past cosmetic use to identify steroid-induced thinning or chemical burn before selecting laser parameters."
            },
            {
                "step": "02. Micro-Infusion Preparation",
                "detail": "Application of a gentle enzymatic softener to prepare the knuckle stratum corneum without mechanical abrasion."
            },
            {
                "step": "03. Calibrated Q-Switched Laser Toning",
                "detail": "Sub-photothermal Nd:YAG laser energy targets intracellular melanosomes within knuckle folds with minimal heat spread."
            },
            {
                "step": "04. Transdermal Antioxidant Seal",
                "detail": "Infusion of tranexamic acid, licorice root, and peptide-rich barrier hydrators locked with an intensive ceramide emulsion."
            }
        ],
        "benefits": [
            "Gradual, controlled lightening of knuckle folds without risk of blanching or scarring.",
            "Repairs skin barrier damage caused by prior steroid creams and harsh bleaches.",
            "Restores soft, supple texture to creased knuckle joints.",
            "Blends finger tone seamlessly with natural hand and forearm coloration."
        ],
        "suitability": (
            "Suitable for individuals with chronic knuckle discoloration. A mandatory patch test is performed to guarantee safe "
            "energy absorption on delicate joint skin."
        ),
        "precautions": [
            "Never use unbranded 'whitening' or 'bleaching' creams containing hydroquinone or clobetasol propionate.",
            "Wear protective gloves when handling household detergents, dish soaps, or cleaning chemicals.",
            "Consistently apply mineral sunscreen to the backs of hands and knuckles throughout the day."
        ],
        "aftercare": [
            "Keep hands consistently hydrated with prescribed ceramide hand balms, especially after washing.",
            "Apply SPF 50+ mineral sunscreen to hands and reapply after hand-washing.",
            "Avoid manual tasks that cause intense friction against knuckle joints for 48 hours.",
            "Do not pick, scratch, or physically abrade knuckle skin."
        ],
        "faqs": [
            {
                "q": "Why are knuckles so difficult to lighten?",
                "a": "Knuckle skin is in constant mechanical motion, has few oil glands, and is frequently exposed to hand soaps and sunlight. In South Asian genetics, melanocytes in this region are particularly sensitive to irritation."
            },
            {
                "q": "Can prior damage from fairness creams be reversed?",
                "a": "Yes, but it requires patience and gentle barrier restoration. We first heal damaged, thinned skin before introducing laser toning."
            },
            {
                "q": "How soon will I notice clarification?",
                "a": "Subtle softening of texture is noticeable after 1–2 sessions; visible lightening typically manifests across 4 to 6 sessions."
            }
        ],
        "related_concerns": ["dark-knuckles", "dark-hands", "pigmentation", "skin-texture"]
    },
    "dark-hands": {
        "slug": "dark-hands",
        "name": "Dark Hands Radiance",
        "category": "targeted",
        "category_label": "Targeted Skin Areas",
        "short_desc": "Restores environmental sun-tanned dorsal skin with antioxidants, hydrating hydro-dermabrasion, and broad-spectrum photoprotection guidance.",
        "tagline": "Rejuvenating sun-tanned and environmentally stressed hands.",
        "image": "thumb-hands.jpg",
        "banner_image": "thumb-hands.jpg",
        "primary_concern": "Dorsal Hand Tanning, Photoaging, Loss of Firmness & Ashiness",
        "duration": "40–50 Minutes",
        "downtime": "Zero (Immediate return to daily activities)",
        "frequency": "3–4 Sessions spaced 4 weeks apart",
        "pricing_note": "Starting from PKR 14,000 per session / Hand & wrist rejuvenation package available",
        "overview": (
            "The backs of the hands (dorsal skin) are among the most sun-exposed areas of the body, especially during driving and outdoor routines "
            "in Pakistan's intense solar climate. Hands are washed dozens of times daily, stripping protective natural lipids while rarely receiving "
            "consistent sunscreen reapplication. Over time, this leads to chronic photo-tanning, uneven solar lentigines, loss of collagen, "
            "and pronounced dryness. The DERMORA Dark Hands protocol combines gentle hydra-exfoliation, antioxidant micro-delivery, "
            "and low-fluence laser toning to revive skin tone and elasticity."
        ),
        "concerns_addressed": [
            "Chronic driving and sun-induced dorsal hand tanning",
            "Sunspots, age spots, and mottled pigmentation on hand skin",
            "Thinning, crepey skin texture and prominent superficial veins",
            "Dryness and premature barrier breakdown from harsh soaps"
        ],
        "how_it_works": [
            {
                "step": "01. Hand Hydro-Exfoliation",
                "detail": "Gentle vortex vacuum and lactic acid remove weathered, keratinized surface cells and environmental pollutants."
            },
            {
                "step": "02. Low-Fluence Laser Phototoning",
                "detail": "Gentle laser pulses break apart localized sun-induced melanin clusters without epidermal peeling or downtime."
            },
            {
                "step": "03. Antioxidant & Peptide Infusion",
                "detail": "High-concentration vitamin C, ferulic acid, and hyaluronic acid are transdermally infused to stimulate dermal collagen."
            },
            {
                "step": "04. Intensive Paraffin/Ceramide Occlusion",
                "detail": "A restorative thermal barrier lock drenches the hands in deep hydration and creates an immediate soft, radiant touch."
            }
        ],
        "benefits": [
            "Evens out stubborn driving tans and restores hand color closer to the inner arm tone.",
            "Reduces the appearance of superficial sunspots and textural roughness.",
            "Firms delicate dorsal skin and deeply replenishes lost cellular moisture.",
            "Completely non-invasive with immediate aesthetic improvement."
        ],
        "suitability": (
            "Recommended for anyone troubled by dark, weathered, or aging hands. Especially beneficial for daily commuters and outdoor professionals."
        ),
        "precautions": [
            "Daily commitment to hand sun protection is required to preserve results.",
            "Avoid gel manicures with UV curing lamps immediately after laser sessions.",
            "Always wear protective gloves when washing dishes or handling harsh cleaning solutions."
        ],
        "aftercare": [
            "Apply a broad-spectrum SPF 50+ mineral sunscreen to hands every morning and after washing.",
            "Keep a hydrating travel hand cream containing ceramides and niacinamide readily accessible.",
            "Wear UV-protective driving gloves during sunny commutes."
        ],
        "faqs": [
            {
                "q": "Why do my hands look so much darker than my face?",
                "a": "Hands receive almost equal sun exposure to the face but are washed frequently, removing sunscreen and protective oils. Driving in strong sunlight without UV protection also accelerates hand tanning."
            },
            {
                "q": "Will the treatment make my skin thin or fragile?",
                "a": "No. Our protocol stimulates natural collagen synthesis and repairs the moisture barrier. We do not use thinning cortisone or harsh acids."
            },
            {
                "q": "How long will the hand radiance last?",
                "a": "With consistent sunscreen application and gentle hand care, improvements remain sustained for many months."
            }
        ],
        "related_concerns": ["dark-hands", "dark-knuckles", "uneven-skin-tone", "skin-texture"]
    },
    "dark-ankles": {
        "slug": "dark-ankles",
        "name": "Dark Ankles Restoration",
        "category": "targeted",
        "category_label": "Targeted Skin Areas",
        "short_desc": "Gentle lactic resurfacing, pressure-point hyperkeratosis relief, and deep lipid barrier repair designed for seated pressure zones.",
        "tagline": "Comforting renewal for friction-darkened malleolar joints.",
        "image": "thumb-ankles.jpg",
        "banner_image": "thumb-ankles.jpg",
        "primary_concern": "Malleolar Friction Calluses, Seated Posture Darkening, Joint Roughness",
        "duration": "30–45 Minutes",
        "downtime": "Zero (Gentle micro-peeling over days 4–6)",
        "frequency": "3–5 Sessions spaced 3–4 weeks apart",
        "pricing_note": "Price on consultation / Lower extremity protocols available",
        "overview": (
            "Darkened malleolar joints (ankle bones) are particularly prevalent in South Asian cultures due to regular cross-legged sitting "
            "(palthi/charpoy seating), prayer postures, and friction from stiff footwear or straps. The prominent bony protrusion bears direct "
            "mechanical weight against hard floors, leading the body to develop thick, protective calluses infused with deep melanin deposits. "
            "Our Dark Ankles protocol combines customized lactic-glycolic peels with deep barrier emollients and pressure counseling to soften "
            "compacted keratin and progressively clarify hyperpigmented skin."
        ),
        "concerns_addressed": [
            "Dark, rough patches over the lateral and medial malleolus (ankle bones)",
            "Thickened, callus-like texture from cross-legged seated pressure",
            "Footwear friction marks and chronic strap hyperpigmentation",
            "Severe localized ashiness and rough joint dryness"
        ],
        "how_it_works": [
            {
                "step": "01. Pressure Point Inspection",
                "detail": "Examination to confirm hyperkeratosis and rule out circulatory stasis or deep fungal conditions."
            },
            {
                "step": "02. Targeted Enzymatic Softening",
                "detail": "Application of a specialized softening complex to loosen dense keratin bonds over the ankle prominence."
            },
            {
                "step": "03. Gentle Resurfacing & Laser Clarification",
                "detail": "Safe multi-acid exfoliation and mild non-ablative laser passes disperse localized melanin clusters."
            },
            {
                "step": "04. Intensive Barrier Occlusion",
                "detail": "Application of high-potency ceramide-urea barrier ointment under occlusive dressing for optimal deep absorption."
            }
        ],
        "benefits": [
            "Noticeably softens stubborn, thick calluses over ankle bones.",
            "Progressively clarifies localized dark patches without harsh chemical burns.",
            "Restores smooth, even skin tone to the lower extremities.",
            "Relieves discomfort and roughness caused by continuous floor contact."
        ],
        "suitability": (
            "Ideal for individuals with persistent ankle darkening from seated postures or footwear. Not performed on open ulcers "
            "or active vascular dermatitis."
        ),
        "precautions": [
            "Avoid sitting cross-legged directly on hard tiles or concrete; use soft cushions or mats during recovery.",
            "Never aggressively scrub ankle bones with pumice stones or rasps; mechanical irritation worsens darkening.",
            "Wear soft cotton socks and well-fitted footwear that does not chafe the malleolar bones."
        ],
        "aftercare": [
            "Massage prescribed keratolytic emollient over ankle bones every evening.",
            "Use soft floor mats or cushions when sitting on the floor.",
            "Keep ankles protected from sun exposure with SPF 50+ when wearing open sandals."
        ],
        "faqs": [
            {
                "q": "Why did my ankle bones become so dark?",
                "a": "Sitting cross-legged on hard surfaces creates concentrated pressure and friction against the bone. The body produces excess keratin and melanin to protect the joint, creating a dark, thickened patch."
            },
            {
                "q": "Can I prevent it from returning after treatment?",
                "a": "Yes! Along with our clinic sessions, simply placing a soft cushion or prayer mat under your feet when sitting prevents the mechanical pressure that triggered the darkening initially."
            },
            {
                "q": "How many sessions are recommended?",
                "a": "Because ankle calluses are dense, 3 to 5 sessions spaced 3 to 4 weeks apart deliver the most dramatic and lasting smoothing."
            }
        ],
        "related_concerns": ["dark-ankles", "dark-elbows", "skin-texture", "pigmentation"]
    }
}

