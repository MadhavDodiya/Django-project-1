from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def table(request):
    return HttpResponse('''
                        <center>
                        <table style="border:2px solid green;margin-top:250px">
                        <tr >
                        <td style="padding: 10px 20px;background-color: orange;border:2px solid green"><b>Sr.No</td>
                        <td style="padding: 10px 20px;background-color: orange;border:2px solid green"><b>Roll No</td>
                        <td style="padding: 10px 20px;background-color: orange;border:2px solid green"><b>Name</td>
                        <td style="padding: 10px 20px;background-color: orange;border:2px solid green"><b>Team</td>
                        </tr>

                        <tr>
                        <td style="padding: 10px 20px;background-color: orange;text-align: center;border:2px solid green"><b>1</td>
                        <td style="text-align:center;border:2px solid green">1001</td>
                        <td style="text-align:center;border:2px solid green">Jhon</td>
                        <td style="text-align:center;border:2px solid green">Red</td>
                        </tr>

                        <tr>
                        <td style="padding: 10px 20px;background-color: orange;text-align: center;border:2px solid green"><b>2</td>
                        <td style="text-align:center;border:2px solid green">1002</td>
                        <td style="text-align:center;border:2px solid green">Peter</td>
                        <td style="text-align:center;border:2px solid green">Blue</td>
                        </tr>

                        <tr>
                        <td style="padding: 10px 20px;background-color: orange;text-align: center;border:2px solid green"><b>3</td>
                        <td style="text-align:center;border:2px solid green">1003</td>
                        <td style="text-align:center;border:2px solid green">Henry</td>
                        <td style="text-align:center;border:2px solid green">Green</td>
                        </tr>
                        </table>
                        </center>''')

def form(request):
    return HttpResponse('''<form style="background-image: linear-gradient(to right,pink,blue)">
                        <div style="background-color:black;border-radius: 10px;height: 500px;width: 500px">
                            <h2 style="color: white;padding: 10px 0px;text-align: center">Contact Us<h2>
                        </div>
                        </form>''')
