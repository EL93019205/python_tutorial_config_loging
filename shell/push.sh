if [ -z $1 ]; then
	echo "error! please write commit message!"
	exit 1
fi
cd ..
git add .
git commit -m $1
git push 
vim main.py
