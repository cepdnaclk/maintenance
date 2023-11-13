import os
import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import timedelta


SERVERS = ["turing","kepler","ai4covid","ampere"]
LOGS_DIRECTORY = '../../reports/server-gpu-util/logs/'
JSON_FILE = "./gpu-info.json"
OUT_FOLDER = "../../reports/server-gpu-util/plots/"


if __name__=="__main__":

    # print()

    t0 = pd.datetime.now()
    refinedDateRage = pd.date_range(start= t0 - pd.Timedelta(30, unit='d'), end= t0, freq="D").floor("D")


    data = {}
    JSON = json.load(open(JSON_FILE))
    
    # iterate over files in
    # that directory
    for filename in os.listdir(LOGS_DIRECTORY):
        f = os.path.join(LOGS_DIRECTORY, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            if not ("gpu-202308" in f or "gpu-202309" in f or "gpu-202310" in f or "gpu-202311" in f): continue
            s = f.split("/")[-1].split("-")[0]
            
            
            fDataFrame = pd.read_csv(f)
            # if "turing" in f:
            #     print(fDataFrame.dtypes)
                

            fDataFrame = fDataFrame.rename(columns=lambda x: x.strip())
            fDataFrame = fDataFrame.dropna()

            if "gpuid" in  fDataFrame.columns:
                try:
                    fDataFrame.gpuid = fDataFrame.gpuid.astype(int)
                    fDataFrame.timestamp = fDataFrame.timestamp.astype('datetime64[ns]')
                except:
                    continue

                if s not in data:
                    data[s] = fDataFrame
                else:
                    data[s] = data[s].append(fDataFrame)



    
    for s in SERVERS:
        print(s)
        # data[s] = data[s].rename(columns=lambda x: x.strip())
        print(data[s])    
        data[s] = data[s][data[s]["gpuid"].apply(lambda x: str(x).isdigit())] #Keep only rows where GPUID \in int 
        print(data[s])

        data[s]["timestamp"] = data[s]["timestamp"].apply(pd.to_datetime)
        data[s]["power.draw [W]"] = data[s]["power.draw [W]"].apply(lambda x: float(x.replace(" W","")))
        data[s]["utilization.gpu [%]"] = data[s]["utilization.gpu [%]"].apply(lambda x: float(x.replace(" %","")))
        data[s]["memory.used [MiB]"] = data[s]["memory.used [MiB]"].apply(lambda x: float(x.replace(" MiB","")))

        for i in [0,1]:
            if str(i) in JSON[s]:
                if bool(JSON[s][str(i)]["active"]):#==True: 
                    data[s+"-"+str(i)] = data[s][:][data[s].gpuid == i]
        del data[s]



    for s in data:
        print(s)
        data[s].head()
        print("!!!")
        data[s] = data[s].groupby(data[s].timestamp.dt.floor("D")).mean()
        data[s] = data[s].reindex(refinedDateRage,fill_value=0)
        data[s] = data[s].tail(30)

        print(data[s])
        print("---------------")


    for s in data:
        print(s+"------------------")
        print(data[s].columns)
        print(data[s].head())
        # _=input("")
        ax = data[s].plot(y=["utilization.gpu [%]","memory.used [MiB]"],secondary_y = ["memory.used [MiB]"],ylim=(0,100),marker="*",\
                          style={"utilization.gpu [%]":"*-r","memory.used [MiB]":"*-b"},lw=0.3)
        ax.set_ylabel("utilization.gpu [%]",color="r")
        ax.right_ax.set_ylabel("memory.used [MiB]",color="b")
        ax.right_ax.set_ylim(0,JSON[s.split("-")[0]][s.split("-")[1]]["memory"])
        ax.get_legend().remove()
        
        
        plt.savefig(OUT_FOLDER+"/"+"plot{}.jpeg".format(s),bbox_inches='tight')
            


