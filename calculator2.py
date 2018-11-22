#coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

resultEntry = None
window = None

class Handler:
    def on_window_destroy(self, *args):
        Gtk.main_quit()

    def on_menuitem_activate(self, widget):
        text = widget.get_label()
        if text == 'StyleElementary':
            provider = Gtk.CssProvider()
            provider.load_from_data(open("style/elementary/gtk.css").read())
            apply_css(window, provider)
            window.show_all()
        elif text == 'StyleElementaryDark':
            provider = Gtk.CssProvider()
            provider.load_from_data(open("style/elementary/gtk-dark.css").read())
            apply_css(window, provider)
            window.show_all()
        elif text == 'Exit':
            Gtk.main_quit()
            

    def on_button_clicked(self, widget):
        text = widget.get_label()
        if text == '':
            return
        elif text in "0123456789+-*/.":
            resultEntry.set_text(resultEntry.get_text() + text)
        elif text in "=":
            try:
                resultEntry.set_text('{origin}={result}'.format(
                    origin=resultEntry.get_text(), 
                    result=eval(resultEntry.get_text())))
            except:
                resultEntry.set_text("some error occurs, press cls!")
        elif text in "cls":
            resultEntry.set_text('')

def apply_css(widget, provider):
    Gtk.StyleContext.add_provider(widget.get_style_context(),provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    if isinstance(widget, Gtk.Container):
        widget.forall(apply_css, provider)

if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("calculator.glade")
    builder.connect_signals(Handler())
    window = builder.get_object("window")
    resultEntry = builder.get_object("resultEntry")
    window.show_all()
    Gtk.main()