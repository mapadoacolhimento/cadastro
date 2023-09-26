from django.conf import settings

virtual_hosts = {
    settings.VOLUNTEER_HOST: "volunteers.urls",
    settings.MSR_HOST: "msrs.urls",
}


class VirtualHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # let's configure the root urlconf
        host = request.get_host()
        request.urlconf = virtual_hosts.get(host)
        # order matters!
        response = self.get_response(request)
        return response
