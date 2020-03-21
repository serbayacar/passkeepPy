class HelpString:
    main = {
        "main_description": "Keep your credentials on local with PassKeepPy",
        "help_usage": """passkeep <command> [<args>]
        The most commonly used git commands are:
        add       Add new credentials to saved as encrypted
        remove    Delete your credentials has been saved
        show      Show your credentials has been saved
        generate  Generate custom username/password
        config    Set program configuration""",
    }

    add = {
        "add_description": "Add new credentials to saved as encrypted",
        ## Arguments help texts
        "arg_alias": "Remembering given shortname",
        "arg_website": "Set Website URL",
        "arg_username": "Set username of credentials",
        "arg_password": "Set password of credentials",
        "arg_generate": "Generate auto password",
    }

    remove = {
        "remove_description": "Delete your credentials has been saved",
        ## Arguments help texts
        "arg_alias": "Deleting given alias",
        "arg_website": "Deleting Website URL",
    }

    show = {
        "show_description": "Show your credentials has been saved",
        ## Arguments help texts
        "arg_alias": "Showing given alias",
        "arg_website": "Showing by  given website url",
    }

    generate = {
        "generate_description": "Generate custom username/password",
        ## Arguments help texts
        "arg_count": "Set character count",
        "arg_charset": "Set specific charset",
    }

    config = {
        "config_description": "Set configuration variables",
        ## Arguments help texts
        "arg_set": "Set config variables to manuplate",
        "arg_get": "Set value of selected configuration variable",
        "arg_value": "Get value of selected configuration variable",
    }

    @staticmethod
    def get_main_string(arg_name):
        return HelpString.main.get(arg_name)

    @staticmethod
    def get_add_string(arg_name):
        return HelpString.add.get(arg_name)

    @staticmethod
    def get_remove_string(arg_name):
        return HelpString.remove.get(arg_name)

    @staticmethod
    def get_show_string(arg_name):
        return HelpString.show.get(arg_name)

    @staticmethod
    def get_generate_string(arg_name):
        return HelpString.generate.get(arg_name)

    @staticmethod
    def get_config_string(arg_name):
        return HelpString.config.get(arg_name)
