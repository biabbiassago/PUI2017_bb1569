Last login: Tue Nov 21 18:38:03 on ttys000
ZhouBaolings-MacBook-Air:~ zhoubaoling$ cd../
-bash: cd../: No such file or directory
ZhouBaolings-MacBook-Air:~ zhoubaoling$ pui2017
ZhouBaolings-MacBook-Air:PUI2017 zhoubaoling$ cd../
-bash: cd../: No such file or directory
ZhouBaolings-MacBook-Air:PUI2017 zhoubaoling$ git clone https://github.com/baolingz/PUI2017_bb1569.git
Cloning into 'PUI2017_bb1569'...
lsremote: Counting objects: 449, done.
remote: Compressing objects: 100% (59/59), done.
remote: Total 449 (delta 39), reused 62 (delta 21), pack-reused 367
Receiving objects: 100% (449/449), 3.91 MiB | 544.00 KiB/s, done.
Resolving deltas: 100% (221/221), done.
ZhouBaolings-MacBook-Air:PUI2017 zhoubaoling$ ls -ltr
total 4248
-rw-r--r--@  1 zhoubaoling  staff    36110 Sep 16 17:07 setup_env.png
-rw-r--r--@  1 zhoubaoling  staff    56838 Sep 16 17:15 bz882_bash.png
-rw-r--r--   1 zhoubaoling  staff      677 Sep 16 18:01 README.md~
drwxr-xr-x   3 zhoubaoling  staff      102 Sep 25 23:53 HW1_bz882
-rw-r--r--   1 zhoubaoling  staff   340679 Sep 25 23:53 HW1_3.ipynb
drwxr-xr-x  10 zhoubaoling  staff      340 Sep 26 00:02 HW2_bz882
drwxr-xr-x   3 zhoubaoling  staff      102 Oct 11 02:36 lab3_bz882
-rw-r--r--   1 zhoubaoling  staff      683 Oct 11 02:36 README.md
drwxr-xr-x  12 zhoubaoling  staff      408 Nov  5 23:45 HW5_bz882
drwxr-xr-x  12 zhoubaoling  staff      408 Nov  6 00:45 HW3_bz882
drwxr-xr-x   9 zhoubaoling  staff      306 Nov 13 15:32 HW4_bz882
drwxr-xr-x   9 zhoubaoling  staff      306 Nov 13 22:29 HW6_bz882
drwxr-xr-x  16 zhoubaoling  staff      544 Nov 14 14:52 HW7_bz882
drwxr-xr-x  10 zhoubaoling  staff      340 Nov 14 15:35 HW8_bz882
-rw-r--r--@  1 zhoubaoling  staff   358470 Nov 16 18:16 Geopandas State Flowers.ipynb
-rw-r--r--@  1 zhoubaoling  staff     1400 Nov 16 18:18 stateflowers.txt
-rw-r--r--@  1 zhoubaoling  staff  1362888 Nov 16 18:22 cb_2016_us_state_5m.shp
drwxr-xr-x  10 zhoubaoling  staff      340 Nov 21 18:43 HW9_bz882
drwxr-xr-x  14 zhoubaoling  staff      476 Nov 21 18:59 PUI2017_bb1569
ZhouBaolings-MacBook-Air:PUI2017 zhoubaoling$ cd PUI2017_bb1569
ZhouBaolings-MacBook-Air:PUI2017_bb1569 zhoubaoling$ ls
CitibikeReview_ssb602.md		HW6_bb1569
HW1_bb1569						HW7_bb1569
HW2_bb1569								HW8_bb1569
HW3_bb1569										Lab3_bb1569
HW4_bb1569												README.md
HW5_bb1569
ZhouBaolings-MacBook-Air:PUI2017_bb1569 zhoubaoling$ puidata
ZhouBaolings-MacBook-Air:PUIdata zhoubaoling$ ls
911%20copy.csv			 PUI2017_bb1569
ZhouBaolings-MacBook-Air:PUIdata zhoubaoling$ cd PUI2017_bb1569/HW8_bb1569
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ ls
HW8plot_bb1569.ipynb		    README.md
HW9_1_bb1569.md				tempPlot.png
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git add HW9_1_bb1569.md 
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git commit HW9_1_bb1569.md -m 'upload'
[master c074c03] upload
 Committer: ZhouBaoling <zhoubaoling@ZhouBaolings-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 HW8_bb1569/HW9_1_bb1569.md
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git push
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 117.57 KiB | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/baolingz/PUI2017_bb1569.git
   003c488..c074c03  master -> master
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git add HW9_1_bb1569.md 
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git commit HW9_1_bb1569.md -m 'upload'
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
	  .DS_Store
	  HW9_1_bb1569.md~

nothing added to commit but untracked files present
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ cd PUI2017_bb1569/HW8_bb1569
-bash: cd: PUI2017_bb1569/HW8_bb1569: No such file or directory
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ puidata
ZhouBaolings-MacBook-Air:PUIdata zhoubaoling$ cd PUI2017_bb1569/HW8_bb1569
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git add HW9_1_bb1569.md~
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git commit HW9_1_bb1569.md~ -m 'upload'
[master 544b19c] upload
 Committer: ZhouBaoling <zhoubaoling@ZhouBaolings-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 HW8_bb1569/HW9_1_bb1569.md~
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ git push
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 337 bytes | 0 bytes/s, done.
Total 4 (delta 2), reused 1 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/baolingz/PUI2017_bb1569.git
   c074c03..544b19c  master -> master
ZhouBaolings-MacBook-Air:HW8_bb1569 zhoubaoling$ pui2017
ZhouBaolings-MacBook-Air:PUI2017 zhoubaoling$ cd HW9_bz882/
ZhouBaolings-MacBook-Air:HW9_bz882 zhoubaoling$ emacs HW9_1_bb1569.md

# Peer Review for Bianca Brusco (bb1569)

## Reviewer: Baoling Zhou (bz882)

![]( tempPlot.png)

## Comments

### Clarity

-   The graph is good to understand with the help of bottom detailed caption.
-   It is easy to see how many degrees each bar represents with the help of the\
 white-colored dividers.

[Suggestion]

-   I was confused at beginning to understand what the period’s mean represent.\
 It cannot be specified more clearly in the bottom caption.

### Aesthetic

-   The red-blue color combination is easy to recognize. I can even tell that a\
-uuu:---F1  HW9_1_bb1569.md   Top L1     (Fundamental)--------------------------
Loading image...done
