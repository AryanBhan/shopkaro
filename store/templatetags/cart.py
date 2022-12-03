from django import template

register = template.Library()
@register.filter(name='product_in_cart')

def product_in_cart(product,cart):
    key=cart.keys()
    for i in key:
        if int(i)==product.id:
            return True
    return False
    
@register.filter(name='quan_in_cart')
def quan_in_cart(product,cart):
    key=cart.keys()
    for i in key:
        if int(i)==product.id:
            return cart.get(i)
    return 0
@register.filter(name='total_price')
def total_price(product,cart):
    return product.price * quan_in_cart(product,cart)
@register.filter(name='total_cart_price')
def total_cart_price(product,cart):
    sum=0
    for p in product:
        sum+=total_price(p,cart)
        
    return sum

    
    