# coding:utf-8
class UrlManager:
    def __init__(self):
        #定义两个url集合：未爬过的url和已爬过的url，集合可以防止值重复
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return
        #如果传进来的url没有在新url 以及 没有在就url，则插进新url集合中
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def add_new_urls(self, root_urls):
        if root_urls is None or len(root_urls) == 0:
            return
        #如果传进来的url列表中不为空，则循环插进新url集合中
        for root_url in root_urls:
            self.add_new_url(root_url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
