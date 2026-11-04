"""DERMORA Configuration module.

Defines application settings and environment-based configurations.
Designed for maintainability and seamless transition from Phase 1 portfolio
prototype to full production deployment in later phases.
"""

import os


class Config:
    """Base configuration class."""

    # Security
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "dermora-phase1-portfolio-dev-secret-key-change-in-prod"
    )

    # Application details
    CLINIC_NAME = "DERMORA"
    CLINIC_TAGLINE = "Advanced Skin & Laser Dermatology"
    CLINIC_LOCATION = "Gulberg III, Lahore, Pakistan"
    CONTACT_PHONE_PLACEHOLDER = "+92 (42) 3578-XXXX"
    CONTACT_EMAIL_PLACEHOLDER = "concierge@dermora.pk"
    CONSULTATION_HOURS = "Monday - Saturday: 10:00 AM - 08:00 PM"

    # Static assets: Disable aggressive browser caching during development
    SEND_FILE_MAX_AGE_DEFAULT = 0


class DevelopmentConfig(Config):
    """Development environment configuration."""

    DEBUG = True
    ENV = "development"
    SEND_FILE_MAX_AGE_DEFAULT = 0


class ProductionConfig(Config):
    """Production environment configuration."""

    DEBUG = False
    ENV = "production"
    # In production, ensure SECRET_KEY is set via environment variable
    SECRET_KEY = os.environ.get("SECRET_KEY", "dermora-production-secure-key")


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

