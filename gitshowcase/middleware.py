from django.http import HttpResponsePermanentRedirect


class CanonicalDomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        path = request.get_full_path()

        # Redirect ANY herokuapp.com domain
        if host.endswith("herokuapp.com"):
            return HttpResponsePermanentRedirect(
                f"https://www.gitshowcase.dev{path}"
            )

        # Redirect non-www custom domain → www
        if host == "gitshowcase.dev":
            return HttpResponsePermanentRedirect(
                f"https://www.gitshowcase.dev{path}"
            )

        return self.get_response(request)
