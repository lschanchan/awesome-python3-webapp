#!/usr/bin/env python
# -*- coding:utf-8 -*-

from orm import Model, StringField, IntegerField

class User(Model):
	__table__ = 'users'

	id = IntegerField(primary_key = True)
	name = StringField()