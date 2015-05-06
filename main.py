import argparse
import utils

parser = argparse.ArgumentParser()
args = parser.parse_args()

print utils.list_cloudsql_instances(10)