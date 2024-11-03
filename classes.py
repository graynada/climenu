import subprocess
from abc import ABC

class Item(ABC):
    """An abstract parent classs for all other types of items

    Attributes:
        name (str):     The displayed name of the Item
        prefix (str):   A prefix string that is added before the display name.
                        Can aid identification of type of item or action
                        performed; default ""
    """
    def __init__(self, name, prefix = ""):
        self.name = name
        self.prefix = prefix

class Launcher(Item):
    """A class for launching an action from climenu

    Attributes:
        name (str):     The displayed name of the Launcher
        prefix (str):   A prefix string that is added before the display name.
                        Can aid identification as a Launcher; default "  "
        action ([]):    An array of str that form the cli action to be performed
                        or an array of other launchers.  It cannot be a mix
        shell (bool):   Sets whether to invoke `shell=True`; default  `False`
    """
    def __init__(self,
        name,
        action,
        prefix = "  ",
        shell=False,
    ):
        super().__init__(name, prefix)
        self.action = action
        if shell:
            self.action.append("shell=True")

class Menu(Item):
    """A class for containing other items in climenu, acts as a directory

    Attributes:
        name (str):     The displayed name of the Menu
        prefix (str):   A prefix string that is added before the display name.
                        Can aid identification as a Menu type entry; default "> "
        items ([Item]): An array of climenu Items that form the contents to be
                        displeyed when this menu is selcted; default []
        have_back (bool):  Sets whether the menu has the `back` Navigator; default True
        have_home (bool):  Sets whether the menu has the `home` Navigator; default False
        have_quit (bool):  Sets whether the menu has the `quit` Navigator; default False
    """
    def __init__(self,
        name,
        items = [],
        have_back = True,
        have_home = False,
        have_quit = False,
        prefix = "> "
    ):
        super().__init__(name, prefix)
        if have_back: items.append(back)
        if have_home: items.append(home)
        if have_quit: items.append(quit)
        self.items = items

    def add_item(self, item):
        self.items.insert(-1, item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

class Navigator(Item):
    """A class to define menu navigation Items

    Attributes:
        name (str):     The displayed name of the Navigator
        prefix (str):   A prefix string that is added before the display name.
        Aids identification of the Navigator action; default ""
    """
    def __init__(self, name, prefix):
        super().__init__(name, prefix)

# Navigation items
back = Navigator("Back", "< ")
home = Navigator("Home", "^ ")
quit = Navigator("Quit", "X ")
