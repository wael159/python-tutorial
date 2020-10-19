#here i make a dictionary for the items and there price
import os
import json
import csv
filename = 'items.txt'
store = {}
with open(filename) as fh:
    for line in fh:
        item,value = line.strip().split('-', 1)

        store[item] = value.strip()
print(json.dumps(store, indent=2, sort_keys=True))
#___________________________________________________________________________________________________________________________

#create a new  csv file to save comments, rating for each client , and another one for the history purchases
if os.path.isfile('./purchases.csv')==False:
    with open('purchases.csv', 'w', newline='') as file:
        writer2 = csv.writer(file)
        writer2.writerow(["purchases_product", "price"])
if os.path.isfile('./reviews.csv.csv')==False:
    with open('reviews.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["proposed_items", "comment", "rate"])
#__________________________________________________________________________________________________________________________
# Taking the input from the user, check if it is in our store
# display the total price
# take comment/ review from the customer in the end of the process

total_price=0
end=False
while end==False:
    print("this is the prducts that we have in out store "+','.join(store.keys()))
    product = str(input("please choose an item that you want to buy from the above list, if you want to end please write quit"))

    # here we ask if the item is in our store,if it is in our store we will save it in the history file
    if product in store.keys():
        print("the price for these product is {} ".format(int(store.get(product))))
        with open('purchases.csv', 'a') as file:
            writer2=csv.writer(file)
            writer2.writerow([product,int(store.get(product))])
        total_price+=int(store.get(product))
     # if the customer choose to end the purchase, we print the total price,
    # and taking from him the reviws and save it in another file
    elif product =='quit':
        print("thank you, the total price is {} ".format(total_price))
        propose_newItem=str(input('which items you propose to our store'))
        comment=str(input("submit your comment here about our store"))
        Rate=int(input('Please Rate the supermarket out of 5'))
        with open('reviews.csv', 'a') as file:
            writer=csv.writer(file)
            writer.writerow([propose_newItem,comment,Rate])
        end=True
        break
    elif ((product not in store.keys()) and (product != 'quit')):
        print("there is no items in out store please choose another thing")
#___________________________________________________________________________________________________________________________
# make new function to display the mean rating
def clients_feedback(review_file):
    #read the csv file
    history_file=review_file
    # find the mean of the rate
    mean_rating=history_file['rate'].mean()
    print(mean_rating)
    #find the best proposed_item
    best_items=history_file.groupby(['proposed_items'])['proposed_items'].count().sort_values(ascending=False).index[0]
    # printing the best items that the customer proposed
    if (len(set(history_file.groupby(['proposed_items'])['proposed_items'].count()))) > 1:
        print("the best item is {}".format(best_items))
    else:
        print("all the items that has been proposed are the same, there is no preferable item, you see here the list of the proposed items \n {}".format(history_file['proposed_items']))
    print("the mean rating of the customers is {}".format(mean_rating))

    #printing two comments for each max rating and min rating
    comment_maxRate=history_file['comment'][history_file['rate'].idxmax(skipna=True)]
    comment_minRate=history_file['comment'][history_file['rate'].idxmin(skipna=True)]
    print("the comment for the max rating was :{}".format(comment_maxRate))
    print("the comment for the min rating was :{}".format(comment_minRate))
#______________________________________________________________________________________________________________________
def statistic_purchase(file):
    '''these functiom make a statistic for the purchase rate of eath product in our store
    :arg:csv file'''
    purchased=file
    purchase_rate=purchased.groupby(['purchases_product'])['purchases_product'].count().sort_values(ascending=False)
    print("you can see here the purchased rate for each item {} ".format(purchase_rate))

# calling the two functions
import pandas as pd
clients_feedback(pd.read_csv("reviews.csv"))
statistic_purchase(pd.read_csv("purchases.csv"))


