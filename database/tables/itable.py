
class ITable:

    def up(self):
        raise Exception('define method up')

    def down(self):
        raise Exception('define method down')

    def getTableName(self):
        raise Exception('define method getTableName')