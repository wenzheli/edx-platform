from datetime import datetime, timedelta

import pytz
import sys

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


def is_entitlement_expired(entitlement, policy):
    """
    Determines from the policy if an entitlement can be redeemed, if it has not passed the
    expiration period of policy.expiration_period_days, and has not already been redeemed
    """
    utc = pytz.UTC
    return ((datetime.utcnow().replace(tzinfo=utc) - entitlement.created).days > policy.get('expiration_period_days',
                                                                                            sys.maxint) and
            not entitlement.enrollment_course_run)


def is_entitlement_refundable(entitlement, policy):
    """
    Determines from the policy if an entitlement can still be refunded, if the entitlement has not
    yet been redeemed (enrollment_course_run is NULL) and policy.refund_period_days has not yet passed

    """
    utc = pytz.UTC
    return ((datetime.utcnow().replace(tzinfo=utc) - entitlement.created).days < policy.get('refund_period_days',
                                                                                            sys.maxint) and
            not entitlement.enrollment_course_run)


def is_entitlement_regainable(entitlement, policy):
    """
    Determines from the policy if an entitlement can still be regained by the user, if they choose
    to by leaving and regaining their entitlement within policy.regain_period_days days from start date of
    the course or their redemption, whichever comes later
    """
    if entitlement.enrollment_course_run:
        utc = pytz.UTC
        course_overview = CourseOverview.get_from_id(entitlement.enrollment_course_run.course_id)
        now = datetime.utcnow().replace(tzinfo=utc)
        return ((now - course_overview.start).days < policy.get('regain_period_days', sys.maxint) or
                (now - entitlement.created).days < policy.get('regain_period_days', sys.maxint))
    return False


def get_days_until_expiration(entitlement, policy):
    """
    Returns an integer of number of days until the entitlement expires
    """
    expiry_date = entitlement.created + timedelta(days=policy.get('expiration_period_days', sys.maxint))
    utc = pytz.UTC
    now = datetime.utcnow().replace(tzinfo=utc)
    return (expiry_date - now).days
