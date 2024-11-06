
import os

# Replace with the relative path to your image
relative_path = 'CSS/style_sheet_ui_001.css' # 'images/star_wars_space_background.jpg'
#relative_path_CSS = 'CSS/style_sheet_ui_001.css'
# Get the absolute path
absolute_path = os.path.abspath(relative_path)
#absolute_path_CSS = os.path.abspath(relative_path_CSS)

# Print the absolute path
print("Absolute path of the image:", absolute_path)
#print("Absolute path of the CSS file:", relative_path_CSS)

# Absolute path of the CSS: C:\Docs\maya\scripts\Maya_Python_Qt_UIs\CSS\style_sheet_ui_001.css
# Absolute path of t image: C:\Docs\maya\scripts\Maya_Python_Qt_UIs\images\star_wars_space_background.jpg