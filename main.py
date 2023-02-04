import pandas as pd
import sys

"""
                            Some notes about my program:
        
        
    The program is written in Python
and so requires an environment in which 
1. Python can be run and 
2. the Pandas library can be imported (Pandas library must be installed)




please run argument as              e.g.           python3 main.py 5000

(the name of the Python file is main.py)


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
            points_to_spend += abs(curr_payer_points)
            payers_and_points[curr_row_payer] = 0  # reset to 0
        else:
            points_to_spend -= curr_payer_points
            if points_to_spend >= 0:
                payers_and_points[curr_row_payer] = 0
            else:
                payers_and_points[curr_row_payer] = abs(points_to_spend)
                points_to_spend = 0

    print(payers_and_points) # print out results








points_to_spend = int(sys.argv[1])

get_payer_balances_after_all_transactions(points_to_spend=points_to_spend, csv_file_name="transactions.csv")

