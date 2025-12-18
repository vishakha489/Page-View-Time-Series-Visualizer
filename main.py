from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate Line Plot
line_fig = draw_line_plot()
print("Line plot generated and saved as 'line_plot.png'.")

# Generate Bar Plot
bar_fig = draw_bar_plot()
print("Bar plot generated and saved as 'bar_plot.png'.")

# Generate Box Plots
box_fig = draw_box_plot()
print("Box plots generated and saved as 'box_plot.png'.")

print("All plots created successfully!")
