#Copyright (C) 2011 Mark Reid <mindmark@gmail.com>

#This file is part of Project Browser.

#Project Browser is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#Project Browser is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with Project Browser.  If not, see <http://www.gnu.org/licenses/>.

import settings
import utilities
import flipbook_tool

def project_treeview_contextmenu_actions():
    actions =[]
    
    actions.append({'name':'Cut','func':project_cut})
    actions.append({'name':'Copy','func':project_copy})
    actions.append({'name':'Paste','func':project_paste})
    actions.append(None)
    actions.append({'name':'Rename','func':project_rename})
    actions.append({'name':'Delete','func':project_delete})

    return actions

def project_paste(project_item):
    utilities.paste(project_item)

def project_copy(project_item):
    utilities.copy(project_item)

def project_cut(project_item):
    utilities.cut(project_item)

def project_rename(project_item):
    # print project_item
    pass

def project_delete(project_item):
    # print project_item
    pass

def content_treeview_contextmenu_actions():
    
    
    actions =[]
    
    actions.append({'name':'Open','func':open_action})
    actions.append({'name':'Open with...','func':open_with_action})
    actions.append({'name':"Open in %s" % utilities.filebrowser_name().capitalize(),'func':show_content_in_file_browser})
    actions.append({'name':'Open with Packager','func':open_with_packager_action})
    actions.append(None)
    actions.append({'name':'Cut','func':cut_action})
    actions.append({'name':'Copy','func':copy_action})
    actions.append({'name':'Copy Clipboard','func':copy_content_path})
    actions.append(None)
    actions.append({'name':'Rename','func':rename_action})
    actions.append({'name':'Delete','func':delete_action})
    actions.append(None)
    actions.append({'name':"Flipbook",'func':flipbook})

    return actions

def open_with_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()
    utilities.open_with(path)

def open_with_packager_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()    
    utilities.open_packger(path)

def open_action(project_item, file_items):
    path = file_items[0].content.nice_path()
    utilities.open_file(path)

def cut_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()
    utilities.cut(path)

def copy_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()
    utilities.copy(path)

def paste_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()
    utilities.paste(path)

def rename_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()
    utilities.rename(path)

def delete_action(project_item, file_items):
    # print project_item, file_items
    path = file_items[0].content.nice_path()
    utilities.delete(path)


def show_content_in_file_browser(project_item,file_items):
    print 'showing in finder'
    print project_item,file_items
    
    path = file_items[0].content.nice_path()
    utilities.show_file_in_folder(path)

def copy_content_path(project_item,file_items):
    import gui_utilities
    
    paths = []
    
    string = ""
    
    for item in file_items:
        
        path = item.content.path()
        
        paths.append(path)
        #string += '%s\n' % path
        #paths.append(path)
    
    print 'copying content path to clipboard'
    print string
    
    gui_utilities.copy_string_to_clipboard('\n'.join(paths))
    
    
def flipbook(project_item,file_items):
    
    print 'flipbooking'
    #reload(flipbook_tool)
    flipbook_tool.launch_flipbook_tool(file_items)
    