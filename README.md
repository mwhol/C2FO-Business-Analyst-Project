# Data Analyst Project
 
This was created for a job interview as a demonstration of the basic skills required. Since then I have been progressively adding to it, including with projects I have had to complete for other jobs with the idea being that eventually it will be impressive enough to get me hired! Right now it's a bit of a spaghetti mess with a bunch of different components. Once I find a compelling large public dataset I'll probably redo everything with that one data source. Just on the lookout for something like that right now.

~~A basic demonstration of the technical skills required for the job I applied to with C2FO. I whipped this up real quick as proof that I have the requisite data visualization and ETL skills. I know the code needs commenting, I may go back and do that.~~

--------------------

## As of 9/13

I've got two different methods here to grab the data and perform some basic transformations/cleaning on it. First up is Excel VBA, upon opening the file will automatically begin the process of reaching out to the relevant URL to download our data, import it into the workbook and then, because the People table is wrong and lacking information, it remakes it from scratch with several new columns, formulas with INDEX(MATCH()), VLOOKUP, COUNTIF, SUMIF, AVERAGEIF are used as demonstrations. Below is a video of it running:

https://user-images.githubusercontent.com/13397624/133176373-8deeb024-4db5-44eb-ab7b-49d3e06fcfb3.mov

[And here's the location](https://github.com/mwhol/Data-Analyst-Project/tree/main/ETL/VBA)


-----------------

Second up is the exact same extraction, transformation and cleaning but performed with python and SQL. The python code downloads the file from the URL, uses pandas to transform it to an sqlite database, then runs the SQL code on the database. The SQL code uses a variety of functions, SELECT, INSERT, ROLLBACK, ALTER TABLE and finishes with a heavily nested query made of an UPDATE on a SELECT on a JOIN. Below is a video of that running:


https://user-images.githubusercontent.com/13397624/133176353-e00cf881-cd3a-470e-bbb2-024270152193.mov

[And here's the location](https://github.com/mwhol/Data-Analyst-Project/tree/main/ETL/Python_SQL)

---------------------

And next up a little bit of analysis in Tableau. I've loaded the data from the Excel file we generated in part one and then generated a dashboard page. On this dashboard you can see three charts - a Profit by State chart on the left and a Profit by Category and Top and Bottom Customers by Profit charts on the right. The state chart acts as a filter for the charts on the right. The profits by category chart is relatively straightforward, the Top and Bottom chart is a little more complex with sets and custom parameters to ensure that we always get the Top 4 and Bottom 4 customers. Below you can see a video of me clicking through that.


https://user-images.githubusercontent.com/13397624/133176042-a030b44d-fbe5-4511-8bdf-254e5fd8469c.mov

Edit: I've also created a bar race chart for the profit by sub-category over time, you can see that below:

https://user-images.githubusercontent.com/13397624/134106099-d2632499-725a-4156-b011-9b85d254ba83.mov


---------------

## As of 9/20


And when speaking to Rachel she wanted to know about cluster models so I figured what the heck and coded up a simple kmeans model at the same time. Unfortunately the data I've been using for this project so far isn't really suited to kmeans very well (very little continuous data, it's almost all categorical) so after seeing how bad the clusters turned out, I created another python file which runs the code on the iris sample dataset and that ends up showing the clusters much more clearly.

https://user-images.githubusercontent.com/13397624/134106242-fa71d82c-4049-44e0-84cd-26c6c9b7b367.mov


----------------

## As of 9/29

I have used a #RealWorldFakeData dataset made about employee characteristics into a simple Tableau Dashboard. The Dashboard itself is relatively simple and the data was also a bit disappointing, as you click around you'll notice the data was generated pretty evenly in terms of characteristics so the company seems to have achieved almost supernaturally uniform diversity. Regardless, the point was to figure out Tableau Public, so you yourself can click around in the dashboard [here.](https://public.tableau.com/app/profile/michael.wholey/viz/Main_16329184010700/HRDashboard) Give it a shot!

------------------------

I also had a short coding test for a position which required a simple data transformation. Options were pretty open on how to complete the task but I chose python/pandas as it seems the most natural to me and is what I'd like to work with most. Basically the task is to take a 2gb csv file on calls to the San Francisco Fire Department and figure out the 90th percentile response time per month per Battalion for the most recent 12 months. This one was already nicely packaged for my submission and I should note there was a two hour time limit which I did obey, so I know there could probably be some fixes to it but overall, pretty decent code I think. It's heavily commented so it's probably better to read it straight than to show a video of it running, you can find it [here.](https://github.com/mwhol/Data-Analyst-Project/blob/main/ETL/Python_Pandas/main.py) Do note that the formatting of the output was strictly specified which is why there is so much formatting code.
