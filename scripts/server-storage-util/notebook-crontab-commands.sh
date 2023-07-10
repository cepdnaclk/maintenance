sudo crontab -e


# KEPLER >>>>>>>>>>>

# 00 00 * * * date +\%F > /localhome/gihan/logging/kepler/kepler-storage.log; du -hs --threshold=10G --exclude /storage/datasets /storage/* | sort -hr >> /localhome/gihan/logging/kepler/kepler-storage.log;


00 00 * * * date +\%F > /localhome/servermonitoring/logging/kepler/kepler-storage.log; du -hs --threshold=10G --exclude /storage/datasets /storage/* | sort -hr >> /localhome/servermonitoring/logging/kepler/kepler-storage.log;



# TURING >>>>>>>>>>>>>

00 00 * * * date +\%F > /localhome/servermonitoring/logging/turing/turing-storage.log; (du -hs --threshold=10G /storage/scratch/*;  du -hs --threshold=10G /storage/projects1/*; du -hs --threshold=10G /storage/projects2/*) | sort -hr >> /localhome/servermonitoring/logging/turing/turing-storage.log;



#  Babbage
rm /home/e14158/babbage-storage.log; (du -hs --threshold=10G /storage/scratch/*;  du -hs --threshold=10G /export/home/*; du -hs --threshold=10G /export/home2/*) | sort -hr >> /home/e14158/babbage-storage.log;

