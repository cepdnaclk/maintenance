# This is just a notebook used to keeptrack of some commands. Don't use these :-)


nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60

nvidia-smi --query-gpu=index,timestamp,utilization.gpu,utilization.memory --format=csv -l 5


echo "hi!" >  $HOME/`date +\%Y\%m\%d\%H\%M\%S`-cron.log




# KEPLER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

crontab -e

# 00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localhome/gihan/logging/kepler/kepler-gpu-`date +\%Y\%m\%d`.log
# @reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localhome/gihan/logging/kepler/kepler-gpu-`date +\%Y\%m\%d`.log 


00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localhome/servermonitoring/logging/kepler/kepler-gpu-`date +\%Y\%m\%d`.log
@reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localhome/servermonitoring/logging/kepler/kepler-gpu-`date +\%Y\%m\%d`.log 

# TURING >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

crontab -e

# 00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /storage/scratch/e14-4yp-low-light-images/logging/turing/turing-gpu-`date +\%Y\%m\%d`.log
# @reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /storage/scratch/e14-4yp-low-light-images/logging/turing/turing-gpu-`date +\%Y\%m\%d`.log


00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localhome/servermonitoring/logging/turing/turing-gpu-`date +\%Y\%m\%d`.log
@reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localhome/servermonitoring/logging/turing/turing-gpu-`date +\%Y\%m\%d`.log



# AMPERE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

crontab -e

00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localHome/servermonitoring/logging/ampere/ampere-gpu-`date +\%Y\%m\%d`.log
@reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /localHome/servermonitoring/logging/ampere/ampere-gpu-`date +\%Y\%m\%d`.log





# ai4COVID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

crontab -e

00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /userhomes/gihan/logging/ai4covid/ai4covid-gpu-`date +\%Y\%m\%d`.log
@reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /userhomes/gihan/logging/ai4covid/ai4covid-gpu-`date +\%Y\%m\%d`.log



00 00 * * * killall nvidia-smi; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /userhomes/servermonitoring/logging/ai4covid/ai4covid-gpu-`date +\%Y\%m\%d`.log
@reboot sleep 300; nvidia-smi --query-gpu=index,timestamp,power.draw,temperature.gpu,utilization.gpu,memory.used --format=csv -l 60 >>  /userhomes/gihan/logging/servermonitoring/ai4covid-gpu-`date +\%Y\%m\%d`.log


