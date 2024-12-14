import qrcode

img = qrcode.make('HelloWorld')
img.save('helloWorld.jpg')