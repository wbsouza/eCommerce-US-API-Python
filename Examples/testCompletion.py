import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-1408564920.33"
amount = "0.00"
txn_number ="775161-0_10"
crypt = "7"

p = USmpgClasses.USCompletion(order_id, amount, txn_number, crypt)

p.setCommcardInvoice("COM INVOICE 1")
p.setCommcardTaxAmount("0.10")

req = USmpgClasses.mpgHttpsPost(host, store_id, api_token, p)
req.postRequest()
resp = req.getResponse()
print ("ReceiptId: " + resp.getReceiptId()) 
print ("ReferenceNum: " + resp.getReferenceNum()) 
print ("ResponseCode: " + resp.getResponseCode()) 
print ("AuthCode: " + resp.getAuthCode()) 
print ("TransTime: " + resp.getTransTime()) 
print ("TransDate: " + resp.getTransDate()) 
print ("TransType: " + resp.getTransType()) 
print ("Complete: " + resp.getComplete()) 
print ("Message: " + resp.getMessage()) 
print ("TransAmount: " + resp.getTransAmount()) 
print ("CardType: " + resp.getCardType()) 
print ("TransID: " + resp.getTransID()) 
print ("TimedOut: " + resp.getTimedOut()) 
print ("BankTotals: " + resp.getBankTotals()) 
print ("Ticket: " + resp.getTicket()) 
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage()) 


