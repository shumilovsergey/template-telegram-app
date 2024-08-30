import uuid

class CSPNonceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        nonce = uuid.uuid4().hex
        request.csp_nonce = nonce

        response = self.get_response(request)

        csp = (
            f"script-src 'self' https://telegram.org 'nonce-{nonce}'; "
            f"style-src 'self' 'nonce-{nonce}';"  # Example for allowing inline styles
        )

        if 'Content-Security-Policy' in response:
            response['Content-Security-Policy'] += f" {csp}"
        else:
            response['Content-Security-Policy'] = csp

        return response
