import rhinoscriptsyntax as rs
import scriptcontext
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
import Eto
from scriptcontext import escape_test


##Geometry dialog class##
class hfactor_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'hfactor'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        
        # Create controls for the dialog
        self.h1_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h1_textbox = forms.TextBox(Text = None)
        self.h2_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h2_textbox = forms.TextBox(Text = None)
        self.h3_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h3_textbox = forms.TextBox(Text = None)
        self.h4_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h4_textbox = forms.TextBox(Text = None)
        self.h5_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h5_textbox = forms.TextBox(Text = None)
        self.h6_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h6_textbox = forms.TextBox(Text = None)
        self.h7_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h7_textbox = forms.TextBox(Text = None)
        self.h8_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h8_textbox = forms.TextBox(Text = None)
        self.h9_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h9_textbox = forms.TextBox(Text = None)
        self.h10_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h10_textbox = forms.TextBox(Text = None)
        self.h11_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h11_textbox = forms.TextBox(Text = None)
        self.h12_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h12_textbox = forms.TextBox(Text = None)
        self.h13_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h13_textbox = forms.TextBox(Text = None)
        self.h14_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h14_textbox = forms.TextBox(Text = None)
        self.h15_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h15_textbox = forms.TextBox(Text = None)
        self.h16_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h16_textbox = forms.TextBox(Text = None)
        self.h17_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h17_textbox = forms.TextBox(Text = None)
        self.h18_label = forms.Label(Text = 'Provide Height for Triangle:')
        self.h18_textbox = forms.TextBox(Text = None)
        
        
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.on_close_button_click
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(10, 10)
        layout.AddRow('Please provide the hfactor.:')
        layout.AddRow(self.h1_label, self.h1_textbox)
        layout.AddRow(self.h2_label, self.h2_textbox)
        layout.AddRow(self.h3_label, self.h3_textbox)
        layout.AddRow(self.h4_label, self.h4_textbox)
        layout.AddRow(self.h5_label, self.h5_textbox)
        layout.AddRow(self.h6_label, self.h6_textbox)
        layout.AddRow(self.h7_label, self.h7_textbox)
        layout.AddRow(self.h8_label, self.h8_textbox)
        layout.AddRow(self.h9_label, self.h9_textbox)
        layout.AddRow(self.h10_label, self.h10_textbox)
        layout.AddRow(self.h11_label, self.h11_textbox)
        layout.AddRow(self.h12_label, self.h12_textbox)
        layout.AddRow(self.h13_label, self.h13_textbox)
        layout.AddRow(self.h14_label, self.h14_textbox)
        layout.AddRow(self.h15_label, self.h15_textbox)
        layout.AddRow(self.h16_label, self.h16_textbox)
        layout.AddRow(self.h17_label, self.h17_textbox)
        layout.AddRow(self.h18_label, self.h18_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    # Start of the class functions
    # Get the value of the textbox
    
    
    def get_h1(self):
        return self.h1_textbox.Text
    
    def get_h2(self):
        return self.h2_textbox.Text
    
    def get_h3(self):
        return self.h3_textbox.Text
    
    def get_h4(self):
        return self.h4_textbox.Text
    
    def get_h5(self):
        return self.h5_textbox.Text
    
    def get_h6(self):
        return self.h6_textbox.Text
    
    def get_h7(self):
        return self.h7_textbox.Text
    
    def get_h8(self):
        return self.h8_textbox.Text
    
    def get_h9(self):
        return self.h9_textbox.Text
    
    def get_h10(self):
        return self.h10_textbox.Text
        
    def get_h11(self):
        return self.h11_textbox.Text
        
    def get_h12(self):
        return self.h12_textbox.Text
        
    def get_h13(self):
        return self.h13_textbox.Text
        
    def get_h14(self):
        return self.h14_textbox.Text
        
    def get_h15(self):
        return self.h15_textbox.Text
        
    def get_h16(self):
        return self.h16_textbox.Text
        
    def get_h17(self):
        return self.h17_textbox.Text
        
    def get_h18(self):
        return self.h18_textbox.Text
        
    # Close button click handler
    
    def on_close_button_click(self, sender, e):
        self.h1_textbox.Text = ""
        self.Close(False)
        self.h2_textbox.Text = ""
        self.Close(False)
        self.h3_textbox.Text = ""
        self.Close(False)
        self.h4_textbox.Text = ""
        self.Close(False)
        self.h5_textbox.Text = ""
        self.Close(False)
        self.h6_textbox.Text = ""
        self.Close(False)
        self.h7_textbox.Text = ""
        self.Close(False)
        self.h8_textbox.Text = ""
        self.Close(False)
        self.h9_textbox.Text = ""
        self.Close(False)
        self.h10_textbox.Text = ""
        self.Close(False)
        self.h11_textbox.Text = ""
        self.Close(False)
        self.h12_textbox.Text = ""
        self.Close(False)
        self.h13_textbox.Text = ""
        self.Close(False)
        self.h14_textbox.Text = ""
        self.Close(False)
        self.h15_textbox.Text = ""
        self.Close(False)
        self.h16_textbox.Text = ""
        self.Close(False)
        self.h17_textbox.Text = ""
        self.Close(False)
        self.h18_textbox.Text = ""
        self.Close(False)
        


    # OK button click handler
    def on_ok_button_click(self, sender, e):
        if self.h1_textbox.Text == "":
            self.Close(False)
        elif self.h2_textbox.Text == "":
            self.Close(False)
        elif self.h3_textbox.Text == "":
            self.Close(False)
        elif self.h4_textbox.Text == "":
            self.Close(False)
        elif self.h5_textbox.Text == "":
            self.Close(False)
        elif self.h6_textbox.Text == "":
            self.Close(False)
        elif self.h7_textbox.Text == "":
            self.Close(False)
        elif self.h8_textbox.Text == "":
            self.Close(False)
        elif self.h9_textbox.Text == "":
            self.Close(False)
        elif self.h10_textbox.Text == "":
            self.Close(False)
        elif self.h11_textbox.Text == "":
            self.Close(False)
        elif self.h12_textbox.Text == "":
            self.Close(False)
        elif self.h13_textbox.Text == "":
            self.Close(False)
        elif self.h14_textbox.Text == "":
            self.Close(False)
        elif self.h15_textbox.Text == "":
            self.Close(False)
        elif self.h16_textbox.Text == "":
            self.Close(False)
        elif self.h17_textbox.Text == "":
            self.Close(False)
        elif self.h18_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
    ## End of Dialog Class ##

