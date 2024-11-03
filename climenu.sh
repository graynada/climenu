#!/usr/bin/env python3
"""
A Command Line Menu utility using simple_term_menu

Provides configuration of 3 types of menu items:
    Menus - A collection of items for display and selection as a menu. It can
       contain, and can be a mixture of, Launchers, Navigators and other Menus
       and can be part of another menu.
    Launchers - When selected it carries out the action, or series of actions
       it defines and exits climenu
    Navigators - Provide menu entries that provide menu navigation. Default
       Navigators avialable are:
           back - goes back one level of menu or exits if at the Home Menu
           home - returns to the Home Menu
           quit - quits climenu

Contents of the menus are set in config.py

Inspired by:

Demonstration example for GitHub Project at
https://github.com/IngoMeyer441/simple-term-menu

This code only works in python3. Install per

    sudo pip3 install simple-term-menu

To fix a problem maybe no one else had :)
"""
import subprocess
import atexit

from classes import *
from config import *
from simple_term_menu import TerminalMenu

exit_action = []

def main():

    # Parameters for simple_term_menu TerminalMenu constructor
    menu_title = "\nCLI menu navigator, press Q or Esc to quit.\n"
    menu_cursor_style = ("fg_green", "bold")
    menu_style = ("bg_green", "fg_black")
    menu_cursor = ""

    menu_trail = [home_menu]

    cli_menu_exit = False

    while not cli_menu_exit:
        active_menu = menu_trail[-1]
        menu_items =[]
        if isinstance(active_menu, Menu):
            menu_path = "\n"
            for level in menu_trail:
                menu_path = menu_path + level.name + "> "
            for item in active_menu.items:
                menu_items.append(item.prefix + item.name)
            display_menu = TerminalMenu(
                menu_items,
                title=menu_title + menu_path,
                menu_cursor=menu_cursor,
                menu_cursor_style=menu_cursor_style,
                menu_highlight_style=menu_style,
                cycle_cursor=True,
                clear_screen=True,
            )
            while active_menu == menu_trail[-1]:
                index_sel = display_menu.show()

                # TerminalMenu.show() returns either and int, an array or None.
                # climenu allows single selection only and needs an index int
                # of the selected item or None, which is treated as back
                # navigation.  This if/else handles the possible show() returns
                if isinstance(index_sel, int):
                    item_sel = active_menu.items[index_sel]
                else:
                    item_sel = back

                # Handle TerminalMenu.show() return selection
                if isinstance(item_sel, Navigator):
                    if item_sel == back and active_menu == home_menu:
                        exit()
                    elif item_sel == back:
                        menu_trail.pop()
                    elif item_sel == home:
                        menu_trail = [home_menu]
                    elif item_sel == quit:
                        exit()
                elif isinstance(item_sel, Launcher):
                    set_exit_action(item_sel.action)
                    exit()
                elif isinstance(item_sel, Menu):
                    menu_trail.append(item_sel)

def set_exit_action(action):
    global exit_action
    exit_action = action

def run_cmd():
    # Detect if action is one or multiple actions
    for index, item in enumerate(exit_action):
        if isinstance(item, Launcher):
            subprocess.call(item.action)
        elif isinstance(item, str) and index == 0:
            subprocess.call(exit_action)
            break

atexit.register(run_cmd)

if __name__ == "__main__":
    main()
