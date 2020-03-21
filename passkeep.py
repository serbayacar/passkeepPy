#!/usr/bin/env python

import argparse
import re
import sys

from src.configs.helpstrings import HelpString
from src.modules.config import Config
from src.modules.crypto import Crypto
from src.modules.file import File
from src.modules.xml import XML


class PassKeep(object):
    config: None

    def __init__(self):
        self.config = Config()
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

        xmlPointer = XML()
        xmlPointer.insert_record(args.alias, args.website, args.username, args.password)
        xmlPointer.write_xml()
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

        xmlPointer = XML()
        record = xmlPointer.remove_record(args.alias, args.website)
        xmlPointer.write_xml()

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

        xmlPointer = XML()
        element = xmlPointer.find_record(args.alias, args.website)

        if element is not None:
            alias_text = element.find("Alias").text
            website_text = element.find("Website").text
            username_text = element.find("Username").text
            password_text = element.find("Password").text
            print("*********************************")
            print(f"Alias: {alias_text}")
            print(f"Website: {website_text}")
            print(f"Username: {username_text}")
            print(f"Password: {password_text}")
            print("*********************************")
        else:
            print("Searched credential is not found!")

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
