import sublime, sublime_plugin
import re

NUMBER_REGEX = r'^\d+$'

class IncrementNumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      selection_str = self.view.substr(region)

      if re.match(NUMBER_REGEX, selection_str):
        detected_number = int(selection_str) + 1
        self.view.replace(edit, region, str(detected_number))

class DecrementNumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      selection_str = self.view.substr(region)

      if re.match(NUMBER_REGEX, selection_str):
        detected_number = int(selection_str) - 1
        self.view.replace(edit, region, str(detected_number))
