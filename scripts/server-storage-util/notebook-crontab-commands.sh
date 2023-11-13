sudo crontab -e


# KEPLER >>>>>>>>>>>

00 00 * * * date +\%F > /localhome/servermonitoring/logging/kepler/kepler-storage.log; du -hs --threshold=10G --exclude /storage/datasets /storage/* | sort -hr >> /localhome/servermonitoring/logging/kepler/kepler-storage.log;



# TURING >>>>>>>>>>>>>

00 00 * * * date +\%F > /localhome/servermonitoring/logging/turing/turing-storage.log; (du -hs --threshold=10G /storage/scratch/*;  du -hs --threshold=10G /storage/projects1/*; du -hs --threshold=10G /storage/projects2/*) | sort -hr >> /localhome/servermonitoring/logging/turing/turing-storage.log;


# TURING >>>>>>>>>>>>>

00 00 * * * date +\%F > /localHome/servermonitoring/logging/ampere/ampere-storage.log; (du -hs --threshold=10G /storage/scratch0/*;  du -hs --threshold=10G /storage/scratch1/*; du -hs --threshold=10G /storage/scratch2/*) | sort -hr >> /localHome/servermonitoring/logging/ampere/ampere-storage.log;


#  Babbage  >>>>>>>>>>>>>
00 00 * * * date +\%F > /home/e14158/logging/babbage/babbage-storage.log; du -hs --threshold=10G /export/home/* | sort -hr >> /home/e14158/logging/babbage/babbage-storage.log;