from tabulate import tabulate

class Table:
    outputformat = 'presto'

    @staticmethod
    def createTable(data, headers_data, style_data = outputformat):
        print(tabulate(data, headers= headers_data, tablefmt= style_data))

