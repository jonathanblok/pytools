import binascii

couponList = [ "n<MibgC7sn", "mNYS#gC7sn", "o*IVigC7sn", "k#pDlgC7sn", "o*I]pgC7sn", "n(XRvgC7sn", "n(XLtgC7sn", "k#*AfgC7sn", "q:<IqgC7sn", "pEw8ogC7sn", "pes[BgC7sn", "l}6D$gC7ss" ]

prevInt = 0

for couponIndex in couponList:
    #hexCouponIndexString = binascii.hexlify(couponIndex)
    binCouponIndexString = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in couponIndex), 0))
    binSubstring = '0' + binCouponIndexString[2:]
    print(binSubstring)
    intCouponIndex = int(binSubstring, 2)
    print(intCouponIndex, " difference: ", (prevInt - intCouponIndex))
    prevInt = intCouponIndex

for couponIndex in couponList:
    binCouponIndexString = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in couponIndex), 0))
    hexCouponIndexString = hex(int(binCouponIndexString, 2))
    print(hexCouponIndexString)

