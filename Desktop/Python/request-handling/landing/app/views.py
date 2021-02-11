from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    counter_1 = request.GET.get('from-landing')
    counter_click[counter_1] += 1
    return render(request, 'index.html')


def landing(request):
    params = request.GET.get('ab-test-arg')
    counter_show[params] += 1
    if params == 'original':
        return render(request, 'landing.html')
    elif params == 'test':
        return render(request, 'landing_alternate.html')
    else:
        return render(request, 'landing.html')



def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:

    try:
        test_conversion = counter_click["test"]/counter_show["test"]
    except ZeroDivisionError:
        test_conversion =0

    try:
        original_conversion = counter_click['original']/counter_show['original']
    except ZeroDivisionError:
        original_conversion = 0

    count = {
        'test_conversion': test_conversion,
        'original_conversion': original_conversion
    }
    return render(request, 'stats.html', context=count)
