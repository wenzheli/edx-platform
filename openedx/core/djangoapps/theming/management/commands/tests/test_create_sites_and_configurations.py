import ddt
from django.test import TestCase
from django.contrib.sites.models import Site
import mock

from django.core.management import call_command, CommandError

SITES = ['site_alpha', 'site_beta']


def _generate_site_config(dns_name, site_domain):
    """ Generate the site configuration for a given site """
    return {
        "lms_url": "{domain}-{dns_name}.sandbox.edx.org".format(domain=site_domain, dns_name=dns_name),
        "platform_name": "{domain}-{dns_name}".format(domain=site_domain, dns_name=dns_name)
    }


def _get_sites(dns_name):
    """ Creates the mocked data for management command """
    sites = {}
    for site in SITES:
        sites.update({
            site: {
                "theme_dir_name": "{}_dir_name".format(site),
                "configuration": _generate_site_config(dns_name, site)
            }
        })
    return sites


class TestCreateSiteAndConfiguration(TestCase):
    """ Test the create_site_and_configuration command """
    def setUp(self):
        super(TestCreateSiteAndConfiguration, self).setUp()

        self.dns_name = 'dummy_dns'
        self.site_count = 2

    def test_without_dns(self):
        """ Test the command without dns_name """
        with self.assertRaises(CommandError):
            call_command(
                "create_sites_and_configurations"
            )

    @mock.patch('openedx.core.djangoapps.theming.management.commands.create_sites_and_configurations.get_sites')
    def test_with_dns(self, mock_get_sites):
        """ Test the command with dns_name """
        mock_get_sites.return_value = _get_sites(self.dns_name)
        call_command(
            "create_sites_and_configurations",
            "--dns-name", self.dns_name
        )

        sites = Site.objects.all()
        for site in sites:
            if site.name in SITES:
                self.assertDictEqual(
                    dict(site.configuration.values),
                    _generate_site_config(self.dns_name, site.name)
                )

