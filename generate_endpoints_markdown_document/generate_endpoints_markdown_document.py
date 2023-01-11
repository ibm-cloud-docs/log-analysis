#!/usr/bin/env python3

import collections
import json
import os

import jinja2
import nslookup
import tabulate

DOMAIN = "logging.cloud.ibm.com"

# To make the IP addresses align nicely we add extra spaces
# if we need to. Given the maximum length of IPv4 address
# ( xxx.xxx.xxx.xxx ) being 12 numbers and 3 dots and we
# add a trailing space we end up with 16.
LENGTH_OF_FULL_IP_ADDRESS_WITH_TRAILING_SPACE = 12 + 3 + 1

def format_ips(list_of_ips):
    formatted_string = ""

    for ip in sorted(list_of_ips):
        padding = LENGTH_OF_FULL_IP_ADDRESS_WITH_TRAILING_SPACE - len(ip)
        formatted_string += ip + (padding * " ")

    return formatted_string


def generate_mapping():
    locations = {
        "in-che": "`Asia Pacific`",
        "jp-osa": "`Asia Pacific`",
        "au-syd": "`Asia Pacific`",
        "jp-tok": "`Asia Pacific`",
        "eu-de": "`Europe`",
        "eu-gb": "`Europe`",
        "us-south": "`North America`",
        "ca-tor": "`North America`",
        "us-east": "`North America`",
        "br-sao": "`South America`",
    }

    envs = {
        "in-che": "`Chennai (in-che)`",
        "us-south": "`Dallas (us-south)`",
        "eu-de": "`Frankfurt (eu-de)`",
        "eu-gb": "`London (eu-gb)`",
        "jp-osa": "`Osaka (jp-osa)`",
        "br-sao": "`Sao Paulo (br-sao)`",
        "au-syd": "`Sydney (au-syd)`",
        "jp-tok": "`Tokyo (jp-tok)`",
        "ca-tor": "`Toronto (ca-tor)`",
        "us-east": "`Washington (us-east)`",
    }

    api_endpoints = ["api", "api.private"]
    ingestion_endpoints = ["logs", "logs.private"]
    syslog_tcp_endpoints = ["syslog-a", "syslog-a.private"]
    syslog_udp_endpoints = ["syslog-u", "syslog-u.private"]
    syslog_tls_endpoints = ["syslog-a", "syslog-a.private"]

    app_endpoints = ["app"]

    q = nslookup.Nslookup()

    service_to_ip_mapping = {
        "api_endpoints": {"public": {}, "private": {}},
        "ingestion_endpoints": {"public": {}, "private": {}},
        "syslog_tcp_endpoints": {"public": {}, "private": {}},
        "syslog_udp_endpoints": {"public": {}, "private": {}},
        "syslog_tls_endpoints": {"public": {}, "private": {}},
        "app_endpoints": {"public": {}, "private": {}},
    }

    for env in envs.keys():
        for endpoint in api_endpoints:
            record = f"{endpoint}.{env}.{DOMAIN}"
            response = q.dns_lookup(record)

            if "private" in endpoint:
                service_to_ip_mapping["api_endpoints"]["private"][env] = {
                    "Region": envs[env],
                    "Private API endpoint": f"`{record}`",
                    "Private IP addresses": format_ips(response.answer),
                    "Ports": "TCP 443   TCP 80",
                }
            else:
                service_to_ip_mapping["api_endpoints"]["public"][env] = {
                    "Region": envs[env],
                    "Public API endpoint": f"`{record}`",
                    "Public IP addresses": format_ips(response.answer),
                    "Ports": "TCP 443   TCP 80",
                }

        for endpoint in ingestion_endpoints:
            record = f"{endpoint}.{env}.{DOMAIN}"
            response = q.dns_lookup(record)

            if "private" in endpoint:
                service_to_ip_mapping["ingestion_endpoints"]["private"][env] = {
                    "Region": envs[env],
                    "Private Ingestion endpoint": f"`{record}`",
                    "Private IP addresses": format_ips(response.answer),
                    "Ports": "TCP 443   TCP 80",
                }
            else:
                service_to_ip_mapping["ingestion_endpoints"]["public"][env] = {
                    "Region": envs[env],
                    "Public Ingestion endpoint": f"`{record}`",
                    "Public IP addresses": format_ips(response.answer),
                    "Ports": "TCP 443   TCP 80",
                }

        for endpoint in syslog_tcp_endpoints:
            record = f"{endpoint}.{env}.{DOMAIN}"
            response = q.dns_lookup(record)

            if "private" in endpoint:
                service_to_ip_mapping["syslog_tcp_endpoints"]["private"][env] = {
                    "Region": envs[env],
                    "Private Syslog TCP Endpoint": f"`syslog://{record}`",
                    "Private IP addresses": format_ips(response.answer),
                }
            else:
                service_to_ip_mapping["syslog_tcp_endpoints"]["public"][env] = {
                    "Region": envs[env],
                    "Public Syslog TCP Endpoint": f"`syslog://{record}`",
                    "Public IP addresses": format_ips(response.answer),
                }

        for endpoint in syslog_udp_endpoints:
            record = f"{endpoint}.{env}.{DOMAIN}"
            response = q.dns_lookup(record)

            if "private" in endpoint:
                service_to_ip_mapping["syslog_udp_endpoints"]["private"][env] = {
                    "Region": envs[env],
                    "Private Syslog UDP Endpoint": f"`syslog://{record}`",
                    "Private IP addresses": format_ips(response.answer),
                }
            else:
                service_to_ip_mapping["syslog_udp_endpoints"]["public"][env] = {
                    "Region": envs[env],
                    "Public Syslog UDP Endpoint": f"`syslog://{record}`",
                    "Public IP addresses": format_ips(response.answer),
                }

        for endpoint in syslog_tls_endpoints:
            record = f"{endpoint}.{env}.{DOMAIN}"
            response = q.dns_lookup(record)

            if "private" in endpoint:
                service_to_ip_mapping["syslog_tls_endpoints"]["private"][env] = {
                    "Region": envs[env],
                    "Private Syslog TLS Endpoint": f"`syslog-tls://{record}`",
                    "Private IP addresses": format_ips(response.answer),
                }
            else:
                service_to_ip_mapping["syslog_tls_endpoints"]["public"][env] = {
                    "Region": envs[env],
                    "Public Syslog TLS Endpoint": f"`syslog-tls://{record}`",
                    "Public IP addresses": format_ips(response.answer),
                }

    for env in locations.keys():
        for endpoint in app_endpoints:
            record = f"{endpoint}.{env}.{DOMAIN}"

            service_to_ip_mapping["app_endpoints"]["public"][env] = {
                "Location": locations[env],
                "Region": envs[env],
                "Public Endpoint": f"`https://{record}`",
            }

    return service_to_ip_mapping


def main():
    mapping = generate_mapping()

    tables = {}

    for table in mapping.keys():
        for type in ["public", "private"]:
            table_name = f"{type}_{table}"
            _table = tabulate.tabulate(
                mapping[table][type].values(),
                tablefmt="github",
                headers="keys",
            )
            tables[table_name] = _table

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            os.path.join(os.path.dirname(__file__), "templates/")
        )
    )
    template = environment.get_template("endpoints.jj2")
    result = template.render(
        public_api_endpoints_table=tables["public_api_endpoints"],
        private_api_endpoints_table=tables["private_api_endpoints"],
        public_ingestion_endpoints_table=tables["public_ingestion_endpoints"],
        private_ingestion_endpoints_table=tables["private_ingestion_endpoints"],
        public_app_endpoints_table=tables["public_app_endpoints"],
        public_syslog_tcp_endpoints_table=tables["public_syslog_tcp_endpoints"],
        private_syslog_tcp_endpoints_table=tables["private_syslog_tcp_endpoints"],
        public_syslog_udp_endpoints_table=tables["public_syslog_udp_endpoints"],
        private_syslog_udp_endpoints_table=tables["private_syslog_udp_endpoints"],
        public_syslog_tls_endpoints_table=tables["public_syslog_tls_endpoints"],
        private_syslog_tls_endpoints_table=tables["private_syslog_tls_endpoints"],
    )

    print(result)


if __name__ == "__main__":
    main()
