from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS

from .debug import debug

DESC = """

        <<<---------- {{ cookiecutter.repo_name }} Help -------------->>>

List of Commands:

     debug -->  used as a dummy entry point to test your project skelleton! 

"""

# Add your entry points / arguments in this function.....
def parse_args():
    parser = ArgumentParser(description=DESC, formatter_class=RawTextHelpFormatter, usage=SUPPRESS)
    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    debug_parser = sub_parsers.add_parser('debug')
    debug_parser.set_defaults(func=debug)


    return parser.parse_args()
