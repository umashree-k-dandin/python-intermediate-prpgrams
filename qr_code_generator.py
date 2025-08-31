import qrcode 
upi_id=input("enter the UPI ID=")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining payment url based onthe UPI ID and payment app
#you can modify these URLS based on the UPI ID apps you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create QR code for each payment app
phonepe_url=qrcode.make(phonepe_url)
googlepay_url=qrcode.make(googlepay_url)
paytm_url=qrcode.make(paytm_url)

#save the qr code to image file
phonepe_url.save('phonepe_qr.png')
googlepay_url.save('googlepay_qr.png')
paytm_url.save('paytm_qr.png')

#Displaying the QR codes(you may need to install the pillow)

phonepe_url.show()
googlepay_url.show()
paytm_url.show()

