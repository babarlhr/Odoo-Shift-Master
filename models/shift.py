# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class Shift(models.Model):
	_name = 'ksshiftmaster.shift'
	_description = 'Duty Shift'

	name 			= fields.Char(required=True)
	description 	= fields.Char()
	start_hours		= fields.Integer(required=True)
	start_minutes	= fields.Integer()

# Time can never move backwards. If end < start it is assumed to be in next day.
	end_hours		= fields.Integer(required=True)
	end_minutes		= fields.Integer()
	grace_minutes	= fields.Integer()
# Days or Dates should never be part of shift.

	active			= fields.Boolean('Active?', default=True)
