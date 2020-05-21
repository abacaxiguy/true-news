from django import template
from posts.models import Post

register = template.Library()


@register.filter(name='plural')
def plural_comentarios(n):
    try:
        n = int(n)
        if n == 0:
            return f'Nenhum comentário.'
        if n == 1:
            return f'{n} comentário.'
        else:
            return f'{n} comentários'


    except:
        return f'{n} comentário(s)'



