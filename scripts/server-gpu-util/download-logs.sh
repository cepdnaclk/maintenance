scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@turing.ce.pdn.ac.lk:/localhome/servermonitoring/logging/turing/*gpu* ../../reports/server-gpu-util/logs/;
scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@kepler.ce.pdn.ac.lk:~/logging/kepler/*gpu* ../../reports/server-gpu-util/logs/;
scp -J servermonitoring@tesla.ce.pdn.ac.lk servermonitoring@ai4covid.ee.pdn.ac.lk:~/logging/ai4covid/*gpu* ../../reports/server-gpu-util/logs/;
find ../../reports/server-gpu-util/logs/ -type f -exec sed -i 's/index/gpuid/g' {} \;