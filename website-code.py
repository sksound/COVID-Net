from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    xray_img = ""
    
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    xray_img = file
    predictions, prediction = anvil.server.call('predict_image', xray_img)
    self.label_2.text = "COVID: " + str(round(predictions[0] * 100, 2)) + "%"
    self.label_1.text = "Non-COVID: " + str(round(predictions[1] * 100, 2)) + "%"
    self.label_3.text = "Normal: " + str(round(predictions[2] * 100, 2)) + "%"
    self.label_5.text = "Prediction: " + str(prediction)
    self.image_1.source = file
    
