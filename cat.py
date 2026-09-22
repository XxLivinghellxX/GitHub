----------------git init--------------------
create .git folder. turn this into Git repository


--------------------git status--------------------
check unsaved work (up to date)
check what branch you are in


--------------------git checkout -b "[new branch name]" --------------------
 branch off from staging


--------------------git switch ["name"]--------------------
swtch to stage/ branch


--------------------git branch--------------------
to see what branch u r at


--------------------git branch -m [new name]--------------------
to rename the branch


--------------------git branch -d [branchname]--------------------
delete branch


--------------------gitreflog--------------------
show all log 


--------------------git log  // log --oneline--------------------
show commited file 


--------------------git diff ---------------------
show the different between commit and none commit 


--------------------git add . --------------------
Add all changed files in this current project folder to the staging area


--------------------git commit -m ['comment']---
to save work in git history 

 
-------------------- git commit --amend -m "[message]"--------------------
change the current commit name 


--------------------git stash --------------------
to put work aside, no save
-git stash list
-git stash clear


--------------------git stash pop --------------------
to put it back


--------------------git reset --hard  [ID]--------------------
go back to the commited file 


--------------------git reset --soft  [ID]--------------------
to switch back to the commited file 
need to review whats changed


--------------------git reset --soft head~1-----------------------
move to previous commit file 



------------------------------------------------------------
hard reset 
- auto update 
- use reflog to see all commited file 


soft reset 
- review the file 
- stash
- done 
- use git pop if u want it back


git stash and pop 
- stash the uncommited part
- move to another branch
- stash pop to get the changes back
- commit 
- stash clear

------------------------------------------------------------

