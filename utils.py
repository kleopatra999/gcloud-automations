import json
import subprocess

__author__ = 'gautam'


def list_cloudsql_instances(limit=None):
    args = ['gcloud', 'sql', 'instances', 'list', '--format', 'json']
    if limit:
        args += ['--limit', str(limit)]
    json_result = subprocess.check_output(args)
    return json.loads(json_result)


def assign_ip(instances, async=False):
    """
    Assign an IP to each cloudsql instance
    :param instances: a list of instance dict like instance objects with the key 'instance'
    :param async: run the command with the --async flag. Doesnt wait for the operation to complete
    :return:
    """