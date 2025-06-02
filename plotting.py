# This script call motion_detector.py to generate a DataFrame.
# When this script is executed, the motion_detector.py is executed as well.
from motion_detector import df
from bokeh.plotting import figure, show, output_file
# ColumnDataSource is a standardized way to provide data to a Bokeh plot
# If you've got data frames, list, or other objects for some for some functions in Bokeh you need to convert them to a ColumnDataSource object
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")  # Convert Start to string for display
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")  # Convert End to string for display

cds=ColumnDataSource(df)  # Convert the DataFrame to a ColumnDataSource

p=figure(title="Motion Detection Times", x_axis_label='Time', y_axis_label='Motion Status', x_axis_type='datetime', sizing_mode="stretch_both", min_height=100)
#p.yaxis.minor_tick_line_color = None
#p.yaxis.ticker.desired_num_ticks = 10  # Set the number of ticks on the y-axis to 1

hover=HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

p.quad(top=1, bottom=0, left="Start", right="End", fill_color="green", line_color="black", alpha=0.5, legend_label="Motion Detected", source=cds)  # Use quad glyph to represent motion detection periods

output_file("motion_detection.html")
show(p)  # Display the plot in a web browser