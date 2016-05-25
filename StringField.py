#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Field

class StringField(Field):
	def __init__(self, name = None, primary_key = False, default = None, ddl = 'varchar(100)'):
		super().__init__(name, ddl, primary_key, default)