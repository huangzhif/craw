import urllib.request


class HtmlDownloader:
    def download(self, new_root):
        if new_root is None:
            return None

        response = urllib.request.urlopen(new_root)
        if response.getcode() != 200:
            return None

        return response.read()
