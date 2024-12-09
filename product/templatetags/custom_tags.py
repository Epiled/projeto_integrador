from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adiciona a classe CSS fornecida ao campo de formulário.
    """
    # Se o campo já tiver classes, adiciona a nova classe ao conjunto
    classes = field.field.widget.attrs.get('class', '')
    if classes:
        css_class = f"{classes} {css_class}"
    
    # Retorna o campo com a classe CSS adicionada
    return field.as_widget(attrs={"class": css_class})