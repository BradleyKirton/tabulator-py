# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import io
from .. import errors, helpers
from .api import API


class File(API):
    """Loader to load source from filesystem.
    """

    # Public

    def __init__(self, source, encoding=None, **options):
        self.__source = source
        self.__encoding = encoding
        self.__options = options

    def load(self, mode, detect_encoding=True):

        # Prepare source
        schema = 'file://'
        source = self.__source
        if source.startswith(schema):
            source = source.replace(schema, '', 1)

        # Prepare bytes
        bytes = io.open(source, 'rb')

        # Prepare encoding
        encoding = self.__encoding
        if detect_encoding:
            if encoding is None:
                encoding = helpers.detect_encoding(bytes)

        # Return or raise
        if mode == 'b':
            return (bytes, encoding)
        elif mode == 't':
            chars = io.TextIOWrapper(bytes, encoding, **self.__options)
            return chars
        else:
            message = 'Mode %s is not supported' % mode
            raise errors.Error(message)
