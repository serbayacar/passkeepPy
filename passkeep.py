#!/usr/bin/env python

import argparse
import sys
import re

from src.modules.crypto import Crypto
from src.modules.xml import XML
from src.modules.file import File
from src.modules.config import Config

class PassKeep(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Pretends to be git',
            usage='''passkeep <command> [<args>]

                    The most commonly used git commands are:
                    add       Add new credentials to saved as encrypted
                    remove    Delete your credentials has been saved
                    show      Show your credentials has been saved
                    generate  Generate custom username/password
                    config    Set program configuration
                    ''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def add(self):
        parser = argparse.ArgumentParser(
            description='Add new credentials to saved as encrypted')
        # prefixing the argument with -- means it's optional
        parser.add_argument('--alias', required=True, action='store', help='Remembering given shortname')
        parser.add_argument('--website', required=True, action='store', help='Set Website URL')
        parser.add_argument('--username', required=True, action='store', help='Set username of credentials')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--password', action='store', help='Set password of credentials')
        group.add_argument('-g', action='store_true', default= False, help= 'Generate auto password')
        args = parser.parse_args(sys.argv[2:])
    
        credentString = 'Alias: {}, Website: {}, Username: {}, Password: {}'.format( args.alias, args.website, args.username, args.password)
        filePointer = File('./credentials.txt')
        filePointer.write(credentString)
        pass

    def remove(self):
        parser = argparse.ArgumentParser(
            description='Delete your credentials has been saved')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('--alias')
        parser.add_argument('--website', action='store_true')
        args = parser.parse_args(sys.argv[2:])
        print('Removing, alias=%s' % args.alias)

    def show(self):
        parser = argparse.ArgumentParser(
            description='Show your credentials has been saved')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('--alias', action='store')
        parser.add_argument('--website', action='store')
        args = parser.parse_args(sys.argv[2:])

        aliasRegexElimeter = '[\w:\d.\.\/]+'
        websiteRegexElimeter = '[\w:.\/]+'
        if args.alias is not None:
            aliasRegexElimeter = args.alias
        if args.website is not None:
            websiteRegexElimeter = args.website

        regexString = 'r\'Alias: (?P<alias>{}), Website: (?P<website>{}), Username: (?P<username>[\w:.\/@]+), Password: (?P<password>[\w:\d.\.\/]+)'.format(aliasRegexElimeter, websiteRegexElimeter
        print(regexString)

    def generate(self):
        parser = argparse.ArgumentParser(
            description='Generate custom username/password')
        # NOT any arguments
        parser.add_argument('--count', action='store', default=8, type=int, help='Set character count')
        parser.add_argument('--charset', action='store', help='Set specific charset')
        args = parser.parse_args(sys.argv[2:])
        
        crypto=Crypto()
        generatedKey = crypto.generate(args.count, args.charset)
        print('Generated PassKey : %s' % generatedKey)

    def config(self):
        parser = argparse.ArgumentParser(
            description='Set configuration variables')
        # NOT any arguments
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--set', action='store', choices=['PUBLIC_KEY', 'SECRET_KEY','CONF_PATH'],type=str, help='Set config variables to manuplate')
        group.add_argument('--get', action='store', help='Set value of selected configuration variable')
        parser.add_argument('--value', action='store', help='Set value of selected configuration variable')
        args = parser.parse_args(sys.argv[2:])
        
        config=Config()
        if args.set is not None:
            if args.value is None:
                print('--value option is must be filled')
            else:
                config.setConfig('main', args.set, args.value)
        
        if args.get is not None:
            value = config.getConfig('main', args.get)
            print("Configuration key found ({} : {})".format(args.get,value))
        # generatedKey = crypto.generate(args.count, args.charset)
        # print('Generated PassKey : %s' % generatedKey)
        pass


if __name__ == '__main__':
    PassKeep()