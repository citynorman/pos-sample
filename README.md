# pos-sample for freelancer.com

## instructions:
build a very simple web page (don't worry about formatting etc, just take a basic bootstrap page if you like)
1) link the table to read data from api using async calls (see API usage below). make sure to include authorization header
3) add sorting, filtering, pagination to table (like this http://ng-table.com/#/loading/demo-external-array)
2) allow user to accept an order from the order list, PATCH to update order status (see API usage below) and show updated status in table 

# api usage
python api-freelance.py
include header: x-api-key "abcdef123" (the sample api works without the header but the real api needs one)

## get all orders
GET http://127.0.0.1:5000/api/order

## update order status
PATCH http://127.0.0.1:5000/api/order/1
{
      "status": "confirmed"
    }
