class Pagination(object):
    def __init__(self, input_list, per_page):
        self.input_list = input_list
        self.per_page = per_page
        self.last_page = len(input_list) / self.per_page
        self.n_pages = self.last_page
        self.n_inter = len(self.input_list)

        if len(input_list) % 2 == 0:
            self.last_page -= 1

    def iter_pages(self):
        input_list = self.input_list
        curr = 0
        curr_page = self.__new_page()

        for i, val in enumerate(input_list):
            if i > 0 and i % self.per_page == 0:
                yield curr_page
                curr += 1
                curr_page = self.__new_page(curr)
            curr_page["items"].append(input_list[i])

        if len(curr_page["items"]) > 0:
            yield curr_page

    def __new_page(self, curr=0):
        n = curr+1
        if n > self.last_page:
            n = -1

        return {
            "items": [],
            "prev": curr-1,
            "curr": curr,
            "next": n
        }
