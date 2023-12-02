# my_solution
# class PaginationHelper:
    
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.itcount = len(collection)
#         self.itperpage = items_per_page
    
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return self.itcount
    
#     # returns the number of pages
#     def page_count(self):
#         pagecount = (self.itcount/self.itperpage)
#         if pagecount == int(pagecount):
#             return pagecount
#         else:
#             return int(pagecount)+1
    
#     # returns the number of items on the given page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         if page_index < 0 or self.itcount ==0 or (page_index + 1) > self.page_count():
#             return -1
#         if  self.itperpage > self.itcount:
#             return self.itcount
#         remaining_items_on_last_page = self.itcount - page_index * self.itperpage

#         if remaining_items_on_last_page >= 0:
#             return min(self.itperpage, remaining_items_on_last_page)
#         else:
#             return -1
    
#     # determines what page an item at the given index is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         if item_index > self.itcount -1 or item_index < 0 or self.itcount ==0:
#             return -1
#         item_page = ((item_index+1)/self.itperpage)
#         if item_page == int(item_page):
#             if item_page == 0:
#                 return 0
#             else:
#                 print("test")
#                 return int(item_page) -1
#         else:
#             return int(item_page)

# better solution
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1

collection = ['a','b','c','d','e','f','g','h','e','f','g','h','e','f','g','h','e','f','g','h']
helper = PaginationHelper(collection, 16)
print(helper.page_item_count(1))