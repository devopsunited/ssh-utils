import argparse
from ssh_utils import Ssh_utils


def test_rsa(args):
    """ fonction for test_rsa subcommand"""
    ssh_obj = Ssh_utils()
    ssh_obj.execute_test()




# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "testrsa" command
parser_testrsa = subparsers.add_parser('test_rsa', help='test ssh on remote with RSA')
parser_testrsa.set_defaults(func=test_rsa)


try:
    args = parser.parse_args()
    args.func(args)
except Exception as e:
    parser.parse_args(['--help'])