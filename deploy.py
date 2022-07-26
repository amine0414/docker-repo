import sys,os
args=sys.argv.count()
os.system("branch=$(git branch --show-current)")
os.system("git add -A")
if args != 1:
    os.system("git commit")
else:
    os.system(""" echo "+============================-----+-----============================+"
    git status
    echo "+============================-----+-----============================+"
    sleep 2
    git commit -m "$1" """)
os.system(""" git push -u origin "$branch" """)