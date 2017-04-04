__author__ = 'robusgauli@gmail.com'

from pqb.exceptions import BadQueryException


class Column(object):
    def __init__(self, name):
        self.name = name
    
    def get_string(self):
        if self.name:
            return str(self.name)
        else:
            raise ValueError('Can\'t convert to string')
            return
    

class QueryBuilder(object):

    def __init__(self):

        self.SELECT  = 'SELECT '
        self.FROM = 'FROM '
        self.WHERE = 'WHERE '

        self.select_query = False
        self.update_query = False
        self.insert_query = False
    
    def select(self, *cols):
        '''This method will chain the columns together'''

        if self.update_query or self.select_query:
            raise BadQuery('Bad Query chaining')

        self.SELECT  += ', '.join(col.get_string() for col in cols)
        #now update the select_query to true
        self.select_query = True
        return self
    
    def _from(self, table):
        self.FROM += table.__tablename__
        return self
    
    def where(self, col, val):
        val = "'{0}'".format(val) if isinstance(val, str) else str(val)
        self.WHERE += (col.get_string() + ' = ' + val)
        return self
    
    def _and(self, col, val):
        val = "'{0}'".format(val) if isinstance(val, str) else str(val)
        self.WHERE += (' and ' + col.get_string()) + ' = ' + val
        return self
    
    def _get_select_query(self):
        return self.SELECT + ' ' + self.FROM + ' '+ self.WHERE

    def __call__(self):
        if self.select_query:
            return self._get_select_query()
    