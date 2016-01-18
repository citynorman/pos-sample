# angular.js pos-sample for freelancer.com

## instructions:
build a very simple angular.js web page (don't worry about formatting etc, just take a basic bootstrap page if you like)

1) link the table to read data from api using async calls (see API usage below). make sure to include authorization header

2) add sorting, filtering, pagination to table

3) allow user to accept orders from the order list (one at a time), PATCH to update order status (see API usage below, make sure to include authorization header) and show updated status in table

Commit *on a new branch*

# api usage
python api-freelance.py

include header: x-api-key "abcdef123" (the sample api works without the header but the real api needs one)

## get all orders
GET http://104.131.61.25:5000/api/order

## update order status
PATCH http://104.131.61.25:5000/api/order/1
{
      "status": "confirmed"
    }
