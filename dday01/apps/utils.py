from django.utils.safestring import mark_safe

import copy
class pags(object):
    def __init__(self,request,sqls,page_param="page",page_size=10,plus=5):
        request_copy=copy.deepcopy(request.GET)
        request_copy._mutable=True
        # request_copy.setlist("wood",[11])
        self.request_copy=request_copy


        page=request.GET.get(page_param,"1")
        if page.isdecimal():
            page=int(page)

        else:
            page=1
        self.page=page
        self.page_size=page_size
        self.start=(page-1)*self.page_size
        self.end=page*self.page_size
        self.queryset=sqls[self.start:self.end]
        counts=sqls.count()
        sum_number,div=divmod(counts,page_size)

        if div:
            sum_number+=1
        self.sum_number=sum_number
        self.plus=5

    def html(self):
        li_list=[]
        # 数据库较少，没有达到11页时
        if self.sum_number<=2*self.plus+1:
          page_start=1
          page_end=self.sum_number
        else:
            #判断self.plus是否大于page
            if self.page<=self.plus:
                page_start=1
                page_end=2*self.plus+1
                #判断 page+5是否大于self.sum_number
            elif self.page+self.plus>= self.sum_number:
                page_start = self.sum_number - 2 * self.plus
                page_end = self.sum_number
            else:
                page_start = self.page - self.plus
                page_end = self.page + self.plus
        self.request_copy.setlist("page",[1])

        str = '<li><a href="?{}">首页</a></li>'.format(self.request_copy.urlencode())
        li_list.append(str)
        # 上一页
        if self.page > 1:
            self.request_copy.setlist("page", [self.page - 1])
            str = '<li><a href="?{}">上一页</a></li>'.format(self.request_copy.urlencode())
        else:
            self.request_copy.setlist("page", [1])
            str = '<li><a href="?{}">上一页</a></li>'.format(self.request_copy.urlencode())
        li_list.append(str)
        for li in range(page_start, page_end + 1):
            # 没有固定的10码数  需要判断是否超过页码数
            if li == self.page:
                self.request_copy.setlist("page",[li])
                str = '<li class="active" ><a href="?{}">{}</a></li>'.format(self.request_copy.urlencode(), li)
            else:
                self.request_copy.setlist("page", [li])
                str = '<li><a href="?{}">{}</a></li>'.format(self.request_copy.urlencode(), li)

            li_list.append(str)

            # 下一页
        if self.page < self.sum_number:
            self.request_copy.setlist("page", [self.page + 1])
            str = '<li><a href="?{}">下一页</a></li>'.format(self.request_copy.urlencode())
        else:
            self.request_copy.setlist("page", [self.sum_number])
            str = '<li><a href="?{}">下一页</a></li>'.format(self.request_copy.urlencode())
        li_list.append(str)
        print(self.request_copy.urlencode())
        # 尾页
        self.request_copy.setlist("page", [self.sum_number])
        str = '<li><a href="?{}">尾页</a></li>'.format(self.request_copy.urlencode())
        li_list.append(str)
        str_li_list = ''.join(li_list)
        str_li_list = mark_safe(str_li_list)
        return str_li_list