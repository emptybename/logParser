class UrlHelper:
    @staticmethod
    def mask_url(url):
        url_list = url.split('/')
        for idx in range(0, len(url_list)):
            if url_list[idx].isdigit():
                url_list[idx] = '{id}'
        return '/'.join(url_list)