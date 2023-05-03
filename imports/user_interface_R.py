import rhinoscriptsyntax as rs
import scriptcontext
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
import Eto
from scriptcontext import escape_test


##Geometry dialog class##
class rfactor_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'rfactor'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        
        # Create controls for the dialog
        self.r1_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r1_textbox = forms.TextBox(Text = None)
        self.r2_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r2_textbox = forms.TextBox(Text = None)
        self.r3_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r3_textbox = forms.TextBox(Text = None)
        self.r4_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r4_textbox = forms.TextBox(Text = None)
        self.r5_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r5_textbox = forms.TextBox(Text = None)
        self.r6_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r6_textbox = forms.TextBox(Text = None)
        self.r7_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r7_textbox = forms.TextBox(Text = None)
        self.r8_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r8_textbox = forms.TextBox(Text = None)
        self.r9_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r9_textbox = forms.TextBox(Text = None)
        self.r10_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r10_textbox = forms.TextBox(Text = None)
        self.r11_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r11_textbox = forms.TextBox(Text = None)
        self.r12_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r12_textbox = forms.TextBox(Text = None)
        self.r13_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r13_textbox = forms.TextBox(Text = None)
        self.r14_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r14_textbox = forms.TextBox(Text = None)
        self.r15_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r15_textbox = forms.TextBox(Text = None)
        self.r16_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r16_textbox = forms.TextBox(Text = None)
        self.r17_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r17_textbox = forms.TextBox(Text = None)
        self.r18_label = forms.Label(Text = 'Provide Radius for Triangle:')
        self.r18_textbox = forms.TextBox(Text = None)
        
        
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.on_close_button_click
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(10, 10)
        layout.AddRow('Please provide the rfactor.:')
        layout.AddRow(self.r1_label, self.r1_textbox)
        layout.AddRow(self.r2_label, self.r2_textbox)
        layout.AddRow(self.r3_label, self.r3_textbox)
        layout.AddRow(self.r4_label, self.r4_textbox)
        layout.AddRow(self.r5_label, self.r5_textbox)
        layout.AddRow(self.r6_label, self.r6_textbox)
        layout.AddRow(self.r7_label, self.r7_textbox)
        layout.AddRow(self.r8_label, self.r8_textbox)
        layout.AddRow(self.r9_label, self.r9_textbox)
        layout.AddRow(self.r10_label, self.r10_textbox)
        layout.AddRow(self.r11_label, self.r11_textbox)
        layout.AddRow(self.r12_label, self.r12_textbox)
        layout.AddRow(self.r13_label, self.r13_textbox)
        layout.AddRow(self.r14_label, self.r14_textbox)
        layout.AddRow(self.r15_label, self.r15_textbox)
        layout.AddRow(self.r16_label, self.r16_textbox)
        layout.AddRow(self.r17_label, self.r17_textbox)
        layout.AddRow(self.r18_label, self.r18_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    # Start of the class functions
    # Get the value of the textbox
    
    
    def get_r1(self):
        return self.r1_textbox.Text
    
    def get_r2(self):
        return self.r2_textbox.Text
    
    def get_r3(self):
        return self.r3_textbox.Text
    
    def get_r4(self):
        return self.r4_textbox.Text
    
    def get_r5(self):
        return self.r5_textbox.Text
    
    def get_r6(self):
        return self.r6_textbox.Text
    
    def get_r7(self):
        return self.r7_textbox.Text
    
    def get_r8(self):
        return self.r8_textbox.Text
    
    def get_r9(self):
        return self.r9_textbox.Text
    
    def get_r10(self):
        return self.r10_textbox.Text
        
    def get_r11(self):
        return self.r11_textbox.Text
        
    def get_r12(self):
        return self.r12_textbox.Text
        
    def get_r13(self):
        return self.r13_textbox.Text
        
    def get_r14(self):
        return self.r14_textbox.Text
        
    def get_r15(self):
        return self.r15_textbox.Text
        
    def get_r16(self):
        return self.r16_textbox.Text
        
    def get_r17(self):
        return self.r17_textbox.Text
        
    def get_r18(self):
        return self.r18_textbox.Text
        
    # Close button click handler
    
    def on_close_button_click(self, sender, e):
        self.r1_textbox.Text = ""
        self.Close(False)
        self.r2_textbox.Text = ""
        self.Close(False)
        self.r3_textbox.Text = ""
        self.Close(False)
        self.r4_textbox.Text = ""
        self.Close(False)
        self.r5_textbox.Text = ""
        self.Close(False)
        self.r6_textbox.Text = ""
        self.Close(False)
        self.r7_textbox.Text = ""
        self.Close(False)
        self.r8_textbox.Text = ""
        self.Close(False)
        self.r9_textbox.Text = ""
        self.Close(False)
        self.r10_textbox.Text = ""
        self.Close(False)
        self.r11_textbox.Text = ""
        self.Close(False)
        self.r12_textbox.Text = ""
        self.Close(False)
        self.r13_textbox.Text = ""
        self.Close(False)
        self.r14_textbox.Text = ""
        self.Close(False)
        self.r15_textbox.Text = ""
        self.Close(False)
        self.r16_textbox.Text = ""
        self.Close(False)
        self.r17_textbox.Text = ""
        self.Close(False)
        self.r18_textbox.Text = ""
        self.Close(False)
        


    # OK button click handler
    def on_ok_button_click(self, sender, e):
        if self.r1_textbox.Text == "":
            self.Close(False)
        elif self.r2_textbox.Text == "":
            self.Close(False)
        elif self.r3_textbox.Text == "":
            self.Close(False)
        elif self.r4_textbox.Text == "":
            self.Close(False)
        elif self.r5_textbox.Text == "":
            self.Close(False)
        elif self.r6_textbox.Text == "":
            self.Close(False)
        elif self.r7_textbox.Text == "":
            self.Close(False)
        elif self.r8_textbox.Text == "":
            self.Close(False)
        elif self.r9_textbox.Text == "":
            self.Close(False)
        elif self.r10_textbox.Text == "":
            self.Close(False)
        elif self.r11_textbox.Text == "":
            self.Close(False)
        elif self.r12_textbox.Text == "":
            self.Close(False)
        elif self.r13_textbox.Text == "":
            self.Close(False)
        elif self.r14_textbox.Text == "":
            self.Close(False)
        elif self.r15_textbox.Text == "":
            self.Close(False)
        elif self.r16_textbox.Text == "":
            self.Close(False)
        elif self.r17_textbox.Text == "":
            self.Close(False)
        elif self.r18_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
    ## End of Dialog Class ##

