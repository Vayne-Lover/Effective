# -*- coding: utf-8 -*-

from sys import exit
from random import randint

class Scene:
  def enter(self):
    print("This scene is not yet configured.Subclass it and implement enter().")
    exit(1)

class Engine:
  def __init__(self,scene_map):
    self.scene_map=scene_map

  def play(self):
    current_scene=self.scene_map.opening_scene()
    last_scene=self.scene_map.next_scene("finished")

    while(current_scene!=last_scene):
      next_scene_name=current_scene.enter()
      current_scene=self.scene_map.next_scene(next_scene_name)

    current_scene.enter()
