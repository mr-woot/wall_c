import os
import subprocess
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="WALL_C")

        # set fixed width, resizable=false, and centers window
        self.set_border_width(100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)

        # initialize vertical box
        layout = Gtk.Box(spacing=70)
        self.add(layout)

        #change bg
        button = Gtk.Button("Wall_C")
        button.connect("clicked", self.on_file_clicked)
        layout.add(button)


    def on_file_clicked(self, widget):

        dialog = Gtk.FileChooserDialog("Select image file", None, Gtk.FileChooserAction.OPEN,
                                       ("Open", Gtk.ResponseType.OK,
                                        "Cancel", Gtk.ResponseType.CANCEL))

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("File Selected" + dialog.get_filename())
            #dir_name = dialog.get_current_folder_uri
            FILE_NAME = dialog.get_filename()
            PARAMS = "gsettings set org.gnome.desktop.background picture-uri file://" + FILE_NAME
            subprocess.call(PARAMS,shell=True)
            #print(dir_name)
        elif response == Gtk.ResponseType.CANCEL:
            print("Oops..! Canceled")

        dialog.destroy()


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()