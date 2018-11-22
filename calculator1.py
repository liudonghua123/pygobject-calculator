#coding: utf-8

# 参考文档
# https://pygobject.readthedocs.io/en/latest/getting_started.html
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html#grid
# https://lazka.github.io/pgi-docs/Gtk-3.0/classes.html

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="简易计算器")
        self.initUI()

    def initUI(self):
        # 使用grid布局显示界面
        grid = Gtk.Grid()
        self.add(grid)
        # 定义按钮显示内容
        names = ['', '', '', 'cls',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = Gtk.Button(label=name)
            button.set_hexpand(True)
            button.set_vexpand(True)
            # 设置button的点击事件处理方法
            button.connect("clicked", self.on_button_clicked)
            # 这里的位置需要逆转，依次是 left top width height
            position = position[::-1] + (1, 1)
            grid.attach(button, *position)

        # 设置显示结果的输入框
        self.resultEntry = Gtk.Entry()
        self.resultEntry.set_editable(False)
        self.resultEntry.set_hexpand(True)
        self.resultEntry.set_vexpand(True)
        grid.attach(self.resultEntry, 0, 0, 3, 1)

    def on_button_clicked(self, widget):
        text = widget.get_label()
        if text == '':
            return
        elif text in "0123456789+-*/.":
            self.resultEntry.set_text(self.resultEntry.get_text() + text)
        elif text in "=":
            try:
                self.resultEntry.set_text('{origin}={result}'.format(
                    origin=self.resultEntry.get_text(), 
                    result=eval(self.resultEntry.get_text())))
            except:
                self.resultEntry.set_text("some error occurs, press cls!")
        elif text in "cls":
            self.resultEntry.set_text('')

if __name__ == "__main__":
    window = Window()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()