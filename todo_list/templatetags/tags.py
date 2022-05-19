from django import template


register = template.Library()


def goal_status(value):
    if value:
        return 'Done'
    else:
        return 'Not completed'

register.filter('goal_status', goal_status)


