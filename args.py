import argparse
import requests

parser = argparse.ArgumentParser(description='Change host for run tests')
parser.add_argument('testhost', type=str, help='host for run test')
args = parser.parse_args()

if args.testhost == "dev":
    a = requests.get("https://ya.ru")
    print(a.content)
elif args.testhost == "prod":
    b = requests.get("https://google.ru")
    print(b.content)
