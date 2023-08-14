class CakeShop:
    def __init__(self,cakeid,cakename,costperkg,cakequant):
        self.cakeid = cakeid
        self.cakename = cakename
        self.costperkg = costperkg
        self.cakequant = cakequant

    def __str__(self):
        data = str(self.cakeid)+","+self.cakename+","+str(self.costperkg)+","+str(self.cakequant)
        return data

class Cakecustomer:
    def __init__(self,cakeid,cakequant):
        self.cakeid = cakeid
        #self.cakename = cakename
        self.cakequant = cakequant

    def __str__(self):
        data = str(self.cakeid)+","+str(self.cakequant)
        return data

class Bill:
    def __init__(self,cakenm,cakeid,cakequant,total):
        self.cakeid = cakeid
        self.cakenm = cakenm
        self.cakequant = cakequant
        self.total = total

    def __str__(self):
        data = str(self.cakeid)+","+str(self.cakenm)+","+str(self.cakequant)+","+str(self.total)
        return data