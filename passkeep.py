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
            description=HelpString.getMainString("main_description"),
            usage=HelpString.getMainString("help_usage"),
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
            description=HelpString.getMainString("add_description")
        )
        parser.add_argument(
            "--alias",
            required=True,
            action="store",
            help=HelpString.getAddString("arg_alias"),
        )
        parser.add_argument(
            "--website",
            required=True,
            action="store",
            help=HelpString.getAddString("arg_website"),
        )
        parser.add_argument(
            "--username",
            required=True,
            action="store",
            help=HelpString.getAddString("arg_username"),
        )
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "--password", action="store", help=HelpString.getAddString("arg_password")
        )
        group.add_argument(
            "-g",
            action="store_true",
            default=False,
            help=HelpString.getAddString("arg_generate"),
        )
        args = parser.parse_args(sys.argv[2:])

        xmlPointer = XML()
        xmlPointer.insertRecord(
            args.alias, args.website, args.username, args.password)
        xmlPointer.writeXML()
        pass

    def remove(self):
        parser = argparse.ArgumentParser(
            description=HelpString.getRemoveString("remove_description")
        )
        parser.add_argument(
            "--alias", action="store", help=HelpString.getRemoveString("arg_alias")
        )
        parser.add_argument(
            "--website", action="store", help=HelpString.getRemoveString("arg_website")
        )
        args = parser.parse_args(sys.argv[2:])

        aliasRegexElimeter = "[\w:\d.\.\/]+"
        websiteRegexElimeter = "[\w:.\/]+"
        if args.alias is not None:
            aliasRegexElimeter = args.alias
        if args.website is not None:
            websiteRegexElimeter = args.website

        regexString = r"Alias: (?P<alias>{}), Website: (?P<website>{}), Username: (?P<username>[\w:.\/@]+), Password: (?P<password>[\w:\d.\.\/]+)".format(
            aliasRegexElimeter, websiteRegexElimeter
        )

        filePointer = File(self.config.getConfig("main", "credentials_path"))
        data = filePointer.read()

        credent = re.sub(regexString, "", data)
        filePointer.reset(credent)

    def show(self):
        parser = argparse.ArgumentParser(
            description=HelpString.getShowString("show_description")
        )
        parser.add_argument(
            "--alias", action="store", help=HelpString.getShowString("arg_alias")
        )
        parser.add_argument(
            "--website", action="store", help=HelpString.getShowString("arg_website")
        )
        args = parser.parse_args(sys.argv[2:])

        aliasRegexElimeter = "[\w:\d.\.\/]+"
        websiteRegexElimeter = "[\w:.\/]+"
        if args.alias is not None:
            aliasRegexElimeter = args.alias
        if args.website is not None:
            websiteRegexElimeter = args.website

        regexString = r"Alias: (?P<alias>{}), Website: (?P<website>{}), Username: (?P<username>[\w:.\/@]+), Password: (?P<password>[\w:\d.\.\/]+)".format(
            aliasRegexElimeter, websiteRegexElimeter
        )

        filePointer = File(self.config.getConfig("main", "credentials_path"))
        data = filePointer.read()
        credent = re.match(regexString, data)
        if credent is not None:
            print(
                """
*********************************
Alias: {}
Website: {}
Username: {}
Password: {}
*********************************
                  """.format(
                    credent.group("alias"),
                    credent.group("website"),
                    credent.group("username"),
                    credent.group("password"),
                )
            )
        else:
            print("Searched credential is not found")

    def generate(self):
        parser = argparse.ArgumentParser(
            description=HelpString.getGenerateString("generate_description")
        )
        # NOT any arguments
        parser.add_argument(
            "--count",
            action="store",
            default=8,
            type=int,
            help=HelpString.getGenerateString("arg_count"),
        )
        parser.add_argument(
            "--charset",
            action="store",
            help=HelpString.getGenerateString("arg_charset"),
        )
        args = parser.parse_args(sys.argv[2:])

        crypto = Crypto()
        generatedKey = crypto.generate(args.count, args.charset)
        print("Generated PassKey : %s" % generatedKey)

    def config(self):
        parser = argparse.ArgumentParser(
            description=HelpString.getConfigString("config_description")
        )
        # NOT any arguments
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "--set",
            action="store",
            choices=["PUBLIC_KEY", "SECRET_KEY", "CONF_PATH"],
            type=str,
            help=HelpString.getConfigString("arg_set"),
        )
        group.add_argument(
            "--get", action="store", help=HelpString.getConfigString("arg_get")
        )
        parser.add_argument(
            "--value", action="store", help=HelpString.getConfigString("arg_value")
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
            print("Configuration key found ({} : {})".format(args.get, value))
        pass


if __name__ == "__main__":
    PassKeep()
