# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:30:45 2024

@author: Haroon
"""

from databricks import sql
import os

connection = sql.connect(
                        server_hostname = "dbc-409663c5-8ce7.cloud.databricks.com",
                        http_path = "/sql/1.0/warehouses/6f8737e4c7d463da",
                        access_token = "<access-token>")

cursor = connection.cursor()

cursor.execute("SELECT * from range(10)")
print(cursor.fetchall())

cursor.close()
connection.close()