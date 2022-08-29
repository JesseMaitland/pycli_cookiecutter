from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS

from . import version

DESC = """

        <<<---------- {{ cookiecutter.repo_name }} Help -------------->>>

List of Commands:

     version -->  print the project version to the terminal 

"""

# Add your entry points / arguments in this function.....
def parse_args():
    parser = ArgumentParser(description=DESC, formatter_class=RawTextHelpFormatter, usage=SUPPRESS)
    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    debug_parser = sub_parsers.add_parser('debug')
    debug_parser.set_defaults(func=debug)


    return parser.parse_args()
