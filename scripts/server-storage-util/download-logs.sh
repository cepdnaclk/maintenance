# Create the servermonitoring@tesla account and uncomment this.
# scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@turing.ce.pdn.ac.lk:/localhome/servermonitoring/logging/turing/*storage* ../../reports/server-storage-util/logs/;
# scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@kepler.ce.pdn.ac.lk:/localhome/servermonitoring/logging/kepler/*storage* ../../reports/server-storage-util/logs/;
# scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@10.40.18.10:/localHome/servermonitoring/logging/ampere/*storage* ../../reports/server-storage-util/logs/;

scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@turing.ce.pdn.ac.lk:/localhome/servermonitoring/logging/turing/*storage* ../../reports/server-storage-util/logs/;
scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@kepler.ce.pdn.ac.lk:/localhome/servermonitoring/logging/kepler/*storage* ../../reports/server-storage-util/logs/;
scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@10.40.18.10:/localHome/servermonitoring/logging/ampere/*storage* ../../reports/server-storage-util/logs/;

scp -P 222 e14158@babbage.ce.pdn.ac.lk:/home/e14158/logging/babbage/*storage* ../../reports/server-storage-util/logs/;