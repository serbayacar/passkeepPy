#!/usr/bin/env python

import argparse
import re
import sys

from src.configs.helpstrings import HelpString
from src.modules.xml import XML
from src.classes.credents import Credentials


class PassKeep(object):
    config: None

    def __init__(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_main_string("main_description"),
            usage=HelpString.get_main_string("help_usage"),
        )
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def add(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_main_string("add_description")
        )
        parser.add_argument(
            "--alias",
            required=True,
            action="store",
            help=HelpString.get_add_string("arg_alias"),
        )
        parser.add_argument(
            "--website",
            required=True,
            action="store",
            help=HelpString.get_add_string("arg_website"),
        )
        parser.add_argument(
            "--username",
            required=True,
            action="store",
            help=HelpString.get_add_string("arg_username"),
        )
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "--password", action="store", help=HelpString.get_add_string("arg_password")
        )
        group.add_argument(
            "-g",
            action="store_true",
            default=False,
            help=HelpString.get_add_string("arg_generate"),
        )
        args = parser.parse_args(sys.argv[2:])

        credent_object = Credentials(args.alias, args.website)
        credent_object.insert_record(args.alias, args.website, args.username, args.password)
        pass

    def remove(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_remove_string("remove_description")
        )
        parser.add_argument(
            "--alias", action="store", help=HelpString.get_remove_string("arg_alias")
        )
        parser.add_argument(
            "--website",
            action="store",
            help=HelpString.get_remove_string("arg_website"),
        )
        args = parser.parse_args(sys.argv[2:])

        credent_object = Credentials(args.alias, args.website)
        record = credent_object.remove_record(args.alias, args.website)
        pass

    def show(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_show_string("show_description")
        )
        parser.add_argument(
            "--alias", action="store", help=HelpString.get_show_string("arg_alias")
        )
        parser.add_argument(
            "--website", action="store", help=HelpString.get_show_string("arg_website")
        )
        args = parser.parse_args(sys.argv[2:])

        credent_object = Credentials(args.alias, args.website)
        credent = credent_object.find_record(args.alias, args.website)
        credent_object.show(credent)
        pass


    def generate(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_generate_string("generate_description")
        )
        # NOT any arguments
        parser.add_argument(
            "--count",
            action="store",
            default=8,
            type=int,
            help=HelpString.get_generate_string("arg_count"),
        )
        parser.add_argument(
            "--charset",
            action="store",
            help=HelpString.get_generate_string("arg_charset"),
        )
        args = parser.parse_args(sys.argv[2:])

        crypto = Crypto()
        generatedKey = crypto.generate(args.count, args.charset)
        print(f"Generated PassKey : {generatedKey}")

    def config(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_config_string("config_description")
        )
        # NOT any arguments
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "--set",
            action="store",
            choices=["PUBLIC_KEY", "SECRET_KEY", "CONF_PATH"],
            type=str,
            help=HelpString.get_config_string("arg_set"),
        )
        group.add_argument(
            "--get", action="store", help=HelpString.get_config_string("arg_get")
        )
        parser.add_argument(
            "--value", action="store", help=HelpString.get_config_string("arg_value")
        )
        args = parser.parse_args(sys.argv[2:])

        config = Config()
        if args.set is not None:
            if args.value is None:
                print("--value option is must be filled")
            else:
                config.setConfig("main", args.set, args.value)

        if args.get is not None:
            value = config.getConfig("main", args.get)
            print(f"Configuration key found ({args.get} : {value})")
        pass


if __name__ == "__main__":
    PassKeep()
