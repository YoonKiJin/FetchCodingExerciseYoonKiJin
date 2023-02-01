import pandas as pd

"""
                            Some notes about my program:
        
        
    The program is written in Python
and so requires an environment in which 
1. Python can be run and 
2. the Pandas library can be imported (Pandas library must be installed)









The tester is only required to change the value for the points to be spent
this can be done so by changing the value of the variable 
    points_to_spend
which can be seen near the bottom of the program
    (it is currently set at 5000 following the example)
    
    
(I wasn't exactly sure what kind of method would be used to pass in the argument when running the program.
So, I decided to keep things as simple as possible and require the tester to only change a variable value to test
the program)


once the value of
    points_to_spend
is changed to fit the tester's desired value, assuming the csv file's data is in the same format as given by the
example, the tester simply has to run the code and the results should be printed out
        
"""




def get_payer_balances_after_all_transactions(points_to_spend, csv_file_name="transactions.csv"):
    points_to_spend = points_to_spend

    df = pd.read_csv(csv_file_name)
    payers_and_points = {}

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df.sort_values(by="timestamp", inplace=True)
    df.reset_index(inplace=True)

    for index in range(len(df)):
        # save current data record     payer   and   points     as variables for easier design below
        curr_row_payer = df.loc[index, "payer"]
        curr_row_points = df.loc[index, "points"]

        # update payer points based on current data record
        if curr_row_payer in payers_and_points:
            payers_and_points[curr_row_payer] += curr_row_points
        else:
            payers_and_points[curr_row_payer] = curr_row_points

        curr_payer_points = payers_and_points[curr_row_payer]  # updated value of current data record payer's points

        if curr_payer_points < 0:  # check if current payer's points has gone negative after updating based on current data record
            points_to_spend += abs(curr_payer_points)  #
            payers_and_points[curr_row_payer] = 0  # reset to 0
        else:
            points_to_spend -= curr_payer_points
            if points_to_spend >= 0:
                payers_and_points[curr_row_payer] = 0
            else:
                payers_and_points[curr_row_payer] = abs(points_to_spend)
                points_to_spend = 0

    print(payers_and_points) # print out results








points_to_spend = 5000 # please change this value of 5000 from the example to fit the testing value of "points to spend"

get_payer_balances_after_all_transactions(points_to_spend=points_to_spend, csv_file_name="transactions.csv")