cd /app/src
pip install -r ../requirements.txt
export PYTHONPATH=$(pwd)
python3 backend/server.py
