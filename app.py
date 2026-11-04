"""DERMORA - Advanced Skin & Laser Dermatology.

Phase 2: Complete Website Pages, Treatment Experiences & Content Structure.
Flask application entry point.
"""

from datetime import datetime
import os
from flask import Flask, render_template, abort, redirect, url_for
from config import config_by_name
from data import TREATMENTS, CONCERNS, PACKAGES, PACKAGE_FAQS, FAQS_BY_CATEGORY


def create_app(config_name=None):
    """Application factory for DERMORA."""
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "development")

    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name["default"]))

    # Context processor to inject global clinic branding and metadata into all templates
    @app.context_processor
    def inject_clinic_context():
        return {
            "clinic_name": app.config.get("CLINIC_NAME", "DERMORA"),
            "clinic_tagline": app.config.get(
                "CLINIC_TAGLINE", "Advanced Skin & Laser Dermatology"
            ),
            "clinic_location": app.config.get(
                "CLINIC_LOCATION", "Gulberg III, Lahore, Pakistan"
            ),
            "contact_phone": app.config.get(
                "CONTACT_PHONE_PLACEHOLDER", "+92 (42) 3578-XXXX"
            ),
            "contact_email": app.config.get(
                "CONTACT_EMAIL_PLACEHOLDER", "concierge@dermora.pk"
            ),
            "consultation_hours": app.config.get(
                "CONSULTATION_HOURS", "Monday - Saturday: 10:00 AM - 08:00 PM"
            ),
            "current_year": datetime.now().year,
            "asset_version": int(datetime.now().timestamp()),
            "all_treatments": TREATMENTS,
            "all_concerns": CONCERNS,
        }

    # Core Homepage Route (Phase 1 preserved)
    @app.route("/")
    def index():
        """Renders the DERMORA cinematic homepage."""
        return render_template("index.html")

    # 1. Treatments Overview
    @app.route("/treatments")
    def treatments_overview():
        """Dedicated Treatments landing page with category filtering."""
        return render_template("treatments.html", treatments=TREATMENTS)

    # 2. Individual Treatment Details
    @app.route("/treatments/<slug>")
    def treatment_detail(slug):
        """Dedicated 10-section individual treatment detail page."""
        treatment = TREATMENTS.get(slug)
        if not treatment:
            abort(404)
        # Find related concerns objects for cross-linking
        related_concerns = [
            CONCERNS[c_slug] for c_slug in treatment.get("related_concerns", []) if c_slug in CONCERNS
        ]
        return render_template(
            "treatment_detail.html",
            treatment=treatment,
            related_concerns=related_concerns,
        )

    # 3. Skin Concerns Overview
    @app.route("/concerns")
    def concerns_overview():
        """Dedicated Skin Concerns landing page with category filtering."""
        return render_template("concerns.html", concerns=CONCERNS)

    # 4. Individual Skin Concern Details
    @app.route("/concerns/<slug>")
    def concern_detail(slug):
        """Dedicated individual skin concern detail page."""
        concern = CONCERNS.get(slug)
        if not concern:
            abort(404)
        # Find related treatments objects for cross-linking
        related_treatments = [
            TREATMENTS[t_slug] for t_slug in concern.get("related_treatments", []) if t_slug in TREATMENTS
        ]
        return render_template(
            "concern_detail.html",
            concern=concern,
            related_treatments=related_treatments,
        )

    # 5. Offers & Packages
    @app.route("/packages")
    @app.route("/offers")
    def packages_page():
        """Dedicated Offers & Packages page."""
        return render_template(
            "packages.html",
            packages=PACKAGES,
            package_faqs=PACKAGE_FAQS,
        )

    # 6. Results Journal
    @app.route("/results")
    def results_page():
        """Dedicated Results Journal page with interactive before/after slider."""
        return render_template("results.html")

    # 7. About DERMORA
    @app.route("/about")
    def about_page():
        """Dedicated About DERMORA page."""
        return render_template("about.html")

    # 8. Contact Page
    @app.route("/contact")
    def contact_page():
        """Dedicated Contact & Clinic Suite page with interactive form."""
        return render_template("contact.html")

    # 9. FAQs Page
    @app.route("/faqs")
    def faqs_page():
        """Dedicated Frequently Asked Questions page with accordion navigation."""
        return render_template("faqs.html", faqs_by_category=FAQS_BY_CATEGORY)

    # Direct consultation shortcut
    @app.route("/consultation")
    def consultation():
        return redirect(url_for("contact_page", _anchor="consultation"))

    # Error handling
    @app.errorhandler(404)
    def page_not_found(e):
        return (
            render_template(
                "base.html",
                title="Page Not Found | DERMORA",
                error_code="404",
                error_message="The page you requested could not be located in our clinical registry.",
            ),
            404,
        )

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
