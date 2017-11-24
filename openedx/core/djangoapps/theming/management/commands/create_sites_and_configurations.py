
import logging

from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError

from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from openedx.core.djangoapps.theming.models import SiteTheme

logger = logging.getLogger(__name__)


def get_sites(dns_name):

    return {
        "mitxpro": {
            "theme_dir_name": "mitxpro.mit.edu",
            "configuration": {
                "ACTIVATION_EMAIL_SUPPORT_LINK": "https://mitxpro-{}.sandbox.edx.org/contact".format(dns_name),
                "ALWAYS_REDIRECT_HOMEPAGE_TO_DASHBOARD_FOR_AUTHENTICATED_USER": False,
                "CONTACT_EMAIL": "mitxpro@mit.edu",
                "COURSE_ABOUT_VISIBILITY_PERMISSION": "see_about_page",
                "COURSE_CATALOG_VISIBILITY_PERMISSION": "see_in_catalog",
                "COURSE_CATALOG_API_URL": "https://discovery-mitxpro-{}.edx.org/api/v1/".format(dns_name),
                "course_email_from_addr": {
                    "MITProfessionalX": "mitxpro@mit.edu",
                    "MIT xPRO": "MIT xPRO <mitxpro@mit.edu>"
                },
                "course_email_template_name": {
                    "MIT xPRO": "mitxpro"
                },
                "course_org_filter": [
                    "MITxPRO",
                    "MITProfessionalX"
                ],
                "DISPLAY_ACCOUNT_ACTIVATION_MESSAGE_ON_SIDEBAR": True,
                "DISPLAY_COURSE_MODES_ON_DASHBOARD": False,
                "SHOW_ECOMMERCE_REPORTS": False,
                "EDITABLE_SHORT_DESCRIPTION": True,
                "ECOMMERCE_API_URL": "https://https://ecommerce-mitxpro-{}.edx.org/api/v2".format(dns_name),
                "ECOMMERCE_PUBLIC_URL_ROOT": "https://ecommerce-mitxpro-{}.edx.org".format(dns_name),
                "ECOMMERCE_RECEIPT_PAGE_URL": "/checkout/receipt/?order_number=",
                "email_from_address": "mitxpro@mit.edu",
                "ENABLE_COMBINED_LOGIN_REGISTRATION": True,
                "ENABLE_EXTENDED_COURSE_DETAILS": True,
                "ENABLE_MKTG_SITE": False,
                "ENABLE_PAID_COURSE_REGISTRATION": True,
                "ENABLE_SHOPPING_CART": True,
                "ENABLE_SHOPPING_CART_BULK_PURCHASE": False,
                "ENABLE_THIRD_PARTY_AUTH": False,
                "ENABLE_DONATIONS": False,
                "extended_profile_fields": [
                    "first_name",
                    "last_name",
                    "company",
                    "title",
                    "state",
                    "country"
                ],
                "DEFAULT_FROM_EMAIL": "mitxpro@mit.edu",
                "LMS_BASE": "mitxpro-{}.sandbox.edx.org".format(dns_name),
                "LMS_ROOT_URL": "https://mitxpro-{}.sandbox.edx.org".format(dns_name),
                "logo_image_url": "mitxpro-{}.sandbox.edx.org/images/mitx-pro-logo.png".format(dns_name),
                "ORG_LOGO_MAP": {
                    "MIT xPRO": "images/mitx-pro-logo.png"
                },
                "PASSWORD_RESET_SUPPORT_LINK": "https://mitxpro-{}.sandbox.edx.org/contact".format(dns_name),
                "platform_name": "MIT xPro",
                "PLATFORM_NAME": "MIT xPro",
                "REGISTRATION_EXTRA_FIELDS": {
                    "first_name": "required",
                    "last_name": "required",
                    "level_of_education": "required",
                    "gender": "required",
                    "year_of_birth": "required",
                    "mailing_address": "hidden",
                    "goals": "hidden",
                    "terms_of_service": "required",
                    "honor_code": "required",
                    "state": "required",
                    "country": "required",
                    "company": "required",
                    "title": "required"
                },
                "SESSION_COOKIE_DOMAIN": "mitxpro-{}.sandbox.edx.org".format(dns_name),
                "show_homepage_promo_video": False,
                "SHOW_PROGRAMS_ON_DASHBOARD": True,
                "SHOW_SOCIAL_LINKS_IN_FOOTER": {
                    "MIT xPRO": False
                },
                "site_domain": "mitxpro-{}.sandbox.edx.org".format(dns_name),
                "SITE_NAME": "mitxpro-{}.sandbox.edx.org".format(dns_name),
                "SOCIAL_SHARING_SETTINGS": {
                    "CERTIFICATE_FACEBOOK": True,
                    "CERTIFICATE_TWITTER": True
                },
                "student_profile_download_fields": [
                    "id",
                    "username",
                    "name",
                    "email",
                    "language",
                    "location",
                    "year_of_birth",
                    "gender",
                    "level_of_education",
                    "mailing_address",
                    "goals",
                    "meta.first-name",
                    "meta.last-name",
                    "meta.company",
                    "meta.title",
                    "meta.state",
                    "meta.country"
                ],
                "SUPPORT_SITE_LINK": "https://mitxpro-{}.sandbox.edx.org/contact".format(dns_name),
                "urls": {
                    "TOS_AND_HONOR": "https://mitxpro-{}.sandbox.edx.org/tos".format(dns_name),
                    "PRIVACY": "https://mitxpro-{}.sandbox.edx.org/privacy".format(dns_name),
                    "ABOUT": "https://mitxpro-{}.sandbox.edx.org/about".format(dns_name)
                },
                "CREDENTIALS_INTERNAL_SERVICE_URL": "https://mitxpro-{}-certificates.sandbox.org".format(dns_name),
                "CREDENTIALS_PUBLIC_SERVICE_URL": "https://mitxpro-{}-certificates.sandbox.org".format(dns_name),
            }
        },
        "hms": {
            "theme_dir_name": "globalacademy.hms.harvard.edu",
            "configuration": {
                "ALWAYS_REDIRECT_HOMEPAGE_TO_DASHBOARD_FOR_AUTHENTICATED_USER": False,
                "CONTACT_EMAIL": "globalacademy@hms.harvard.edu",
                "COURSE_ABOUT_VISIBILITY_PERMISSION": "see_about_page",
                "COURSE_CATALOG_VISIBILITY_PERMISSION": "see_in_catalog",
                "course_email_from_addr": "globalacademy@hms.harvard.edu",
                "course_email_template_name": "hmsga",
                "course_org_filter": "HarvardMedGlobalAcademy",
                "DISPLAY_ACCOUNT_ACTIVATION_MESSAGE_ON_SIDEBAR": True,
                "DISPLAY_COURSE_MODES_ON_DASHBOARD": False,
                "EDITABLE_SHORT_DESCRIPTION": True,
                "ECOMMERCE_API_URL": "https://https://ecommerce-hms-{}.edx.org/api/v2".format(dns_name),
                "ECOMMERCE_PUBLIC_URL_ROOT": "https://ecommerce-hms-{}.edx.org".format(dns_name),
                "email_from_address": "globalacademy@hms.harvard.edu",
                "ENABLE_COMBINED_LOGIN_REGISTRATION": True,
                "ENABLE_EXTENDED_COURSE_DETAILS": True,
                "ENABLE_MKTG_SITE": False,
                "ENABLE_PAID_COURSE_REGISTRATION": True,
                "COURSE_CATALOG_API_URL": "https://discovery-hms-{}.edx.org/api/v1/".format(dns_name),
                "ENABLED_PROGRAM_TYPES": [
                    "professional-certificate"
                ],
                "ENABLE_SHOPPING_CART": True,
                "ENABLE_SHOPPING_CART_BULK_PURCHASE": False,
                "ENABLE_THIRD_PARTY_AUTH": False,
                "extended_profile_fields": [
                    "first_name",
                    "last_name",
                    "state",
                    "country",
                    "profession",
                    "specialty"
                ],
                "DEFAULT_FROM_EMAIL": "globalacademy@hms.harvard.edu",
                "homepage_promo_video_youtube_id": "8uIB3zoRRNE",
                "LMS_BASE": "hms-{}.sandbox.edx.org".format(dns_name),
                "LMS_ROOT_URL": "https://hms-{}.sandbox.edx.org".format(dns_name),
                "logo_image_url": "hms-{}.sandbox.edx.org/images/hms-logo.png".format(dns_name),
                "PASSWORD_RESET_SUPPORT_LINK": "https://hms-{}.sandbox.edx.org/contact".format(dns_name),
                "platform_name": "Harvard Medical School Global Academy",
                "PLATFORM_NAME": "Harvard Medical School Global Academy",
                "REGISTRATION_EXTRA_FIELDS": {
                    "first_name": "required",
                    "last_name": "required",
                    "level_of_education": "hidden",
                    "gender": "hidden",
                    "profession": "required",
                    "specialty": "required",
                    "year_of_birth": "hidden",
                    "mailing_address": "hidden",
                    "goals": "hidden",
                    "terms_of_service": "required",
                    "honor_code": "hidden",
                    "state": "required",
                    "country": "required"
                },
                "REGISTRATION_FIELD_ORDER": [
                    "email",
                    "name",
                    "username",
                    "password",
                    "first_name",
                    "last_name",
                    "state",
                    "country",
                    "profession",
                    "specialty",
                    "city",
                    "title",
                    "confirm_email",
                    "company",
                    "terms_of_service",
                    "year_of_birth",
                    "level_of_education",
                    "goals",
                    "honor_code",
                    "gender",
                    "mailing_address"
                ],
                "EXTRA_FIELD_OPTIONS": {
                    "profession": [
                        "Physician",
                        "Physician Assistant",
                        "Nurse",
                        "Nurse Practitioner",
                        "Administrator",
                        "Athletic Trainer",
                        "Certified Nurse Midwife",
                        "Chiropractor",
                        "Clergy",
                        "Coach",
                        "Consultant",
                        "Counselor",
                        "Dentist",
                        "Diagnostic Medical Sonographer",
                        "Educator",
                        "Employee of Industry",
                        "Genetic Counselor",
                        "Lawyer",
                        "Massage Therapist",
                        "Nurse Anesthetist",
                        "Nurse Midwife",
                        "Occupational Therapist",
                        "Optometrist",
                        "Pharmacist",
                        "Physical Therapist",
                        "Podiatrist",
                        "Psychologist",
                        "Radiologic Technician",
                        "Registered Dietitian",
                        "Researcher",
                        "Respiratory Therapist",
                        "Scientist",
                        "Social Worker",
                        "Speech Pathologist",
                        "Student",
                        "Technician",
                        "Veterinarian",
                        "Other"
                    ],
                    "specialty": [
                        "Addiction Medicine",
                        "Allergy and Immunology",
                        "Anesthesiology",
                        "Cardiology and Vascular Medicine",
                        "Colon and Rectal Surgery",
                        "Critical Care and Trauma",
                        "Dermatology",
                        "Emergency Medicine",
                        "Endocrinology",
                        "Family Medicine",
                        "Gastroenterology",
                        "Genetics",
                        "Geriatrics",
                        "Healthcare Education and Leadership",
                        "Infectious Disease",
                        "Internal Medicine",
                        "Lifestyle and Mind-Body Medicine",
                        "Medical Genetics and Genomics",
                        "Neonatology",
                        "Nephrology",
                        "Neurology",
                        "Nutrition",
                        "Obstetrics and Gynecology",
                        "Obesity Medicine",
                        "Oncology and Hematology",
                        "Ophthalmology",
                        "Orthopedics",
                        "Otolaryngology",
                        "Pain Medicine",
                        "Palliative Medicine",
                        "Pathology",
                        "Pediatrics and Adolescent Medicine",
                        "Pharmacology",
                        "Physical Medicine & Rehabilitation",
                        "Plastic Surgery",
                        "Podiatry",
                        "Preventative Medicine",
                        "Psychiatry",
                        "Psychology and Mental Health",
                        "Public Health",
                        "Pulmonary Medicine",
                        "Radiology and Nuclear Medicine",
                        "Rheumatology",
                        "Sleep Medicine",
                        "Sports Medicine",
                        "Surgery",
                        "Thoracic Surgery",
                        "Urology",
                        "N/A",
                        "Other"
                    ]
                },
                "rss_urls": {
                    "deans_corner": {
                        "link": "https://hms.harvard.edu/about-hms/deans-corner/deans-blog",
                        "rss": "http://hms.harvard.edu/rss/blog/2685"
                    },
                    "lean_forward": {
                        "link": "https://leanforward.hms.harvard.edu",
                        "rss": "https://leanforward.hms.harvard.edu/feed"
                    },
                    "trends_in_medicine": {
                        "link": "https://trendsinmedicine.wordpress.com",
                        "rss": "https://trendsinmedicine.wordpress.com/feed"
                    }
                },
                "SESSION_COOKIE_DOMAIN": "hms-{}.sandbox.edx.org".format(dns_name),
                "show_homepage_promo_video": True,
                "SHOW_PROGRAMS_ON_DASHBOARD": True,
                "site_domain": "hms-{}.sandbox.edx.org".format(dns_name),
                "SITE_NAME": "hms-{}.sandbox.edx.org".format(dns_name),
                "SOCIAL_SHARING_SETTINGS": {
                    "CERTIFICATE_TWITTER": True,
                    "CERTIFICATE_TWITTER_TEXT": "I just earned a Certificate on Harvard Medical School Global Academy! Check it out:",
                    "DASHBOARD_FACEBOOK": False,
                    "DASHBOARD_TWITTER": True,
                    "TWITTER_BRAND": "@AcademyHMS"
                },
                "student_profile_download_fields": [
                    "id",
                    "username",
                    "name",
                    "email",
                    "language",
                    "location",
                    "year_of_birth",
                    "gender",
                    "level_of_education",
                    "mailing_address",
                    "goals",
                    "meta.first-name",
                    "meta.last-name",
                    "meta.state",
                    "meta.country"
                ],
                "SUPPORT_SITE_LINK": "hms-{}.sandbox.edx.org/contact".format(dns_name),
                "urls": {
                    "TOS_AND_HONOR": "hms-{}.sandbox.edx.org/tos".format(dns_name),
                    "PRIVACY": "hms-{}.sandbox.edx.org/privacy".format(dns_name),
                    "ABOUT": "hms-{}.sandbox.edx.org/about".format(dns_name),
                },
                "CREDENTIALS_INTERNAL_SERVICE_URL": "https://hms-{}-certificates.sandbox.org".format(dns_name),
                "CREDENTIALS_PUBLIC_SERVICE_URL": "https://hms-{}-certificates.sandbox.org".format(dns_name),
            }
        },
        "wharton": {
            "theme_dir_name": "professionaleducation.wharton.upenn.edu",
            "configuration": {
                "ALWAYS_REDIRECT_HOMEPAGE_TO_DASHBOARD_FOR_AUTHENTICATED_USER": False,
                "CONTACT_EMAIL": "whartononlineprofed@wharton.upenn.edu",
                "COURSE_ABOUT_VISIBILITY_PERMISSION": "see_about_page",
                "COURSE_CATALOG_VISIBILITY_PERMISSION": "see_in_catalog",
                "course_email_from_addr": "whartononlineprofed@wharton.upenn.edu",
                "course_email_template_name": "wharton",
                "course_org_filter": "WhartonOnlineProfessionalEd",
                "DISPLAY_ACCOUNT_ACTIVATION_MESSAGE_ON_SIDEBAR": True,
                "DISPLAY_COURSE_MODES_ON_DASHBOARD": False,
                "EDITABLE_SHORT_DESCRIPTION": True,
                "ECOMMERCE_API_URL": "https://ecommerce-wharton-{}.edx.org/api/v2".format(dns_name),
                "ECOMMERCE_PUBLIC_URL_ROOT": "https://ecommerce-wharton-{}.edx.org".format(dns_name),
                "email_from_address": "whartononlineprofed@wharton.upenn.edu",
                "ENABLE_COMBINED_LOGIN_REGISTRATION": True,
                "ENABLE_EXTENDED_COURSE_DETAILS": True,
                "ENABLE_MKTG_SITE": False,
                "ENABLE_PAID_COURSE_REGISTRATION": True,
                "ENABLE_SHOPPING_CART_BULK_PURCHASE": False,
                "ENABLE_THIRD_PARTY_AUTH": False,
                "COURSE_CATALOG_API_URL": "https://discovery-wharton-{}.edx.org/api/v1/".format(dns_name),
                "extended_profile_fields": [
                    "first_name",
                    "last_name",
                    "country"
                ],
                "DEFAULT_FROM_EMAIL": "whartononlineprofed@wharton.upenn.edu",
                "LMS_BASE": "wharton-{}.sandbox.edx.org".format(dns_name),
                "LMS_ROOT_URL": "https://wharton-{}.sandbox.edx.org".format(dns_name),
                "logo_image_url": "wharton-{}.sandbox.edx.org/images/logo.png".format(dns_name),
                "PASSWORD_RESET_SUPPORT_LINK": "https://wharton-{}.sandbox.edx.org/help".format(dns_name),
                "platform_name": "Wharton Online Professional Education",
                "PLATFORM_NAME": "Wharton Online Professional Education",
                "REGISTRATION_EXTRA_FIELDS": {
                    "first_name": "required",
                    "last_name": "required",
                    "level_of_education": "hidden",
                    "gender": "hidden",
                    "year_of_birth": "hidden",
                    "mailing_address": "hidden",
                    "goals": "hidden",
                    "terms_of_service": "required",
                    "honor_code": "required",
                    "state": "hidden",
                    "country": "required"
                },
                "REQUEST_MORE_INFO_EMAIL": "dhall@edx.org",
                "REQUEST_MORE_INFO_URL": "https://hooks.zapier.com/hooks/catch/1942999/hhcp52/",
                "SESSION_COOKIE_DOMAIN": "wharton-{}.sandbox.edx.org".format(dns_name),
                "show_homepage_promo_video": False,
                "site_domain": "wharton-{}.sandbox.edx.org".format(dns_name),
                "SITE_NAME": "wharton-{}.sandbox.edx.org".format(dns_name),
                "student_profile_download_fields": [
                    "id",
                    "username",
                    "name",
                    "email",
                    "language",
                    "location",
                    "meta.first-name",
                    "meta.last-name",
                    "meta.country"
                ],
                "SUPPORT_SITE_LINK": "wharton-{}.sandbox.edx.org/help".format(dns_name),
                "urls": {
                    "TOS_AND_HONOR": "https://wharton-{}.sandbox.edx.org/tos".format(dns_name),
                    "PRIVACY": "https://wharton-{}.sandbox.edx.org/privacy".format(dns_name),
                    "ABOUT": "https://wharton-{}.sandbox.edx.org/about".format(dns_name)
                },
                "CREDENTIALS_INTERNAL_SERVICE_URL": "https://wharton-{}-certificates.sandbox.org".format(dns_name),
                "CREDENTIALS_PUBLIC_SERVICE_URL": "https://wharton-{}-certificates.sandbox.org".format(dns_name),
            }
        },
        "harvardx": {
            "theme_dir_name": "harvardxplus.harvard.edu",
            "configuration": {
                "ALWAYS_REDIRECT_HOMEPAGE_TO_DASHBOARD_FOR_AUTHENTICATED_USER": False,
                "CONTACT_EMAIL": "hxplus-support@edx.org",
                "COURSE_ABOUT_VISIBILITY_PERMISSION": "see_about_page",
                "COURSE_CATALOG_VISIBILITY_PERMISSION": "see_in_catalog",
                "course_email_from_addr": "no-reply@harvardxplus.harvard.edu",
                "course_email_template_name": "harvardxplus",
                "course_org_filter": "HarvardXPLUS",
                "DISPLAY_ACCOUNT_ACTIVATION_MESSAGE_ON_SIDEBAR": True,
                "DISPLAY_COURSE_MODES_ON_DASHBOARD": False,
                "EDITABLE_SHORT_DESCRIPTION": True,
                "ECOMMERCE_API_URL": "https://ecommerce-harvardx-{}.edx.org/api/v2".format(dns_name),
                "ECOMMERCE_PUBLIC_URL_ROOT": "https://ecommerce-harvardx-{}.edx.org".format(dns_name),
                "email_from_address": "hxplus-support@edx.org",
                "ENABLE_COMBINED_LOGIN_REGISTRATION": True,
                "ENABLE_EXTENDED_COURSE_DETAILS": True,
                "ENABLE_MKTG_SITE": False,
                "ENABLE_PAID_COURSE_REGISTRATION": True,
                "ENABLE_SHOPPING_CART": True,
                "ENABLE_SHOPPING_CART_BULK_PURCHASE": False,
                "ENABLE_THIRD_PARTY_AUTH": False,
                "COURSE_CATALOG_API_URL": "https://discovery-harvardx-{}.edx.org/api/v1/".format(dns_name),
                "extended_profile_fields": [
                    "first_name",
                    "last_name",
                    "state",
                    "country"
                ],
                "DEFAULT_FROM_EMAIL": "hxplus-support@edx.org",
                "homepage_promo_video_youtube_id": "yGi5ftN_-Wo",
                "LMS_BASE": "harvardx-{}.sandbox.edx.org".format(dns_name),
                "LMS_ROOT_URL": "https://harvardx-{}.sandbox.edx.org".format(dns_name),
                "logo_image_url": "harvardx-{}.sandbox.edx.org/images/mitx-pro-logo.png".format(dns_name),
                "PASSWORD_RESET_SUPPORT_LINK": "https://harvardx-{}.sandbox.edx.org/contact".format(dns_name),
                "platform_name": "HarvardXPLUS",
                "PLATFORM_NAME": "HarvardXPLUS",
                "REGISTRATION_EXTRA_FIELDS": {
                    "first_name": "required",
                    "last_name": "required",
                    "level_of_education": "optional",
                    "gender": "optional",
                    "year_of_birth": "required",
                    "mailing_address": "hidden",
                    "goals": "hidden",
                    "terms_of_service": "required",
                    "honor_code": "hidden",
                    "state": "required",
                    "country": "required"
                },
                "SESSION_COOKIE_DOMAIN": "harvardx-{}.sandbox.edx.org".format(dns_name),
                "show_homepage_promo_video": True,
                "site_domain": "harvardx-{}.sandbox.edx.org".format(dns_name),
                "SITE_NAME": "harvardx-{}.sandbox.edx.org".format(dns_name),
                "SOCIAL_SHARING_SETTINGS": {
                    "CERTIFICATE_LINKEDIN_MODE_TO_CERT_NAME": {
                        "no-id-professional": "{platform_name} Credential for {course_name}"
                    }
                },
                "student_profile_download_fields": [
                    "id",
                    "username",
                    "name",
                    "email",
                    "language",
                    "location",
                    "year_of_birth",
                    "gender",
                    "level_of_education",
                    "mailing_address",
                    "goals",
                    "meta.first-name",
                    "meta.last-name",
                    "meta.state",
                    "meta.country"
                ],
                "SUPPORT_SITE_LINK": "https://harvardx-{}.sandbox.edx.org/contact".format(dns_name),
                "urls": {
                    "TOS_AND_HONOR": "https://harvardx-{}.sandbox.edx.org/tos".format(dns_name),
                    "PRIVACY": "https://harvardx-{}.sandbox.edx.org/privacy".format(dns_name),
                    "ABOUT": "https://harvardx-{}.sandbox.edx.org/about".format(dns_name)
                },
                "CREDENTIALS_INTERNAL_SERVICE_URL": "https://harvardx-{}-certificates.sandbox.org".format(dns_name),
                "CREDENTIALS_PUBLIC_SERVICE_URL": "https://harvardx-{}-certificates.sandbox.org".format(dns_name),
            }
        }
    }


class Command(BaseCommand):
    """
    Command to create the site, site themes and configuration for all WL-sites.

    Example:
    ./manage.py lms create_sites_and_configurations --dns-name whitelabel
    """

    def add_arguments(self, parser):
        """
        Add arguments to the command parser.
        """

        parser.add_argument(
            '--dns-name',
            type=str,
            help='Enter DNS name of sandbox.',
            required=True
        )

    def handle(self, *args, **options):

        dns_name = options['dns_name']

        logger.info("Creating sites with '{dns_name}' dns name".format(dns_name=dns_name))

        for domain, site_data in get_sites(dns_name).items():

            logger.info("Creating '{domain}' Site".format(domain=domain))
            site, created = Site.objects.get_or_create(
                domain="{domain}-{dns_name}.sandbox.edx.org".format(domain=domain, dns_name=dns_name),
                defaults={"name": domain}
            )
            if created:
                logger.info("Creating '{domain}' SiteTheme".format(domain=domain))
                SiteTheme.objects.create(site=site, theme_dir_name=site_data['theme_dir_name'])

                logger.info("Creating '{domain}' SiteConfiguration".format(domain=domain))
                SiteConfiguration.objects.create(site=site, values=site_data['configuration'], enabled=True)
            else:
                logger.info(" '{}' site already exists".format(domain))
