import sublime
import sublime_plugin

"""A simple Sublime Text 3 plugin for python users that uses regular expressions
to estimate the class that the cursor is at. This was made mostly for personal 
use so only osx is supported at this time. 
"""

class ClassfindCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        myClass = None

        # get a list of regions that start with the word 'class' and end at a linebreak
        CLASS_REGEX = '^class\s.*'
        regions = self.view.find_all(CLASS_REGEX, sublime.IGNORECASE)

        if (regions):
            selection = self.view.sel()
            for region in regions:
                if region.end() <= selection[0].begin():
                    # save the region if it comes before the selection
                    myClass = region
                else:
                    if myClass:
                        # only display the last region before the selection
                        window.status_message(self.view.substr(myClass))
                if region.end() <= selection[0].begin() and region == regions[-1] and myClass:
                    # edge case for when the selection is in the last class
                    window.status_message(self.view.substr(myClass))