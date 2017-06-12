import binascii

couponList = [ "n<MibgC7sn", "mNYS#gC7sn", "o*IVigC7sn", "k#pDlgC7sn", "o*I]pgC7sn", "n(XRvgC7sn", "n(XLtgC7sn", "k#*AfgC7sn", "q:<IqgC7sn", "pEw8ogC7sn", "pes[BgC7sn", "l}6D$gC7ss" ]
prevBinCoupon = 0;

for couponIndex in couponList:
    #hexCouponIndexString = binascii.hexlify(couponIndex)
    binCouponIndexString = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in couponIndex), 0))
    print(binCouponIndexString)


#for couponIndex in couponList:
#    binCouponIndexString = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in couponIndex), 0))
#    hexCouponIndexString = hex(int(binCouponIndexString, 2))
#    print(hexCouponIndexString)

