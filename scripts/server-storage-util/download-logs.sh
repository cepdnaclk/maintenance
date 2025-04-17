# 1.a) Create the servermonitoring@tesla account and uncomment this.
# scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@turing.ce.pdn.ac.lk:/localhome/servermonitoring/logging/turing/*storage* ../../reports/server-storage-util/logs/;
# scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@kepler.ce.pdn.ac.lk:/localhome/servermonitoring/logging/kepler/*storage* ../../reports/server-storage-util/logs/;
# scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@10.40.18.10:/localHome/servermonitoring/logging/ampere/*storage* ../../reports/server-storage-util/logs/;


# 1.b) Until we have the servermonitoring@tesla account, I will be using my personal account e14158@tesla.ce.pdn.ac.lk
scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@turing.ce.pdn.ac.lk:/localhome/servermonitoring/logging/turing/*storage* ../../reports/server-storage-util/logs/;
scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@kepler.ce.pdn.ac.lk:/localhome/servermonitoring/logging/kepler/*storage* ../../reports/server-storage-util/logs/;
scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@10.40.18.10:/localHome/servermonitoring/logging/ampere/*storage* ../../reports/server-storage-util/logs/;

# 2.a) I am commenting out this because Babbage seems to have closed the SSH port
# scp -P 222 e14158@babbage.ce.pdn.ac.lk:/home/e14158/logging/babbage/*storage* ../../reports/server-storage-util/logs/;
# 2.b) I can access the same file from tesla.ce.pdn.ac.lk
scp e14158@tesla.ce.pdn.ac.lk:/home/e14158/logging/babbage/*storage* ../../reports/server-storage-util/logs/;