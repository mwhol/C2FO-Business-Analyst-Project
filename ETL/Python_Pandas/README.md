# My Solution to the Data Analyst Interview Assessment

**Once prepared, write up a short (3-5 sentences or bullet points) summary of 
how you prepared this table.**

My script begins by loading in the data (skipping columns we don't need.) 
Then it formats the datetime columns, throws away the rows older than our cutoff 
(12 months) and calculates the difference between the time of the call and the 
time that units arrived on scene. Afterwards it groups the data by battalion and 
month and calculates the 90th percentiles. Finally, it saves the answer to the csv 
file 'answer.csv.'


**Next write up a short (3-5 sentences or bullet points) summary of how you would 
make this task trivial to repeat every day.**

I would write another python script to download the csv file.
Then I would setup a scheduled task or cronjob that runs the downloader script, 
then the processing script, then notifies the user that the task has been completed. 
I'd probably also setup a few tests to verify that everything has run correctly.
Finally, because the source file is so large I'd see if there is some way to stream
just the new rows, which would yield a pretty large speedup.

----------------------

The original sourcefile I was working with was 2gb uncompressed which obviously
can't be sent through email but I thought I should have sourcedata in the zip so
I've included a mini version to make it easy to run. If you're on a 
computer with python3 and pandas (I saw pandas mentioned in the job listing for 
backend engineer so I'm assuming a bit) all you should have to do is execute 
main.py from within this directory and it should create answer.csv exactly as it
is now.

Thanks for your consideration!