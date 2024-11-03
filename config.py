"""
Provides configuration of 3 types of menu items:
    Menus - A collection of items for display and selection as a menu. It can
       contain, and can be a mixture of, Launchers, Navigators and other Menus
       and can be part of another menu.
    Launchers - When selected it carries out the action, or series of actions
       it defines and exits climenu
    Navigators - Provide menu entries that provide menu navigation. Included
       Navigators include:
           back - goes back one level of menu or exits if at the Home Menu
           home - returns to the Home Menu
           quit - quits climenu

The example layout, sub menus are shown on selection of their parent:
    Home>
    > Favourites       (Menu)
        Update         (Launcher)
        Btop           (Launcher)
      < Back           (default Navigator)
    > Files            (Menu)
        Ranger         (Launcher)
      > Places         (Menu)
            Music      (Launcer)
            Downloads  (Launcher)
            Documents  (Launcher)
          < Back       (default Navigator)
          ^ Home       (added Navigator)
    > Internet         (Menu)
        Firefox        (Launcher)
        Brave          (Launcher)
        w3m            (Launcher)
        Thunderbird    (Launcher)
      < Back           (default Navigator)
    > ssh connections  (Menu)
        NAS            (Launcher)
        PiHole         (Launcher)
    X Quit             (Navigator)
"""

from classes import Menu, Launcher

# home_menu is the container for all other items and it's contents are
# display on launch of climenu. Created empty and populated with other
# menus, launchers and navigators after they have been created
home_menu = Menu(
    name="Home",
    have_back=False,
    have_quit=True
)

# Application launchers
btop = Launcher(
    name="btop",
    action=["btop"]
)
ranger = Launcher(
    name="Ranger",
    action=["ranger"]
)
firefox = Launcher(
    name="Firefox",
    action=["nohup", "firefox"]
)
brave = Launcher(
    name="Brave",
    action=["nohup", "brave-browser"]
)
thunderbird = Launcher(
    name="Thunderbird",
    action=["nohup", "thunderbird"]
)
w3m = Launcher(
    name="w3m",
    action=["w3m", "https://duckduckgo.com"]
)

# Place launchers
documents = Launcher(
    name="Nextcloud",
    action=["ranger", "/home/user/Documents"]
)
music = Launcher(
    name="Music",
    action=["ranger", "/home/user/Music"]
)
downloads = Launcher(
    name="Downloads",
    action=["ranger", "/home/user/Downloads"]
)

# Script launchers
update_system = Launcher(
    name="Update system",
    action=["sudo", "apt", "upgrade", "-y"]
)

# ssh launchers
nas = Launcher(
    name="NAS",
    action=["ssh", "-X", "graham@192.168.1.236"]
)
pihole = Launcher(
    name="PiHole",
    action=["ssh", "graham@192.168.1.113"]
)

# Menus
favourite_menu = Menu(
    name="Favourites",
    items=[update_system, btop], prefix="* "
)
places_menu = Menu(
    name="Places",
    items=[music, downloads, documents], have_home=True
)
files_menu = Menu(
    name="Files",
    items=[ranger, places_menu]
)
internet_menu = Menu(
    name="Internet",
    items=[firefox, brave, w3m, thunderbird]
)
ssh_menu = Menu(
    name="SSH connections",
    items=[nas, pihole], have_back=False
)
# Populate home_menu
home_menu.add_items([
    favourite_menu,
    files_menu,
    internet_menu,
    ssh_menu
])
