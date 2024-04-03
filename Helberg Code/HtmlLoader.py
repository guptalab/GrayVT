import webbrowser
import os

# Author: Devdeep.js
# Description: HTML loader for displaying results.
# Date: 2024-01-05

class HtmlLoader:
    """
    This class provides methods to generate and load HTML content.
    """

    def generateHtmlFromCsv(self, inputCsv, outputHtml):
        """
        Generate HTML table from a CSV file.

        Args:
            inputCsv (str): Path to the input CSV file.
            outputHtml (str): Path to the output HTML file.

        Returns:
            None
        """
        # Read the .csv file
        with open(inputCsv, 'r') as f:
            data = f.readlines()

        # Start the HTML output
        html_output = '<table style="width:100%">\n'

        # Add the data
        for line in data:
            html_output += '<tr><td>{}</td></tr>\n'.format(line.strip())

        # End the HTML output
        html_output += '</table>\n'

        # Write the HTML output to a file
        with open(outputHtml, 'w') as f:
            f.write(html_output)

    def loadHtmlInBrowser(self, htmlFile):
        """
        Open the HTML file in the default web browser.

        Args:
            htmlFile (str): Path to the HTML file.

        Returns:
            None
        """
        webbrowser.open('file://' + os.path.realpath(htmlFile))

# Example usage:
if __name__ == "__main__":
    loader = HtmlLoader()
    loader.generateHtmlFromCsv('output.csv', 'index.html')
    loader.loadHtmlInBrowser('index.html')
