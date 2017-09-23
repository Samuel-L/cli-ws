from platform import system as system_name
from os import system as system_call


def ping_several_hosts(hosts_list):
    """ Ping all hosts in hosts_list and return dict with statuses of hosts

    :param list hosts_list: a list of hostnames
    :return: dict containing hosts that works and hosts that doesn't work
    :rtype: dict
    """
    WORKING = 1
    NOT_WORKING = 2
    hosts_dict = {WORKING: [], NOT_WORKING: []}

    for host in hosts_list:
        if ping(host):
            hosts_dict[WORKING].append(host)
        else:
            hosts_dict[NOT_WORKING].append(host)

    return hosts_dict


def ping(host):
    """ Retrun True if host responds to a ping

    :param str host: hostname
    :return: True if host responds to ping, false if not
    :rtype: Bool
    """
    parameters = "-n 1" if system_name().lower() == "windows" else "-c 1"

    return system_call(f"ping {parameters} {host}") == 0
