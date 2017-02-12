"""
 This module contains useful utilities for GeoDjango.
"""
from contextlib import suppress

from django.contrib.gis.gdal import HAS_GDAL
from django.core.exceptions import ImproperlyConfigured

if HAS_GDAL:
    from django.contrib.gis.utils.ogrinfo import ogrinfo  # NOQA
    from django.contrib.gis.utils.ogrinspect import mapping, ogrinspect  # NOQA
    from django.contrib.gis.utils.srs import add_srs_entry  # NOQA
    with suppress(ImproperlyConfigured):
        # LayerMapping requires DJANGO_SETTINGS_MODULE to be set,
        # ImproperlyConfigured is raised if that's not the case.
        from django.contrib.gis.utils.layermapping import LayerMapping, LayerMapError  # NOQA
