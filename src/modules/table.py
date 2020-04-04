from tabulate import tabulate

class Table:

    @staticmethod
    def createTable(data, headers_data, style_data = 'presto'):
        data = [ data ]
        print(tabulate(data, headers= headers_data, tablefmt= style_data))

