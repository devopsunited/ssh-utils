import argparse
from ssh_utils import Ssh_utils


def test_rsa(args):
    """ fonction for test_rsa subcommand"""
    ssh_obj = Ssh_utils()
    ssh_obj.execute_test()




# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "config" command
parser_config = subparsers.add_parser('test_rsa', help='test ssh on remote with RSA')
parser_config.set_defaults(func=test_rsa)


try:
    args = parser.parse_args()
    args.func(args)
except Exception as e:
    print(e)
    parser.parse_args(['--help'])