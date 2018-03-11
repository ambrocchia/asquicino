# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

#TODO Move to constant file
COLORS = (
    ('BLUE', u'Bue'),
    ('BLACK', u'Black'),
    ('WHITE', u'White'),
    ('RED', u'Red'),
    ('PINK', u'Pink'),
)

SEASONS = (
    ('W', u'Winter'),
    ('S', u'Summer'),
    ('P', u'Spring'),
    ('A', u'Autumn'),
)

STYLE = (
    ('SPORT', u'Sport'),
    ('ROCK', u'Rock'),
    ('BASIC', u'Basic'),
    ('CHIC', u'Chic'),
)

LAYERS = (
    (1, u'First'),
    (2, u'Second'),
    (3, u'Third'),
    (4, u'Fourth'),
    (5, u'Fifth'),
    (6, u'Sixth'),
    (7, u'Seventh'),
    (8, u'Eigth'),
    (9, u'Nineth'),
    (10, u'Tenth'),
)


class ClothesElement(models.Model):
    """Basic piece of clothes"""
    code = models.CharField(u'Code', max_length=15, db_index=True)
    name = models.CharField(u'Name', max_length=15)
    img = models.ImageField(upload_to='site_media')
    brand = models.CharField(u'Brand', max_length=15, db_index=True)
    description = models.CharField(u'Description')
    active = models.BooleanField(u'Active', default=False)
    colour = ArrayField(models.CharField(u'Colour', max_length=10, choices=COLORS),
            default=list)
    season = ArrayField(models.CharField(u'Season', max_length=4, choices=SEASONS),
            default=list)
    style = ArrayField(models.CharField(u'Style', max_length=10, choices=STYLE),
            default=list)
    layer = ArrayField(models.IntegerField(u'Layer', max_length=10, choices=LAYERS),
            default=list)

