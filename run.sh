set -e

echo "Creating .venv"
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt