from django.utils.encoding import smart_text
from rest_framework import renderers


class SVGRenderer(renderers.BaseRenderer):
    media_type = "image/svg"
    format = "svg"
    render_style = "text"

    def render(self, data, media_type=None, renderer_context=None):
        return smart_text(data, encoding=self.charset)
