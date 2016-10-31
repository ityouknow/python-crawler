#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()