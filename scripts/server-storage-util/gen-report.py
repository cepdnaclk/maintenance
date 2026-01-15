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
<h3><a href="https://www.pdn.ac.lk/">University of Peradeniya</a>: <a href="https://www.ce.pdn.ac.lk/">Department of Computer Engineering: <a href="https://cepdnaclk.github.io/maintenance/">Server Usage</a> :</h3>
<h1>Server Storage Usage</h1>
<hr>
<p>This table shows the usage reports for folders that are larger than 10G on CO Department server.</p>
<h3 id="listOfServers">List of servers</h3>
''')

for ssIdx,ss in enumerate(["kepler", "turing", "ampere", "babbage", "ada"]):
    fOut.write("{}. <a href=\"#{}\">{}</a><br>\n".format(ssIdx+1,ss,ss))

for ss in ["kepler", "turing", "ampere", "babbage", "ada"]:
    ff = "../../reports/server-storage-util/logs/{}-storage.log".format(ss)
    fIn = open(ff,"r")

    lines = fIn.readlines()
    fOut.write("<br><br><h3 id=\"{}\">{}</h3> Read on: {}.\n".format(ss,ss,lines[0]))

    if ss == "babbage":
        fOut.write("<p><span style=\"background: orange\">ORANGE = Alumni using more than 10GB</span></p>")
        fOut.write("<p><span style=\"background: yellow\">YELLOW = Students using more than 50GB</span></p>")

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
            if studentID[0:3] in ["e"+str(x) for x in range(0,19+1)]:
                fOut.write("<td bgcolor=\"orange\"><a href=\"https://people.ce.pdn.ac.lk/students/e{}/{}/\">profile</a></td>"\
                           .format(studentID[1:3],studentID[3:6]))
            elif studentID[0]=="e" and studentID[1:].isdigit() and int(usageGB[:-1])>50:
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
<hr>
This source code for generating this report is available <a href="https://github.com/cepdnaclk/maintenance">here</a>.<br>
<a href="https://www.cs.umd.edu/~gihan/contact/">Contact Gihan via email</a> for all questions about this report. 

</body>
</html>
'''.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

fIn.close()
fOut.close()

print("END: gen-report.py ( -> " + args.outFile + ")")