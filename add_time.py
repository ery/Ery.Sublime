import sublime, sublime_plugin, datetime

class AddTimeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command("insert_snippet",
      {
        "contents": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
      }
    )
