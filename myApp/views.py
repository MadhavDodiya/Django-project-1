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
    return HttpResponse('''<body style="display: flex; justify-content: center; align-items: center; height: 100vh; background: linear-gradient(to bottom right, #e20078, #7b22ff);">
    <div style="background-color: #1c1c1c; padding: 30px; border-radius: 10px; width: 400px; box-shadow: 0 0 15px rgba(0,0,0,0.2);">
        <h2 style="color: white; text-align: center; margin-bottom: 20px;">Contact Us</h2>
        <form>
            <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                <div style="flex: 0.48;">
                    <label for="first-name" style="color: white; display: block; margin-bottom: 5px;">Full name <span style="color: red;">*</span></label>
                    <input type="text" id="first-name" placeholder="First" required style="width: 90%; padding: 10px; border-radius: 5px; border: none;">
                </div>
                <div style="flex: 0.48;">
                    <label for="last-name" style="color: white; display: block; margin-bottom: 5px;">&nbsp;</label>
                    <input type="text" id="last-name" placeholder="Last" required style="width: 90%; padding: 10px; border-radius: 5px; border: none;">
                </div>
            </div>
            <div style="margin-bottom: 15px;">
                <label for="email" style="color: white; display: block; margin-bottom: 5px;">Email <span style="color: red;">*</span></label>
                <input type="email" id="email" required style="width: 95%; padding: 10px; border-radius: 5px; border: none;">
            </div>
            <div style="margin-bottom: 15px;">
                <label for="message" style="color: white; display: block; margin-bottom: 5px;">Leave us a few words <span style="color: red;">*</span></label>
                <textarea id="message" rows="5" style="width: 95%; padding: 10px; border-radius: 5px; border: none;"></textarea>
            </div>
            <div style="text-align: center;">
                <button type="submit" style="background-color: #ff0059; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Submit</button>
            </div>
        </form>
    </div>
</body>''')
