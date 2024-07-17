rm ../../reports/server-gpu-util/plots/*.jpeg
#./download-logs.sh
python generate-graphs.py
cd ../../
# git add .
# git commit -m "updating plots for server util"
# git push origin main
