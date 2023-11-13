import argparse
import datetime

args=argparse.ArgumentParser()

args.add_argument("--outFile","-o",type=str,help="Output file",default="../../reports/server-storage-util/index.html")
args = args.parse_args()

fOut = open(args.outFile,"w+")

fOut.write('''
<html>
<head>
<title>Server Storage Usage</title>
</head>
<body>
<h1>Server Storage Usage</h1>
<p>This table shows the usage reports for folders that are larger than 10G on the Turing server.</p>

''')

for ss in ["kepler", "turing", "ampere", "babbage"]:
    ff = "../../reports/server-storage-util/logs/{}-storage.log".format(ss)
    fIn = open(ff,"r")

    lines = fIn.readlines()
    fOut.write("<b>{}</b> Read on: </td><td>".format(ss)+lines[0]+"</td></tr><br><br>\n")


    fOut.write('''
    <table border="1" style="border-collapse:collapse;">
    <tr>
    <th>Usage</th>
    <th>Path</th>
    <th>Owner</th>
    </tr>
    ''')








    for line in lines[1:]:
        usageGB = line.split()[0]
        folder = line.split()[1]
        
                

        fOut.write("<tr><td>" + usageGB + "</td><td>" + folder + "</td>")

        if ss=="babbage":
            studentID = folder.split("/")[3]
            print(studentID)
            if studentID[0]=="e" and studentID[1:].isdigit() and int(usageGB[:-1])>100:
                fOut.write("<td bgcolor=\"yellow\"><a href=\"https://people.ce.pdn.ac.lk/students/e{}/{}/\">profile</a></td>"\
                           .format(studentID[1:3],studentID[3:6]))
            else:
                fOut.write("<td></td>")
        else:
            fOut.write("<td></td>")
        
        fOut.write("</tr>\n")



    fOut.write('''
    </table>
    <br><br>''')


fOut.write('''
<p>This page was last updated on {}.</p>

</body>
</html>
'''.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

fIn.close()
fOut.close()

print("END: gen-report.py ( -> " + args.outFile + ")")