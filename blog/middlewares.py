from .models import ProfileLog
class TrafficMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_view(self,request,view_func,*view_args,**view_kargs):
       pass
        # x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(",")[0]
        # else:
        #     ip = request.META.get("REMOTE_ADDR")
        # user_agent = request.META.get("HTTP_USER_AGENT")
        # ProfileLog.objects.create(ip_address=ip,user_agent=user_agent,user=request.user)
    # def process_template_response(self,request,response):
    #     pass