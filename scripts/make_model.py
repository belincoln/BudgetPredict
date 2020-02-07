# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:58:39 2020

@author: mczerwinski
"""

key_columns['percent awarded over total amount'] = key_columns.current_total_value_of_award/ key_columns.potential_total_value_of_award
key_columns['percent obligated of potential total award value'] = key_columns.total_dollars_obligated/ key_columns.potential_total_value_of_award
key_columns['percent obligated of total awarded value'] = key_columns.total_dollars_obligated/ key_columns.current_total_value_of_award
