echo "BUILD START"
py -m pip install -r requirement.txt
py manage.py collectstatic --noinput --clear
echo "BIULD END"