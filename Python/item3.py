#!/usr/local/bin/python
# coding=utf-8
import sys

def to_unicode(unicode_or_str):
  if isinstance(unicode_or_str,str):
    v=unicode_or_str.decode('utf-8')
  else:
    v=unicode_or_str
  return v

def to_str(unicode_or_str):
  if isinstance(unicode_or_str,unicode):
    v=unicode_or_str.encode('utf-8')
  else:
    v=unicode_or_str
  return v

str='十大'
print to_str(str)
print sys.getdefaultencoding()
