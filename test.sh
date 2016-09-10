cd $(dirname "$0")
pwd
rm *.pyc
python -m pytest -s trivia-test.py > new.txt
diff -s old.txt <(cat new.txt | sed 's/0\.01/0.00/g')

python -m pytest -s unit-test.py
