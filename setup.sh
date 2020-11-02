#install dependancies for bot
echo "Installing depenancies..."
pip install -r requirements.txt
#create start.sh file
echo "python3 scripts/main.py || python scripts/main.py" > start.sh
chmod +x start.sh
