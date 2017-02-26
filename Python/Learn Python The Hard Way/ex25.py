# -*- coding: utf-8 -*-

def break_word(w):
  return w.split(" ")

def sort_word(w):
  ws=break_word(w)
  return sorted(ws)

def print_first_word(w):
  ws=break_word(w)
  return ws.pop(0)

def print_last_word(w):
  ws=break_word(w)
  return ws.pop(-1)

sentences="All good things come to those who wait."

print(break_word(sentences))

print(sort_word(sentences))

print(print_first_word(sentences))

print(print_last_word(sentences))
