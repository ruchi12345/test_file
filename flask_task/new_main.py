# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#    f = open("/home/brahmjot/flask_task/static/text_files/file1.txt", "r")
#    sentences=[]
#    if f.mode == 'r':
#       contents = f.read()
#       sentences.append(contents)
#    return render_template('showresult.html',sentences=sentences)
#
# @app.route('/show/<filename>')
# def my_file():
#    filename = request.args.get('filename')
#    if(filename=="file2"):
#       f = open("/home/brahmjot/flask_task/static/text_files/file2.txt", "r")
#       sentences=[]
#       if f.mode == 'r':
#          contents = f.read()
#          sentences.append(contents)
#    else:
#       f = open("/home/brahmjot/flask_task/static/text_files/file3.txt", "r")
#       sentences = []
#       if f.mode == 'r':
#          contents = f.read()
#          sentences.append(contents)
#
#    return render_template('showresult.html',filename=sentences)
#
#
# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask , request
import os
from django.utils.encoding import smart_str

app = Flask(__name__)

project_Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def index():
    number_Lines = []
    lines = []
    file="file1.txt"
    filelist = open(file, 'r')
    for line in filelist:
       number_Lines.append(line)
       lines.append(str(line).replace('\t', '').replace('\n', ''))
    number_of_Lines = len(number_Lines)
    json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
    return '''<h1>json :{}</h1>'''.format(json)

@app.route('/file/<file>')
def file_upload(file):
    file = file
    print (file,'fgggggggggggg')
    starting_line = request.args.get('starting_line')
    end_line = request.args.get('end_line')
    print(file)
    print(starting_line)
    print(end_line)
    # if file == None and starting_line == None and end_line == None:
    #    number_Lines = []
    #    lines = []
    #    filelist = open(file, 'r')
    #    for line in filelist:
    #       number_Lines.append(line)
    #       lines.append(str(line).replace('\t', '').replace('\n', ''))
    #    number_of_Lines = len(number_Lines)
    #    json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
    # else:
    json = ''
    try:
       if file != None:
          number_Lines = []
          lines = []
          filelist = open(file, 'r')
          for line in filelist:
             number_Lines.append(line)
             lines.append(str(line).replace('\t', '').replace('\n', ''))
          number_of_Lines = len(number_Lines)

          json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
          if starting_line == None and end_line == None:
             number_Lines = []
             lines = []
             filelist = open(file, 'r')
             for line in filelist:
                number_Lines.append(line)
                lines.append(str(line).replace('\t', '').replace('\n', ''))
             number_of_Lines = len(number_Lines)
             json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
          else:
             if starting_line == None:
                number_Lines = []
                lines = []
                filelist = open(file, 'r')
                for line in filelist:
                   number_Lines.append(line)
                   lines.append(str(line).replace('\t', '').replace('\n', ''))
                number_of_Lines = len(number_Lines)
                json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
             elif end_line == None:
                number_Lines = []
                lines = []
                filelist = open(file, 'r')
                for line in filelist:
                   number_Lines.append(line)
                   lines.append(str(line).replace('\t', '').replace('\n', ''))
                number_of_Lines = len(number_Lines)
                json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
             else:
                print('Else Method')
                number_Lines = []
                lines = []
                lineslist = []
                filelist = open(file, 'r')
                for line in filelist:
                   number_Lines.append(line)
                   lineslist.append(str(line).replace('\t', '').replace('\n', ''))
                for i in range(int(smart_str(starting_line)), int(smart_str(end_line))):
                   lines.append(lineslist[i])
                number_of_Lines = len(lines)

                json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
    except Exception as e:
       number_Lines = []
       lines = []
       filelist = open(file, 'r')
       for line in filelist:
          number_Lines.append(line)
          lines.append(str(line).replace('\t', '').replace('\n', ''))
       number_of_Lines = len(number_Lines)
       json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
       print e

    return '''<h1>json :{}</h1>'''.format(json)

# @app.route('/query-example')
# def query_example():
#     file = request.args.get('file')
#     starting_line = request.args.get('starting_line')
#     end_line = request.args.get('end_line')
#
#     return '''<h1>The language value is: {}</h1>'''.format(file)
#
# @app.route('/<str:filename>')
# def index1(filename):
#     file = request.args.get('filename')
#     starting_line = request.args.get('starting_line')
#     end_line = request.args.get('end_line')
#     # print(file)
#     # print(starting_line)
#     # print(end_line)
#     json = ''
#     try:
#        number_Lines = []
#        lines = []
#        filelist = open(file, 'r')
#        for line in filelist:
#           number_Lines.append(line)
#           lines.append(str(line).replace('\t','').replace('\n',''))
#        number_of_Lines = len(number_Lines)
#        json = {'file_Name' :file , 'number_of_lines_read':number_of_Lines,'lines':lines}
#     except Exception as e:
#        number_Lines = []
#        lines = []
#        filelist = open(file, 'r')
#        for line in filelist:
#           number_Lines.append(line)
#           lines.append(str(line).replace('\t', '').replace('\n', ''))
#        number_of_Lines = len(number_Lines)
#        json = {'file_Name': file, 'number_of_lines_read': number_of_Lines, 'lines': lines}
#        print e
#
#     return '''<h1>{}</h1>'''.format(json)


if __name__ == '__main__':
   app.run(debug = True)