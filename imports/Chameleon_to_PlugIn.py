#Sanchez Anthony
#04-29-23
#Chameleon 
#Project Description
#This study aims to deepen the understanding of physical objects and their innate imperfections by integrating photogrammetry-based color mapping techniques into digital models, 
#enabling users to visualize and recreate individual real-world objects or environments through an algorithm that transforms point cloud data into color coordinates and represents 
#color intensity based on the number of edges in each pyramid.

import rhinoscriptsyntax as rs
import random
import math
from math import radians
from math import cos
from math import sin
import Rhino.UI
import System.Guid, System.Drawing.Color
import Eto.Drawing as drawing
import Eto.Forms as forms
import scriptcontext as sc
from scriptcontext import escape_test

# User Libraries
#######################################################
import color_tools as ct
import viewport_tools as vt
import user_interface_H as ut
reload (ut)
import user_interface_R as ur
reload (ur)
# Reload all libraries
for module in [ct, vt, ut]:
    reload(module)

#Definitions
#######################################################

#Creates goemtry for pyramid
def trig_circle(sides, radius, center):
    cx, cy, cz = center
    step = int(360/sides)
    points = []
    for i in range(0,360,step):
        angle = radians(i)
        x = cos(angle)*radius + cx
        y = sin(angle)*radius + cy
        z = cz
        point = (x, y, z)
        points.append(point)
    return points

#Creates pyramid
def pyramid(radius, height, sides, center):
    cx, cy, cz = center
    points = trig_circle(sides, radius, center)
    vertex = rs.AddPoint(cx, cy, cz + height)
    points_2 = rs.AddPoints(points)
    lines = []
    for i in points_2:
        line = rs.AddLine(i, vertex)
        lines.append(line)
    surf = rs.AddLoftSrf(lines, loft_type=2, closed=True)
    mirrored_vertex = rs.AddPoint(cx, cy, cz - height)
    mirrored_lines = []
    for i in points_2:
        mirrored_line = rs.AddLine(i, mirrored_vertex)
        mirrored_lines.append(mirrored_line)
    mirrored_surf = rs.AddLoftSrf(mirrored_lines, loft_type=2, closed=True)
    final_geometry = rs.JoinSurfaces([surf, mirrored_surf], True)
    return final_geometry

# Define a function to calculate the color intensity
def color_intensity(color):
    r, g, b = color.R, color.G, color.B
    h, s, v = ct.rgb_to_hsv(r, g, b)
    intensity = int(math.sqrt(0.299 * h**2 + 0.587 * s**2 + 0.114 * v**2))
    return intensity

# Assigns color to objects
def assign_material_color(object, color, transparency):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialTransparency(index, transparency)
    color = rs.CreateColor(color.R, color.G, color.B)
    rs.MaterialColor(index, color)

#Creates Pyramids based on color intensity
def Pyr_Box(depth):
    AddLayer()
    rs.EnableRedraw(False)
    if depth == 0:
        return
    id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    if not id:
        return
    dialog1 = ut.hfactor_dialog()
    dialog2 = ur.rfactor_dialog()
    rc1 = dialog1.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    rc2 = dialog2.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if rc1:
        hfactor = [int(getattr(dialog1, "get_h{}".format(i))()) for i in range(1, 19)]
    points = rs.PointCloudPoints(id)
    point_colors = rs.PointCloudPointColors(id)
    if rc2:
        rfactor = [int(getattr(dialog2, "get_r{}".format(i))()) for i in range(1, 19)]
    points = rs.PointCloudPoints(id)
    point_colors = rs.PointCloudPointColors(id)
    size_map = {
        (0, 20): 3,
        (21, 40): 4,
        (41, 60): 6,
        (61, 80): 8,
        (81, 100): 10,
        (101, 120): 12,
        (121, 140): 14,
        (141, 160): 16,
        (161, 180): 18,
        (181, 200): 22,
        (201, 220): 24,
        (221, 240): 26,
        (241, 260): 28,
        (261, 280): 30,
        (281, 300): 32,
        (301, 320): 34,
        (321, 340): 36,
        (341, 360): 38,
    }
    for point, color in zip(points, point_colors):
        #rs.Sleep(1)
        r, g, b = color.R, color.G, color.B
        h, s, v = ct.rgb_to_hsv(r, g, b)
        intensity = color_intensity(color)
        for i, ((low, high), tri_radius) in enumerate(size_map.items()):
            if low <= intensity <= high:
                layer_name = "Intensity {:02}".format(i + 1)
                rs.CurrentLayer(layer_name)
                pt2 = rs.PointAdd(point, [h, s, v])
                tri = pyramid(rfactor[i], hfactor[i], tri_radius, pt2)
                if random.randint(0, 1) == 1:
                    assign_material_color(tri, color, 0.5)
                else:
                    assign_material_color(tri, color, 0.0)

#Names Layers
def _get_unused_name(prefix):
    number = 1
    while True:
        number_str = str(number)
        name = "{0} {1}".format(prefix, number_str.zfill(2))
        layer = sc.doc.Layers.FindName(name)
        if layer:
            number += 1
        else:
            return name

#Creates Layers
def AddLayer():
    color = System.Drawing.Color.Red
    for i in range(0, 18):
        name = _get_unused_name("Intensity")
        sc.doc.Layers.Add(name, color)

##Image dialog class##
class image_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'Image'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        # Create controls for the dialog
        self.rr_label = forms.Label(Text = 'Rotate right and left:')
        self.rr_textbox = forms.TextBox(Text = None)
        self.ru_label = forms.Label(Text = 'Rotate up and down:')
        self.ru_textbox = forms.TextBox(Text = None)
        
        
        
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.on_close_button_click
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow('Please angle for view port.:')
        layout.AddRow(self.rr_label, self.rr_textbox)
        layout.AddRow(self.ru_label, self.ru_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    # Start of the class functions
    # Get the value of the textbox
    
    
    def get_rr(self):
        return self.rr_textbox.Text
    
    def get_ru(self):
        return self.ru_textbox.Text
    
    
    # Close button click handler
    
    def on_close_button_click(self, sender, e):
        self.rr_textbox.Text = ""
        self.Close(False)
        self.ru_textbox.Text = ""
        self.Close(False)


    # OK button click handler
    def on_ok_button_click(self, sender, e):
        if self.rr_textbox.Text == "":
            self.Close(False)
        elif self.ru_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
    ## End of Dialog Class ##

#Allow user to save image or animtation
def save_file():
    #rs.EnableRedraw (True)
    view_port = "Port"
    dialog = image_dialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        rotate_right = int(dialog.get_rr())
        rotate_up = int(dialog.get_ru())
    vt.create_parallel_view(view_port, (1000, 1000))
    vt.set_axon_view (rotate_right, rotate_up, view_port)
    rs.ZoomExtents()
    vt.zoom_scale(2, view_port)
    vt.set_display_mode (view_port, "Shaded")
    options_v = ('Yes', 'No')
    if options_v:
        like_view = rs.ListBox(options_v, 'Do you like the view?')
        if like_view == 'Yes':
            option_1 = ('Animation', 'Image', 'No')
            if option_1:
                save_1 = rs.ListBox(option_1, 'Would you like to save?')
                if save_1  == "Animation":
                    file_name = rs.StringBox('Please provide a file name.', None, 'File')
                    folder_name = file_name + " folder"
                     
                    for i in range (90):
                        rs.Sleep(1)
                        vt.set_axon_view(1, 0, view_port)
                        animate_name = file_name + str("%04d"%i)
                        vt.capture_view(2, animate_name, folder_name)
                        
                elif save_1  == "Image":
                    file_name = rs.StringBox('Please provide a file name.', None, 'File')
                    folder_name = file_name + " folder"
                    
                    vt.capture_view(2, file_name, folder_name)
                    options_again = ('Yes', 'No')
                    if options_again:
                        view_again = rs.ListBox(options_again, 'Would you like to save a different angle view?')
                        if view_again == 'Yes':
                            save_file()
                else:
                    pass
        if like_view == 'No':
            save_file()

#To start as blank or keep the previous object
def clear_file():
    options_1 = ('Yes', 'No')
    if options_1:
        delete_1 = rs.ListBox(options_1, 'Would you like to delete all objects?')
        if delete_1 == "Yes":
            all_objects = rs.AllObjects()
            rs.DeleteObjects(all_objects)
        else:
            pass

#main
#######################################################
# Start
def main():
    message1 = "This command builds a voxelized model from point cloud data saved .ply format. Please locate your file before proceeding."
    message2 = "Now the magic happens!"
    message3 = "Select a PointCloud"
    rs.MessageBox(message1, buttons=0,title="Gray Level")
    rs.MessageBox(message2, buttons=0,title="Gray Level")
    rs.MessageBox(message3, buttons=0,title="Gray Level")
    x = 1
    Pyr_Box(x)
    points_delete = rs.ObjectsByType(rs.filter.point)
    curves_delete = rs.ObjectsByType(rs.filter.curve)
    rs.DeleteObjects(points_delete)
    rs.DeleteObjects(curves_delete)
    save_file()

main()