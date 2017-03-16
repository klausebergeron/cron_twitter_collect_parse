import os
import re
import sys

#go through tweets in quickClass_streaming
#assign to either c_false_learning_set_tweets or c_false_learning_set_tweets
#clear the duplicates in those files
#add lines to c_total_true or false (as these will not be cleared once used)

quickClass_streaming_tweets_path = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//quickClass_streaming_tweets.txt"
quickClass_streaming_tweets = open(quickClass_streaming_tweets_path, 'r')

c_false_learning_set_tweets_path = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//c_false_learning_set_tweets.txt"
c_false_learning_set_tweets = open(c_false_learning_set_tweets_path, 'w+')
c_true_learning_set_tweets_path = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//c_true_learning_set_tweets.txt"
c_true_learning_set_tweets = open(c_true_learning_set_tweets_path, 'w+')

c_total_false_path = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//totals/claudias/c_total_false"
c_total_false = open(c_total_false_path, 'a')
c_total_true_path = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//totals//claudias//c_total_true"
c_total_true = open(c_total_true_path, 'a')

#clear the duplicate tweets from a file
def clearDups(filename):
    lines = open(filename, 'r').readlines()
    lines_set = set(lines)
    out  = open(filename, 'w')
    for line in lines_set:
        print(line)
    out.writelines(sorted(lines_set))
    out.close()

#for each tweet in the latest quickClass_streaming_tweets file,
#sort into either c_true_learning_set_tweets or c_false~
#which are the tomporary files that will be deleted after
#consolidation with the z_true/z_false files
with quickClass_streaming_tweets as infile:
    for line in infile:
        keepGoing = True
        while keepGoing == True:
            classif = input("Enter t if depressed, f if not:\n"+line)
            if classif not in 'tf':
                print("\nThat's not a t or f.  ")
                continue
            else:
                if classif == 't':
                    c_true_learning_set_tweets.write(line)
                if classif == 'f':
                    c_false_learning_set_tweets.write(line)
                keepGoing = False

print("\n\nThat's all for now!")

#clearDups(c_true_learning_set_tweets_path)
#clearDups(c_false_learning_set_tweets_path)

#dump the sorted lines into the permanent, aggragate true file
#called c_total_true
with c_true_learning_set_tweets as infile:
    for line in infile:
        c_total_true.write(line)
c_total_true.close()

#dump the sorted lines into the permanent, aggragate false file
#called c_total_true
with c_false_learning_set_tweets as infile:
    for line in infile:
        c_total_false.write(line)
c_total_false.close()


quickClass_streaming_tweets.close()
c_false_learning_set_tweets.close()
c_true_learning_set_tweets.close()


