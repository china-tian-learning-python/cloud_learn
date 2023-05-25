from django.shortcuts import render,redirect,reverse
from django.utils.deprecation import MiddlewareMixin


class wo(MiddlewareMixin):

    def process_request(self,request):
    #     print("hello world")
    #     print(reverse('user_list'))
    #     print(request.META.get("REMOTE_ADDR"))
        if request.path_info == reverse("admin_login") or  '/admin/ajax' in request.path_info:
            print(request.path_info)
            return None
        else:
            wood=request.session.get("info")
            if wood:
                return None
            else:
                return redirect(reverse("admin_login"))