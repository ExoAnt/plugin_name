#Sanchez Anthony
#03-22-23
#Grey Level 
#Project Description
#This study aims to deepen the understanding of physical objects and their innate imperfections by integrating photogrammetry-based color mapping techniques into digital models, 
#enabling users to visualize and recreate individual real-world objects or environments through an algorithm that transforms point cloud data into color coordinates and represents 
#color saturation based on the number of edges in each pyramid.


#Future Ideas
#######################################################
#revert to adjusting color of pointcloud through color saturation which could allow the user to have more outputs therefore creating more variety

#Sources
#######################################################
#https://www.guru99.com/python-check-if-file-exists.html
#https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
#https://developer.rhino3d.com/guides/rhinopython/python-reading-writing/
#https://developer.rhino3d.com/samples/rhinopython/export-points/
#https://www.youtube.com/watch?v=uoFPfR3ImAo&t=1821s
#https://chat.openai.com/chat/8170938e-69ca-4659-9170-ca52e1f529eb
#https://chat.openai.com/chat/d077e946-aed1-4292-980a-751c475ad2ac

#Imports
#######################################################
import rhinoscriptsyntax as rs
import random
import scriptcontext
import Rhino.Geometry as geo
import math
import scriptcontext
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
from scriptcontext import escape_test
from math import radians
from math import cos
from math import sin

#User Libraries
#######################################################
import color_tools as ct
reload(ct)
import viewport_tools as vt
reload (vt)
import user_interface as ut
reload (ut)
#Definitions
#######################################################

def center_cube(center, radius):
    cx, cy , cz = center
    #lower points
    p1 = (cx - radius, cy - radius, cz - radius)
    p2 = (cx + radius, cy - radius, cz - radius)
    p3 = (cx + radius, cy + radius, cz - radius)
    p4 = (cx - radius, cy + radius, cz - radius)
    #upper points
    p5 = (cx - radius, cy - radius, cz + radius)
    p6 = (cx + radius, cy - radius, cz + radius)
    p7 = (cx + radius, cy + radius, cz + radius)
    p8 = (cx - radius, cy + radius, cz + radius)
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    #create a new box 
    box = rs.AddBox(points)
    return box

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

# Assigns color to line
def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex (object)
    rs.MaterialColor(index, color)

def Pyr_Box(depth, h=None, v=None, cube_radius=None):
    rs.EnableRedraw(False)
    if depth == 0:
        return
    id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    if not id:
        return
    dialog = ut.hfactor_dialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        hfactor0_10 = int(dialog.get_h1())
        hfactor11_20 = int(dialog.get_h2())
        hfactor21_30 = int(dialog.get_h3())
        hfactor31_40 = int(dialog.get_h4())
        hfactor41_50 = int(dialog.get_h5())
        hfactor51_60 = int(dialog.get_h6())
        hfactor61_70 = int(dialog.get_h7())
        hfactor71_80 = int(dialog.get_h8())
        hfactor81_90 = int(dialog.get_h9())
        hfactor91_100 = int(dialog.get_h10())
    points = rs.PointCloudPoints(id)
    point_colors = rs.PointCloudPointColors(id)
    for i in range(len(points)):
        color = point_colors[i]
        r, g, b = color.R, color.G, color.B
        h, s, v = ct.rgb_to_hsv(r, g, b)
        scriptcontext.escape_test()
        saturation = color_intensity(color)
        if points:
            size_map = {
                (0, 10): hfactor0_10,
                (11, 20): hfactor11_20,
                (21, 30): hfactor21_30,
                (31, 40): hfactor31_40,
                (41, 50): hfactor41_50,
                (51, 60): hfactor51_60,
                (61, 70): hfactor61_70,
                (71, 80): hfactor71_80,
                (81, 90): hfactor81_90,
                (91, 100): hfactor91_100
            }
    for i in range(len(points)):
        color = point_colors[i]
        r, g, b = color.R, color.G, color.B
        h, s, v = ct.rgb_to_hsv(r, g, b)
        saturation = color_intensity(color)
        if points:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor0_10, 3, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor0_10)
            #assign_material_color(box, color)
        if 11 <= saturation <= 20:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor11_20, 4, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor11_20)
            #assign_material_color(box, color)
        if 21 <= saturation <= 30:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor21_30, 6, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor21_30)
            #assign_material_color(box, color)
        if 31 <= saturation <= 40:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor31_40, 8, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor31_40)
            #assign_material_color(box, color)
        if 41 <= saturation <= 50:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor41_50, 10, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor41_50)
            #assign_material_color(box, color)
        if 51 <= saturation <= 60:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor51_60, 12, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor51_60)
            #assign_material_color(box, color)
        if 61 <= saturation <= 70:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor61_70, 14, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor61_70)
            #assign_material_color(box, color)
        if 71 <= saturation <= 80:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor71_80, 16, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor71_80)
            #assign_material_color(box, color)
        if 81 <= saturation <= 90:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor81_90, 18, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor81_90)
            #assign_material_color(box, color)
        if 91 <= saturation <= 100:
            pt1 = points[i]
            pt2 = rs.PointAdd(pt1, [h, s, v])
            tri = pyramid(10, hfactor91_100, 20, pt2)
            assign_material_color(tri, color)
            #box = center_cube(pt2, hfactor91_100)
            #assign_material_color(box, color)

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

##Allow user to save image or animtation##
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

##To start as blank or keep the previous object##
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
    rs.MessageBox(message1, buttons=0,title="Gray Level")
    rs.Command("Import")
    rs.MessageBox(message2, buttons=0,title="Gray Level")
    
    x = 1
    Pyr_Box(x)
    points_delete = rs.ObjectsByType(rs.filter.point)
    curves_delete = rs.ObjectsByType(rs.filter.curve)
    rs.DeleteObjects(points_delete)
    rs.DeleteObjects(curves_delete)
    rs.Command("SelPolysrf")
    rs.Command("Group")
    save_file()
    #clear_file()

main()