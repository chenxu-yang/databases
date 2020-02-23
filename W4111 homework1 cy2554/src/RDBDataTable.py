from src.BaseDataTable import BaseDataTable
import pymysql
import logging
import src.SQLHelper as SQLHelper

class RDBDataTable(BaseDataTable):

    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. with extend the
    base class and implement the abstract methods.
    """

    def __init__(self, table_name, connect_info, key_columns):
        """

        :param table_name: Logical name of the table.
        :param connect_info: Dictionary of parameters necessary to connect to the data.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
        """
        self.table_name=table_name
        self.connect_info=connect_info
        self.key_columns=key_columns
    def find_by_primary_key(self, key_fields, field_list=None):
        """

        :param key_fields: The list with the values for the key_columns, in order, to use to find a record.
        :param field_list: A subset of the fields of the record to return.
        :return: None, or a dictionary containing the requested fields for the record identified
            by the key.
        """

        cox = pymysql.connect(**self.connect_info)
        template=dict(zip(self.key_columns,key_fields))
        sql, args = SQLHelper.create_select(self.table_name, template, field_list)
        num, res = SQLHelper.run_q(sql, args,cox)

    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """

        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}
        :param field_list: A list of request fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A list containing dictionaries. A dictionary is in the list representing each record
            that matches the template. The dictionary only contains the requested fields.
        """
        cox = pymysql.connect(**self.connect_info)
        sql, args = SQLHelper.create_select(table_name=self.table_name, template=template, fields=field_list)
        num, res = SQLHelper.run_q(sql, args, cox)
        return res


    def delete_by_key(self, key_fields):
        """

        Deletes the record that matches the key.

        :param template: A template.
        :return: A count of the rows deleted.
        """
        cox = pymysql.connect(**self.connect_info)
        template = dict(zip(self.key_columns, key_fields))
        sql, args = SQLHelper.create_delete(self.table_name, template)
        num, res = SQLHelper.run_q(sql, args, cox)
        return num
    def delete_by_template(self, template):
        """

        :param template: Template to determine rows to delete.
        :return: Number of rows deleted.
        """
        cox = pymysql.connect(**self.connect_info)
        sql, args = SQLHelper.create_delete(table_name=self.table_name, template=template)
        num, res = SQLHelper.run_q(sql, args, cox)
        return num

    def update_by_key(self, key_fields, new_values):
        """

        :param key_fields: List of value for the key fields.
        :param new_values: A dict of field:value to set for updated row.
        :return: Number of rows updated.
        """
        cox = pymysql.connect(**self.connect_info)
        template = dict(zip(self.key_columns, key_fields))
        sql, args = SQLHelper.create_update(self.table_name, new_values, template)
        num, res = SQLHelper.run_q(sql, args, cox)
        return num

    def update_by_template(self, template, new_values):
        """

        :param template: Template for rows to match.
        :param new_values: New values to set for matching fields.
        :return: Number of rows updated.
        """
        cox = pymysql.connect(**self.connect_info)
        sql, args = SQLHelper.create_update(self.table_name, new_values,template)
        num, res = SQLHelper.run_q(sql, args, conn=cox)
        return num

    def insert(self, new_record):
        """

        :param new_record: A dictionary representing a row to add to the set of records.
        :return: None
        """
        cox = pymysql.connect(**self.connect_info)
        sql, args = SQLHelper.create_insert(self.table_name, new_record)
        num, res = SQLHelper.run_q(sql, args, cox)
        return None
    def get_rows(self):
        cox = pymysql.connect(**self.connect_info)
        sql, args = SQLHelper.create_select(self.table_name, None,None)
        num, res = SQLHelper.run_q(sql, args, cox)
        return res






