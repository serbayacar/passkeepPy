#!/usr/bin/env python

import argparse
import sys

from src.configs.helpstrings import HelpString
from src.classes.credents import Credentials
from src.classes.password import Password
from src.classes.configurator import Configurator


class PassKeep(object):

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

        password_val = args.password
        if args.g is not False:
            password_val = Password().generate()
            
        try:
            print('\n')
            credent_object = Credentials(args.alias, args.website)
            element = credent_object.insert_record(args.alias, args.website, args.username, password_val)
            credent_object.show(element)
            print('\n Showing credential has been created successfully \n')

        except Warning as war:
            print(war)
            exit(1)

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

        try:
            print('\n')
            credent_object = Credentials(args.alias, args.website)
            credent = credent_object.find_record(args.alias, args.website)
            credent_object.show(credent)
            record = credent_object.remove_record(args.alias, args.website)
            print('\n Showing credential has been romoved successfully \n')
        except Warning as war:
            print(war)
            exit(1)

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


        if (len(sys.argv) > 2) is False:
            credent_object = Credentials('all', 'all')
            elements = credent_object.find_record('all', 'all')
            credent_object.showAll(elements)

        pass

        try:
            print('\n')
            credent_object = Credentials(args.alias, args.website)
            credent = credent_object.find_record(args.alias, args.website)
            credent_object.show(credent)
        except Warning as war:
            print(war)
            exit(1)

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

        try:
            print('\n')
            password = Password(args.count, args.charset).generate()
        except Warning as war:
            print(war)
            exit(1)
        finally:
            password.show(password)

        pass

    def config(self):
        parser = argparse.ArgumentParser(
            description=HelpString.get_config_string("config_description")
        )
        # NOT any arguments
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "--set",
            action="store",
            choices=["CONF_PATH"],
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

        config = Configurator()
        if args.set is not None:
            if args.value is None:
                print("--value option is must be filled")
            else:
                try:    
                    config.setConfig( args.set, args.value)
                except Warning as war:
                    print(war)
                    exit(1)

        if args.get is not None:

            try:    
                value = config.getConfig(args.get)
                print(f"Configuration key found ({args.get} : {value})")
            except Warning as war:
                print(war)
                exit(1)
        pass


if __name__ == "__main__":
    PassKeep()
