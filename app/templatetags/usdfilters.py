from django import template
register=template.Library()

@register.filter(name='swap')
def swapping(value):
    return value.swapcase()

@register.filter()
def counting(value,args):
    res=0
    for i in range(len(value)):
        if value[i:i+len(args)]==args:
            res+=1
    return res



@register.filter()
def remove(value,args):
    return value.replace(args,'')