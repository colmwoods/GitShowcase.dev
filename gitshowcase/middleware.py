from django.shortcuts import redirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        if host == "gitshowcase.dev":
            return redirect(
                "https://www.gitshowcase.dev" + request.get_full_path()
            )

        return self.get_response(request)