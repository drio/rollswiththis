import unittest
from rwt.pagination import Pagination


class TestPagination(unittest.TestCase):
    def test_test(self):
        assert 1 == 1

    def test_less(self):
        _list = range(0, 6)
        p = Pagination(_list, 8)
        pages = []

        i = 0
        for page in p.iter_pages():
            pages.append(page)
            for it in page["items"]:
                assert it == i
                i += 1

        assert len(pages) == 1

        p = pages[0]
        assert len(p["items"]) == 6
        assert p["prev"] == -1
        assert p["next"] == -1

    def test_even(self):
        _list = range(0, 6)
        p = Pagination(_list, 2)
        pages = []

        i = 0
        for page in p.iter_pages():
            pages.append(page)
            for it in page["items"]:
                assert it == i
                i += 1

        assert len(pages) == 3

        p = pages[0]
        assert len(p["items"]) == 2
        assert p["prev"] == -1
        assert p["next"] == 1

        p = pages[1]
        assert len(p["items"]) == 2
        assert p["prev"] == 0
        assert p["next"] == 2

        p = pages[2]
        assert len(pages[2]["items"]) == 2
        assert p["prev"] == 1
        assert p["next"] == -1

    def test_odd(self):
        _list = range(0, 5)
        p = Pagination(_list, 2)
        pages = []

        i = 0
        for page in p.iter_pages():
            pages.append(page)
            for it in page["items"]:
                assert it == i
                i += 1

        assert len(pages) == 3

        p = pages[0]
        assert len(p["items"]) == 2
        assert p["prev"] == -1
        assert p["next"] == 1

        p = pages[1]
        assert len(p["items"]) == 2
        assert p["prev"] == 0
        assert p["next"] == 2

        p = pages[2]
        assert len(pages[2]["items"]) == 1
        assert p["prev"] == 1
        assert p["next"] == -1



if __name__ == '__main__':
    unittest.main()
