from flask_table import *
from operating_conditions import *
from characterization_corners import *
from deliverables import *
from timing_and_current_data import *
from in_out import *
import os
from globals import OPTS

class datasheet():

    def __init__(self,identifier):
        self.io = []
        self.corners = []
        self.timing = []
        self.operating = []
        self.dlv = []
        self.name = identifier
        self.html = ""
        

    def generate_html(self):
        with open(os.path.abspath(os.environ.get("OPENRAM_HOME")) + '/datasheet/assets/datasheet.css', 'r') as datasheet_css:
            self.html += datasheet_css.read()
         
        self.html +='<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>'+ self.name + '.html' + '</p>'

        self.html +='<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>Ports and Configuration (DEBUG)</p>'
        self.html += in_out(self.io,table_id='data').__html__().replace('&lt;','<').replace('&#34;','"').replace('&gt;',">")

        self.html +='<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>Operating Conditions</p>'
        self.html += operating_conditions(self.operating,table_id='data').__html__()

        self.html += '<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>Timing and Current Data</p>'
        self.html += timing_and_current_data(self.timing,table_id='data').__html__()

        self.html += '<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>Characterization Corners</p>'
        self.html += characterization_corners(self.corners,table_id='data').__html__()

        self.html +='<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>Deliverables</p>'
        self.html += deliverables(self.dlv,table_id='data').__html__().replace('&lt;','<').replace('&#34;','"').replace('&gt;',">")

        self.html +='<p style=font-size: 20px;font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;>*Feature only supported with characterizer</p>'
        
        self.html +='<img src=' + os.path.abspath(os.environ.get("OPENRAM_HOME")) + '/datasheet/assets/vlsi_logo.png alt="VLSIDA" />' 
