class Article:
    '''
    this class will create all the objects in article
    '''
    def __init__(self,image,title,author,description,time,url):
        self.image = image
        self.title = title
        self.author = author
        self.description = description
        self.time = time
        self.url = url

class Source:
    '''
    this is a class that defines the source objects
    '''

    def __init__(self,id,name,url,description):
        self.id = id 
        self.name = name
        self.url = url
        self.description = description

