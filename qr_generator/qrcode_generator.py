import qrcode

class qrgenerate():
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(box_size = size, border = padding)

    def create(self,filename,fg,bg):
        try:
            data = input("Enter content ")
            self.qr.add_data(data)
            qrimg = self.qr.make_image(fill_color=fg,back_color=bg)
            qrimg.save(filename)
            print("successfully created")
        except Exception as e:
            print(e)

code = qrgenerate(30,5)
code.create('qr.png','black','white')
       
