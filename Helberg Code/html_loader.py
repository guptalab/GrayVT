import webbrowser
import os

# Read the .txt file
with open('output.csv', 'r') as f:
    data = f.readlines()

# Start the HTML output
html_output = '<table style="width:100%">\n'

# Add the data
for line in data:
    html_output += '<tr><td>{}</td></tr>\n'.format(line.strip())

# End the HTML output
html_output += '</table>\n'

# Write the HTML output to a file
with open('output.html', 'w') as f:
    f.write(html_output)

# Open the HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath('output.html'))
