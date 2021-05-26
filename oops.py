class Book:
    def __init__(self,bid,btitle,aname,btype,bprice,stat):
        self.bookID=bid
        self.bookTitle=btitle
        self.authorName=aname
        self.bookType=btype
        self.bookprice=bprice
        self.status=stat
class Library:
    def __init__(self,blist):
        self.bookList=blist
    def issueBook(self,bookTitle,bookType):
        for i in self.bookList:
            if i.bookTitle==bookTitle and i.bookType==bookType and i.status=='available':
                i.status='unavailable'
                return True
        return False
    def findCostliestBookname(self,aname):
        maxprice=0
        maxpricebook=None
        for i in self.bookList:
            if i.authorName==aname:
                if i.bookPrice>maxprice:
                    maxprice=i.bookPrice
                    maxpricebook=i
        if maxpricebook=='':
            return None
        else:
            return maxpricebook
if __name__=='__main__':
    n=int(input())
    booklist=[]
    for i in range(n):
        a=input()
        b=input()
        c=input()
        d=input()
        p=int(input())
        s=input()
        booklist.append((Book(a,b,c,d,p,s)))
    obj=Library(booklist)
    btitle=input()
    btype=input()
    aname=input()
    res=obj.issueBook(btitle,btype)
    if res==True:
        print("Book issued")
        for i in obj.bookList:
            print(i.bookTitle+' -> '+ i.status)
    res1=obj.findCostliestBookname(aname)
    if res1==None:
        print("Book Not Found")
        print("Author Not Found")
    else:
        print(res1.bookTitle+' -> '+res.status)
    



