# C2FO Business Analyst Project
 
A basic demonstration of the technical skills required for the job I applied to with C2FO. I whipped this up real quick as proof that I have the requisite data visualization and ETL skills. I know the code needs commenting, I may go back and do that.

------------------



I've got two different methods here to grab the data and perform some basic transformations/cleaning on it. First up is Excel VBA, upon opening the file will automatically begin the process of reaching out to the relevant URL to download our data, import it into the workbook and then, because the People table is wrong and lacking information, it remakes it from scratch with several new columns, formulas with INDEX(MATCH()), VLOOKUP, COUNTIF, SUMIF, AVERAGEIF are used as demonstrations. Below is a video of it running:





https://user-images.githubusercontent.com/13397624/133176373-8deeb024-4db5-44eb-ab7b-49d3e06fcfb3.mov



-----------------

Second up is the exact same extraction, transformation and cleaning but performed with python and SQL. The python code downloads the file from the URL, uses pandas to transform it to an sqlite database, then runs the SQL code on the database. The SQL code uses a variety of functions, SELECT, INSERT, ROLLBACK, ALTER TABLE and finishes with a heavily nested query made of an UPDATE on a SELECT on a JOIN. Below is a video of that running:





https://user-images.githubusercontent.com/13397624/133176353-e00cf881-cd3a-470e-bbb2-024270152193.mov



---------------------

And last but not least a little bit of analysis in Tableau. I've loaded the data from the Excel file we generated in part one and then generated a dashboard page. On this dashboard you can see three charts - a Profit by State chart on the left and a Profit by Category and Top and Bottom Customers by Profit charts on the right. The state chart acts as a filter for the charts on the right. The profits by category chart is relatively straightforward, the Top and Bottom chart is a little more complex with sets and custom parameters to ensure that we always get the Top 4 and Bottom 4 customers. Below you can see a video of me clicking through that.


https://user-images.githubusercontent.com/13397624/133176042-a030b44d-fbe5-4511-8bdf-254e5fd8469c.mov
