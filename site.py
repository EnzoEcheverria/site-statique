import markdown2
import os
import click

@click.command()
@click.option(
    "-i",
    "--imput-file",
    "infile",
    help= "",
)

@click.command()
@click.option(
    "-o",
    "--output-directory",
    "outfile",
)

def convert(file, outfolder):
	
	HTML_start = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + title + '</title>\n</head>\n<body>\n' 
	HTML_end = '</body>\n</html>'
	file = imput_file

    convert_file = open(file, mode='r', encoding="utf-8")
    text = convert_file.read()
    html = markdown2.markdown(text)
    output = open(output_file, "w+").write(HTML_start + html + HTML_end)












































































